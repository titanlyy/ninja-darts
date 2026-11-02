#!/usr/bin/env python3
"""
Build script: converts DARTSLIVE scraper CSV output into the JSON data files
used by the Ninja Darts map app.

Usage:
    python3 tools/build_data.py [dartslive_shops.csv] [output_dir]

Reads the combined CSV (or per-country CSVs) and writes:
    data/index.json    -> country metadata (code, name, venue count, bounds)
    data/<cc>.json     -> venue array for each country

Venue records use compact keys to keep the payload small:
    id   shop_enc_id (DARTSLIVE)
    n    shop name
    g    genre
    a    address
    la   latitude
    lo   longitude
    st   nearest station(s)
    h    business hours
    ho   regular holidays
    w    website url
    ig   instagram
    tw   x/twitter
    fb   facebook
    d3   DARTSLIVE3 units
    d2   DARTSLIVE2 units
    L    official league venue (1/0)
    C    has campaign (1/0)
    url  DARTSLIVE shop page
"""

import csv
import json
import math
import os
import sys

COUNTRY_NAMES = {
    "jp": "Japan", "au": "Australia", "ca": "Canada", "cn": "China",
    "es": "Spain", "fi": "Finland", "fr": "France", "hk": "Hong Kong / Macau",
    "id": "Indonesia", "kr": "Korea", "my": "Malaysia", "nz": "New Zealand",
    "ph": "Philippines", "qa": "Qatar", "sg": "Singapore", "ch": "Switzerland",
    "tw": "Taiwan", "th": "Thailand", "us": "USA", "ae": "UAE",
    "gb": "United Kingdom",
}

FIELD_MAP = {
    "shop_id": "id", "shop_name": "n", "genre": "g", "address": "a",
    "latitude": "la", "longitude": "lo", "nearest_station": "st",
    "business_hours": "h", "regular_holidays": "ho", "website_url": "w",
    "instagram": "ig", "x_twitter": "tw", "facebook": "fb",
    "dartslive3_units": "d3", "dartslive2_units": "d2",
    "shop_page_url": "url",
}


def parse_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "dartslive_shops.csv"
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(out_dir, exist_ok=True)

    rows = []
    if os.path.isdir(src):
        for fn in sorted(os.listdir(src)):
            if fn.endswith(".csv"):
                with open(os.path.join(src, fn), encoding="utf-8") as f:
                    rows.extend(list(csv.DictReader(f)))
    else:
        with open(src, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

    countries = {}
    for r in rows:
        cc = r.get("region_code", "").strip().lower()
        if not cc:
            continue
        try:
            la = float(r.get("latitude") or 0)
            lo = float(r.get("longitude") or 0)
        except (TypeError, ValueError):
            continue
        if not (-90 <= la <= 90 and -180 <= lo <= 180) or (la == 0 and lo == 0):
            continue

        venue = {new: (r.get(old, "") or "").strip() for old, new in FIELD_MAP.items()}
        venue["la"] = la
        venue["lo"] = lo
        venue["d3"] = parse_int(r.get("dartslive3_units"))
        venue["d2"] = parse_int(r.get("dartslive2_units"))
        venue["L"] = 1 if r.get("has_official_league") == "Yes" else 0
        venue["C"] = 1 if r.get("has_campaign") == "Yes" else 0
        countries.setdefault(cc, []).append(venue)

    index = []
    for cc in sorted(countries):
        venues = countries[cc]
        lats = [v["la"] for v in venues]
        lons = [v["lo"] for v in venues]
        entry = {
            "cc": cc,
            "name": COUNTRY_NAMES.get(cc, cc.upper()),
            "count": len(venues),
            "bounds": [[min(lats), min(lons)], [max(lats), max(lons)]],
        }
        index.append(entry)
        with open(os.path.join(out_dir, f"{cc}.json"), "w", encoding="utf-8") as f:
            json.dump(venues, f, ensure_ascii=False, separators=(",", ":"))
        print(f"  {cc}: {len(venues)} venues")

    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
    print(f"Done: {sum(c['count'] for c in index)} venues across {len(index)} countries -> {os.path.abspath(out_dir)}")


if __name__ == "__main__":
    main()
