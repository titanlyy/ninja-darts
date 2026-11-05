import csv
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DirectoryDataTests(unittest.TestCase):
    def test_original_dartslive_ids_coordinates_and_counts(self):
        countries = json.loads((ROOT/"data/index.json").read_text())
        ids = set()
        for country in countries:
            rows = json.loads((ROOT/f"data/{country['cc']}.json").read_text())
            self.assertEqual(len(rows), country["count"], country["cc"])
            for row in rows:
                self.assertNotIn(row["id"], ids)
                ids.add(row["id"])
                self.assertTrue(row["url"].startswith("https://search.dartslive.com/"))
                self.assertTrue(math.isfinite(row["la"]) and -90 <= row["la"] <= 90)
                self.assertTrue(math.isfinite(row["lo"]) and -180 <= row["lo"] <= 180)
                self.assertNotEqual((row["la"], row["lo"]), (0, 0))

    def test_phoenix_exports_and_coverage_are_consistent(self):
        manifest = json.loads((ROOT/"data/phoenix/index.json").read_text())
        self.assertEqual(len(manifest["countries"]), 33)
        for country in manifest["countries"]:
            with self.subTest(country=country["country_code"]):
                if "file" not in country:
                    self.assertEqual(country["status"], "pending")
                    continue
                source = ROOT/country["file"]
                feed = json.loads(source.read_text())
                rows = feed["venues"]
                self.assertEqual(len(rows), country["collected"])
                self.assertEqual(len({r["source_id"] for r in rows}), len(rows))
                mapped = [r for r in rows if r.get("map_eligible") and r.get("directory_eligible", True)]
                self.assertEqual(len(mapped), country["mapped"])
                for record in mapped:
                    self.assertTrue(math.isfinite(record["latitude"]) and -90 <= record["latitude"] <= 90)
                    self.assertTrue(math.isfinite(record["longitude"]) and -180 <= record["longitude"] <= 180)
                    self.assertNotEqual((record["latitude"], record["longitude"]), (0, 0))
                if country["status"] == "complete":
                    self.assertEqual(len(rows), country["discovered"])
                with source.with_suffix(".csv").open(newline="", encoding="utf-8-sig") as handle:
                    csv_rows = list(csv.DictReader(handle))
                self.assertEqual(len(csv_rows), len(rows))
                self.assertEqual({r["source_id"] for r in csv_rows}, {r["source_id"] for r in rows})


if __name__ == "__main__":
    unittest.main()
