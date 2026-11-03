#!/usr/bin/env python3
"""Paced public Phoenix business-facts importer. No account/player data or bypass.

Each country is independently checkpointed. A 403/429 stops the run. A missing
or changed directory is explicitly unavailable/failed, never reported as zero
installed machines. Japan uses its linked, separate public directory template.
"""
import argparse
import csv
import json
import math
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
COUNTRIES = [
    ("sg", "Singapore"), ("bn", "Brunei"), ("kh", "Cambodia"),
    ("ae", "United Arab Emirates"), ("sa", "Saudi Arabia"), ("in", "India"),
    ("id", "Indonesia"), ("my", "Malaysia"), ("hk", "Hong Kong"),
    ("tw", "Taiwan"), ("th", "Thailand"), ("vn", "Vietnam"),
    ("mn", "Mongolia"), ("cn", "China"), ("au", "Australia"),
    ("nz", "New Zealand"), ("nc", "New Caledonia"), ("ca", "Canada"),
    ("ie", "Ireland"), ("uk", "United Kingdom"), ("ma", "Morocco"),
    ("lu", "Luxembourg"), ("at", "Austria"), ("be", "Belgium"),
    ("cz", "Czechia"), ("de", "Germany"), ("pt", "Portugal"),
    ("ch", "Switzerland"), ("es", "Spain"), ("fr", "France"),
    ("us", "USA"), ("kr", "Korea"), ("jp", "Japan"),
]
HELD_SG = {
    "PHOENIXDARTS SG OFFICE", "TEST MACHINE FOR SINGAPORE",
    "FORTRESS MESS (WTD)", "SEMBAWANG CAMP", "WELLS SINGAPORE", "NCS PTE LTD",
}
COORDINATE_HOLD = "Pin falls outside permissive source-country geometry checks; verify before mapping"


def now():
    return datetime.now(timezone.utc).isoformat()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2))
    temporary.replace(path)


def cc_for(route):
    return "gb" if route == "uk" else route


def in_country(record, bounds):
    lat, lon = record.get("latitude"), record.get("longitude")
    if lat is None or lon is None or not math.isfinite(lat) or not math.isfinite(lon):
        return False
    return any(w - .3 <= lon <= e + .3 and s - .3 <= lat <= n + .3
               for w, s, e, n in bounds)


def start_for(route):
    if route == "jp":
        return "https://vs.phoenixdarts.com/jp/shop/shopSearch_terms"
    return f"https://www.phoenixdarts.com/{route}/shop/shopSearch"


def text(node):
    return node.get_text(" ", strip=True) if node else ""


def split_title(value, route):
    """Separate the source's balanced location prefix, including [[MY]City]."""
    value = value.strip()
    if not value.startswith("["):
        return value, ""
    depth = 0
    for index, character in enumerate(value):
        if character == "[":
            depth += 1
        elif character == "]":
            depth -= 1
            if depth == 0:
                region = value[1:index].strip()
                for code in {route.upper(), cc_for(route).upper()}:
                    tag = f"[{code}]"
                    if region.upper().startswith(tag):
                        region = region[len(tag):].strip()
                        break
                return value[index + 1:].strip(), region
    return value, ""


def repair_nested_title(record, route):
    """Migrate the old split at the first ] without fetching source pages again."""
    region = record.get("region", "")
    if region.upper() not in {f"[{route.upper()}", f"[{cc_for(route).upper()}"}:
        return False
    old_name = record.get("name", "")
    reconstructed = f"[{region}]{old_name}"
    name, fixed_region = split_title(reconstructed, route)
    if not name or not fixed_region or fixed_region == region:
        return False
    record["title_repair"] = {
        "method": "Balanced nested location prefix reconstructed from legacy parsed fields",
        "previous_name": old_name, "previous_region": region,
    }
    record["name"], record["region"] = name, fixed_region
    return True


def machines_from(value):
    # Global "." suffix, Japanese 台 suffix, and model:count listing tags.
    result = []
    for model, count in re.findall(
        r"([A-Za-z][A-Za-z0-9 +_-]*?)\s*(?::|\s)\s*(\d+)\s*(?:台|\.|(?=\s|$))", value
    ):
        model = model.strip(" ,")
        if model and not any(m["model"] == model for m in result):
            result.append({"model": model, "count": int(count)})
    return result


class AccessBlocked(RuntimeError):
    pass


