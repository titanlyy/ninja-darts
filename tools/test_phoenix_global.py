"""Parser regression fixtures modelled on the fetched public country templates."""
import unittest
from bs4 import BeautifulSoup
from phoenix_global import listing_rows, machines_from, parse_detail


class ParserTests(unittest.TestCase):
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
