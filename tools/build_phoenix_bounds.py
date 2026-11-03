#!/usr/bin/env python3
"""Derive permissive per-polygon country boxes from sourced Natural Earth data."""
import json
from pathlib import Path
import requests
from phoenix_global import COUNTRIES, ROOT, cc_for, save

URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_0_countries.geojson"


def country_boxes(source, wanted):
    boxes = {}
    for feature in source["features"]:
        props = feature["properties"]
        code = props.get("ISO_A2_EH", props.get("ISO_A2", "")).lower()
        if code not in wanted:
            continue
        geometry = feature["geometry"]
        polygons = geometry["coordinates"] if geometry["type"] == "MultiPolygon" else [geometry["coordinates"]]
        # Multiple admin features can share an ISO code, e.g. Australia and
        # Ashmore/Cartier Islands. Retain all components, not just the last one.
        boxes.setdefault(code, [])
        for polygon in polygons:
            xs, ys = zip(*polygon[0])
            boxes[code].append([round(min(xs), 5), round(min(ys), 5), round(max(xs), 5), round(max(ys), 5)])
    if wanted - set(boxes):
        raise ValueError(f"Missing country geometry: {wanted - set(boxes)}")
    return boxes


def main():
    cache = ROOT.parent / "natural-earth-10m-countries.geojson"
    if not cache.exists():
        response = requests.get(URL, timeout=90)
        response.raise_for_status()
        cache.write_bytes(response.content)
    source = json.loads(cache.read_text())
    boxes = country_boxes(source, {cc_for(r) for r, _ in COUNTRIES})
    save(ROOT / "data/phoenix-country-bounds.json", {
        "source_url": URL, "source": "Natural Earth 1:10m Admin 0 countries",
        "method": "Bounding box per component polygon, with a permissive 0.3-degree margin applied by importer. Not cadastral or political-boundary verification.",
        "countries": boxes,
    })
    print(f"Saved {len(boxes)} country/region geometry checks")


if __name__ == "__main__":
    main()
