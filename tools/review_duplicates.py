#!/usr/bin/env python3
"""Conservative, read-only cross-provider review. Never edits venue feeds."""
import argparse
import csv
import html
import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ("docs/DUPLICATE_REVIEW.md", "docs/duplicate-review/candidates.json",
           "docs/duplicate-review/candidates.csv")
GENERIC = {"bar", "darts", "dart", "cafe", "club", "dartsbar", "dartbar",
           "pool", "billiards", "phoenix", "dartslive", "ダーツ", "バー",
           "ダーツバー", "dartsclub", "dartscafe", "dartsandbar"}
ALIASES = {"rd": "road", "st": "street", "ave": "avenue", "blvd": "boulevard",
           "ctr": "centre", "center": "centre", "bldg": "building"}


def normalize(value, address=False):
    value = unicodedata.normalize("NFKC", value or "").casefold()
    words = re.findall(r"[^\W_]+", value, flags=re.UNICODE)
    return "".join(ALIASES.get(w, w) if address else w for w in words)


def similarity(a, b):
    return SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else 0


def units(address):
    value = unicodedata.normalize("NFKC", address or "").casefold()
    rooms = set(re.findall(r"#\s*(\d{1,3}-[\w/-]+)", value))
    rooms.update(re.findall(r"\b(?:unit|suite|apt|room)\s*[:#]?\s*([\w-]+)", value))
    floors = set(re.findall(r"(?<![a-z0-9])(b?\d{1,2})\s*(?:f\b|階|楼|樓)", value))
    floors.update(re.findall(r"\b(?:floor|level)\s*(b?\d{1,2})\b", value))
    return {"rooms": sorted(rooms), "floors": sorted(floors)}


def unit_conflict(a, b):
    return any(a[k] and b[k] and not set(a[k]).intersection(b[k]) for k in a)


def address_numbers(address):
    value = unicodedata.normalize("NFKC", address or "").casefold()
    value = re.sub(r"#\s*\d{1,3}-[\w/-]+", "", value)
    value = re.sub(r"\b(?:unit|suite|apt|room)\s*[:#]?\s*[\w-]+", "", value)
    return set(re.findall(r"\d+[a-z]?", value))


def distinct_name(value):
    name = normalize(value)
    return len(name) >= 4 and name not in GENERIC


def position(record, phoenix=False):
    lat = record.get("latitude" if phoenix else "la")
    lon = record.get("longitude" if phoenix else "lo")
    if (isinstance(lat, (int, float)) and isinstance(lon, (int, float))
            and math.isfinite(lat) and math.isfinite(lon)
            and -90 <= lat <= 90 and -180 <= lon <= 180
            and (lat, lon) != (0, 0)):
        return lat, lon
    return None


def distance(a, b):
    if not a or not b:
        return None
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 6371000 * 2 * math.asin(min(1, math.sqrt(h)))


def readiness(manifest):
    countries = manifest.get("countries", [])
    by_cc = {c["country_code"]: c for c in countries}
    errors = [f"{cc}: recovery not complete" for cc in ("es", "jp")
              if by_cc.get(cc, {}).get("status") != "complete"]
    errors.extend(f"{c['country_code']}: {c.get('status', 'missing status')}"
                  for c in countries if c.get("status") not in {"complete", "failed", "unavailable"})
    if len(countries) != 33:
        errors.append(f"Expected 33 tracked directories; found {len(countries)}")
    return errors