class Client:
    def __init__(self, delay):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "NinjaDarts-DirectoryResearch/1.0 (public business facts; paced)"
        self.delay = max(1.2, delay)
        self.last = 0

    def get(self, url):
        if urlparse(url).hostname not in {"www.phoenixdarts.com", "vs.phoenixdarts.com"}:
            raise ValueError("Unexpected source host")
        for attempt in range(3):
            time.sleep(max(0, self.delay - (time.monotonic() - self.last)))
            try:
                response = self.session.get(url, timeout=45)
                self.last = time.monotonic()
                if response.status_code in (403, 429):
                    raise AccessBlocked(f"HTTP {response.status_code}; stopped without bypass: {url}")
                response.raise_for_status()
                if urlparse(response.url).hostname not in {"www.phoenixdarts.com", "vs.phoenixdarts.com"}:
                    raise ValueError("Unexpected redirected host")
                return BeautifulSoup(response.content, "html.parser")
            except (requests.Timeout, requests.ConnectionError):
                self.last = time.monotonic()
                if attempt == 2:
                    raise
            except requests.HTTPError:
                if response.status_code < 500 or attempt == 2:
                    raise
                self.last = time.monotonic() + 3 * (attempt + 1)


def listing_rows(soup, route, url):
    rows = {}
    for link in soup.select(f'a[href*="/{route}/shop/shopDetail?s_seq="]'):
        sid = re.search(r"s_seq=(\d+)", link["href"])
        # Do not collect decorative/recommended links elsewhere on the page.
        dt = link.select_one("dt")
        if not sid or not dt:
            continue
        raw_name = text(dt)
        name, region = split_title(raw_name, route)
        address_node = link.select_one(".address")
        dds = link.select("dd")
        address = text(address_node) if address_node else (text(dds[0]) if dds else "")
        machine_node = link.select_one(".machine")
        machine_text = text(machine_node) or " ".join(text(n) for n in link.select(".tag"))
        rows[sid[1]] = {
            "source_id": sid[1], "name": name, "address": address,
            "region": region, "source_title": raw_name,
            "source_url": urljoin(url, link["href"]),
            "machine_text": machine_text, "machines": machines_from(machine_text),
        }
    return rows


def parse_detail(soup, row, route):
    record = dict(row)
    heading = soup.select_one("#subSection .pageTitle h2")
    if heading:
        record["source_title"] = text(heading)
        record["name"], region = split_title(record["source_title"], route)
        if region:
            record["region"] = region
    fields = {}
    for anchor in soup.select('a[href*="shopSearch_region"]'):
        area = parse_qs(urlparse(anchor["href"]).query).get("ac4_n")
        if area:
            record["area"] = area[0]
    for tr in soup.select("tr"):
        th, td = tr.find("th"), tr.find("td")
        if th and td:
            clone = BeautifulSoup(str(td), "html.parser")
            for anchor in clone.select("#btnMap"):
                anchor.decompose()
            fields[text(th).lower()] = text(clone)
    address = soup.select_one("td.address")
    if address:
        clone = BeautifulSoup(str(address), "html.parser")
        for anchor in clone.select("a"):
            anchor.decompose()
        record["address"] = text(clone)
    else:
        record["address"] = fields.get("住所", fields.get("주소", record["address"]))
    latitude, longitude = soup.select_one("#lat"), soup.select_one("#lag")
    if not latitude or not longitude:
        raise ValueError(f"No detail coordinate inputs: {row['source_url']}")
    def number(node):
        try:
            value = float(node.get("value", ""))
            return value if math.isfinite(value) else None
        except (ValueError, TypeError):
            return None
    lat, lon = number(latitude), number(longitude)
    valid = lat is not None and lon is not None and -90 <= lat <= 90 and -180 <= lon <= 180 and (lat, lon) != (0, 0)
    if route == "sg":
        valid = valid and 1.15 <= lat <= 1.5 and 103.55 <= lon <= 104.15
    machine_text = fields.get("machine installation", fields.get("設置マシン", ""))
    # Some locales omit the inventory table; the directory listing still has it.
    if machine_text:
        record["machine_text"] = machine_text
        record["machines"] = machines_from(machine_text) or record["machines"]
    record.update({
        "parser_version": 3, "provider": "phoenix", "country_code": cc_for(route),
        "latitude": lat, "longitude": lon, "map_eligible": bool(valid),
        "directory_eligible": bool(record["name"] and record["address"]),
        "off_days": fields.get("off days", fields.get("휴무일", "")),
        "website": fields.get("url", ""),
        "collected_at": now(),
    })
    if route == "sg" and record["name"].upper().strip() in HELD_SG:
        record["directory_eligible"] = False
        record["exclusion_reason"] = "Test, office, workplace or camp; public access unverified"
    # Obvious administrative/test entries are retained in exports, not advertised.
    if re.search(r"(?i)\b(test machine|test shop|test store|phoenixdarts tournaments|phoenixdarts .*office)\b", record["name"]):
        record["directory_eligible"] = False
        record["exclusion_reason"] = "Provider administration, event or test listing; public access unverified"
    return record


