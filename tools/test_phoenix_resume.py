import unittest
from phoenix_resume import continuation_routes


class ContinuationTests(unittest.TestCase):
    def partial(self, code="jp", attempt=0):
        return {"country_code": code, "status": "partial",
                "continuation_attempt": attempt,
                "note": "Checkpointed before runner time limit; resume with saved country cache"}

    def test_only_checkpointed_budget_stops_are_continued(self):
        countries = [self.partial(), self.partial("gb"), self.partial()]
        countries += [{"country_code": "fr", "status": "complete"},
                      {"country_code": "cn", "status": "failed"},
                      {"country_code": "ie", "status": "unavailable"},
                      {"country_code": "us", "status": "pending"},
                      {"country_code": "kr", "status": "partial", "note": "Unrelated condition"}]
        self.assertEqual(continuation_routes({"countries": countries}), ["jp", "uk"])

    def test_cap_and_country_validation(self):
        countries = [self.partial(attempt=3), self.partial("sg"),
                     self.partial("not-a-route"), self.partial("kr", attempt=2)]
        self.assertEqual(continuation_routes({"countries": countries}), ["kr"])

    def test_any_provider_block_prevents_automatic_dispatch(self):
        countries = [self.partial(), {"country_code": "us", "status": "blocked"}]
        self.assertEqual(continuation_routes({"countries": countries}), [])


if __name__ == "__main__":
    unittest.main()
