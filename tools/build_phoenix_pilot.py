#!/usr/bin/env python3
"""Build an additive Singapore Phoenix feed; conservative cross-brand matching.

Only exact normalized names with a pin within 100 m are auto-matched.
Other candidates require a reviewed source-ID mapping in --matches.
The original DARTSLIVE JSON files are never modified.
"""
import argparse
import csv
import json
import math
import re
from difflib import SequenceMatcher
from pathlib import Path


def norm(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def distance(a, b):
    return math.hypot(a["latitude"] - b["la"],
                      (a["longitude"] - b["lo"]) * math.cos(math.radians(a["latitude"]))) * 111320


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--matches", default="")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    phoenix = json.loads(Path(args.input).read_text())
    dartslive = json.loads((root / "data/sg.json").read_text())
    reviewed = json.loads(Path(args.matches).read_text()) if args.matches else {}
    review = []
    matched_ids = set()
    for p in phoenix:
        held_for_access_review = {
            "PHOENIXDARTS SG OFFICE", "TEST MACHINE FOR SINGAPORE",
            "FORTRESS MESS (WTD)", "SEMBAWANG CAMP",
            "WELLS SINGAPORE", "NCS PTE LTD",
        }
        p["directory_eligible"] = p["name"].strip().upper() not in held_for_access_review
        if not p["directory_eligible"]:
            p["exclusion_reason"] = "Test, office, workplace or camp listing; public visitor access requires verification"
        candidates = []
        if not p["name"] or norm(p["name"]) == "":
            raise ValueError(f"Invalid name: {p['source_id']}")
        for d in dartslive:
            if not p["map_eligible"]:
                continue
            dist = distance(p, d)
            sim = SequenceMatcher(None, norm(p["name"]), norm(d["n"])).ratio()
            if dist < 150 or sim > 0.65:
                candidates.append({"dartslive_id": d["id"], "name": d["n"],
                                   "address": d["a"], "distance_m": round(dist),
                                   "name_similarity": round(sim, 3)})
            if norm(p["name"]) == norm(d["n"]) and dist <= 100:
                p["dartslive_id"] = d["id"]
                p["match_reason"] = "Exact normalized name and coordinates within 100 m"
        if p["source_id"] in reviewed:
            match = reviewed[p["source_id"]]
            if match["dartslive_id"] not in {d["id"] for d in dartslive}:
                raise ValueError("Reviewed DARTSLIVE ID not found")
            p["dartslive_id"] = match["dartslive_id"]
            p["match_reason"] = match["reason"]
        if p.get("dartslive_id"):
            if p["dartslive_id"] in matched_ids:
                raise ValueError("Multiple Phoenix records match one venue; review required")
            matched_ids.add(p["dartslive_id"])
        review.append({"phoenix_id": p["source_id"], "name": p["name"],
                       "address": p["address"], "matched": p.get("dartslive_id"),
                       "candidates": sorted(candidates, key=lambda c: c["distance_m"])})
    output = {
        "scope": "Singapore pilot", "provider": "phoenix",
        "source": "https://www.phoenixdarts.com/sg/shop/shopSearch",
        "venues": phoenix,
    }
    (root / "data/phoenix-sg.json").write_text(json.dumps(output, ensure_ascii=False, indent=2))
    (root / "docs/phoenix-sg-match-review.json").write_text(json.dumps(review, ensure_ascii=False, indent=2))
    with (root / "data/phoenix-sg.csv").open("w", newline="") as f:
        fields = ["source_id", "name", "address", "latitude", "longitude", "map_eligible",
                  "directory_eligible", "exclusion_reason", "machine_text", "source_url",
                  "collected_at", "dartslive_id", "match_reason"]
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(phoenix)
    print(f"Phoenix: {len(phoenix)}, map eligible: {sum(p['map_eligible'] for p in phoenix)}, directory eligible: {sum(p['map_eligible'] and p['directory_eligible'] for p in phoenix)}, merged: {len(matched_ids)}")
    for r in review:
        if r["candidates"]:
            print(json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main()