def collect(route, cache, client):
    name = dict(COUNTRIES)[route]
    out = ROOT / "data/phoenix" / f"{cc_for(route)}.json"
    checkpoint = cache / route / "listing.json"
    progress = json.loads(checkpoint.read_text()) if checkpoint.exists() else {
        "rows": {}, "visited": [], "next": start_for(route), "complete": False,
    }
    coverage = {
        "country_code": cc_for(route), "name": name, "source_url": start_for(route),
        "status": "collecting", "updated_at": now(),
    }
    records = json.loads(out.read_text()).get("venues", []) if out.exists() else []
    def export():
        coverage["discovered"] = len(progress["rows"])
        coverage["collected"] = len(records)
        coverage["mapped"] = sum(r.get("map_eligible", False) and r.get("directory_eligible", True) for r in records)
        coverage["listing_pages"] = len(progress["visited"])
        coverage["updated_at"] = now()
        save(out, {"coverage": coverage, "venues": records})
    try:
        while not progress["complete"]:
            url = progress["next"]
            if url in progress["visited"] or len(progress["visited"]) >= 10000:
                raise ValueError("Pagination cycle/guard; directory incomplete")
            soup = client.get(url)
            rows = listing_rows(soup, route, url)
            if not rows:
                # Empty/unavailable is not asserted to mean no machines installed.
                coverage["status"] = "unavailable" if not progress["rows"] else "failed"
                coverage["note"] = "Public directory returned no usable venue rows; not proof of zero installations"
                export()
                return
            overlap = set(rows) <= set(progress["rows"])
            if overlap and progress["rows"]:
                raise ValueError("Pagination repeated the same venue IDs")
            progress["rows"].update(rows)
            progress["visited"].append(url)
            nxt = soup.select_one(".paging a.btn_next")
            progress["next"] = urljoin(url, nxt["href"]) if nxt else None
            progress["complete"] = not bool(nxt)
            save(checkpoint, progress)
            if len(progress["visited"]) % 20 == 1:
                print(f"{route}: {len(progress['rows'])} listings / {len(progress['visited'])} pages", flush=True)
        done = {r["source_id"]: r for r in records}
        for sid, row in progress["rows"].items():
            factfile = cache / route / f"{sid}.json"
            if factfile.exists():
                record = json.loads(factfile.read_text())
            elif sid in done and done[sid].get("parser_version") == 3:
                record = done[sid]
            else:
                record = parse_detail(client.get(row["source_url"]), row, route)
                save(factfile, record)
            done[sid] = record
            records = list(done.values())
            if len(records) % 25 == 0:
                export()
                print(f"{route}: details {len(records)}/{len(progress['rows'])}", flush=True)
        coverage["status"] = "complete"
        export()
    except AccessBlocked as error:
        coverage.update(status="blocked", note=str(error))
        export()
        raise
    except Exception as error:
        coverage.update(status="failed", note=str(error))
        export()
        print(f"{route}: FAILED {error}", flush=True)


