import unittest
from DartsliveScraper import is_venue_website


class SourceLinkTests(unittest.TestCase):
    def test_corporate_footer_is_not_a_venue_website(self):
        self.assertFalse(is_venue_website("https://www.segasammy.co.jp/en/socialmediapolicy/"))
        self.assertFalse(is_venue_website("javascript:alert(1)"))

    def test_valid_venue_site_is_preserved(self):
        self.assertTrue(is_venue_website("https://www.xinyan-livehouse.sg"))
        self.assertTrue(is_venue_website("https://g.co/kgs/example"))


if __name__ == "__main__":
    unittest.main()
