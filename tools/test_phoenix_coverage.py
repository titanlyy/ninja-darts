import unittest
from check_phoenix_coverage import requested_coverage


class CoverageTests(unittest.TestCase):
    def test_failed_country_is_not_complete_despite_saved_records(self):
        manifest = {"countries": [{"country_code": "es", "name": "Spain", "status": "complete"},
                                  {"country_code": "jp", "name": "Japan", "status": "failed", "collected": 100}]}
        self.assertFalse(requested_coverage(manifest, ["es", "jp"])[1])
        self.assertTrue(requested_coverage(manifest, ["es"])[1])

    def test_partial_unavailable_and_missing_are_explicit_gaps(self):
        manifest = {"countries": [{"country_code": "jp", "name": "Japan", "status": "partial"},
                                  {"country_code": "bn", "name": "Brunei", "status": "unavailable"}]}
        for route in ["jp", "bn", "xx"]:
            self.assertFalse(requested_coverage(manifest, [route])[1])

    def test_uk_route_uses_gb_feed(self):
        manifest = {"countries": [{"country_code": "gb", "name": "United Kingdom", "status": "complete"}]}
        self.assertTrue(requested_coverage(manifest, ["uk"])[1])


if __name__ == "__main__":
    unittest.main()
