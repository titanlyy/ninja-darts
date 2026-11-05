import unittest
from review_duplicates import compare, normalize, units, readiness, candidates


class DuplicateReviewTests(unittest.TestCase):
    def records(self):
        dl = {"id": "d1", "n": "Example Darts", "a": "12 Example Rd #02-09 Singapore 123456",
              "la": 1.3, "lo": 103.8, "d2": 2, "d3": 1}
        ph = {"source_id": "p1", "name": "EXAMPLE DARTS", "address": "12 Example Road #02-09 Singapore 123456",
              "latitude": 1.30001, "longitude": 103.8, "directory_eligible": True}
        return dl, ph

    def test_unicode_preserved(self):
        self.assertEqual(normalize("快活ＣＬＵＢ 池袋"), "快活club池袋")
        self.assertNotEqual(normalize("東京"), normalize("大阪"))

    def test_strong_full_address_and_name(self):
        dl, ph = self.records()
        self.assertEqual(compare("sg", dl, ph)["confidence"], "high_confidence_candidate")

    def test_different_units_block_high_confidence(self):
        dl, ph = self.records()
        ph["address"] = ph["address"].replace("02-09", "03-09")
        result = compare("sg", dl, ph)
        self.assertTrue(result["unit_conflict"])
        self.assertEqual(result["confidence"], "uncertain")

    def test_missing_floor_is_uncertain(self):
        dl, ph = self.records()
        ph["address"] = ph["address"].replace("#02-09", "")
        self.assertEqual(compare("sg", dl, ph)["confidence"], "uncertain")

    def test_nearby_alone_is_not_candidate(self):
        dl, ph = self.records()
        ph.update(name="Entirely Different", address="88 Other Street")
        self.assertIsNone(compare("sg", dl, ph))

    def test_same_chain_next_door_is_not_high_confidence(self):
        dl, ph = self.records()
        ph["address"] = ph["address"].replace("12 Example", "13 Example")
        self.assertEqual(compare("sg", dl, ph)["confidence"], "uncertain")

    def test_stale_coordinates_and_missing_coordinates_are_not_high(self):
        dl, ph = self.records()
        ph["latitude"] = 2
        self.assertEqual(compare("sg", dl, ph)["confidence"], "uncertain")
        ph["latitude"] = None
        self.assertEqual(compare("sg", dl, ph)["confidence"], "uncertain")

    def test_multiple_strong_candidates_are_downgraded(self):
        dl, ph = self.records()
        another = dict(dl, id="d2")
        self.assertTrue(all(c["confidence"] == "uncertain" for c in candidates("sg", [dl, another], [ph])))

    def test_floor_parsing(self):
        self.assertEqual(units("Example 3Ｆ")["floors"], ["3"])
        self.assertEqual(units("東京都中央ビル3Ｆ")["floors"], ["3"])
        self.assertEqual(units("Level 6")["floors"], ["6"])

    def test_failed_japan_cannot_start_final_review(self):
        manifest = {"countries": [{"country_code": "es", "status": "complete"},
                                  {"country_code": "jp", "status": "failed"}]}
        self.assertIn("jp: recovery not complete", readiness(manifest))


if __name__ == "__main__":
    unittest.main()
