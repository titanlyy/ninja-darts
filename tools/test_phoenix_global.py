"""Parser regression fixtures modelled on the fetched public country templates."""
import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, call, patch
from bs4 import BeautifulSoup
from phoenix_global import ROOT, AccessBlocked, Client, CollectionDeferred, collect, in_country, listing_rows, machines_from, parse_detail, repair_nested_title, save, split_title
from build_phoenix_bounds import country_boxes


class ParserTests(unittest.TestCase):
    def row(self, sid, route="es"):
        return {"source_id": str(sid), "name": f"Venue {sid}", "address": f"{sid} Main St",
                "source_url": f"https://www.phoenixdarts.com/{route}/shop/shopDetail?s_seq={sid}",
                "machines": [{"model": "VSS", "count": 1}], "machine_text": "VSS 1 ."}

    def soup(self, html):
        return BeautifulSoup(html, "html.parser")

    def test_missing_coordinate_inputs_are_retained_not_mapped(self):
        row = self.row(1)
        for html in ("<main>Venue information</main>", '<input id="lat" value="40">'):
            with self.subTest(html=html):
                record = parse_detail(self.soup(html), row, "es")
                self.assertEqual(record["name"], row["name"])
                self.assertEqual(record["address"], row["address"])
                self.assertEqual(record["machines"], row["machines"])
                self.assertFalse(record["map_eligible"])
                self.assertTrue(record["directory_eligible"])
                self.assertIsNone(record["longitude"])
                self.assertEqual(record["detail_status"], "missing_coordinates")
                self.assertIn("Missing source coordinate", record["coordinate_review"])

    def test_directory_response_cannot_overwrite_original_venue(self):
        soup = self.soup('''<section id="subSection"><div class="pageTitle">
          <h2>Buscar local top</h2></div></section>
          <a href="/es/shop/shopDetail?s_seq=999"><dl><dt>Another shop</dt>
          <dd class="address">Wrong address</dd></dl></a>
          <table><tr><th>Address</th><td class="address">Another address</td></tr>
          <tr><th>Machine installation</th><td>VSP 99 .</td></tr></table>''')
        row = self.row(1)
        record = parse_detail(soup, row, "es")
        for key in ("name", "address", "machines", "machine_text", "source_id", "source_url"):
            self.assertEqual(record[key], row[key])
        self.assertFalse(record["map_eligible"])
        self.assertIsNone(record["latitude"])
        self.assertIsNone(record["longitude"])
        self.assertEqual(record["detail_status"], "directory_response")

    def test_cached_details_survive_missing_coordinates_and_rerun(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cache = root / "cache"
            rows = {str(sid): self.row(sid) for sid in (1, 2, 3)}
            original = parse_detail(self.soup('<input id="lat" value="40"><input id="lag" value="-3">'),
                                    rows["1"], "es")
            save(root / "data/phoenix/es.json", {"coverage": {"status": "failed"}, "venues": [original]})
            save(cache / "es/listing.json", {"rows": rows, "visited": ["saved-page"],
                                            "next": None, "complete": True})
            client = Mock()
            client.get.side_effect = [self.soup("<main>No coordinates</main>"),
                                      self.soup('<input id="lat" value="41"><input id="lag" value="-4">')]
            with patch("phoenix_global.ROOT", root):
                collect("es", cache, client)
            self.assertEqual(client.get.call_args_list,
                             [call(rows["2"]["source_url"]), call(rows["3"]["source_url"])])
            result = json.loads((root / "data/phoenix/es.json").read_text())
            self.assertEqual(result["coverage"]["status"], "complete")
            self.assertEqual(result["coverage"]["collected"], 3)
            self.assertEqual(result["coverage"]["mapped"], 2)
            self.assertEqual(result["venues"][0], original)
            self.assertFalse(result["venues"][1]["map_eligible"])
            client.get.reset_mock(side_effect=True)
            client.get.side_effect = AssertionError("A cached source page must not be fetched again")
            with patch("phoenix_global.ROOT", root):
                collect("es", cache, client)
            client.get.assert_not_called()
            again = json.loads((root / "data/phoenix/es.json").read_text())
            self.assertEqual(again["venues"], result["venues"])

    def test_japan_pagination_resumes_at_saved_next_page(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, rows = Path(temporary), {"1": self.row(1, "jp")}
            cache = root / "cache"
            next_page = "https://vs.phoenixdarts.com/jp/shop/shopSearch_terms/page/117"
            save(cache / "jp/listing.json", {"rows": rows,
                 "visited": [f"saved-page-{i}" for i in range(116)],
                 "next": next_page, "complete": False})
            original = parse_detail(self.soup('<input id="lat" value="35"><input id="lag" value="139">'),
                                    rows["1"], "jp")
            save(cache / "jp/1.json", original)
            page = self.soup('''<a href="/jp/shop/shopDetail?s_seq=2"><dl>
              <dt>Venue 2</dt><dd>Tokyo</dd></dl></a>''')
            client = Mock()
            client.get.side_effect = [page, self.soup('<input id="lat" value="35"><input id="lag" value="139">')]
            with patch("phoenix_global.ROOT", root):
                collect("jp", cache, client)
            self.assertEqual(client.get.call_args_list, [
                call(next_page), call("https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=2")])
            result = json.loads((root / "data/phoenix/jp.json").read_text())
            self.assertEqual(result["coverage"]["listing_pages"], 117)
            self.assertEqual(result["coverage"]["status"], "complete")
            self.assertEqual(result["coverage"]["collected"], 2)
            self.assertEqual(result["venues"][0], original)

    def test_access_block_still_stops_after_retaining_coordinate_hold(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, rows = Path(temporary), {str(sid): self.row(sid) for sid in (1, 2)}
            cache = root / "cache"
            save(cache / "es/listing.json", {"rows": rows, "visited": ["saved-page"],
                                            "next": None, "complete": True})
            client = Mock()
            client.get.side_effect = [self.soup("<main>No coordinates</main>"),
                                      AccessBlocked("HTTP 429; stopped without bypass")]
            with patch("phoenix_global.ROOT", root), self.assertRaises(AccessBlocked):
                collect("es", cache, client)
            result = json.loads((root / "data/phoenix/es.json").read_text())
            self.assertEqual(result["coverage"]["status"], "blocked")
            self.assertEqual(result["coverage"]["collected"], 1)
            self.assertEqual(result["venues"][0]["source_id"], "1")
            self.assertFalse(result["venues"][0]["map_eligible"])

    def test_soft_budget_stops_before_another_source_request(self):
        client = Client(1.2)
        client.deadline = -1
        with patch.object(client.session, "get") as get:
            with self.assertRaises(CollectionDeferred):
                client.get("https://www.phoenixdarts.com/my/shop/shopSearch")
            get.assert_not_called()

    def test_deferred_collection_exports_partial_not_complete(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            client = Mock()
            client.get.side_effect = CollectionDeferred("Checkpointed for resumption")
            with patch("phoenix_global.ROOT", root):
                collect("my", root / "cache", client)
            result = json.loads((root / "data/phoenix/my.json").read_text())
            self.assertEqual(result["coverage"]["status"], "partial")
            self.assertEqual(result["coverage"]["collected"], 0)
            self.assertIn("resumption", result["coverage"]["note"])
            self.assertEqual(result["coverage"]["continuation_attempt"], 0)
            with patch("phoenix_global.ROOT", root):
                collect("my", root / "cache", client)
            resumed = json.loads((root / "data/phoenix/my.json").read_text())
            self.assertEqual(resumed["coverage"]["continuation_attempt"], 1)

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
