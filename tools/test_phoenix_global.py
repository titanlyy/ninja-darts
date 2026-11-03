"""Parser regression fixtures modelled on the fetched public country templates."""
import unittest
import json
from bs4 import BeautifulSoup
from phoenix_global import ROOT, in_country, listing_rows, machines_from, parse_detail, repair_nested_title, split_title
from build_phoenix_bounds import country_boxes


class ParserTests(unittest.TestCase):
    def test_duplicate_iso_features_are_aggregated(self):
        def feature(points):
            return {"properties": {"ISO_A2_EH": "ZZ"}, "geometry": {
                "type": "Polygon", "coordinates": [points],
            }}
        source = {"features": [
            feature([[0, 0], [1, 0], [1, 1], [0, 0]]),
            feature([[10, 10], [11, 10], [11, 11], [10, 10]]),
        ]}
        self.assertEqual(country_boxes(source, {"zz"})["zz"], [[0, 0, 1, 1], [10, 10, 11, 11]])

    def test_australian_source_pin_matches_sourced_geometry(self):
        bounds = json.loads((ROOT / "data/phoenix-country-bounds.json").read_text())["countries"]
        # Phoenix's Pelican RSL Club source coordinates, not invented geography.
        self.assertTrue(in_country({"latitude": -33.0689049, "longitude": 151.6445364}, bounds["au"]))

    def test_nested_country_city_prefix(self):
        self.assertEqual(split_title("[[MY]Kuala Lumpur]Q2 SNOOKER (KL)", "my"),
                         ("Q2 SNOOKER (KL)", "Kuala Lumpur"))
        self.assertEqual(split_title("[Central] Real Venue", "sg"), ("Real Venue", "Central"))
        self.assertEqual(split_title("Venue [VIP]", "my"), ("Venue [VIP]", ""))
        self.assertEqual(split_title("[Unclosed Venue", "my"), ("[Unclosed Venue", ""))
        soup = BeautifulSoup('''<a href="/my/shop/shopDetail?s_seq=46668"><dl>
          <dt>[[MY]Kuala Lumpur]Q2 SNOOKER (KL)</dt><dd>498 Jalan Tun Razak</dd>
          <dd class="machine">VSS 1 .</dd></dl></a>''', "html.parser")
        row = listing_rows(soup, "my", "https://www.phoenixdarts.com/my/shop/shopSearch")["46668"]
        self.assertEqual(row["region"], "Kuala Lumpur")
        self.assertEqual(row["name"], "Q2 SNOOKER (KL)")
        self.assertEqual(row["source_title"], "[[MY]Kuala Lumpur]Q2 SNOOKER (KL)")
        detail = BeautifulSoup('''<section id="subSection"><div class="pageTitle">
          <h2>[[MY]Kuala Lumpur]Q2 SNOOKER (KL)</h2></div></section>
          <input id="lat" value="3.13324"><input id="lag" value="101.71858">''', "html.parser")
        parsed = parse_detail(detail, row, "my")
        self.assertEqual(parsed["name"], "Q2 SNOOKER (KL)")
        self.assertEqual(parsed["region"], "Kuala Lumpur")
        self.assertEqual(parsed["source_title"], row["source_title"])

    def test_legacy_title_repair_is_idempotent(self):
        record = {"name": "Kuala Lumpur]Q2 SNOOKER (KL)", "region": "[MY", "source_id": "46668"}
        self.assertTrue(repair_nested_title(record, "my"))
        self.assertEqual(record["name"], "Q2 SNOOKER (KL)")
        self.assertEqual(record["region"], "Kuala Lumpur")
        self.assertEqual(record["title_repair"]["previous_name"], "Kuala Lumpur]Q2 SNOOKER (KL)")
        self.assertEqual(record["source_id"], "46668")
        self.assertFalse(repair_nested_title(record, "my"))

    def test_country_sanity_check(self):
        self.assertTrue(in_country({"latitude": 1.3, "longitude": 103.8}, [[103.6, 1.2, 104.1, 1.5]]))
        self.assertFalse(in_country({"latitude": 40.7, "longitude": -74}, [[103.6, 1.2, 104.1, 1.5]]))
    def test_native_listing(self):
        soup = BeautifulSoup('''<a href="/kr/shop/shopDetail?s_seq=84814"><dl>
          <dt><span>[서울특별시]</span>짱게임(은평)</dt><dd>서울특별시 은평구</dd>
          <dd class="machine"><span>VSS</span> 2 .</dd></dl></a>''', "html.parser")
        rows = listing_rows(soup, "kr", "https://www.phoenixdarts.com/kr/shop/shopSearch")
        self.assertEqual(rows["84814"]["name"], "짱게임(은평)")
        self.assertEqual(rows["84814"]["region"], "서울특별시")
        self.assertEqual(rows["84814"]["machines"], [{"model": "VSS", "count": 2}])

    def test_japanese_details(self):
        soup = BeautifulSoup('''<input id="lat" value="38.262541"><input id="lag" value="140.8709566">
          <a href="/jp/shop/shopSearch_region?ac4_n=仙台市青葉区">city</a>
          <table><tr><th>住所</th><td>宮城県仙台市青葉区</td></tr>
          <tr><th>設置マシン </th><td><span>VSPhoenix X</span> 5台</td></tr></table>''', "html.parser")
        row = {"source_id": "89592", "name": "Dart＆Beer Pong GAME sendai",
               "address": "", "source_url": "https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89592",
               "machines": [], "machine_text": ""}
        record = parse_detail(soup, row, "jp")
        self.assertEqual(record["area"], "仙台市青葉区")
        self.assertEqual(record["machines"], [{"model": "VSPhoenix X", "count": 5}])
        self.assertEqual(record["address"], "宮城県仙台市青葉区")
        self.assertTrue(record["map_eligible"])

    def test_machine_models(self):
        self.assertEqual(machines_from("VSS 2 ., VSP 1 ."),
                         [{"model": "VSS", "count": 2}, {"model": "VSP", "count": 1}])
        self.assertEqual(machines_from("VSX:5"), [{"model": "VSX", "count": 5}])

    def test_hidden_heading_and_invalid_coordinate(self):
        soup = BeautifulSoup('''<h2>메인메뉴</h2><section id="subSection"><div class="pageTitle">
          <h2>[Central]Real Venue</h2></div></section>
          <input id="lat" value="NaN"><input id="lag" value="103.8">
          <table><tr><th>Address</th><td class="address">1 Main Street <a id="btnMap">[View Map]</a></td></tr></table>''', "html.parser")
        record = parse_detail(soup, {"name": "Real Venue", "address": "", "source_url": "https://www.phoenixdarts.com/sg/shop/shopDetail?s_seq=1",
                                    "machine_text": "", "machines": []}, "sg")
        self.assertEqual(record["name"], "Real Venue")
        self.assertEqual(record["address"], "1 Main Street")
        self.assertFalse(record["map_eligible"])
        self.assertIsNone(record["latitude"])


if __name__ == "__main__":
    unittest.main()
