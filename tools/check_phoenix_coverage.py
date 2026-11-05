"""Fail a collection's completion check when a requested country is incomplete."""
import argparse
import json
from pathlib import Path


def requested_coverage(manifest, routes):
    countries = {c["country_code"]: c for c in manifest["countries"]}
    rows = [countries.get("gb" if r == "uk" else r,
                          {"name": r, "status": "missing", "collected": 0, "mapped": 0})
            for r in routes]
    return rows, all(c["status"] == "complete" for c in rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--countries", required=True)
    parser.add_argument("--manifest", default="data/phoenix/index.json")
    args = parser.parse_args()
    routes = json.loads(args.countries)
    if not isinstance(routes, list) or not routes or not all(isinstance(r, str) for r in routes):
        parser.error("--countries must be a nonempty JSON array of routes")
    rows, complete = requested_coverage(json.loads(Path(args.manifest).read_text()), routes)
    print("# Requested Phoenix country coverage\n")
    print("Source failures/unavailable directories are coverage gaps, not zero installations.\n")
    print("| Country | Status | Collected | Map eligible |\n|---|---|---:|---:|")
    for c in rows:
        print(f"| {c['name']} | {c['status']} | {c.get('collected', 0)} | {c.get('mapped', 0)} |")
    print("\n[Full coverage audit](https://github.com/titanlyy/ninja-darts/blob/main/docs/PHOENIX_COVERAGE.md)")
    raise SystemExit(0 if complete else 1)


if __name__ == "__main__":
    main()