def build():
    folder = ROOT / "data/phoenix"
    folder.mkdir(parents=True, exist_ok=True)
    columns = ["source_id", "country_code", "name", "address", "region",
               "latitude", "longitude", "map_eligible", "directory_eligible",
               "exclusion_reason", "machine_text", "source_url", "collected_at", "coordinate_review"]
    def export_csv(path, venues):
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
            writer.writeheader()
            # Business names/addresses are untrusted input, not spreadsheet code.
            writer.writerows({k: "'" + v if isinstance(v, str) and v.lstrip().startswith(("=", "+", "-", "@")) else v
                              for k, v in record.items()} for record in venues)
    # Preserve all reviewed pilot decisions while other countries are collected.
    if not (folder / "sg.json").exists():
        pilot = json.loads((ROOT / "data/phoenix-sg.json").read_text())
        venues = pilot["venues"]
        save(folder / "sg.json", {"coverage": {
            "country_code": "sg", "name": "Singapore", "source_url": start_for("sg"),
            "status": "complete", "collected": len(venues), "discovered": len(venues),
            "mapped": sum(v["map_eligible"] and v.get("directory_eligible", True) for v in venues),
            "note": "Existing reviewed Singapore pilot", "updated_at": max(v["collected_at"] for v in venues),
        }, "venues": venues})
    countries = []
    bounds_path = ROOT / "data/phoenix-country-bounds.json"
    bounds = json.loads(bounds_path.read_text())["countries"] if bounds_path.exists() else {}
    for route, name in COUNTRIES:
        path = folder / f"{cc_for(route)}.json"
        if not path.exists():
            countries.append({"country_code": cc_for(route), "name": name,
                              "source_url": start_for(route), "status": "pending"})
            # Stable URLs for live spreadsheets before collection finishes.
            export_csv(path.with_suffix(".csv"), [])
            continue
        feed = json.loads(path.read_text())
        changed = False
        for record in feed["venues"]:
            if repair_nested_title(record, route):
                changed = True
            # Recheck only importer-created geographic holds. A corrected
            # country geometry must not leave valid pins permanently excluded;
            # unrelated manual, access or invalid-coordinate exclusions remain.
            if record.get("coordinate_review") == COORDINATE_HOLD and cc_for(route) in bounds and in_country(record, bounds[cc_for(route)]):
                record["map_eligible"] = True
                record.pop("coordinate_review")
                changed = True
            if record.get("map_eligible") and cc_for(route) in bounds and not in_country(record, bounds[cc_for(route)]):
                record["map_eligible"] = False
                record["coordinate_review"] = COORDINATE_HOLD
                changed = True
        if changed:
            feed["coverage"]["mapped"] = sum(v.get("map_eligible", False) and v.get("directory_eligible", True) for v in feed["venues"])
            save(path, feed)
        coverage = feed["coverage"]
        countries.append({**coverage, "file": f"data/phoenix/{cc_for(route)}.json"})
        # Per-country spreadsheet-compatible export, including held/unmappable rows.
        export_csv(path.with_suffix(".csv"), feed["venues"])
    save(folder / "index.json", {
        "provider": "phoenix", "updated_at": now(), "countries": countries,
        "scope": "Public directories exposed by Phoenix country selector; not a guaranteed worldwide installation census",
    })
    with (folder / "coverage.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "country_code", "name", "status", "discovered", "collected",
            "mapped", "updated_at", "source_url", "note",
        ], extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(countries)
    lines = [
        "# Phoenix collection coverage", "",
        "This is a collection audit, not a worldwide installation census. Pending, unavailable and failed directories do not mean zero machines.", "",
        "The original DARTSLIVE files and reviewed Singapore exclusions are preserved. Source venue records can be stale, duplicated across providers or have inaccurate coordinates; a public listing is not a public-access guarantee.", "",
        "Business facts only are collected. No player data, descriptions or photos are imported. Automated access is paced and stops on HTTP 403/429. Redistribution and commercial use require a permission review under [Phoenix terms](https://www.phoenixdarts.com/us/help/clause).", "",
        "| Country directory | Status | Records collected | Eligible map records | Source |",
        "|---|---|---:|---:|---|",
    ]
    notes = []
    for c in countries:
        lines.append(f"| {c['name']} | {c['status']} | {c.get('collected', 'n.a.')} | {c.get('mapped', 'n.a.')} | [Public directory]({c['source_url']}) |")
        if c.get("note"):
            notes.append(f"- {c['name']}: {c['note']}")
    lines.extend(["", "## Collection notes", ""] + notes)
    (ROOT / "docs/PHOENIX_COVERAGE.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--countries", default="")
    parser.add_argument("--cache", default=str(ROOT.parent / "phoenix-global-cache"))
    parser.add_argument("--delay", type=float, default=1.2)
    parser.add_argument("--build-only", action="store_true")
    args = parser.parse_args()
    if not args.build_only:
        client = Client(args.delay)
        routes = args.countries.split(",") if args.countries else [r for r, _ in COUNTRIES if r != "sg"]
        for route in routes:
            if route not in dict(COUNTRIES):
                raise ValueError(f"Unknown country route: {route}")
            try:
                collect(route, Path(args.cache), client)
            finally:
                build()
    build()


if __name__ == "__main__":
    main()
