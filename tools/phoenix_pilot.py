#!/usr/bin/env python3
"""Public Singapore Phoenix shop facts; single-threaded, paced, checkpointed.

No login, private endpoints, player data, descriptions, photos or access
control circumvention. Stop on 403/429; rerun later using cached facts.
Usage: python3 tools/phoenix_pilot.py --output <json> --cache <folder>
"""
import argparse
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE = "https://www.phoenixdarts.com"
START = BASE + "/sg/shop/shopSearch"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--cache", required=True)
    args = parser.parse_args()
    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers["User-Agent"] = "NinjaDarts-SingaporePilot/1.0 (public venue directory research)"
    last_request = 0

    def get(url):
        nonlocal last_request
        time.sleep(max(0, 1.2 - (time.monotonic() - last_request)))
        response = session.get(url, timeout=30)
        last_request = time.monotonic()
        if response.status_code in (403, 429):
            raise RuntimeError(f"Access/rate limit {response.status_code}; stopped without bypass: {url}")
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")

    listing_path = cache / "listing.json"
    if listing_path.exists():
        listing = json.loads(listing_path.read_text())
    else:
        listing = {}
        next_url = START
        visited = set()
        while next_url and next_url not in visited:
            if len(visited) >= 100:
                raise RuntimeError("Listing pagination guard reached")
            visited.add(next_url)
            soup = get(next_url)
            links = soup.select('a[href*="/sg/shop/shopDetail?s_seq="]')
            for link in links:
                match = re.search(r"s_seq=(\d+)", link["href"])
                if match:
                    listing[match[1]] = urljoin(BASE, link["href"])
            print(f"Listing page {len(visited)}: {len(listing)} unique venues", flush=True)
            nxt = soup.select_one(".paging a.btn_next")
            next_url = urljoin(BASE, nxt["href"]) if nxt else None
            if next_url and urlparse(next_url).netloc != urlparse(BASE).netloc:
                raise RuntimeError("Unexpected pagination host")
        if not listing:
            raise RuntimeError("No venue links extracted; refusing empty import")
        listing_path.write_text(json.dumps(listing, indent=2))

    records = []
    for sid, url in listing.items():
        factfile = cache / f"{sid}.json"
        if factfile.exists() and json.loads(factfile.read_text()).get("parser_version") == 2:
            record = json.loads(factfile.read_text())
        else:
            soup = get(url)
            heading = soup.select_one("#subSection .pageTitle h2")
            if not heading:
                raise RuntimeError(f"Missing shop heading: {url}")
            name = re.sub(r"^\[[^]]+\]\s*", "", heading.get_text(" ", strip=True))
            fields = {}
            for row in soup.select("tr"):
                key = row.find("th")
                value = row.find("td")
                if key and value:
                    text = value.get_text(" ", strip=True)
                    if text:
                        fields[key.get_text(" ", strip=True).lower()] = text
            lat, lon = soup.select_one("#lat"), soup.select_one("#lag")
            latitude = float(lat["value"]) if lat and lat.get("value") else None
            longitude = float(lon["value"]) if lon and lon.get("value") else None
            # The provider's Singapore feed can contain invalid/mislocated pins.
            valid = latitude is not None and longitude is not None and 1.15 <= latitude <= 1.5 and 103.55 <= longitude <= 104.15
            machine_text = fields.get("machine installation", "")
            machines = [{"model": model, "count": int(count)}
                        for model, count in re.findall(r"([A-Z][A-Z0-9 +_-]*?)\s+(\d+)\s*\.", machine_text)]
            record = {
                "parser_version": 2,
                "provider": "phoenix", "source_id": sid, "country_code": "sg",
                "name": name, "address": re.sub(r"\[View Map\]", "", fields.get("address", "")).strip(),
                "latitude": latitude, "longitude": longitude, "map_eligible": valid,
                "machines": machines, "machine_text": machine_text,
                "off_days": fields.get("off days", ""), "website": fields.get("url", ""),
                "source_url": url,
                "collected_at": datetime.now(timezone.utc).isoformat(),
            }
            factfile.write_text(json.dumps(record, ensure_ascii=False, indent=2))
        records.append(record)
        print(f"{len(records)}/{len(listing)} {record['name']} | map={record['map_eligible']}", flush=True)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(records, ensure_ascii=False, indent=2))
    print(f"Saved {len(records)} records; mappable={sum(r['map_eligible'] for r in records)}", flush=True)


if __name__ == "__main__":
    main()