def compare(cc, dartslive, phoenix):
    dn, pn = normalize(dartslive.get("n")), normalize(phoenix.get("name"))
    da, pa = normalize(dartslive.get("a"), True), normalize(phoenix.get("address"), True)
    ns, ads = similarity(dn, pn), similarity(da, pa)
    metres = distance(position(dartslive), position(phoenix, True))
    du, pu = units(dartslive.get("a")), units(phoenix.get("address"))
    conflicts = unit_conflict(du, pu)
    dnrs, pnrs = address_numbers(dartslive.get("a")), address_numbers(phoenix.get("address"))
    number_conflict = bool(dnrs and pnrs and dnrs != pnrs)
    linked = str(phoenix.get("dartslive_id", "")) == str(dartslive.get("id", ""))
    strong_name = distinct_name(phoenix.get("name")) and ns >= .94
    near = metres is not None and metres <= 250
    name_match = ns >= .7 and distinct_name(phoenix.get("name"))
    address_match = ads >= .95 and min(len(da), len(pa)) >= 12
    if not linked and not ((near and (name_match or address_match))
                           or (dn == pn and distinct_name(dn) and address_match)):
        return None
    reasons = [f"Normalized name similarity {ns:.3f}",
               f"Full-address similarity {ads:.3f}",
               f"Source-pin distance {metres:.1f} m" if metres is not None else "A source coordinate is missing"]
    incomplete_unit = any(bool(du[k]) != bool(pu[k]) for k in du)
    confidence = "uncertain"
    if linked:
        confidence = "existing_link"
        reasons.append("Existing explicit provider link; not newly confirmed by this review")
    elif conflicts:
        reasons.append("Different explicit units/floors: likely separate premises; do not merge")
    elif incomplete_unit:
        reasons.append("Unit/floor appears in only one source; confirm the exact premises")
    elif number_conflict:
        reasons.append("Address numbers differ; check street/building numbers, branch and postcode")
    elif strong_name and address_match and metres is not None and metres <= 100 and phoenix.get("map_eligible", True):
        confidence = "high_confidence_candidate"
        reasons.append("Strong name and full-address agreement with nearby source pins; verify before merging")
    if metres is not None and metres > 250:
        reasons.append("Distant pins may be stale/misplaced or refer to another branch")
    if not strong_name:
        reasons.append("Name evidence is weak; a shared building is not identity evidence")
    return {
        "country_code": cc, "confidence": confidence,
        "distance_m": round(metres, 1) if metres is not None else None,
        "name_similarity": round(ns, 3), "address_similarity": round(ads, 3),
        "unit_conflict": conflicts, "unit_incomplete": incomplete_unit, "address_number_conflict": number_conflict,
        "reasons": reasons,
        "dartslive": {
            "source_id": dartslive.get("id"), "name": dartslive.get("n"),
            "address": dartslive.get("a"), "source_url": dartslive.get("url"),
            "latitude": dartslive.get("la"), "longitude": dartslive.get("lo"),
            "machines": {"DARTSLIVE2": dartslive.get("d2"), "DARTSLIVE3": dartslive.get("d3")},
            "units": du,
        },
        "phoenix": {
            key: phoenix.get(key) for key in
            ("source_id", "name", "address", "source_url", "latitude", "longitude",
             "machines", "machine_text", "map_eligible", "directory_eligible", "collected_at")
        } | {"units": pu},
    }


def candidates(cc, dl, ph):
    grid, names, ids = defaultdict(list), defaultdict(list), {}
    for i, d in enumerate(dl):
        ids[str(d["id"])] = i
        names[normalize(d.get("n"))].append(i)
        point = position(d)
        if point:
            grid[(math.floor(point[0]/.002), math.floor(point[1]/.002))].append(i)
    result = []
    for p in ph:
        # Administrative/private entries remain in source data, not public-venue match recommendations.
        if p.get("directory_eligible", True) is False:
            continue
        indices = set(names.get(normalize(p.get("name")), []))
        if str(p.get("dartslive_id", "")) in ids:
            indices.add(ids[str(p["dartslive_id"])])
        point = position(p, True)
        if point:
            x, y = (math.floor(v/.002) for v in point)
            dx = 2
            dy = min(40, math.ceil(300 / (222 * max(.05, math.cos(math.radians(point[0]))))) + 1)
            for a in range(x-dx, x+dx+1):
                for b in range(y-dy, y+dy+1):
                    indices.update(grid.get((a, b), []))
        for i in sorted(indices):
            candidate = compare(cc, dl[i], p)
            if candidate:
                result.append(candidate)
    # A many-to-one collision is evidence of ambiguity, not permission to merge a chain.
    dc = Counter(c["dartslive"]["source_id"] for c in result if c["confidence"] == "high_confidence_candidate")
    pc = Counter(c["phoenix"]["source_id"] for c in result if c["confidence"] == "high_confidence_candidate")
    for c in result:
        if c["confidence"] == "high_confidence_candidate" and (
                dc[c["dartslive"]["source_id"]] > 1 or pc[c["phoenix"]["source_id"]] > 1):
            c["confidence"] = "uncertain"
            c["reasons"].append("Competing strong candidate: resolve many-to-one source records first")
    return result


def md(value):
    return html.escape(str(value or "")).replace("|", "\\|").replace("\n", " ")


