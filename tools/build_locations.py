#!/usr/bin/env python3
"""Add geography from collected source fields without changing venue snapshots.

US, Canadian and Australian locality names are extracted only from an explicit
comma-delimited city, state/province and postal-code sequence. No geocoding,
nearest-city approximation or inferred French city names are used.
"""
import argparse
import csv
import json
import re
from pathlib import Path


def locality(row):
    cc = row["region_code"]
    area = row.get("medium_region", "").strip()
    if area:
        return area, "provider_medium_region"
    patterns = {
        "us": r",\s*([^,]+),\s*(?:[A-Z]{2}|Hawaii|Washington|California|Oregon|Colorado)\s+\d{5}(?:-\d{4})?\b",
        "ca": r",\s*([^,]+),\s*[A-Z]{2}\s+[A-Z]\d[A-Z]\s*\d[A-Z]\d\b",
        "au": r",\s*([^,]+),\s*(?:VIC|NSW|QLD|WA|SA|TAS|ACT|NT)\s+\d{4}\b",
    }
    match = re.search(patterns.get(cc, r"(?!)"), row.get("address", ""), re.I)
    return (match.group(1).strip(), "explicit_address_locality") if match else ("", "")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    valid = {
        c["cc"]: {v["id"] for v in json.loads((root / f"data/{c['cc']}.json").read_text())}
        for c in json.loads((root / "data/index.json").read_text())
    }
    countries = {}
    canonical_localities = {}
    with open(args.csv, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cc, shop_id = row["region_code"], row["shop_id"]
            if shop_id not in valid.get(cc, set()):
                continue
            area, area_source = locality(row)
            region = row.get("large_region", "").strip()
            if area_source == "explicit_address_locality":
                area = re.sub(r"\s+", " ", area)
                key = (cc, region.casefold(), area.casefold())
                area = canonical_localities.setdefault(key, area)
            countries.setdefault(cc, {})[shop_id] = {
                "region": region, "area": area, "area_source": area_source,
            }
    output = {
        "description": "Source administrative areas; address-derived cities where explicit. Not reverse-geocoded.",
        "countries": countries,
    }
    (root / "data/locations.json").write_text(json.dumps(output, ensure_ascii=False, separators=(",", ":")))
    print(f"Location metadata for {sum(map(len, countries.values()))} original venue records")


if __name__ == "__main__":
    main()