def source_link(record, label):
    url = record.get("source_url") or ""
    return f"[{label}]({url})" if url.startswith(("https://", "http://")) else f"{label}: source URL unavailable"


def write_review(root=ROOT, collection_idle_verified=False):
    if not collection_idle_verified:
        raise SystemExit("Verify no active/queued collection runs before generating a final review")
    manifest = json.loads((root/"data/phoenix/index.json").read_text())
    errors = readiness(manifest)
    if errors:
        raise SystemExit("Final review blocked: " + "; ".join(errors))
    rows, dl_total, ph_total, mapped = [], 0, 0, 0
    for country in manifest["countries"]:
        cc = country["country_code"]
        dl_file = root/f"data/{cc}.json"
        dl = json.loads(dl_file.read_text()) if dl_file.exists() else []
        # Only compare actual venue arrays, never unrelated data manifests.
        if not isinstance(dl, list):
            raise ValueError(f"Invalid DARTSLIVE venue feed: {cc}")
        payload = json.loads((root/country["file"]).read_text())
        ph = payload.get("venues", [])
        dl_total += len(dl)
        ph_total += len(ph)
        mapped += sum(v.get("map_eligible", False) and v.get("directory_eligible", True) for v in ph)
        rows.extend(candidates(cc, dl, ph))
    rows.sort(key=lambda c: ({"existing_link": 0, "high_confidence_candidate": 1, "uncertain": 2}[c["confidence"]],
                             c["country_code"], -(c["name_similarity"]+c["address_similarity"]),
                             c["phoenix"]["source_id"], c["dartslive"]["source_id"]))
    counts = Counter(c["confidence"] for c in rows)
    stamp = datetime.now(timezone.utc).isoformat()
    gaps = [c for c in manifest["countries"] if c["status"] != "complete"]
    payload = {"snapshot_at": stamp, "review_only": True, "collection_idle_verified": True,
               "method_version": 1, "coverage_gaps": gaps, "counts": dict(counts), "candidates": rows}
    report = [
        "# Ninja Darts cross-provider duplicate review", "",
        f"Snapshot: {stamp}. This is a review of collected provider records, not verification that a business is currently open. No listings were merged/deleted, no coordinates invented and no production counts changed.", "",
        "## Coverage", "",
        f"- **Collected snapshot**: {ph_total:,} Phoenix records, {mapped:,} map-eligible Phoenix records and {dl_total:,} DARTSLIVE records in overlapping tracked countries. DARTSLIVE-only countries outside the 33 Phoenix routes cannot be cross-compared.", 
        "- **Recovery gate**: Spain and Japan are each country-status complete. The publishing workflow also refuses to audit while a collection run is active/queued or a country is pending/partial.",
        "- **Held records**: Missing-coordinate records are retained without pins. Private/administrative records are retained but excluded from public-venue match recommendations.",
        "- **Freshness**: Per-record Phoenix collection dates are retained in the export. The original DARTSLIVE snapshot has no per-record collection timestamp; matching does not refresh those records.", "",
        "### Explicit source gaps", "",
    ]
    report += [f"- **{md(c['name'])} ({c['country_code']})**: {c['status']}. {md(c.get('note', ''))} [Official directory]({c['source_url']})." for c in gaps]
    if not gaps:
        report.append("All tracked public directory sources completed; this is not a census of every installation.")
    report += [
        "", "## Methodology", "",
        "- **Blocking**: Same-country comparison only. Search source pins within 250 m and exact normalized names across the country; missing/distant coordinates require exact name plus strong address evidence.",
        "- **Normalization**: Unicode NFKC/casefold, punctuation removal and a small English street-abbreviation dictionary. Japanese/Chinese characters are preserved rather than stripped.",
        "- **Premises evidence**: Compare full addresses including explicit units/floors. Different units/floors override nearby pins; missing unit information lowers confidence. Unit extraction is heuristic and does not cover every writing system.",
        "- **High-confidence candidates**: Distinctive name similarity at least 0.94, full-address similarity at least 0.95, pins within 100 m, no detected unit conflict/asymmetry, no conflicting address numbers and no competing strong match. These are candidates, not verified dual-provider venues.",
        "- **Uncertain candidates**: Weaker name/address evidence, different or omitted units, distant/stale pins, shared-address records or competing matches. Proximity alone is not enough. Generic names, chain branches and different businesses in one building must remain separate unless source evidence confirms otherwise.",
        "- **Existing links**: Explicit existing provider IDs are reported separately; this audit does not confer new confirmation. Every exported candidate preserves both source IDs, URLs, coordinates, addresses and inventories.",
        "- **Limitations**: Transliterations, renamed businesses and incomplete addresses can cause missed candidates. Similarity scores are string evidence, not calibrated probabilities. No external geocoder or inferred coordinate is used.", "",
        "## Findings", "",
        f"- **Existing provider links**: {counts['existing_link']:,}.",
        f"- **High-confidence duplicate candidates**: {counts['high_confidence_candidate']:,}; verify before merging.",
        f"- **Uncertain candidates**: {counts['uncertain']:,}; no automatic merge recommended.", "",
        "The full machine-readable evidence is in [candidate JSON](duplicate-review/candidates.json) and [candidate CSV](duplicate-review/candidates.csv). All candidate pairs are listed below with both original venue pages where supplied.", "",
    ]
    for group, title in (("existing_link", "Existing explicit links"), ("high_confidence_candidate", "High-confidence candidates"), ("uncertain", "Uncertain candidates")):
        report += [f"## {title}", ""]
        selected = [c for c in rows if c["confidence"] == group]
        if not selected:
            report += ["No records in this category.", ""]
        for index, c in enumerate(selected, 1):
            d, p = c["dartslive"], c["phoenix"]
            report += [
                f"### {c['country_code'].upper()}: {md(d['name'])} / {md(p['name'])}", "",
                f"- **DARTSLIVE**: {source_link(d, md(d['source_id']))}. {md(d['address'])}. Inventory: {md(json.dumps(d['machines'], ensure_ascii=False))}.",
                f"- **Phoenix**: {source_link(p, md(p['source_id']))}. {md(p['address'])}. Inventory: {md(p.get('machine_text') or json.dumps(p.get('machines'), ensure_ascii=False))}.",
                f"- **Evidence**: {'; '.join(c['reasons'])}.",
                "- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.", "",
            ]
    report += ["## Recommended next actions", "",
               "- **Review first**: Validate high-confidence candidates against both original pages and, where needed, the venue itself; check that both providers are currently present.",
               "- **Do not merge**: Shared buildings, different units/floors, weak names and many-to-one records need manual investigation. No automatic merge or deletion is part of this report.",
               "- **Coverage**: Treat failed/unavailable directories as unmeasured coverage. Retry only through a working public source or obtain an authorised provider feed; never report zero installations from a failed source.",
               "- **Maintenance**: Rerun this deterministic review after completed collection updates. Source changes can invalidate earlier suggestions.", ""]
    for target in OUTPUTS:
        (root/target).parent.mkdir(parents=True, exist_ok=True)
    (root/OUTPUTS[0]).write_text("\n".join(report), encoding="utf-8")
    (root/OUTPUTS[1]).write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    fields = ["country_code", "confidence", "distance_m", "name_similarity", "address_similarity",
              "dartslive_id", "dartslive_name", "dartslive_address", "dartslive_url", "dartslive_machines",
              "phoenix_id", "phoenix_name", "phoenix_address", "phoenix_url", "phoenix_machines", "reasons"]
    with (root/OUTPUTS[2]).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for c in rows:
            row = {k: c[k] for k in fields[:5]}
            for provider in ("dartslive", "phoenix"):
                record = c[provider]
                for short, full in (("id", "source_id"), ("name", "name"), ("address", "address"), ("url", "source_url"), ("machines", "machines")):
                    val = record.get(full)
                    row[f"{provider}_{short}"] = json.dumps(val, ensure_ascii=False) if short == "machines" else val
            row["reasons"] = "; ".join(c["reasons"])
            writer.writerow({k: ("'"+str(v) if str(v).lstrip().startswith(("=", "+", "-", "@")) else v) for k, v in row.items()})
    return {"snapshot_at": stamp, "counts": dict(counts), "coverage_gaps": len(gaps)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-ready", action="store_true")
    parser.add_argument("--collection-idle-verified", action="store_true",
                        help="Only pass after verifying no active/queued source collection runs")
    args = parser.parse_args()
    if args.check_ready:
        issues = readiness(json.loads((ROOT/"data/phoenix/index.json").read_text()))
        print("\n".join(issues) if issues else "ready")
        raise SystemExit(1 if issues else 0)
    print(json.dumps(write_review(collection_idle_verified=args.collection_idle_verified), ensure_ascii=False))
