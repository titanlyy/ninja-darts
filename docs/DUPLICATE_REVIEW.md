# Ninja Darts cross-provider duplicate review

Snapshot: 2026-11-05T18:17:25.056151+00:00. This is a review of collected provider records, not verification that a business is currently open. No listings were merged/deleted, no coordinates invented and no production counts changed.

## Coverage

- **Collected snapshot**: 13,397 Phoenix records, 13,300 map-eligible Phoenix records and 6,843 DARTSLIVE records in overlapping tracked countries. DARTSLIVE-only countries outside the 33 Phoenix routes cannot be cross-compared.
- **Recovery gate**: Spain and Japan are each country-status complete. The publishing workflow also refuses to audit while a collection run is active/queued or a country is pending/partial.
- **Held records**: Missing-coordinate records are retained without pins. Private/administrative records are retained but excluded from public-venue match recommendations.
- **Freshness**: Per-record Phoenix collection dates are retained in the export. The original DARTSLIVE snapshot has no per-record collection timestamp; matching does not refresh those records.

### Explicit source gaps

- **Brunei (bn)**: unavailable. Public directory returned no usable venue rows; not proof of zero installations [Official directory](https://www.phoenixdarts.com/bn/shop/shopSearch).
- **United Arab Emirates (ae)**: unavailable. Public directory returned no usable venue rows; not proof of zero installations [Official directory](https://www.phoenixdarts.com/ae/shop/shopSearch).
- **China (cn)**: failed. HTTPConnectionPool(host=&#x27;www.phoenixdartcn.com&#x27;, port=80): Max retries exceeded with url: /cn (Caused by NameResolutionError(&quot;HTTPConnection(host=&#x27;www.phoenixdartcn.com&#x27;, port=80): Failed to resolve &#x27;www.phoenixdartcn.com&#x27; ([Errno -2] Name or service not known)&quot;)) [Official directory](https://www.phoenixdarts.com/cn/shop/shopSearch).
- **Ireland (ie)**: unavailable. Public directory returned no usable venue rows; not proof of zero installations [Official directory](https://www.phoenixdarts.com/ie/shop/shopSearch).

## Methodology

- **Blocking**: Same-country comparison only. Search source pins within 250 m and exact normalized names across the country; missing/distant coordinates require exact name plus strong address evidence.
- **Normalization**: Unicode NFKC/casefold, punctuation removal and a small English street-abbreviation dictionary. Japanese/Chinese characters are preserved rather than stripped.
- **Premises evidence**: Compare full addresses including explicit units/floors. Different units/floors override nearby pins; missing unit information lowers confidence. Unit extraction is heuristic and does not cover every writing system.
- **High-confidence candidates**: Distinctive name similarity at least 0.94, full-address similarity at least 0.95, pins within 100 m, no detected unit conflict/asymmetry, no conflicting address numbers and no competing strong match. These are candidates, not verified dual-provider venues.
- **Uncertain candidates**: Weaker name/address evidence, different or omitted units, distant/stale pins, shared-address records or competing matches. Proximity alone is not enough. Generic names, chain branches and different businesses in one building must remain separate unless source evidence confirms otherwise.
- **Existing links**: Explicit existing provider IDs are reported separately; this audit does not confer new confirmation. Every exported candidate preserves both source IDs, URLs, coordinates, addresses and inventories.
- **Limitations**: Transliterations, renamed businesses and incomplete addresses can cause missed candidates. Similarity scores are string evidence, not calibrated probabilities. No external geocoder or inferred coordinate is used.

## Findings

- **Existing provider links**: 0.
- **High-confidence duplicate candidates**: 23; verify before merging.
- **Uncertain candidates**: 853; no automatic merge recommended.

The full machine-readable evidence is in [candidate JSON](duplicate-review/candidates.json) and [candidate CSV](duplicate-review/candidates.csv). All candidate pairs are listed below with both original venue pages where supplied.

## Existing explicit links

No records in this category.

## High-confidence candidates

### JP: 快活CLUB 国道2号西宮店 / 快活CLUB国道2号西宮店

- **DARTSLIVE**: [e15ba0f518ecd5cca3f63593b5358cc4](https://search.dartslive.com/jp/shop/e15ba0f518ecd5cca3f63593b5358cc4). 兵庫県西宮市六湛寺町1-13-3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [53279](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53279). 兵庫県西宮市六湛寺町1-13 3F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 69.5 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 静岡寿町店 / 快活CLUB 静岡寿町店

- **DARTSLIVE**: [dda6b2ef88f37b1f58d385ea46352d8f](https://search.dartslive.com/jp/shop/dda6b2ef88f37b1f58d385ea46352d8f). 静岡県静岡市駿河区寿町13-13. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [56124](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56124). 静岡県静岡市駿河区寿町13-13. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 2.9 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB ブランチ福岡下原店 / 快活CLUB ブランチ福岡下原店

- **DARTSLIVE**: [a624bf60ecf9ff00790ab824ce8730e5](https://search.dartslive.com/jp/shop/a624bf60ecf9ff00790ab824ce8730e5). 福岡県福岡市東区下原4-2-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [77826](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77826). 福岡県福岡市東区下原4-2-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 44.8 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 福岡行橋店 / 快活CLUB 福岡行橋店

- **DARTSLIVE**: [61baf91c1d2d3f8efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/61baf91c1d2d3f8efec1ae84bb28bd87). 福岡県行橋市西宮市4-1-12. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [77947](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77947). 福岡県行橋市西宮市4-1-12. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CAFE BAR FLOSSY / CAFE BAR FLOSSY

- **DARTSLIVE**: [b3931fb70e7e5cba0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b3931fb70e7e5cba0d9b047a20a7ba1e). 東京都中野区中央2-58-20. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91859](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91859). 東京都中野区中央2-58-20. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 1.1 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: yaya-矢屋-iriso terrace / yaya～矢屋～iriso terrace

- **DARTSLIVE**: [5f35277a0d9e2be05f9f3321c1147265](https://search.dartslive.com/jp/shop/5f35277a0d9e2be05f9f3321c1147265). 埼玉県狭山市南入曽563-7 ホワイトテラス2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92292](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92292). 埼玉県狭山市南入曽563-7 ホワイトテラス2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY江南高屋店 / JOYJOY 江南高屋店

- **DARTSLIVE**: [c656bed553fb47ca774c926eb736cb5a](https://search.dartslive.com/jp/shop/c656bed553fb47ca774c926eb736cb5a). 愛知県江南市高屋町西町51. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [92473](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92473). 愛知県江南市高屋町西町51. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY甲府山の手通り店 / JOYJOY 甲府山の手通り店

- **DARTSLIVE**: [4c28dea923adf66828032249b44395af](https://search.dartslive.com/jp/shop/4c28dea923adf66828032249b44395af). 山梨県甲府市大和町3-35. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [92590](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92590). 山梨県甲府市大和町3-35. Inventory: VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: NATURAL NINE立教通り店 / NATURAL NINE立教通り店

- **DARTSLIVE**: [16bea65440fad0730d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/16bea65440fad0730d9b047a20a7ba1e). 東京都豊島区西池袋3-33-17 東武西池袋サンライトマンション1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92975](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92975). 東京都豊島区西池袋3-33-17 東武西池袋サンライトマンション1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY岡崎大樹寺店 / JOYJOY 岡崎大樹寺店

- **DARTSLIVE**: [3c08433f1a4a8fe5a3f63593b5358cc4](https://search.dartslive.com/jp/shop/3c08433f1a4a8fe5a3f63593b5358cc4). 愛知県岡崎市鴨田町広元206. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [93377](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93377). 愛知県岡崎市鴨田町広元206. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: THROW CAT / THROW CAT

- **DARTSLIVE**: [14f48d95288a432228032249b44395af](https://search.dartslive.com/jp/shop/14f48d95288a432228032249b44395af). 大阪府枚方市津田駅前1-13-1-201. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94359](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94359). 大阪府枚方市津田駅前1-13-1-201. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Pink Tiger / PINK TIGER

- **DARTSLIVE**: [8fc4d65ce1d6b2020d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8fc4d65ce1d6b2020d9b047a20a7ba1e). 東京都中野区野方5-30-6 ひろきやビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [94501](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94501). 東京都中野区野方5-30-6 ひろきやビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 2.3 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link北朝霞店 / Link 北朝霞店

- **DARTSLIVE**: [b5279c47995667a5790ab824ce8730e5](https://search.dartslive.com/jp/shop/b5279c47995667a5790ab824ce8730e5). 埼玉県朝霞市西原1-5-5 シティイン北朝霞2F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [94870](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94870). 埼玉県朝霞市西原1-5-5 シティイン北朝霞 2F. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CAFE＆BAR Number5 / CAFE&amp;BAR Number5

- **DARTSLIVE**: [0376d5a0e88baa7fb21333aee1bd51e4](https://search.dartslive.com/jp/shop/0376d5a0e88baa7fb21333aee1bd51e4). 埼玉県上尾市平塚811-1-2. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [95040](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95040). 埼玉県上尾市平塚811-1-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 5.8 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: かじゅあるばぁ ぜろ。 / かじゅあるばぁぜろ。

- **DARTSLIVE**: [2358bbd55b3d4b7d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2358bbd55b3d4b7d0d9b047a20a7ba1e). 石川県河北郡津幡町字庄ウ63. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95368](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95368). 石川県河北郡津幡町字庄ウ63. Inventory: VSPhoenix X 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Shop TiTO 大阪梅田店 / Darts Shop TiTO大阪梅田店

- **DARTSLIVE**: [3f742433b5eea395b21333aee1bd51e4](https://search.dartslive.com/jp/shop/3f742433b5eea395b21333aee1bd51e4). 大阪府大阪市北区角田町1-10 くろふねビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97032](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97032). 大阪府大阪市北区角田町1-10　くろふねビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;FreeSpace GUILD / Darts＆FreeSpace GUILD

- **DARTSLIVE**: [7fedf860041d187c5f9f3321c1147265](https://search.dartslive.com/jp/shop/7fedf860041d187c5f9f3321c1147265). 新潟県柏崎市東長浜町3-24-2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97576](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97576). 新潟県柏崎市東長浜町3-24 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 三宮店 / ダイニングダーツバーBee 三宮店

- **DARTSLIVE**: [2a8eba4a1321305d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2a8eba4a1321305d0d9b047a20a7ba1e). 兵庫県神戸市中央区北長狭通1-9-3 レインボープラザビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [95221](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95221). 兵庫県神戸市中央区北長狭通１丁目９−３ レインボープラザビル 6F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.966; Source-pin distance 3.1 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: Shooters Cocktails / Shooters Cocktails

- **DARTSLIVE**: [19cc7265659b497928032249b44395af](https://search.dartslive.com/us/shop/19cc7265659b497928032249b44395af). 10761 Jamacha Blvd Ste C, Spring Valley, CA 91978, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92842](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=92842). 10761 Jamacha Blvd Ste C, Spring Valley, CA 91978. Inventory: VSS 1 ..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.967; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: HAWAIIAN BRIAN&#x27;S / Hawaiian Brian&#x27;s

- **DARTSLIVE**: [cb1ad8bf9fc1327458d385ea46352d8f](https://search.dartslive.com/us/shop/cb1ad8bf9fc1327458d385ea46352d8f). 1680 Kapiolani Boulevard, Honolulu, Hawaii 96814, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 7, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [55663](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=55663). 1680 Kapiolani  Blvd. Honolulu, Hawaii 96814. Inventory: VSS 1 ..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.965; Source-pin distance 4.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: Joycee&#x27;s Cocktails / Joycee’s Cocktails

- **DARTSLIVE**: [5913e7780797d989f454cb89828a1cfe](https://search.dartslive.com/us/shop/5913e7780797d989f454cb89828a1cfe). 1025 Elkelton Blvd., Spring Valley, CA 91977, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92857](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=92857). 1025 Elkelton Blvd Spring Valley, CA 91977. Inventory: VSS 2 ..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.964; Source-pin distance 48.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: DIRK&#x27;S NITECLUB / Dirk’s Nite Club

- **DARTSLIVE**: [2115518595db29ac58d385ea46352d8f](https://search.dartslive.com/us/shop/2115518595db29ac58d385ea46352d8f). 7662 Broadway, Lemon Grove, CA 91945, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92843](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=92843). 7662 Broadway Lemon Grove, CA 91945. Inventory: VSS 5 ..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.951; Source-pin distance 2.2 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: THE LANDING / The Landing

- **DARTSLIVE**: [15b7348988c339bc25d56fb0e5c39bac](https://search.dartslive.com/us/shop/15b7348988c339bc25d56fb0e5c39bac). 1185 E Main St, El Cajon, CA 92021, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98584](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=98584). 1185 E Main St, El Cajon, CA 92021. Inventory: VSS 2 ..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.951; Source-pin distance 0.0 m; Strong name and full-address agreement with nearby source pins; verify before merging.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

## Uncertain candidates

### CA: V-ZONE / Nu-Zone Tactical Laser Tag

- **DARTSLIVE**: [860645b16c8be538a3f63593b5358cc4](https://search.dartslive.com/ca/shop/860645b16c8be538a3f63593b5358cc4). 4411 Number 3 Rd, Unit 111, Richmond, BC V6X 2C3, Canada. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98530](https://www.phoenixdarts.com/ca/shop/shopDetail?s_seq=98530). 4411 Number 3 Rd Unit 111, Richmond, BC V6X 2C3, Canada. Inventory: VSS 4 ..
- **Evidence**: Normalized name similarity 0.296; Full-address similarity 1.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: LA CANTINA / LA CANTINA

- **DARTSLIVE**: [dda3f3f68c54c8ff790ab824ce8730e5](https://search.dartslive.com/fr/shop/dda3f3f68c54c8ff790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100063](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=100063). 45,AVENUE LELIEVRE	59120 LOOS	NORD PAS DE CALAIS. Inventory: VSS 1. VSP 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: LE SCORPION / LE SCORPION

- **DARTSLIVE**: [ddb29bd00eb743d058d385ea46352d8f](https://search.dartslive.com/fr/shop/ddb29bd00eb743d058d385ea46352d8f). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [49306](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=49306). 5,RUE DE LA DEMI-LUNE 86000 POITIERS. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: BISTR&#x27;O JAURES / BISTRO JAURES

- **DARTSLIVE**: [6933bf82fe0014e8fec1ae84bb28bd87](https://search.dartslive.com/fr/shop/6933bf82fe0014e8fec1ae84bb28bd87). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [49920](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=49920). 49,AV JEAN JAURES  86100 CHATELLERAULT  POITOU-CHARENTE. Inventory: VSS 1. VSP 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 5.6 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: BEER COUNTRY / BEER COUNTRY

- **DARTSLIVE**: [9072ba2fe8f8e5b5fec1ae84bb28bd87](https://search.dartslive.com/fr/shop/9072ba2fe8f8e5b5fec1ae84bb28bd87). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [61954](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=61954). PLACE DU 30 OCTOBRE	21000 DIJON BOURGOGNE. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 59.9 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: La Belle Equipe Cafe / LA BELLE EQUIPE CAFE

- **DARTSLIVE**: [5a05d40e9d37cac15f9f3321c1147265](https://search.dartslive.com/fr/shop/5a05d40e9d37cac15f9f3321c1147265). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86968](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=86968). 6,PLACE SAINTE BARBE 56500 MOUSTOIRAC bretagne. Inventory: VSP 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 1.9 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: LE CLEMENT / LE CLEMENT

- **DARTSLIVE**: [7f0218e3eca8c02e25d56fb0e5c39bac](https://search.dartslive.com/fr/shop/7f0218e3eca8c02e25d56fb0e5c39bac). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90849](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=90849). 59,RUE DE LA REPUBLIQUE 89100 SAINT CLEMENT. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 1.3 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: THE DART&#x27;S / THE DARTS

- **DARTSLIVE**: [4df2386c7b8338ac28032249b44395af](https://search.dartslive.com/fr/shop/4df2386c7b8338ac28032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94220](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=94220). 2,IMPASSE FELIX EBOUE	51430 TINQUEUX	PICARDIE. Inventory: VSX 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 9.1 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: LE FONTENOY / LE FONTENOY

- **DARTSLIVE**: [24960b1dcdce5fdfa3f63593b5358cc4](https://search.dartslive.com/fr/shop/24960b1dcdce5fdfa3f63593b5358cc4). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [95842](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=95842). 81,RUE DE LA REPUBLIQUE	60150 THOUROTTE	HAUTS DE France. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 22.7 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: LE SAINT OUEN / LE SAINT OUEN

- **DARTSLIVE**: [9060456e784c44ebf454cb89828a1cfe](https://search.dartslive.com/fr/shop/9060456e784c44ebf454cb89828a1cfe). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97453](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=97453). 28 RUE DE CANADIENS 27670 SAINT OUEN DU TILLEUL. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: ORGE ET HOUBLON (62) / ORGE ET HOUBLON

- **DARTSLIVE**: [46aec5bbd0177b5c5f9f3321c1147265](https://search.dartslive.com/fr/shop/46aec5bbd0177b5c5f9f3321c1147265). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [85315](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=85315). 118, BD EMILE BASLY 62300 LENS. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.929; Full-address similarity 0.000; Source-pin distance 8.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: CAFE DU MARCHE (29) / CAFE DU MARCHE

- **DARTSLIVE**: [430da2f2c62776f5f454cb89828a1cfe](https://search.dartslive.com/fr/shop/430da2f2c62776f5f454cb89828a1cfe). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100326](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=100326). 5,RUE DE L&#x27;&#x27;EGLISE	29290 SAINT RENAN	BRETAGNE. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.923; Full-address similarity 0.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: SKHMET / SEKHMET

- **DARTSLIVE**: [d9ac198631cfc98d28032249b44395af](https://search.dartslive.com/fr/shop/d9ac198631cfc98d28032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [94616](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=94616). 1,RUE MAURICE MALLET	17300 ROCHEFORT SUR MER	NOUVELLE AQUITAINE. Inventory: VSX 1..
- **Evidence**: Normalized name similarity 0.923; Full-address similarity 0.000; Source-pin distance 73.8 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: BEER US / BEER US 2

- **DARTSLIVE**: [1f0f57b7b08bf0b9790ab824ce8730e5](https://search.dartslive.com/fr/shop/1f0f57b7b08bf0b9790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [95059](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=95059). 46 Avenue de la loge, 86440 Migne Auxances. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.923; Full-address similarity 0.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: PADDY ROCK (77) / PADDY ROCK

- **DARTSLIVE**: [edb46ccb54a0dce0790ab824ce8730e5](https://search.dartslive.com/fr/shop/edb46ccb54a0dce0790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92573](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=92573). 27,ROUTE DE PARIS, 77930 CHAILLY EN BIERE,. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.900; Full-address similarity 0.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: BAR LE ZINC BLEU / LE ZINC BLEU

- **DARTSLIVE**: [188d4b390d30b6bdfec1ae84bb28bd87](https://search.dartslive.com/fr/shop/188d4b390d30b6bdfec1ae84bb28bd87). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [46654](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=46654). 12,RUE MARCEL GOULETTE 88130 CHARMES LORRAINE. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.870; Full-address similarity 0.000; Source-pin distance 18.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: BAR LE BOUFFAY / LE BOUFFAY

- **DARTSLIVE**: [13f208bcd6ad2d16790ab824ce8730e5](https://search.dartslive.com/fr/shop/13f208bcd6ad2d16790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52929](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=52929). PLACE DU BOUFFAY 56140 MALESTROIT bretagne. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.857; Full-address similarity 0.000; Source-pin distance 19.8 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: CAFE CHEZ GUSTIN / CHEZ GUSTIN

- **DARTSLIVE**: [60b10c3a394ea39428032249b44395af](https://search.dartslive.com/fr/shop/60b10c3a394ea39428032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [88682](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=88682). 5, PLACE EUGENE	62260 CAUCHY LA TOUR. Inventory: VSS 3. VSP 2..
- **Evidence**: Normalized name similarity 0.833; Full-address similarity 0.000; Source-pin distance 11.4 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: L&#x27;EMBUSCADE 62 / L&#x27;Ambuscade

- **DARTSLIVE**: [dfee97fab1e22858a3f63593b5358cc4](https://search.dartslive.com/fr/shop/dfee97fab1e22858a3f63593b5358cc4). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86862](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=86862). 2 bis rue Faidherbe  62130 Saint Pol sur Ternois. Inventory: VSP 1..
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.000; Source-pin distance 16.9 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: CAFE LA SCENE / CAFE LE NEW

- **DARTSLIVE**: [02c74523174fc769b21333aee1bd51e4](https://search.dartslive.com/fr/shop/02c74523174fc769b21333aee1bd51e4). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [87534](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=87534). 14, RUE DES SOUPIRANTS 62100 CALAIS. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.000; Source-pin distance 135.3 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: LA MINUTE BLONDE POITIER / LA MINUTE BLONDE

- **DARTSLIVE**: [7978f6d9abcbdb72790ab824ce8730e5](https://search.dartslive.com/fr/shop/7978f6d9abcbdb72790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [96602](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=96602). 3,RUE CHALONS	86000 POITIERS	NOUVELLE AQUITAINE. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.000; Source-pin distance 97.8 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: CAFE LE FLANDRE / LE FLANDRES

- **DARTSLIVE**: [e4937b854ca8afb3fec1ae84bb28bd87](https://search.dartslive.com/fr/shop/e4937b854ca8afb3fec1ae84bb28bd87). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98601](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=98601). 6,RUE DU MUSEE	59181 STEENWERCK	NORD PAS DE CALAIS. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.783; Full-address similarity 0.000; Source-pin distance 2.4 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: BAR DE L&#x27;AVENIR / L&#x27;AVENIR

- **DARTSLIVE**: [d7f575e61d4a533128032249b44395af](https://search.dartslive.com/fr/shop/d7f575e61d4a533128032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90782](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=90782). 2,HENT KERNAUDOUR 22140 BEGARD. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.737; Full-address similarity 0.000; Source-pin distance 33.3 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: TRIPLE DARTS PUB AND CO / TRIPLE DARTS

- **DARTSLIVE**: [70252a085708c69e774c926eb736cb5a](https://search.dartslive.com/fr/shop/70252a085708c69e774c926eb736cb5a). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [99637](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=99637). 151,RUE DES CHARMES 	59182 MONTIGNY EN OSTREVAN	NORD PAS DE CALAIS. Inventory: VSS 5..
- **Evidence**: Normalized name similarity 0.733; Full-address similarity 0.000; Source-pin distance 128.2 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### FR: ACROPOLIS / BOWLING ACROPOLIS

- **DARTSLIVE**: [8bc187785306128a28032249b44395af](https://search.dartslive.com/fr/shop/8bc187785306128a28032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [48368](https://www.phoenixdarts.com/fr/shop/shopDetail?s_seq=48368). 8, RUE DE L&#x27;ARTISANAT 59113 SECLIN. Inventory: VSS 7..
- **Evidence**: Normalized name similarity 0.720; Full-address similarity 0.000; Source-pin distance 33.9 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: C Union / C Union

- **DARTSLIVE**: [500965c22727685b58d385ea46352d8f](https://search.dartslive.com/hk/shop/500965c22727685b58d385ea46352d8f). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [15463](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=15463). 九龍窩打老道67號C一樓 何文田. Inventory: VSS 6..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 36.1 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Chop Bar / Chop Bar

- **DARTSLIVE**: [aa4d27ee8d1950befec1ae84bb28bd87](https://search.dartslive.com/hk/shop/aa4d27ee8d1950befec1ae84bb28bd87). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [42872](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=42872). 九龍尖沙咀漆咸道南57-59金馬倫中心3樓. Inventory: VSS 8..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 5.8 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: PISSING PUB / Pissing Pub

- **DARTSLIVE**: [1c7113d98cc71dc5b21333aee1bd51e4](https://search.dartslive.com/hk/shop/1c7113d98cc71dc5b21333aee1bd51e4). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [52675](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=52675). 香港 銅鑼灣 謝斐道460-462號 楊耀熾商業大廈 1樓. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 10.1 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: O2 Pub / O2 Pub

- **DARTSLIVE**: [8839bbc46356bbdcfec1ae84bb28bd87](https://search.dartslive.com/hk/shop/8839bbc46356bbdcfec1ae84bb28bd87). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [62116](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=62116). 九龍廟街262-264號地下. Inventory: VSS 4..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 50.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: NEXUS / Nexus

- **DARTSLIVE**: [db8d9081eda8f7f528032249b44395af](https://search.dartslive.com/hk/shop/db8d9081eda8f7f528032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [67695](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=67695). 旺角彌敦道594-596號旺角新城20樓. Inventory: VSS 3..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 10.4 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: La La Bar / Lala Bar

- **DARTSLIVE**: [f1d7aa1f32985587b21333aee1bd51e4](https://search.dartslive.com/hk/shop/f1d7aa1f32985587b21333aee1bd51e4). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 7}.
- **Phoenix**: [75867](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=75867). 旺角太平道3號一樓全層. Inventory: VSS 6. VSX 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Bar Pacific 77 / Bar Pacific 7

- **DARTSLIVE**: [db2385be6006e5f7a3f63593b5358cc4](https://search.dartslive.com/hk/shop/db2385be6006e5f7a3f63593b5358cc4). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [48082](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=48082). 九龍深水埗元洲街68號地下. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.957; Full-address similarity 0.000; Source-pin distance 244.5 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Penthouse 2 / Pent House

- **DARTSLIVE**: [68505958d096345d28032249b44395af](https://search.dartslive.com/hk/shop/68505958d096345d28032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [43619](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=43619). 太子通菜街216號地下及1樓. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.947; Full-address similarity 0.000; Source-pin distance 5.1 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Bar Pacific 27 / Bar Pacific 72

- **DARTSLIVE**: [91678be08af49dd225d56fb0e5c39bac](https://search.dartslive.com/hk/shop/91678be08af49dd225d56fb0e5c39bac). . Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [64991](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=64991). 九龍旺角塘尾道55號新興鋼具商業大廈地庫及地下部份 Kowloon. Inventory: VSS 3. VSX 1..
- **Evidence**: Normalized name similarity 0.917; Full-address similarity 0.000; Source-pin distance 205.5 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Bar Pacific 38 / Bar Pacific 63

- **DARTSLIVE**: [a6ccfc51d7092d36f454cb89828a1cfe](https://search.dartslive.com/hk/shop/a6ccfc51d7092d36f454cb89828a1cfe). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [94262](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=94262). 新界粉嶺聯和墟和泰街19號地下. Inventory: VSS 3..
- **Evidence**: Normalized name similarity 0.917; Full-address similarity 0.000; Source-pin distance 35.7 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Joe&#x27;s Billiards &amp; Bar (TST) / Joe&#x27;s Billiards &amp; Bar

- **DARTSLIVE**: [03c2d8ce1e291b68a3f63593b5358cc4](https://search.dartslive.com/hk/shop/03c2d8ce1e291b68a3f63593b5358cc4). . Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [15799](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=15799). 尖沙咀諾士佛台1號11-12樓. Inventory: VSP 6..
- **Evidence**: Normalized name similarity 0.914; Full-address similarity 0.000; Source-pin distance 99.2 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: M8 Cafe &amp; Pub / M8 Café &amp; Pub

- **DARTSLIVE**: [3fd62de69cb99913790ab824ce8730e5](https://search.dartslive.com/hk/shop/3fd62de69cb99913790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [51136](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=51136). 九龍紅磡馬頭圍道80號1樓. Inventory: VSS 10..
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.000; Source-pin distance 29.5 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Bar Pacific 16 / Bar Pacific 8

- **DARTSLIVE**: [ae850dae580a0efa790ab824ce8730e5](https://search.dartslive.com/hk/shop/ae850dae580a0efa790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [48690](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=48690). 九龍觀塘康寧道66號地下. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.870; Full-address similarity 0.000; Source-pin distance 242.7 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Bar Pacific 18 / Bar Pacific 69

- **DARTSLIVE**: [0277279093446bd5b21333aee1bd51e4](https://search.dartslive.com/hk/shop/0277279093446bd5b21333aee1bd51e4). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [48296](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=48296). 葵涌青山公路444-448號名堂大樓A座地下B&amp;C號舖. Inventory: VSS 2. VSX 1..
- **Evidence**: Normalized name similarity 0.833; Full-address similarity 0.000; Source-pin distance 248.4 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: C Plus Bar and Cafe / C Plus Bar &amp; Café

- **DARTSLIVE**: [55bd5faee5ce1d7825d56fb0e5c39bac](https://search.dartslive.com/hk/shop/55bd5faee5ce1d7825d56fb0e5c39bac). . Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85076](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=85076). 九龍旺角登打士街43號登打士廣場11樓. Inventory: VSS 4..
- **Evidence**: Normalized name similarity 0.815; Full-address similarity 0.000; Source-pin distance 16.8 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Quarter / Square Bar

- **DARTSLIVE**: [0b33af7bb8c9f849b21333aee1bd51e4](https://search.dartslive.com/hk/shop/0b33af7bb8c9f849b21333aee1bd51e4). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [15762](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=15762). 九龍西洋菜北街300號鉅成大廈2號舖. Inventory: VSS 2..
- **Evidence**: Normalized name similarity 0.750; Full-address similarity 0.000; Source-pin distance 77.1 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: ACE / Space

- **DARTSLIVE**: [e9ad3739dc81283158d385ea46352d8f](https://search.dartslive.com/hk/shop/e9ad3739dc81283158d385ea46352d8f). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85001](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=85001). 新界荃灣沙咀道121-123號地下. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.750; Full-address similarity 0.000; Source-pin distance 81.3 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: LA LA BAR 嘉芙 / Lala Bar - TST

- **DARTSLIVE**: [7652164b5490f63e790ab824ce8730e5](https://search.dartslive.com/hk/shop/7652164b5490f63e790ab824ce8730e5). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [92629](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=92629). 九龍尖沙咀漆咸道南53-55號嘉芙中心2樓. Inventory: VSS 6..
- **Evidence**: Normalized name similarity 0.737; Full-address similarity 0.000; Source-pin distance 7.9 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: Cave Darts &amp; Bar / Focus Darts &amp; Bar

- **DARTSLIVE**: [a66eb67c566fb16a5f9f3321c1147265](https://search.dartslive.com/hk/shop/a66eb67c566fb16a5f9f3321c1147265). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [86732](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=86732). 旺角彌敦道594-596號旺角新城6樓. Inventory: VSS 4..
- **Evidence**: Normalized name similarity 0.720; Full-address similarity 0.000; Source-pin distance 10.7 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: C C Party / M5 Party

- **DARTSLIVE**: [84079087094973c15f9f3321c1147265](https://search.dartslive.com/hk/shop/84079087094973c15f9f3321c1147265). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90562](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=90562). -. Inventory: VSP 1..
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.000; Source-pin distance 212.3 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### HK: IN BULL / Allin@Inbull

- **DARTSLIVE**: [346df7d7da2e8128b21333aee1bd51e4](https://search.dartslive.com/hk/shop/346df7d7da2e8128b21333aee1bd51e4). . Inventory: {&quot;DARTSLIVE2&quot;: 17, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [71701](https://www.phoenixdarts.com/hk/shop/shopDetail?s_seq=71701). 荃灣沙咀道364-366號萬象工業大廈11樓F室. Inventory: VSS 8. VSX 2..
- **Evidence**: Normalized name similarity 0.706; Full-address similarity 0.000; Source-pin distance 21.8 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 東広島西条店 / 快活CLUB 東広島西条店

- **DARTSLIVE**: [04083776fe838d7558d385ea46352d8f](https://search.dartslive.com/jp/shop/04083776fe838d7558d385ea46352d8f). 広島県東広島市西条土与丸6-1-16. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [55387](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=55387). 広島県東広島市西条土与丸6-1-16. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 671.6 m; Distant pins may be stale/misplaced or refer to another branch.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY刈谷駅前店 / JOYJOY 刈谷駅前店

- **DARTSLIVE**: [15f702ba83f2126bb21333aee1bd51e4](https://search.dartslive.com/jp/shop/15f702ba83f2126bb21333aee1bd51e4). 愛知県刈谷市桜町1-19. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94861](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94861). 愛知県刈谷市桜町1-19. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 1.000; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Linkつくば店 / Link つくば店

- **DARTSLIVE**: [70a24704ef11f1fc5f9f3321c1147265](https://search.dartslive.com/jp/shop/70a24704ef11f1fc5f9f3321c1147265). 茨城県つくば市竹園1-9-2 デイズタウンB1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [93710](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93710). 茨城県つくば市竹園1-9-2 デイズタウンB1F. Inventory: VSPhoenix X 2台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.976; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: POOL&amp;DARTS  JOKER / POOL&amp;DARTS JOKER

- **DARTSLIVE**: [33d22c47b4ba9c1b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/33d22c47b4ba9c1b0d9b047a20a7ba1e). 東京都品川区南品川3-5-35 OTビルII. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [91931](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91931). 東京都品川区南品川3-5-35 OTビルⅡ2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.974; Source-pin distance 2.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY津島店 / JOYJOY 津島店

- **DARTSLIVE**: [111e1b866b468b1c25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/111e1b866b468b1c25d56fb0e5c39bac). 愛知県津島市蛭間町字桝田289. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [97372](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97372). 愛知県津島市蛭間町字枡田289. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.933; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Lounge&amp;Dartsbar Ｗ / Lounge&amp;Dartsbar W

- **DARTSLIVE**: [ba948a5fb8324a88790ab824ce8730e5](https://search.dartslive.com/jp/shop/ba948a5fb8324a88790ab824ce8730e5). 東京都豊島区西池袋3-31-5 パークハイムウエスト1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [93346](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93346). 東京都豊島区西池袋３丁目３１－５パークハイムウエスト１階]. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.923; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BeeRUSH 大名店 / BeeRUSH 大名店

- **DARTSLIVE**: [c01be049b52d6f87774c926eb736cb5a](https://search.dartslive.com/jp/shop/c01be049b52d6f87774c926eb736cb5a). 福岡県福岡市中央区大名1-12-56 THE SHOPS DAIMYO2F. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [71749](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71749). 810-0041 福岡県福岡市中央区大名1-12-56 THE SHOPS DAIMYO 2F. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.901; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS BAR COZY / DARTS BAR COZY

- **DARTSLIVE**: [6cee1d555235cf390d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6cee1d555235cf390d9b047a20a7ba1e). 和歌山県和歌山市北ノ新地田町12番地 シャルマンマルナカビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [99841](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99841). 640-8359 和歌山県和歌山市北ノ新地田町12番地 シャルマンマルナカビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.899; Source-pin distance 2.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dining Cafe SHURIO / Dining Cafe SHURIO

- **DARTSLIVE**: [15dd57fc22e3733f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/15dd57fc22e3733f0d9b047a20a7ba1e). 東京都府中市寿町3-4-14 ホテルリブマックス府中 アネックス1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [49751](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49751). 183-0056 東京都府中市寿町3-4-14 ホテルリブマックス府中アネックス1F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.896; Source-pin distance 3.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: aobar / aobar

- **DARTSLIVE**: [3baceaade9fb8a8d5f9f3321c1147265](https://search.dartslive.com/jp/shop/3baceaade9fb8a8d5f9f3321c1147265). 新潟県新潟市中央区東大通1-6-11 東大通蔵ビル2F-202号室. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [72130](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72130). 950-0087 新潟県新潟市中央区東大通1-6-11　東大通蔵ビル2F-202号室. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.892; Source-pin distance 5.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar halo / Darts Bar halo

- **DARTSLIVE**: [09317e700f806ba45f9f3321c1147265](https://search.dartslive.com/jp/shop/09317e700f806ba45f9f3321c1147265). 埼玉県さいたま市見沼区東門前56-1 ハウステンボス2F-201. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90727](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90727). 337-0016 埼玉県さいたま市見沼区東門前56-1ハウステンボス2F 201. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.892; Source-pin distance 52.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar giant killing / Darts Bar GIANTKILLING

- **DARTSLIVE**: [f4d8731250800c2d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f4d8731250800c2d0d9b047a20a7ba1e). 大阪府大阪市中央区宗右衛門町4-4 エーデルプラッツェビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95993](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95993). 742-0084 大阪府大阪市中央区宗右衛門町4-4 エーデルプラッツェビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.892; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JIGEN / JIGEN

- **DARTSLIVE**: [f930d3921d0eeabd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f930d3921d0eeabd0d9b047a20a7ba1e). 埼玉県さいたま市大宮区下町1-5-1 第2マルハチビル204. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [100116](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100116). 330-0844 埼玉県さいたま市大宮区下町1-5-1 第2マルハチビル204. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 65.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 所沢店 / Link 所沢店

- **DARTSLIVE**: [6841c7ae76dd46f40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6841c7ae76dd46f40d9b047a20a7ba1e). 埼玉県所沢市日吉町10-19 Tokorozawa EX4F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [49398](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49398). 359-1123 埼玉県所沢市日吉町10-19 Tokorozawa EX4F. Inventory: VSPhoenix X 2台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Merry Grotto / Merry Grotto

- **DARTSLIVE**: [f26e2c7dfbaf739b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f26e2c7dfbaf739b0d9b047a20a7ba1e). 神奈川県川崎市川崎区東田町11-2 ジョイプラザビル101. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52526](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52526). 210-0005 神奈川県川崎市川崎区東田町11-2 ジョイプラザビル101. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY中川コロナワールド店 / JOYJOY 中川コロナワールド店

- **DARTSLIVE**: [13a689946fe1e027f454cb89828a1cfe](https://search.dartslive.com/jp/shop/13a689946fe1e027f454cb89828a1cfe). 愛知県名古屋市中川区江松3-110 中川コロナワールド2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [64399](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=64399). 454-0954 愛知県名古屋市中川区江松3-110 中川コロナワールド2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 12.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Barts HAT / Barts HAT

- **DARTSLIVE**: [33942a19d84e7fad0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/33942a19d84e7fad0d9b047a20a7ba1e). 千葉県千葉市中央区富士見2-18-10 MF8ビル2F201. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [69973](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69973). 260-0015 千葉県千葉市中央区富士見2-18-10 MF8ビル2F201. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 24.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 浦和店 / Link 浦和店

- **DARTSLIVE**: [ddae0a8d3bd80e605f9f3321c1147265](https://search.dartslive.com/jp/shop/ddae0a8d3bd80e605f9f3321c1147265). 埼玉県さいたま市浦和区高砂2-4-8 レインボー高砂ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [78300](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78300). 330-0063 埼玉県さいたま市浦和区高砂2-4-8 レインボー高砂ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar Take&#x27;s / Bar Take&#x27;s

- **DARTSLIVE**: [d4c96368669691aa0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d4c96368669691aa0d9b047a20a7ba1e). 神奈川県横浜市神奈川区神之木町2-45 スターホームズ1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8160](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8160). 221-0015 神奈川県横浜市神奈川区神之木町2-45 スターホームズ1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 11.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 盛岡大通店 / 快活CLUB 盛岡大通店

- **DARTSLIVE**: [abf103f43f1e07eb28032249b44395af](https://search.dartslive.com/jp/shop/abf103f43f1e07eb28032249b44395af). 岩手県盛岡市大通2-6-8 セントラルガーデンスクエア1～3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82127](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82127). 020-0022 岩手県盛岡市大通2-6-8 セントラルガーデンスクエア1～3F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE渋谷宇田川町店 / ビアポンバーGROVE渋谷宇田川町店

- **DARTSLIVE**: [d8afa344ebf9467cf454cb89828a1cfe](https://search.dartslive.com/jp/shop/d8afa344ebf9467cf454cb89828a1cfe). 東京都渋谷区宇田川町28-3 いちご渋谷文化村通りビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [84801](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84801). 150-0042 東京都渋谷区宇田川町28-3 いちご渋谷文化村通りビル6F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 2.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar iKnow / Bar iKnow

- **DARTSLIVE**: [68ab55095181b0410d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/68ab55095181b0410d9b047a20a7ba1e). 神奈川県横浜市神奈川区入江2-19-3 フェニックス大口2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89737](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89737). 221-0014 神奈川県横浜市神奈川区入江2-19-3 フェニックス大口2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Sports Cafe KAZ / Sports Cafe KAZ

- **DARTSLIVE**: [0bc042302926e5a30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0bc042302926e5a30d9b047a20a7ba1e). 東京都東村山市栄町2-39-18 フローラルマンションB1F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92711](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92711). 189-0013 東京都東村山市栄町2-39-18　フローラルマンションB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe&amp;Bar PLACE / Cafe&amp;Bar PLACE

- **DARTSLIVE**: [b15c3baed83d04dc58d385ea46352d8f](https://search.dartslive.com/jp/shop/b15c3baed83d04dc58d385ea46352d8f). 福岡県北九州市小倉南区下曽根3-4-1 アークガーデン303. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [95505](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95505). 800-0217 福岡県北九州市小倉南区下曽根3-4-1 アークガーデン303. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.885; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Music Bar S / Darts&amp;Music Bar S

- **DARTSLIVE**: [05a9e15a5d1af5580d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/05a9e15a5d1af5580d9b047a20a7ba1e). 神奈川県横浜市都筑区茅ヶ崎中央46-5 カネキビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [54527](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=54527). 224-0032 神奈川県横浜市都筑区茅ヶ崎中央46-5 カネキビルB1F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 福BON / 福BON

- **DARTSLIVE**: [f6e295309958bdcf790ab824ce8730e5](https://search.dartslive.com/jp/shop/f6e295309958bdcf790ab824ce8730e5). 神奈川県相模原市中央区上溝2161-3 銀鏡ハイツ101. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [58514](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58514). 252-0243 神奈川県相模原市中央区上溝2161-3 銀鏡ハイツ101. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 420S / 420S

- **DARTSLIVE**: [0394e96df95fd6eca3f63593b5358cc4](https://search.dartslive.com/jp/shop/0394e96df95fd6eca3f63593b5358cc4). 東京都渋谷区恵比寿南1-2-10 恵比寿ユニオンビル205. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [63705](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=63705). 150-0022 東京都渋谷区恵比寿南1-2-10 恵比寿ユニオンビル205. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 13.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BeeRUSH ミナミ店 / BeeRUSH ミナミ店

- **DARTSLIVE**: [209e5bdc9749bd0e28032249b44395af](https://search.dartslive.com/jp/shop/209e5bdc9749bd0e28032249b44395af). 大阪府大阪市中央区千日前2-9-17 アムザ1000-12F. Inventory: {&quot;DARTSLIVE2&quot;: 7, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72608](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72608). 542-0074 大阪府大阪市中央区千日前2-9-17 アムザ1000 12F. Inventory: VSPhoenix X-MAX 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 小倉北店 / 快活CLUB 小倉北店

- **DARTSLIVE**: [53aaaa278eaf364f774c926eb736cb5a](https://search.dartslive.com/jp/shop/53aaaa278eaf364f774c926eb736cb5a). 福岡県北九州市小倉北区中津口2-2-16 ASOBOX2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [7273](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7273). 802-0018 福岡県北九州市小倉北区中津口2-2-16 ASOBOX2F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 24.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Garden of Eden / Garden Of Eden

- **DARTSLIVE**: [dc4215cffc8266c30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/dc4215cffc8266c30d9b047a20a7ba1e). 愛知県名古屋市港区当知1-1511 グランドヒルズ森1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [74702](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=74702). 455-0804 愛知県名古屋市港区当知1-1511　グランドヒルズ森1F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 2.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 投げBAR / 投げBAR

- **DARTSLIVE**: [c8a8ff62f22135600d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c8a8ff62f22135600d9b047a20a7ba1e). 宮城県仙台市青葉区国分町2-1-10 阿部フォートビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89264](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89264). 980-0803 宮城県仙台市青葉区国分町2-1-10 阿部フォートビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Novel / Novel

- **DARTSLIVE**: [041ffbef693f46b2b21333aee1bd51e4](https://search.dartslive.com/jp/shop/041ffbef693f46b2b21333aee1bd51e4). 静岡県静岡市葵区両替町2-4-9 フィエスタ両替町ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89588](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89588). 420-0032 静岡県静岡市葵区両替町2­-4-­9 フィエスタ両替町ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 3.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;cafe Bar SORA. / Darts＆Cafe Bar SORA.

- **DARTSLIVE**: [3140e29e606f139bf454cb89828a1cfe](https://search.dartslive.com/jp/shop/3140e29e606f139bf454cb89828a1cfe). 福岡県北九州市小倉北区紺屋町11-12 ミューズビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89928](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89928). 802-0081 福岡県北九州市小倉北区紺屋町11-12　ミューズビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar Strad ROX / Bar Strad ROX

- **DARTSLIVE**: [9fd5c87f8a4e4376790ab824ce8730e5](https://search.dartslive.com/jp/shop/9fd5c87f8a4e4376790ab824ce8730e5). 新潟県新潟市中央区米山1-7-1 シーアンドディービル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90819](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90819). 950-0916 新潟県新潟市中央区米山1-7-1 シーアンドディービル1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: GLEEN CAFE EAST / GLEEN CAFE EAST

- **DARTSLIVE**: [b888e405b6e91baa0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b888e405b6e91baa0d9b047a20a7ba1e). 埼玉県越谷市南越谷1-13-3 GAYA113BLDG1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91678](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91678). 343-0845 埼玉県越谷市南越谷1-13-3 GAYA113BLDG1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツスポット投げPON！ / ダーツスポット投げPON!

- **DARTSLIVE**: [4e48219ac0e91ba50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4e48219ac0e91ba50d9b047a20a7ba1e). 神奈川県横浜市中区吉田町12-1 イセザキカザマビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [99643](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99643). 231-0041 神奈川県横浜市中区吉田町12-1 イセザキカザマビル3Ｆ. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.881; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Billiard &amp; Darts SUN 本店 / Billiard&amp;Darts SUN

- **DARTSLIVE**: [c56246b4c88e05850d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c56246b4c88e05850d9b047a20a7ba1e). 大阪府大阪市城東区森之宮2-4-29. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [99066](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99066). 大阪府大阪市城東区森ノ宮2-4-29. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.941; Full-address similarity 0.938; Source-pin distance 1.5 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 24.Van Quatre. / 24.Van Quatre

- **DARTSLIVE**: [8ed83ace221d64060d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8ed83ace221d64060d9b047a20a7ba1e). 東京都江戸川区西小岩1-27-20 小岩イーストビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [100232](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100232). 133-0057 東京都江戸川区西小岩1-27-20 小岩イーストビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 鹿児島中央店 / 自遊空間 鹿児島中央店

- **DARTSLIVE**: [da29b59044bb6ec825d56fb0e5c39bac](https://search.dartslive.com/jp/shop/da29b59044bb6ec825d56fb0e5c39bac). 鹿児島県鹿児島市東郡元町1-10 サンライトゾーン1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [5984](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5984). 890-0068 鹿児島県鹿児島市東郡元町1-10 サンライトゾーン1F. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 37.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 愛媛重信店 / 快活CLUB 愛媛重信店

- **DARTSLIVE**: [a7678752fce3b26b774c926eb736cb5a](https://search.dartslive.com/jp/shop/a7678752fce3b26b774c926eb736cb5a). 愛媛県松山市南梅本町1303-1 グルメアベニュー2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [62963](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=62963). 791-0245 愛媛県松山市南梅本町1303-1 グルメアベニュー2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar IHY / Bar IHY

- **DARTSLIVE**: [8102d3604b03c5b10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8102d3604b03c5b10d9b047a20a7ba1e). 大阪府守口市河原町12-8 富士林プラザ六番館305号. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [67299](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=67299). 570-0038 大阪府守口市河原町12-8 富士林プラザ六番館305号. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 2.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: No Limit / No Limit

- **DARTSLIVE**: [88174b6fd9ff5bc40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/88174b6fd9ff5bc40d9b047a20a7ba1e). 福岡県京都郡苅田町京町1-11-5 マキシム苅田ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7720](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7720). 800-0351 福岡県京都郡苅田町京町1-11-5　マキシム苅田ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 5.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE横浜店 / ビアポンバーGROVE横浜店

- **DARTSLIVE**: [e99b876551757f76f454cb89828a1cfe](https://search.dartslive.com/jp/shop/e99b876551757f76f454cb89828a1cfe). 神奈川県横浜市西区南幸2-17-8 横浜トラストビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [80358](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80358). 220-0005 神奈川県横浜市西区南幸2-17-8 横浜トラストビル6F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE新横浜店 / ビアポンバーGROVE新横浜店

- **DARTSLIVE**: [c0ae7c72442d7486fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/c0ae7c72442d7486fec1ae84bb28bd87). 神奈川県横浜市港北区新横浜2-3-11 第2徳永ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [83791](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83791). 222-0033 神奈川県横浜市港北区新横浜2-3-11 第2徳永ビル3F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 89.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE歌舞伎町店 / ビアポンバーGROVE歌舞伎町2号店

- **DARTSLIVE**: [a28b6b51e477d63d790ab824ce8730e5](https://search.dartslive.com/jp/shop/a28b6b51e477d63d790ab824ce8730e5). 東京都新宿区歌舞伎町1-18-9 ワモール歌舞伎町7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90803](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90803). 東京都新宿区歌舞伎町1-18-9 ワモール歌舞伎4F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.941; Full-address similarity 0.936; Source-pin distance 0.0 m; Different explicit units/floors: likely separate premises; do not merge.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 花鳥風月 YOKOHAMA / 花鳥風月YOKOHAMA

- **DARTSLIVE**: [5c26d0cda1f2ccd00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5c26d0cda1f2ccd00d9b047a20a7ba1e). 神奈川県横浜市青葉区しらとり台1-27 NAGビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9375](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9375). 227-0054 神奈川県横浜市青葉区しらとり台1-27 NAGビル1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Club Boo / Darts Club Boo

- **DARTSLIVE**: [1cddfd6c1892a90b774c926eb736cb5a](https://search.dartslive.com/jp/shop/1cddfd6c1892a90b774c926eb736cb5a). 東京都八王子市寺町51-3 セブンプラザビル4F-402. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94196](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94196). 192-0073 東京都八王子市寺町51-3 セブンプラザビル4F 402. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 2.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Harry&#x27;s Nest / Harry&#x27;s Nest

- **DARTSLIVE**: [f960263fdb1b9be20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f960263fdb1b9be20d9b047a20a7ba1e). 埼玉県富士見市西みずほ台1-1-8 みずほ台J・Jビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99969](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99969). 354-0018 埼玉県富士見市西みずほ台1-1-8 みずほ台J・Jビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.877; Source-pin distance 95.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: バレルカフェ Aims / バレルカフェAims

- **DARTSLIVE**: [489881ff07f3cebe0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/489881ff07f3cebe0d9b047a20a7ba1e). 千葉県習志野市大久保1-16-18 プラザグレミオ2E. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [58532](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58532). 275-0011 千葉県習志野市大久保1-16-18 プラザグレミオ2E. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 16.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 6HUSBAND / 6HUSBAND

- **DARTSLIVE**: [06f01c0024c4ee5c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/06f01c0024c4ee5c0d9b047a20a7ba1e). 大阪府大阪市此花区西九条3-12-17 みづほビル１階. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [67646](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=67646). 554-0012 大阪府大阪市此花区西九条3-12-17 みづほビル1階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: dining bar Leaf / Dining Bar Leaf

- **DARTSLIVE**: [a4d771b840f9321a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a4d771b840f9321a0d9b047a20a7ba1e). 東京都葛飾区新小岩1-40-11 サンフラットワン2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [69142](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69142). 124-0024 東京都葛飾区新小岩1-40-11 サンフラットワン2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Kplus / Kplus

- **DARTSLIVE**: [b79024f7d1acfbd50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b79024f7d1acfbd50d9b047a20a7ba1e). 東京都杉並区高円寺南4-7-4 タワー第7日東ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [70028](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70028). 166-0003 東京都杉並区高円寺南4-7-4 タワー第7日東ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB Luz湘南辻堂店 / 快活CLUB Luz湘南辻堂店

- **DARTSLIVE**: [ed1228848f40a639fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/ed1228848f40a639fec1ae84bb28bd87). 神奈川県藤沢市辻堂神台1-2-12 Luz湘南辻堂4F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7637](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7637). 251-0041 神奈川県藤沢市辻堂神台1-2-12　Luz湘南辻堂4F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 4.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: メディアカフェポパイ 高槻店 / メディアカフェポパイ高槻店

- **DARTSLIVE**: [a336a57b549915110d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a336a57b549915110d9b047a20a7ba1e). 大阪府高槻市高槻町18-1 セントラルマーケット2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [7979](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7979). 569-0803 大阪府高槻市高槻町18-1 セントラルマーケット2F. Inventory: VSPhoenix X-MAX 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 12.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR STRAD / BAR STRAD

- **DARTSLIVE**: [19a3dd6e339274b40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/19a3dd6e339274b40d9b047a20a7ba1e). 新潟県新潟市中央区笹口1-18-4 LOCUS駅南2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [80233](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80233). 950-0911 新潟県新潟市中央区笹口1-18-4 LOCUS駅南2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 6.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE池袋西口店 / ビアポンバー GROVE池袋西口店

- **DARTSLIVE**: [58ad98675ab98f5f5f9f3321c1147265](https://search.dartslive.com/jp/shop/58ad98675ab98f5f5f9f3321c1147265). 東京都豊島区西池袋１-17-7 池袋ルミエールビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [80266](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80266). 171-0021 東京都豊島区西池袋1-17-7 池袋ルミエールビルB1. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CROWBAR / CROW BAR

- **DARTSLIVE**: [a5a1a76754204ecd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a5a1a76754204ecd0d9b047a20a7ba1e). 神奈川県川崎市川崎区砂子2-6-5 日吉屋砂子ビル3Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [82670](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82670). 210-0006 神奈川県川崎市川崎区砂子2-6-5 日吉屋砂子ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 2.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Sole Reef / Sole Reef

- **DARTSLIVE**: [defb2027f230d2960d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/defb2027f230d2960d9b047a20a7ba1e). 神奈川県横浜市都筑区大熊町187-1 コマヤビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [84497](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84497). 224-0042 神奈川県横浜市都筑区大熊町187-1 コマヤビル1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 12.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE歌舞伎町店 / ビアポンバー GROVE 歌舞伎町店

- **DARTSLIVE**: [a28b6b51e477d63d790ab824ce8730e5](https://search.dartslive.com/jp/shop/a28b6b51e477d63d790ab824ce8730e5). 東京都新宿区歌舞伎町1-18-9 ワモール歌舞伎町7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [84752](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84752). 160-0021 東京都新宿区歌舞伎町1-18-9 ワモール歌舞伎町7F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 川越店 / Link 川越店

- **DARTSLIVE**: [bc2861456afef9c9fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/bc2861456afef9c9fec1ae84bb28bd87). 埼玉県川越市脇田町4-2 ドン・キホーテ川越東口店6F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [85251](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85251). 350-1122 埼玉県川越市脇田町4-2 ドン・キホーテ川越東口店6F. Inventory: VSPhoenix X 4台 VSPHOENIX S4 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar CLAN 金山店 / Darts Bar CLAN 金山店

- **DARTSLIVE**: [511881cb2f1fcde4a3f63593b5358cc4](https://search.dartslive.com/jp/shop/511881cb2f1fcde4a3f63593b5358cc4). 愛知県名古屋市中区金山4-1-24 金山コスモビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 10, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [88648](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88648). 460-0022 愛知県名古屋市中区金山4-1-24 金山コスモビル7F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 8.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE 小岩店 / ビアポンバー GROVE 小岩店

- **DARTSLIVE**: [245adf2c907470c228032249b44395af](https://search.dartslive.com/jp/shop/245adf2c907470c228032249b44395af). 東京都江戸川区南小岩7-26-10 第75東京ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91587](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91587). 133-0056 東京都江戸川区南小岩7-26-10 第75東京ビル 2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 1.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Three In The Black / Three In The Black

- **DARTSLIVE**: [c361e54f854440ea0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c361e54f854440ea0d9b047a20a7ba1e). 愛知県豊橋市花田町中ノ坪49-3 フジシロビル1F西. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9259](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9259). 441-8019 愛知県豊橋市花田町中ノ坪49-3 フジシロビル1F西. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 3.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ&amp;ビアポン BASE3 渋谷店 / ダーツ&amp;ビアポン BASE3 渋谷店

- **DARTSLIVE**: [fcf9a5aa75b2c4170d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/fcf9a5aa75b2c4170d9b047a20a7ba1e). 東京都渋谷区宇田川町33-12 J+RサイドRビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92864](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92864). 150-0042 東京都渋谷区宇田川町33-12 J+RサイドRビル7F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツショップ&amp;Bar KINGS / ダーツショップ＆Bar KINGS

- **DARTSLIVE**: [eee3adcf8acc404728032249b44395af](https://search.dartslive.com/jp/shop/eee3adcf8acc404728032249b44395af). 石川県金沢市片町2-21-30 エルビルウエストB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [94343](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94343). 920-0981 石川県金沢市片町2-21-30 エルビルウエストB1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Lounge Arrow / Darts Lounge Arrow

- **DARTSLIVE**: [900d94a1d3efd27e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/900d94a1d3efd27e0d9b047a20a7ba1e). 宮城県仙台市太白区鹿野2丁目16-16 佐金ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [96683](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96683). 9820023 宮城県仙台市太白区鹿野2丁目16-16 佐金ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar Rapt / Darts bar Rapt

- **DARTSLIVE**: [6bc27ff9dbd93499fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/6bc27ff9dbd93499fec1ae84bb28bd87). 東京都豊島区北大塚2-27-2 シューエイト北大塚3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97838](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97838). 170-0004 東京都豊島区北大塚２-２７−2 シューエイト北大塚　3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.873; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 三茶遊びbar Pointbreak 三軒茶屋 / 三茶遊びbar point break 三軒茶屋

- **DARTSLIVE**: [c6d1ef3f128c17060d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c6d1ef3f128c17060d9b047a20a7ba1e). 東京都世田谷区三軒茶屋2-14-12 三元ビル302. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [100587](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100587). 154-0024 東京都世田谷区三軒茶屋2-14-12 三元ビル302. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 14.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: T-R.I.P. / T-R.I.P.

- **DARTSLIVE**: [ae168eac601291c90d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ae168eac601291c90d9b047a20a7ba1e). 神奈川県大和市西鶴間1-13-17 壱番館ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [47732](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47732). 242-0005 神奈川県大和市西鶴間1-13-17 壱番館ビルB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 1.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE渋谷店 / ビアポンバーGROVE渋谷店

- **DARTSLIVE**: [3dc20cba6dd83fef0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3dc20cba6dd83fef0d9b047a20a7ba1e). 東京都渋谷区渋谷2-19-17 第106東京ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [50019](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50019). 150-0002 東京都渋谷区渋谷2-19-17 第106東京ビル4F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 6.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: palace / palace

- **DARTSLIVE**: [6cd771878d8b7f91a3f63593b5358cc4](https://search.dartslive.com/jp/shop/6cd771878d8b7f91a3f63593b5358cc4). 神奈川県横浜市鶴見区豊岡町18-22 日新ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53986](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53986). 964-0917 神奈川県横浜市鶴見区豊岡町18-22 日新ビル2F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 0.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: レインボーワールド 住道店 / レインボーワールド 住道店

- **DARTSLIVE**: [f165e158317a7edf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f165e158317a7edf0d9b047a20a7ba1e). 大阪府大東市赤井1-13-1 ポップタウン1番館3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [59196](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59196). 574-0046 大阪府大東市赤井1-13-1 ポップタウン1番館 3F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: zero R / ZERO-R

- **DARTSLIVE**: [3387652dd89035ccfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/3387652dd89035ccfec1ae84bb28bd87). 静岡県静岡市葵区両替町2-5-13 リッツビル2-3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [6836](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6836). 420-0032 静岡県静岡市葵区両替町2-5-13 リッツビル2 3F. Inventory: VSPhoenix X 3台 VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 6.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BARさんや / BARさんや

- **DARTSLIVE**: [3b6b6529899a38bd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3b6b6529899a38bd0d9b047a20a7ba1e). 東京都府中市宮西町1-17-3 ウエストビルB館3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [70257](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70257). 183-0022 東京都府中市宮西町1-17-3 ウエストビルB館3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 16.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: starry eye / Starry Eye

- **DARTSLIVE**: [bd0239a09f17d7f60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/bd0239a09f17d7f60d9b047a20a7ba1e). 東京都北区上十条2-7-11 ケーユープラザ十条2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7443](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7443). 114-0034 東京都北区上十条2-7-11 ケーユープラザ十条2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 4.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 和やかふぇ こころひとつ / 和やかふぇ　こころひとつ

- **DARTSLIVE**: [d21fdbb03227f7850d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d21fdbb03227f7850d9b047a20a7ba1e). 愛知県名古屋市中区大須1-7-5 アクセス175-1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7577](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7577). 460-0011 愛知県名古屋市中区大須1-7-5　アクセス175　1F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビリヤード クラブ レーヴ / ビリヤードクラブレーヴ

- **DARTSLIVE**: [7b197fdbb8b308600d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7b197fdbb8b308600d9b047a20a7ba1e). 東京都江戸川区瑞江2-3-5 第2田中工業所ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [75978](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75978). 132-0011 東京都江戸川区瑞江2-3-5 第2田中工業所ビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 5.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JackPot / JACKPOT

- **DARTSLIVE**: [e3a3dd3d29f44bb8b21333aee1bd51e4](https://search.dartslive.com/jp/shop/e3a3dd3d29f44bb8b21333aee1bd51e4). 埼玉県川越市中原町2-4-3 アーバンビル中原町2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [78752](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78752). 350-0042 埼玉県川越市中原町2-4-3 アーバンビル中原町2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 24.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe&amp;Bar Day&#x27;s / Cafe&amp;Bar Day&#x27;s

- **DARTSLIVE**: [e39fb25de241f5080d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e39fb25de241f5080d9b047a20a7ba1e). 栃木県宇都宮市江野町11-6 むぎくら中央ﾋﾞﾙ4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [79271](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79271). 320-0802 栃木県宇都宮市江野町11-6 むぎくら中央ビル4F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Cafe Che Bello / Darts Cafe Che Bello

- **DARTSLIVE**: [7809b5bc986b94db0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7809b5bc986b94db0d9b047a20a7ba1e). 神奈川県横浜市金沢区六浦東1-20-6 能登ﾋﾞﾙ2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [81724](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81724). 236-0037 神奈川県横浜市金沢区六浦東1-20-6 能登ビル2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 5.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ部KENⅡ / ダーツ部 KEN Ⅱ

- **DARTSLIVE**: [0d587d86eb9698420d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0d587d86eb9698420d9b047a20a7ba1e). 東京都調布市西つつじケ丘3-25-41 新井ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8250](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8250). 182-0006 東京都調布市西つつじケ丘3-25-41 新井ビル2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 9.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS&amp;BAR FAM / DARTS&amp;BAR FAM

- **DARTSLIVE**: [b5d688214a499e4bb21333aee1bd51e4](https://search.dartslive.com/jp/shop/b5d688214a499e4bb21333aee1bd51e4). 神奈川県藤沢市南藤沢8-3 プレジデント藤沢208. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [95299](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95299). 252-0807 神奈川県藤沢市南藤沢8-3 プレジデント藤沢208. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイナマイツ / ダイナマイツ

- **DARTSLIVE**: [cf4ddeb1a7557ec30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/cf4ddeb1a7557ec30d9b047a20a7ba1e). 東京都江戸川区西小岩1-21-16 やまとみビル3Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9872](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9872). 133-0057 東京都江戸川区西小岩1-21-16 やまとみビル3Ｆ. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.868; Source-pin distance 72.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Mile Stone Cafe LA / Mile Stone Cafe LA

- **DARTSLIVE**: [ae5fcf97a256417b774c926eb736cb5a](https://search.dartslive.com/jp/shop/ae5fcf97a256417b774c926eb736cb5a). 福岡県福岡市博多区美野島2-1-39 キャロメットパークビュー1F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89440](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89440). 812-0017 福岡県福岡市博多区美野島2-1-39 キャメロットパークビュー1F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.866; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE吉祥寺店 / ビアポンバー GROVE 吉祥寺店

- **DARTSLIVE**: [ab7d01d094b3f17bb21333aee1bd51e4](https://search.dartslive.com/jp/shop/ab7d01d094b3f17bb21333aee1bd51e4). 東京都武蔵野市吉祥寺本町1-8-10 KichijojiEx2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91290](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91290). 180-0004 東京都武蔵野市吉祥寺本町1-8-10 kichijoji exビル2F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.866; Source-pin distance 44.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Bar MEBIUS / Darts&amp;Bar MEBIUS

- **DARTSLIVE**: [13593f65dac75eae0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/13593f65dac75eae0d9b047a20a7ba1e). 神奈川県横浜市神奈川区西神奈川1-10-16 斉藤邦楽店ビル2F-A. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9883](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9883). 221-0822 神奈川県横浜市神奈川区西神奈川1-10-16 斉藤邦楽器店ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.866; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファンキータイム 追手筋店 / ファンキータイム追手筋店

- **DARTSLIVE**: [236b47bd42aa79050d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/236b47bd42aa79050d9b047a20a7ba1e). 高知県高知市追手筋1-3-1 ベルエポックビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10106](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10106). 780-0842 高知県高知市追手筋1-3-1 ベルエポックビル6F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 6.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: NEO BAATA / NEO BAATA

- **DARTSLIVE**: [bc253e03a66733750d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/bc253e03a66733750d9b047a20a7ba1e). 沖縄県那覇市識名1198-1 ネットマンガ館2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [42297](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42297). 902-0078 沖縄県那覇市識名1198-1 ネットマンガ館2F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 6.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 本川越店 / Link 本川越店

- **DARTSLIVE**: [10a78d141f3762bd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/10a78d141f3762bd0d9b047a20a7ba1e). 埼玉県川越市新富町1-19-2 第64東京ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [49399](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49399). 350-0043 埼玉県川越市新富町1-19-2 第64東京ビル4F. Inventory: VSPhoenix X 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 1.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: little shot little / little shot little

- **DARTSLIVE**: [3bdc3d4c652d3b590d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3bdc3d4c652d3b590d9b047a20a7ba1e). 東京都目黒区鷹番2-20-19 そしある学芸大3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [54528](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=54528). 152-0004 東京都目黒区鷹番2-20-19 そしある学芸大3F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Triple Crown 湘南 / Triple Crown 湘南

- **DARTSLIVE**: [2588afb68a70afb60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2588afb68a70afb60d9b047a20a7ba1e). 神奈川県藤沢市鵠沼花沢町1-16 千代田ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [56593](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56593). 251-0023 神奈川県藤沢市鵠沼花沢町1-16 千代田ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 3.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Shoot / Shoot

- **DARTSLIVE**: [5898fcbfbf3645a70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5898fcbfbf3645a70d9b047a20a7ba1e). 神奈川県小田原市西大友130 タカナシビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [57808](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=57808). 250-0212 神奈川県小田原市西大友130 タカナシビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 11.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: L-AMUSE / L-AMUSE

- **DARTSLIVE**: [756bd3d459a7bf710d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/756bd3d459a7bf710d9b047a20a7ba1e). 東京都葛飾区新小岩2-7-4 サンシティ新小岩2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [64755](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=64755). 124-0024 東京都葛飾区新小岩2-7-4 サンシティ新小岩2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE池袋東口店 / ビアポンバー GROVE池袋東口店

- **DARTSLIVE**: [ec15a6eb6dd0a58f774c926eb736cb5a](https://search.dartslive.com/jp/shop/ec15a6eb6dd0a58f774c926eb736cb5a). 東京都豊島区南池袋1-27-8 サンパレスビル9F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [70401](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70401). 171-0022 東京都豊島区南池袋1-27-8 サンパレスビル9F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 3.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 町屋 Zooooo / 町屋 Zooooo

- **DARTSLIVE**: [eedf7517fa26f7a05f9f3321c1147265](https://search.dartslive.com/jp/shop/eedf7517fa26f7a05f9f3321c1147265). 東京都荒川区荒川7-39-2 ミツトヨ町屋ビル3Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [73711](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73711). 116-0002 東京都荒川区荒川7-39-2 ミツトヨ町屋ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CAFE&amp;BAR ZERO-ONE / CAFE&amp;BAR ZERO-ONE

- **DARTSLIVE**: [c00d37131c00710d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c00d37131c00710d0d9b047a20a7ba1e). 青森県平川市柏木町藤山25-9 ザ・シティビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [83510](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83510). 036-0104 青森県平川市柏木町藤山25-9 ザ・シティビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bee Bee / BEE BEE

- **DARTSLIVE**: [904b811820c98b945f9f3321c1147265](https://search.dartslive.com/jp/shop/904b811820c98b945f9f3321c1147265). 沖縄県那覇市牧志2-3-20 アーバンコア牧志5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [88420](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88420). 900-0013 沖縄県那覇市牧志2-3-20 アーバンコア牧志5F. Inventory: VSPhoenix X 2台 VSPHOENIX S 8台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: WISH / WISH

- **DARTSLIVE**: [43f70bed08adf5a7790ab824ce8730e5](https://search.dartslive.com/jp/shop/43f70bed08adf5a7790ab824ce8730e5). 大阪府茨木市橋の内2-8-10 ドウエル橋の内1F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89214](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89214). 567-0805 大阪府茨木市橋の内2-8-10 ドウエル橋の内1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 2.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 室蘭中島サンプラザ店 / 自遊空間 室蘭中島サンプラザ店

- **DARTSLIVE**: [ec8d712ff53c08a1f454cb89828a1cfe](https://search.dartslive.com/jp/shop/ec8d712ff53c08a1f454cb89828a1cfe). 北海道室蘭市中島町3丁目29-1 サンプラザ2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [91185](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91185). 050-0074 北海道室蘭市中島町3丁目29-1 サンプラザ2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: C.STAND名古屋駅東口店 / C.STAND 名古屋駅東口店

- **DARTSLIVE**: [19504a99111aff580d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/19504a99111aff580d9b047a20a7ba1e). 愛知県名古屋市西区名駅3-11-2 サンタウン4F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91627](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91627). 451-0045 愛知県名古屋市西区名駅3-11-2 サンタウン4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツカフェ＆バー クルーセ / ダーツカフェ＆バー クルーセ

- **DARTSLIVE**: [229feb92e5d749350d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/229feb92e5d749350d9b047a20a7ba1e). 千葉県松戸市新松戸2-108 太陽新松戸ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9304](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9304). 270-0034 千葉県松戸市新松戸2-108 太陽新松戸ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 8.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 2bit / 2bit

- **DARTSLIVE**: [9ca710f19227f64f5f9f3321c1147265](https://search.dartslive.com/jp/shop/9ca710f19227f64f5f9f3321c1147265). 群馬県伊勢崎市下植木町34 RINOビル201. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [96926](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96926). 372-0024 群馬県伊勢崎市下植木町34 RINOビル 201. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.863; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JUSTICE / justice

- **DARTSLIVE**: [c1aeece4f7cc28820d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c1aeece4f7cc28820d9b047a20a7ba1e). 神奈川県横浜市港南区野庭町278-2 リーリーハイムA号. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100358](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100358). 234-0056 神奈川県横浜市港南区野庭町278-2 リリーハイムA号. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.862; Source-pin distance 13.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: NATURAL NINE NOGATA / NATURAL NINE NOGATA

- **DARTSLIVE**: [dd6f44bc62df59950d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/dd6f44bc62df59950d9b047a20a7ba1e). 東京都中野区野方5-19-13 第3ノーススタービルB1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [59563](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59563). 165-0027 東京都中野区野方5-19-13 第3ノーススタービルB1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.862; Source-pin distance 1.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバー GROVE綱島店 / ビアポンバー GROVE 綱島店

- **DARTSLIVE**: [c3c988cbdcffe93a774c926eb736cb5a](https://search.dartslive.com/jp/shop/c3c988cbdcffe93a774c926eb736cb5a). 神奈川県横浜市港北区綱島西1-7-8 第82東京ビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [88695](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88695). 223-0053 神奈川県横浜市港北区綱島西1-7-8 第82東京ビルB1F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.862; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: あらいふ / あらいふ

- **DARTSLIVE**: [441939912456db330d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/441939912456db330d9b047a20a7ba1e). 兵庫県姫路市十二所前町5 十二所前町クリスタルビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89836](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89836). 670-0911 兵庫県姫路市十二所前町5 十二所前クリスタルビル3F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.862; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 本八幡店 / Link 本八幡店

- **DARTSLIVE**: [23f11723acfb4a300d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/23f11723acfb4a300d9b047a20a7ba1e). 千葉県市川市南八幡4-4-5 ウィンズ本八幡2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [49394](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49394). 272-0023 千葉県市川市南八幡4-4-5 ウィンズ本八幡2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 2.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Irise 荻窪 / Irise荻窪

- **DARTSLIVE**: [beca90edd43c6f010d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/beca90edd43c6f010d9b047a20a7ba1e). 東京都杉並区西荻南3-15-13 高梨ビル202. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52522](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52522). 167-0053 東京都杉並区西荻南3-15-13 高梨ビル202. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 5.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Triple Crown / Triple Crown

- **DARTSLIVE**: [e6128a5a778358950d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e6128a5a778358950d9b047a20a7ba1e). 神奈川県川崎市中原区新城1-10-5 パールハイム新城111. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52523](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52523). 211-0044 神奈川県川崎市中原区新城1-10-5 パールハイム新城111号室. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dining Bar Arist / Dining Bar Arist

- **DARTSLIVE**: [9e77e0660f8869a2fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/9e77e0660f8869a2fec1ae84bb28bd87). 埼玉県川越市脇田本町15-15 ヤマトビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [58801](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58801). 350-1123 埼玉県川越市脇田本町15-15 ヤマトビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツバーbloom / ダーツバーbloom

- **DARTSLIVE**: [dc8a082169d9123a790ab824ce8730e5](https://search.dartslive.com/jp/shop/dc8a082169d9123a790ab824ce8730e5). 大阪府大阪市北区堂山町1-21 モンテビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [64008](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=64008). 530-0027 大阪府大阪市北区堂山町1-21 モンテビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 2.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY豊田駅前店 / JOYJOY 豊田駅前店

- **DARTSLIVE**: [d41836edd81b5f59774c926eb736cb5a](https://search.dartslive.com/jp/shop/d41836edd81b5f59774c926eb736cb5a). 愛知県豊田市西町5-57-1 豊田パールビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [69723](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69723). 471-0025 愛知県豊田市西町5-57-1 豊田パールビル1Ｆ. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 7.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 花鳥風月 KANNAI / 花鳥風月 KANNAI

- **DARTSLIVE**: [283d7ba8c5a5f43b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/283d7ba8c5a5f43b0d9b047a20a7ba1e). 神奈川県横浜市中区羽衣町3-63 高橋ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72148](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72148). 231-0047 神奈川県横浜市中区羽衣町3-63 高橋ビル3F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: C&#x27;est Super NEO / C&#x27;EST SUPER. NEO

- **DARTSLIVE**: [12382d046ebae00e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/12382d046ebae00e0d9b047a20a7ba1e). 福島県郡山市駅前1-6-15 エリート1ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [74012](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=74012). 963-8002 福島県郡山市駅前1-6-15 エリート1ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 4.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: J-style / J-style

- **DARTSLIVE**: [8de8e7a4304fc00d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8de8e7a4304fc00d0d9b047a20a7ba1e). 東京都練馬区練馬4-15-17 ガーデンヒルズ豊島園B106. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81085](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81085). 176-0001 東京都練馬区練馬4丁目15-17 ガーデンヒルズ豊島園B106. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 松戸店 / Link 松戸店

- **DARTSLIVE**: [a054d2856fd0783325d56fb0e5c39bac](https://search.dartslive.com/jp/shop/a054d2856fd0783325d56fb0e5c39bac). 千葉県松戸市松戸1231 アステシオビル8F. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81104](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81104). 271-0092 千葉県松戸市松戸1231 アステシオビル8F. Inventory: VSPhoenix X 3台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE新橋店 / ビアポンバー GROVE 新橋店

- **DARTSLIVE**: [e3843ff58360d26228032249b44395af](https://search.dartslive.com/jp/shop/e3843ff58360d26228032249b44395af). 東京都港区新橋3-16-12 第一横山ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82146](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82146). 105-0004 東京都港区新橋3-16-12 第一横山ビルB1F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 的屋TRIP / 的屋TRIP

- **DARTSLIVE**: [a329eb5aad9221e40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a329eb5aad9221e40d9b047a20a7ba1e). 福岡県北九州市小倉南区下城野1-8-1 グランドール富士見2階. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8245](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8245). 802-0804 福岡県北九州市小倉南区下城野1-8-1 グランドール富士見2F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE秋葉原店 / ビアポンバーGROVE秋葉原店

- **DARTSLIVE**: [c0574c04a2173f70f454cb89828a1cfe](https://search.dartslive.com/jp/shop/c0574c04a2173f70f454cb89828a1cfe). 東京都千代田区外神田1-15-18 奥山ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82627](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82627). 101-0021 東京都千代田区外神田1-15-18 奥山ビル5F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE赤羽店 / ビアポンバーGROVE赤羽店

- **DARTSLIVE**: [b3049494c1ac9888f454cb89828a1cfe](https://search.dartslive.com/jp/shop/b3049494c1ac9888f454cb89828a1cfe). 東京都北区赤羽1-1-6 赤羽駅前第2ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [84226](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84226). 115-0045 東京都北区赤羽1-1-6 赤羽駅前第2ビルB1F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE八王子店 / ビアポンバーGROVE八王子店

- **DARTSLIVE**: [36e9652df1b0afd25f9f3321c1147265](https://search.dartslive.com/jp/shop/36e9652df1b0afd25f9f3321c1147265). 東京都八王子市旭町6-13 第95東京ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85087](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85087). 192-0083 東京都八王子市旭町6-13 第95東京ビル3F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts bar Glanz / Darts bar Glanz

- **DARTSLIVE**: [4f01e52d629c7f5058d385ea46352d8f](https://search.dartslive.com/jp/shop/4f01e52d629c7f5058d385ea46352d8f). 東京都八王子市旭町8-2 プラスリノ八王子3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85485](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85485). 192-0083 東京都八王子市旭町8-2 プラスリノ八王子3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 安-Bartic 片町本店 / 安-Bartic 片町本店

- **DARTSLIVE**: [c0de1f74cc26e2660d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c0de1f74cc26e2660d9b047a20a7ba1e). 石川県金沢市片町1-3-46 片町コレッジオ2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [86563](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86563). 920-0981 石川県金沢市片町1-3-46 片町コレッジオ2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: dining bar カトレア / diningbar カトレア

- **DARTSLIVE**: [0b5def0d9f337af80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0b5def0d9f337af80d9b047a20a7ba1e). 東京都立川市柴崎町2-2-5 あすなろTビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86834](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86834). 190-0023 東京都立川市柴崎町2-2-5 あすなろTビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間米子マンガミュージアム店 / 自遊空間 米子マンガミュージアム店

- **DARTSLIVE**: [35c703dced323b7b774c926eb736cb5a](https://search.dartslive.com/jp/shop/35c703dced323b7b774c926eb736cb5a). 鳥取県米子市角盤町1-27-2 GOOD BLESS GARDEN3・4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [88224](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88224). 683-0812 鳥取県米子市角盤町1丁目27-2 GOOD BLESS GARDEN 3F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 49.8 m; Different explicit units/floors: likely separate premises; do not merge.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Sports&amp;Dining B-SKY / Sports&amp;Dining B-SKY

- **DARTSLIVE**: [ee23282f45e68e5c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ee23282f45e68e5c0d9b047a20a7ba1e). 愛知県豊明市前後町善江1735 パルネス2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8932](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8932). 471-1151 愛知県豊明市前後町善江1735 パルネス2F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 50.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 流川店 / ダイニングダーツバーBee 流川店

- **DARTSLIVE**: [1e3322e39b25b811fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/1e3322e39b25b811fec1ae84bb28bd87). 広島県広島市中区堀川町1-15 ざくろビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 8, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [90077](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90077). 730-0033 広島県広島市中区堀川町1-15 ざくろビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: C.STAND京都河原町店 / C.STAND 京都河原町店

- **DARTSLIVE**: [bd15b3ce8d4115b40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/bd15b3ce8d4115b40d9b047a20a7ba1e). 京都府京都市中京区河原町蛸薬師下ル塩屋町324 古城ビル. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91914](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91914). 604-8027 京都府京都市中京区河原町蛸薬師下ル塩屋町324 古城ビル 5階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: K-CREW / K-CREW

- **DARTSLIVE**: [1594b2c8a7a235890d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1594b2c8a7a235890d9b047a20a7ba1e). 東京都武蔵野市吉祥寺本町2-8-2 若松ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [94465](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94465). 180-0004 東京都武蔵野市吉祥寺本町2-8-2 若松ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Studio SPREAD / Darts Studio SPREAD

- **DARTSLIVE**: [847fda5d954709c225d56fb0e5c39bac](https://search.dartslive.com/jp/shop/847fda5d954709c225d56fb0e5c39bac). 石川県金沢市増泉4-1-1 ニューフナミビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [96847](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96847). 921-8025 石川県金沢市増泉4-1-1 ニューフナミビル1F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 12.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: First Piece / First Piece

- **DARTSLIVE**: [85ccbdff6196e4640d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/85ccbdff6196e4640d9b047a20a7ba1e). 東京都武蔵野市吉祥寺南町1-1-2 喜楽ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9777](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9777). 180-0003 東京都武蔵野市吉祥寺南町1-1-2 喜楽ビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar LIAN / Amusement Bar LIAN

- **DARTSLIVE**: [9d94902f501bba250d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9d94902f501bba250d9b047a20a7ba1e). 神奈川県横浜市緑区鴨居4-1-9 明実ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [98372](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98372). 226-0003 神奈川県横浜市緑区鴨居4-1-9 明実ビルB1F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Triple-A / Triple-A

- **DARTSLIVE**: [3e99f50671b6b68c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3e99f50671b6b68c0d9b047a20a7ba1e). 山口県宇部市中央町1-6-8 エルコ中央ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99263](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99263). 755-0045 山口県宇部市中央町1-6-8 エルコ中央ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 138.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Billiards&amp;Darts RISE / Billiards &amp; Darts RISE

- **DARTSLIVE**: [56d2c6d3687e701825d56fb0e5c39bac](https://search.dartslive.com/jp/shop/56d2c6d3687e701825d56fb0e5c39bac). 東京都江戸川区瑞江2-1-11 カネヘイビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99778](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99778). 132-0011 東京都江戸川区瑞江2-1-11 カネヘイビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS BAR ESCONDiOS / DARTS BAR ESCONDiOS

- **DARTSLIVE**: [1f9f81c1ee09afab0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1f9f81c1ee09afab0d9b047a20a7ba1e). 兵庫県西宮市馬場町5-7 メゾンKATO201. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [99846](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99846). 662-0915 兵庫県西宮市馬場町5-7 メゾンKATO201. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.857; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: LAT.43°N / LAT43°N

- **DARTSLIVE**: [fc3948c10dd302f60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/fc3948c10dd302f60d9b047a20a7ba1e). 北海道札幌市中央区南六条西2丁目8-5 フォレストビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53998](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53998). 064-0806 北海道札幌市中央区南6条西2丁目8-5 フォレストビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.852; Source-pin distance 5.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 321だーーっ!! / 321だーーっ！！

- **DARTSLIVE**: [f39835de9572b2125f9f3321c1147265](https://search.dartslive.com/jp/shop/f39835de9572b2125f9f3321c1147265). 福岡県北九州市小倉北区紺屋町1-12 紺屋町会館1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90400](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90400). 802-0081 福岡県北九州市小倉北紺屋町1-12 紺屋町会館1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.852; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: C.STAND心斎橋店 / C.STAND 心斎橋店

- **DARTSLIVE**: [3ce0d81aa59f01c50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3ce0d81aa59f01c50d9b047a20a7ba1e). 大阪府大阪市中央区東心斎橋1-19-11 鰻谷スクエア4•5F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91628](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91628). 542-0083 大阪府大阪市中央区東心斎橋1-19-11 鰻谷スクエア4,5階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.852; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: STRIKE DARTS / STRIKE DARTS

- **DARTSLIVE**: [0e59a37e6b9a0bda0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0e59a37e6b9a0bda0d9b047a20a7ba1e). 東京都江戸川区松島3-15-4 フェニックスビルB-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9218](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9218). 132-0031 東京都江戸川区松島3-15-4 フェニックスビルB1F. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.852; Source-pin distance 1.9 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link北千住店 / Link 北千住店

- **DARTSLIVE**: [71d0ca2883d90f820d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/71d0ca2883d90f820d9b047a20a7ba1e). 東京都足立区千住旭町3-4 駅前会館ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [49387](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49387). 120-0026 東京都足立区千住旭町3-4 駅前会館ビル4F. Inventory: VSPHOENIX S4 2台 VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 2.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 和光市店 / Link 和光市店

- **DARTSLIVE**: [695efbee164a44390d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/695efbee164a44390d9b047a20a7ba1e). 埼玉県和光市丸山台1-10-4 F&#x27;s BOX5F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [49388](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49388). 351-0112 埼玉県和光市丸山台1-10-4 F&#x27;&#x27;s BOX5F. Inventory: VSPhoenix X 2台 VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アミューズバーGROVE 関内店 / アミューズバーGROVE関内店

- **DARTSLIVE**: [3063c3a04c75405c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3063c3a04c75405c0d9b047a20a7ba1e). 神奈川県横浜市中区吉田町10 斎藤ビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [49395](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49395). 231-0041 神奈川県横浜市中区吉田町10 斎藤ビル6F. Inventory: VSPhoenix X 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 36.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Vermut / VERMUT

- **DARTSLIVE**: [5357eddf0798e8b5a3f63593b5358cc4](https://search.dartslive.com/jp/shop/5357eddf0798e8b5a3f63593b5358cc4). 熊本県熊本市中央区新市街4-6 古城ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53884](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53884). 860-0803 熊本県熊本市中央区新市街4-6 古城ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 13.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bullet / Bullet

- **DARTSLIVE**: [0cb2e2e9f31f78f80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0cb2e2e9f31f78f80d9b047a20a7ba1e). 東京都世田谷区北沢2-2-14 モアイ茶沢3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [58329](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58329). 155-0031 東京都世田谷区北沢2-2-14 モアイ茶沢3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 2.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ENCOUNTER DINING ZOO / ENCOUNTER DINING ZOO

- **DARTSLIVE**: [b8cb0c256957e15225d56fb0e5c39bac](https://search.dartslive.com/jp/shop/b8cb0c256957e15225d56fb0e5c39bac). 岩手県盛岡市大通2-7-20 それんとビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [62442](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=62442). 020-0022 岩手県盛岡市大通2-7-20 それんとビル5F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 11.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar BLANKEY&#x27;S / Darts Bar BLANKEY&#x27;S

- **DARTSLIVE**: [da6f95f5d83e5dc70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/da6f95f5d83e5dc70d9b047a20a7ba1e). 福岡県北九州市小倉北区紺屋町10-10-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [66771](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=66771). 802-0081 福岡県北九州市小倉北区紺屋町10-10 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 2.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 駄菓子屋バー ドロップ / 駄菓子屋バー ドロップ

- **DARTSLIVE**: [75e11ce5de7bd14d774c926eb736cb5a](https://search.dartslive.com/jp/shop/75e11ce5de7bd14d774c926eb736cb5a). 兵庫県尼崎市七松町1-1-10 KT-1ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [67336](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=67336). 660-0052 兵庫県尼崎市七松町1-1-10 KT-1ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SIESTAS&amp;OLAS / SIESTAS&amp;OLAS

- **DARTSLIVE**: [519ddba4106925310d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/519ddba4106925310d9b047a20a7ba1e). 東京都目黒区祐天寺2-12-2 弘益社ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [73145](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73145). 153-0052 東京都目黒区祐天寺2-12-2　弘益社ビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 1.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 居酒屋ハイブリッヂ / 居酒屋ハイブリッヂ

- **DARTSLIVE**: [35c5e50bf696aed00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/35c5e50bf696aed00d9b047a20a7ba1e). 神奈川県大和市上和田969 メゾン山下1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [73344](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73344). 242-0014 神奈川県大和市上和田969 メゾン山下1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 14-1 FOURTEEN-ONE / 14-1 FOURTEEN-ONE

- **DARTSLIVE**: [c6c704641ebf88220d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c6c704641ebf88220d9b047a20a7ba1e). 愛媛県松山市一番町2-4-6 第一吾妻ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [73653](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73653). 790-0001 愛媛県松山市一番町2-4-6 第一吾妻ビル 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 31.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dominator / DOMINATOR

- **DARTSLIVE**: [dcc9248ca80ffb6c5f9f3321c1147265](https://search.dartslive.com/jp/shop/dcc9248ca80ffb6c5f9f3321c1147265). 大阪府泉佐野市上町3-10-6 野出徳ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81066](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81066). 598-0007 大阪府泉佐野市上町3-10-6 野出徳ビル1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 2.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE六本木店 / ビアポンバー GROVE六本木店

- **DARTSLIVE**: [a2b01cfc190a7d135f9f3321c1147265](https://search.dartslive.com/jp/shop/a2b01cfc190a7d135f9f3321c1147265). 東京都港区六本木3-10-5 マリーナビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [83730](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83730). 106-0032 東京都港区六本木3-10-5 マリーナビル3F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe Bar QP&#x27;s / Cafe Bar QP&#x27;s

- **DARTSLIVE**: [a7c9c139fbd8b6cb0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a7c9c139fbd8b6cb0d9b047a20a7ba1e). 東京都世田谷区用賀3-17-5 石黒ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8861](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8861). 158-0097 東京都世田谷区用賀3-17-5 石黒ビルB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 3.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ＆ビアポン BASE1新宿店 / ダーツ＆ビアポン BASE1新宿店

- **DARTSLIVE**: [1bd454594cf0ad740d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1bd454594cf0ad740d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-6-3 東海苑ビル9F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89591](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89591). 160-0021 東京都新宿区歌舞伎町1-6-3 東海苑ビル9F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: No.9 葛西店 / No.9 葛西店

- **DARTSLIVE**: [d707022af3e6dd7c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d707022af3e6dd7c0d9b047a20a7ba1e). 東京都江戸川区東葛西6-6-15 藤美ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90128](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90128). 134-0084 東京都江戸川区東葛西6-6-15 藤美ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 3.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Shrimp Dining Ebi / Shrimp Dining Ebi

- **DARTSLIVE**: [f338db03640241d70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f338db03640241d70d9b047a20a7ba1e). 群馬県高崎市寄合町25-12 スタービル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90152](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90152). 370-0822 群馬県高崎市寄合町25-12 スタービル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ&amp;ビアポン BASE2 新宿歌舞伎町店 / ダーツ&amp;ビアポン BASE2 新宿歌舞伎町店

- **DARTSLIVE**: [4a4930d753d8f4da0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4a4930d753d8f4da0d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-17-2 小松ビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92488](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92488). 160-0021 東京都新宿区歌舞伎町1-17-2 小松ビル7F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 10.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ROCKY / ROCKY

- **DARTSLIVE**: [3fea54aab6f9752d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3fea54aab6f9752d0d9b047a20a7ba1e). 沖縄県那覇市松尾1-3-1 エスプリコート4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9363](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9363). 900-0014 沖縄県那覇市松尾1-3-1 エスプリコート4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 3.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Diner One Star / Darts&amp;Diner　One Star

- **DARTSLIVE**: [36b1630ec4735c6ffec1ae84bb28bd87](https://search.dartslive.com/jp/shop/36b1630ec4735c6ffec1ae84bb28bd87). 新潟県新潟市中央区米山1-6-9 IBビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93749](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93749). 950-0916 新潟県新潟市中央区米山1-6-9 IBビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 3.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Avanti / Avanti

- **DARTSLIVE**: [56f4fba4159e896dfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/56f4fba4159e896dfec1ae84bb28bd87). 静岡県静岡市葵区常磐町1-5-4 パレス1-4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9512](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9512). 420-0034 静岡県静岡市葵区常磐町1-5-4 パレス１ 4F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 50.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link本八幡駅前店 / Link 本八幡駅前店

- **DARTSLIVE**: [915547037f3c375c790ab824ce8730e5](https://search.dartslive.com/jp/shop/915547037f3c375c790ab824ce8730e5). 千葉県市川市八幡2-16-6 八幡ハタビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 8}.
- **Phoenix**: [96985](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96985). 272-0021 千葉県市川市八幡 2-16-6 八幡ハタビル6F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOKERS / JOKERS

- **DARTSLIVE**: [92ed96e6b5aecdea0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/92ed96e6b5aecdea0d9b047a20a7ba1e). 福島県郡山市大町1-4-16 増子第1ビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97663](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97663). 963-8001 福島県郡山市大町1-4-16 増子第1ビル6F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: PATCHE / PATCHE

- **DARTSLIVE**: [398439487106f4270d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/398439487106f4270d9b047a20a7ba1e). 北海道札幌市中央区南5条西4-9-3 ライラックビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [75312](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75312). 064-0805 北海道札幌市中央区南5条西4丁目9-3 ライラックビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.847; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE心斎橋店 / ビアポンバーGROVE 心斎橋店

- **DARTSLIVE**: [8d5e5ff909d96d9b774c926eb736cb5a](https://search.dartslive.com/jp/shop/8d5e5ff909d96d9b774c926eb736cb5a). 大阪府大阪市中央区心斎橋筋1-3-13 茶茶心斎橋ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92374](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92374). 542-0085 大阪府大阪市中央区心斎橋筋１-3-13 茶茶心斎橋ビル3階. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.847; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts bar Black Monkey / Darts bar Black Monkey

- **DARTSLIVE**: [21dc846a06670a730d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/21dc846a06670a730d9b047a20a7ba1e). 神奈川県横浜市中区福富町仲通1-8 沖浜ビル1F-C. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9628](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9628). 231-0043 神奈川県横浜市中区福富町仲通1-8 沖浜ビル1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.846; Source-pin distance 3.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe&amp;darts Flores / Cafe&amp;Darts Flores

- **DARTSLIVE**: [1673976f49e2a94e58d385ea46352d8f](https://search.dartslive.com/jp/shop/1673976f49e2a94e58d385ea46352d8f). 静岡県三島市本町12-8 SOHOビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [47496](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47496). 411-0855 静岡県三島市本町12-8 SOHOビル1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 6.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 相模大野駅前店 / 快活CLUB相模大野駅前店

- **DARTSLIVE**: [58653a000108e3bb5f9f3321c1147265](https://search.dartslive.com/jp/shop/58653a000108e3bb5f9f3321c1147265). 神奈川県相模原市南区相模大野3-12-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [48463](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=48463). 252-0303 神奈川県相模原市南区相模大野3-12-10. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 8.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 西川口店 / Link 西川口店

- **DARTSLIVE**: [a7427117351e97c20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a7427117351e97c20d9b047a20a7ba1e). 埼玉県川口市並木2-1-1 フェストビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [49392](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49392). 332-0034 埼玉県川口市並木2-1-1 フェストビル4F. Inventory: VSPhoenix X 3台 VSPHOENIX S4 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 18.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 大森駅前店 / 快活CLUB 大森駅前店

- **DARTSLIVE**: [e1703d9efc2be0deb21333aee1bd51e4](https://search.dartslive.com/jp/shop/e1703d9efc2be0deb21333aee1bd51e4). 東京都大田区山王2-4-1 大森駅前ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 10, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [72671](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72671). 143-0023 東京都大田区山王2-4-1 大森駅前ビル5F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Root / Root

- **DARTSLIVE**: [14117e10ca5c82befec1ae84bb28bd87](https://search.dartslive.com/jp/shop/14117e10ca5c82befec1ae84bb28bd87). 茨城県日立市大みか町2-25-4 宝ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [75952](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75952). 319-1221 茨城県日立市大みか町2-25-4 宝ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 八幡桃園店 / 快活CLUB 八幡桃園店

- **DARTSLIVE**: [3a0a67a088a5b6c225d56fb0e5c39bac](https://search.dartslive.com/jp/shop/3a0a67a088a5b6c225d56fb0e5c39bac). 福岡県北九州市八幡東区桃園2-1-20-5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [78330](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78330). 805-0068 福岡県北九州市八幡東区桃園2-1-20 5F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: やまとや / やまとや

- **DARTSLIVE**: [7c19183833fe5af70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7c19183833fe5af70d9b047a20a7ba1e). 東京都江東区東陽3-27-18 菅原ビル3Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79661](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79661). 135-0016 東京都江東区東陽3-27-18 菅原ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 7.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BECOME / BECOME

- **DARTSLIVE**: [b761ef2fb18e7d680d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b761ef2fb18e7d680d9b047a20a7ba1e). 新潟県新潟市中央区西堀通7-1545-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [80234](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80234). 951-8061 新潟県新潟市中央区西堀通7-1545 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 122.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts &amp; Cafe FLAMME / Darts&amp;Cafe FLAMME

- **DARTSLIVE**: [141f84ebbcd1264928032249b44395af](https://search.dartslive.com/jp/shop/141f84ebbcd1264928032249b44395af). 福岡県久留米市東町40-15 森川ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [80571](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80571). 830-0032 福岡県久留米市東町40-15 森川ビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE西新宿店 / ビアポンバー GROVE西新宿店

- **DARTSLIVE**: [4259ece57a8dd18658d385ea46352d8f](https://search.dartslive.com/jp/shop/4259ece57a8dd18658d385ea46352d8f). 東京都新宿区西新宿1-13-1 今佐ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [83021](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83021). 160-0023 東京都新宿区西新宿1-13-1 今佐ビル5F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DartsBar Oase / DartsBar Oase

- **DARTSLIVE**: [87b15aa9739609e10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/87b15aa9739609e10d9b047a20a7ba1e). 東京都江東区亀戸5-8-15 森山ビル101. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89950](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89950). 136-0071 東京都江東区亀戸5-8-15 森山ビル101. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ARCANA / ARCANA

- **DARTSLIVE**: [df6b2a9b3091687d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/df6b2a9b3091687d0d9b047a20a7ba1e). 東京都立川市錦町2-1-10 エリア立川1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90031](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90031). 190-0022 東京都立川市錦町2-1-10　エリア立川１F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: abaca / abaca.

- **DARTSLIVE**: [cc45be8fef8d91c0b21333aee1bd51e4](https://search.dartslive.com/jp/shop/cc45be8fef8d91c0b21333aee1bd51e4). 静岡県沼津市御幸町22-35 西川ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90698](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90698). 410-0832 静岡県沼津市御幸町22-35 西川ビル1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Voyage / Voyage

- **DARTSLIVE**: [df0504c7e46f555c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/df0504c7e46f555c0d9b047a20a7ba1e). 大阪府池田市空港1-7-13 ソウルビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91760](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91760). 563-0034 大阪府池田市空港1-7-13 ソウルビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Coffee STARDOM / Darts&amp;Coffee STAR DOM

- **DARTSLIVE**: [6a09983f24676fe90d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6a09983f24676fe90d9b047a20a7ba1e). 東京都中野区中野5-55-1 RGビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [95683](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95683). 164-0001 東京都中野区中野5-55-1 RGビルB1F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bobby&#x27;s Cafe / Bobby&#x27;s Cafe

- **DARTSLIVE**: [66e494a4baf255d60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/66e494a4baf255d60d9b047a20a7ba1e). 神奈川県横浜市中区長者町7-113 伊勢佐木町センタービル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9630](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9630). 231-0033 神奈川県横浜市中区長者町7-113 伊勢崎町センタービル3F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 8.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Yamato Nadeshiko / Yamato Nadeshiko

- **DARTSLIVE**: [7e7d65e822301e230d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7e7d65e822301e230d9b047a20a7ba1e). 東京都大田区西蒲田6-26-3 SSビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9748](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9748). 144-0051 東京都大田区西蒲田6-26-3 S&amp;Sビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.844; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 大須万松寺店 / 亜熱帯 大須万松寺店

- **DARTSLIVE**: [f2eed40b8b60dc3825d56fb0e5c39bac](https://search.dartslive.com/jp/shop/f2eed40b8b60dc3825d56fb0e5c39bac). 愛知県名古屋市中区大須4-11-5 大須カンノンビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [44819](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44819). 460-0011 愛知県名古屋市中区大須4-11-5 カンノンビルB1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.842; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 斑(MADARA) / 斑《MADARA》

- **DARTSLIVE**: [d24900af651b272c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d24900af651b272c0d9b047a20a7ba1e). 福岡県北九州市小倉北区中津口1-10-2 大下ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [69753](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69753). 802-0018 福岡県北九州市小倉北区中津口1丁目10-2 大下ビル2F. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.842; Source-pin distance 4.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツバー あいつんち すすきの / ダーツバー あいつんち すすきの

- **DARTSLIVE**: [5f273ca004f1f2f80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5f273ca004f1f2f80d9b047a20a7ba1e). 北海道札幌市中央区南三条西4-17-3 J・BOXビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [96611](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96611). 060-0063 北海道札幌市中央区南3条西4-17-3 J-Boxビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.842; Source-pin distance 4.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BOX CAFE / BOX CAFE

- **DARTSLIVE**: [30996f7958dd95d30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/30996f7958dd95d30d9b047a20a7ba1e). 北海道旭川市3条通7-423 ビルドビエル7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10638](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10638). 070-0033 北海道旭川市3条通7-423-3 ビルドビエル7F. Inventory: VSPhoenix X 3台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.840; Source-pin distance 38.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: PLAT / PLAT

- **DARTSLIVE**: [0d011aed4fb9ceb3fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/0d011aed4fb9ceb3fec1ae84bb28bd87). 東京都新宿区西新宿7-4-7 イマス浜田ビルB-1. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [50637](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50637). 160-0023 東京都新宿区西新宿7-4-7 イマス浜田ビルB1F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.840; Source-pin distance 6.5 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe&amp;Bar BRAVE / Cafe&amp;Bar BRAVE

- **DARTSLIVE**: [4a6ec74abc5776f90d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4a6ec74abc5776f90d9b047a20a7ba1e). 福岡県北九州市小倉北区古船場町6-3 プレアール古船場町. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [53901](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53901). 802-0082 福岡県北九州市小倉北区古船場町6-3プレアール古船場町102. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.839; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts道場H.J.C / Darts道場 H.J.C

- **DARTSLIVE**: [3683323385e3fe1b5f9f3321c1147265](https://search.dartslive.com/jp/shop/3683323385e3fe1b5f9f3321c1147265). 島根県松江市東出雲町出雲郷1407-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [100402](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100402). 699-0108 島根県松江市東出雲町出雲郷1407-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 5.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 50号笠懸店 / 快活CLUB 50号笠懸店

- **DARTSLIVE**: [31e32aeed603162ca3f63593b5358cc4](https://search.dartslive.com/jp/shop/31e32aeed603162ca3f63593b5358cc4). 群馬県みどり市笠懸町阿左美2823-3. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10045](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10045). 379-2311 群馬県みどり市笠懸町阿左美2823-3. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: リボルト・ブラッズ / リボルト・ブラッズ

- **DARTSLIVE**: [ff0429d16f50e1bf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ff0429d16f50e1bf0d9b047a20a7ba1e). 長野県千曲市杭瀬下45-4 宮沢ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [40066](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=40066). 387-0011 長野県千曲市杭瀬下45-4 宮沢ビル2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 熊本東バイパス店 / 快活CLUB 熊本東バイパス店

- **DARTSLIVE**: [7524427d423f627a58d385ea46352d8f](https://search.dartslive.com/jp/shop/7524427d423f627a58d385ea46352d8f). 熊本県熊本市東区上南部2-1-109-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [42295](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42295). 861-8010 熊本県熊本市東区上南部2-1-109 2F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: THE DAY Cafe 赤坂店 / THE DAY Cafe 赤坂店

- **DARTSLIVE**: [f1fba1fcf30599f00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f1fba1fcf30599f00d9b047a20a7ba1e). 東京都港区赤坂2-14-31 金波ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [49385](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49385). 107-0052 東京都港区赤坂2-14-31 金波ビル4F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: INBULL / IN BULL

- **DARTSLIVE**: [88514244174cfec558d385ea46352d8f](https://search.dartslive.com/jp/shop/88514244174cfec558d385ea46352d8f). 静岡県藤枝市駅前1-6-24 中川ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52746](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52746). 426-0034 静岡県藤枝市駅前1-6-24 中川ビル1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 11.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビリヤード&amp;ダーツ　コモルーム / ビリヤード&amp;ダーツ コモルーム

- **DARTSLIVE**: [a0935742591a5e7a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a0935742591a5e7a0d9b047a20a7ba1e). 神奈川県藤沢市藤沢571 荒井ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52869](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52869). 251-0052 神奈川県藤沢市藤沢571 荒井ビル2F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 86.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Corcovado / Corcovado

- **DARTSLIVE**: [d1158d12aaff5c160d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d1158d12aaff5c160d9b047a20a7ba1e). 東京都中野区中央1-40-6 味正ビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53112](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53112). 164-0011 東京都中野区中央1-40-6 味正ビルB1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 4.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Lau Lau / Lau Lau

- **DARTSLIVE**: [f64542cc2b33f8a20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f64542cc2b33f8a20d9b047a20a7ba1e). 神奈川県横浜市港北区大倉山2-12-20. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [54532](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=54532). 222-0037 神奈川県横浜市港北区大倉山2-12-20. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 8.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Y&#x27;s-spec / Y&#x27;s-spec

- **DARTSLIVE**: [31b68190342d918f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/31b68190342d918f0d9b047a20a7ba1e). 東京都江東区富岡1-25-3 毛利ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [54643](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=54643). 135-0047 東京都江東区富岡1-25-3 毛利ビル4F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 1.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯名東高針店 / 亜熱帯 名東高針店

- **DARTSLIVE**: [654f8c4fcd2d824c28032249b44395af](https://search.dartslive.com/jp/shop/654f8c4fcd2d824c28032249b44395af). 愛知県名古屋市名東区高針原2-1605. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [55556](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=55556). 465-0073 愛知県名古屋市名東区高針原2-1605. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 2.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 名古屋楠インター店 / 快活CLUB 名古屋楠インター店

- **DARTSLIVE**: [3256c87af75548dc25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/3256c87af75548dc25d56fb0e5c39bac). 愛知県名古屋市北区玄馬町234-1-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [57246](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=57246). 462-0018 愛知県名古屋市北区玄馬町234-1 2F. Inventory: VSPhoenix X-MAX 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 215.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 仙台一番町店 / 快活CLUB 仙台一番町店

- **DARTSLIVE**: [1326a8d4ffc393a8fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/1326a8d4ffc393a8fec1ae84bb28bd87). 宮城県仙台市青葉区一番町4-5-13-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [58497](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58497). 980-0811 宮城県仙台市青葉区一番町4-5-13 2F. Inventory: VSPhoenix X-MAX 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Pool&amp;Darts Ape / Pool&amp;Darts Ape

- **DARTSLIVE**: [5c7027e8181d213e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5c7027e8181d213e0d9b047a20a7ba1e). 神奈川県横浜市港南区上大岡西2-3-15. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [70046](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70046). 233-0002 神奈川県横浜市港南区上大岡西2-3-15. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 43.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツバー ブル / ダーツバー ブル

- **DARTSLIVE**: [45de515b544d3c8b25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/45de515b544d3c8b25d56fb0e5c39bac). 石川県金沢市片町2-21-3 社交会館3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7121](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7121). 920-0981 石川県金沢市片町2-21-3 社交会館3F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 11.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Dining CAROL 75 / Darts&amp;Dining CAROL 75

- **DARTSLIVE**: [4590b786dd8f35a1790ab824ce8730e5](https://search.dartslive.com/jp/shop/4590b786dd8f35a1790ab824ce8730e5). 東京都渋谷区幡ヶ谷2-6-7 小西ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [77311](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77311). 151-0072 東京都渋谷区幡ヶ谷2-6-7小西ビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: AZ BOX / AZ BOX

- **DARTSLIVE**: [d359190e52d896a40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d359190e52d896a40d9b047a20a7ba1e). 東京都青梅市新町5-4-6 PAO青梅店内. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [77938](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77938). 198-0024 東京都青梅市新町5-4-6 PAO 青梅店内. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 23.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: どくだみ屋 / どくだみ屋

- **DARTSLIVE**: [4a746afd8687076d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4a746afd8687076d0d9b047a20a7ba1e). 高知県高知市廿代町7-1 上野ビル3F東. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79021](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79021). 780-0843 高知県高知市廿代町7-1 上野ビル3F東. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BULL DOG CAFE QUEEN’S / BULL DOG CAFE QUEEN&#x27;S

- **DARTSLIVE**: [16bc4e89cd673bb80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/16bc4e89cd673bb80d9b047a20a7ba1e). 東京都墨田区押上1-24-3 押上ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [80646](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80646). 131-0045 東京都墨田区押上1-24-3 押上ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 4.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB いわき鹿島店 / 快活CLUB いわき鹿島店

- **DARTSLIVE**: [3ef79c3c86f40537f454cb89828a1cfe](https://search.dartslive.com/jp/shop/3ef79c3c86f40537f454cb89828a1cfe). 福島県いわき市鹿島町走熊小神山66-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [81842](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81842). 971-8141 福島県いわき市鹿島町走熊小神山66-2. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 小倉西港店 / 快活CLUB 小倉西港店

- **DARTSLIVE**: [94b8cd56b1a0260125d56fb0e5c39bac](https://search.dartslive.com/jp/shop/94b8cd56b1a0260125d56fb0e5c39bac). 福岡県北九州市小倉北区西港町30-18. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [81964](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81964). 803-0801 福岡県北九州市小倉北区西港町30-18. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Bar D-WALT&#x27;S / Darts&amp;Bar D-WALT&#x27;S

- **DARTSLIVE**: [7ff2ea872ca6c1c50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7ff2ea872ca6c1c50d9b047a20a7ba1e). 東京都八王子市南町1-3 ITUビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [87355](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=87355). 192-0072 東京都八王子市南町1-3 ITUビル4F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY中川昭和橋店 / JOYJOY 中川昭和橋店

- **DARTSLIVE**: [63b312825e6bfa54b21333aee1bd51e4](https://search.dartslive.com/jp/shop/63b312825e6bfa54b21333aee1bd51e4). 愛知県名古屋市中川区昭和橋通2-37-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [8764](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8764). 454-0852 愛知県名古屋市中川区昭和橋通2-37-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 1.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Girls Bar DOLLs / Girl&#x27;s Bar DOLLs

- **DARTSLIVE**: [9eeadbdece37d4270d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9eeadbdece37d4270d9b047a20a7ba1e). 東京都府中市片町2-18-9 栄ビル3F-A. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [88985](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88985). 183-0021 東京都府中市片町2-18-9 栄ビル3F A. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 3.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DaRGON.GB / DaRGON.GB

- **DARTSLIVE**: [aadbb4357501b4ae0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/aadbb4357501b4ae0d9b047a20a7ba1e). 千葉県市川市八幡2-12-8 牧野ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89174](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89174). 272-0021 千葉県市川市八幡2-12-8 牧野ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 手稲前田店 / 自遊空間 手稲前田店

- **DARTSLIVE**: [b1e4f01fb1d65125774c926eb736cb5a](https://search.dartslive.com/jp/shop/b1e4f01fb1d65125774c926eb736cb5a). 北海道札幌市手稲区前田6条12-1-10. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9110](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9110). 006-0816 北海道札幌市手稲区前田6条12-1-10. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 1.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: .1chi / .1chi

- **DARTSLIVE**: [b235d7f7bf0ba3330d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b235d7f7bf0ba3330d9b047a20a7ba1e). 東京都港区芝5-31-24 勝文館ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [92918](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92918). 108-0014 東京都港区芝5-31-24 勝文館ビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE渋谷明治通り店 / ビアポンバー GROVE 渋谷明治通り店

- **DARTSLIVE**: [0fef464dc6dd31fcf454cb89828a1cfe](https://search.dartslive.com/jp/shop/0fef464dc6dd31fcf454cb89828a1cfe). 東京都渋谷区渋谷1-14-15 森ビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95935](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95935). 150-0002 東京都渋谷区渋谷1-14-15 森ビル6F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dining Darts Bar Fin&#x27;s / Dining Darts Bar Fin’ｓ

- **DARTSLIVE**: [b8977f8a06d365b80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b8977f8a06d365b80d9b047a20a7ba1e). 秋田県秋田市大町4-1-9 ソウルビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [96182](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96182). 010-0921 秋田県秋田市大町4-1-9 ソウルビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: チャビーズ / チャビーズ

- **DARTSLIVE**: [be5352bc07bdc4d00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/be5352bc07bdc4d00d9b047a20a7ba1e). 東京都台東区千束4-13-3 早川ビル１F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97623](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97623). 111-0031 東京都台東区千束4-13-3 早川ビル１F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 191.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Tres Flechas / Tres Flechas

- **DARTSLIVE**: [47f09f8b860cf463790ab824ce8730e5](https://search.dartslive.com/jp/shop/47f09f8b860cf463790ab824ce8730e5). 東京都板橋区常盤台1-2-5 小林ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9823](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9823). 174-0071 東京都板橋区常盤台1-2-5 小林ビル2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン京都伏見店 / ラウンドワン 京都伏見店

- **DARTSLIVE**: [28e471a7620404010d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/28e471a7620404010d9b047a20a7ba1e). 京都府京都市伏見区下鳥羽平塚町131. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98973](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98973). 612-8387 京都府京都市伏見区下鳥羽平塚町131. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.837; Source-pin distance 9.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ&amp;バー who / ダーツ＆バー who

- **DARTSLIVE**: [8360dcacb9b045580d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8360dcacb9b045580d9b047a20a7ba1e). 東京都西多摩郡瑞穂町箱根ケ崎189-3 佐藤ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [52078](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52078). 190-1221 東京都西多摩郡瑞穂町箱根ヶ崎189-3 佐藤ビル1F. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 3.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe &amp; Bar Go / Cafe&amp;Bar GO→

- **DARTSLIVE**: [6c8fac9924ed09bc0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6c8fac9924ed09bc0d9b047a20a7ba1e). 神奈川県横浜市瀬谷区三ツ境14-8 ヴェラ三ツ境1-D. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [61937](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61937). 246-0022 神奈川県横浜市瀬谷区三ツ境14-8 ヴィラ三ツ境1-D. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 9.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: PINK / PINK

- **DARTSLIVE**: [e5e38b7876e73a8f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e5e38b7876e73a8f0d9b047a20a7ba1e). 東京都墨田区押上1-31-10 メティオつくし野B1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [71649](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71649). 131-0045 東京都墨田区押上1-31-10 メディオつくし野B1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bon 小倉朝日ヶ丘 / Bon 小倉朝日ヶ丘

- **DARTSLIVE**: [72ce4b2d85dc66c90d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/72ce4b2d85dc66c90d9b047a20a7ba1e). 福岡県北九州市小倉北区朝日ケ丘3-28 第一ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7995](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7995). 803-0833 福岡県北九州市小倉北区朝日ケ丘3-28第一ビル3階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 17.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar Strad ZERO / Bar Strad ZERO

- **DARTSLIVE**: [c723a21ed32f70fd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c723a21ed32f70fd0d9b047a20a7ba1e). 新潟県新潟市中央区東大通1-9-4 VISIONARⅡ401. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85151](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85151). 950-0087 新潟県新潟市中央区東大通1丁目9-4 VISIONARⅡビル401. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: LION・HEART / LION・HEART

- **DARTSLIVE**: [478a97a6a23b5b930d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/478a97a6a23b5b930d9b047a20a7ba1e). 神奈川県藤沢市鵠沼橘1-17-4 第一興産28号館2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [92703](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92703). 251-0024 神奈川県藤沢市鵠沼橋1-17-4 第一興産28号館2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 236.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CONEY ISLAND / CONEY ISLAND

- **DARTSLIVE**: [3036905c83752d9ca3f63593b5358cc4](https://search.dartslive.com/jp/shop/3036905c83752d9ca3f63593b5358cc4). 大分県大分市都町3-6-14 第7パルコ時計台ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9298](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9298). 870-0034 大分県大分市都町3-6-14　第七パルコ時計台ビル２F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 6.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: HAVE FUN / HAVE FUN

- **DARTSLIVE**: [dff93e7800a9efcf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/dff93e7800a9efcf0d9b047a20a7ba1e). 東京都調布市小島町1-34-1 エクレール調布204. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9838](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9838). 182-0026 東京都調布市小島町1-34-1 エクレール調布204 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 17.2 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン守口店 / ラウンドワン 守口店

- **DARTSLIVE**: [d053595a75f27d6e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d053595a75f27d6e0d9b047a20a7ba1e). 大阪府守口市佐太東町2-6-14 ジャガーグリーン2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98968](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98968). 570-0017 大阪府守口市佐太東町2-6-14 ジャガーグリーン2階. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.836; Source-pin distance 11.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 伊勢佐木長者町店 / 自遊空間 伊勢佐木長者町店

- **DARTSLIVE**: [81752f6480c4ad980d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/81752f6480c4ad980d9b047a20a7ba1e). 神奈川県横浜市中区伊勢佐木町3-98 オデオンビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 7}.
- **Phoenix**: [88117](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88117). 231-0045 神奈川県横浜市中区伊勢佐木町3-98 ニューオデオンビル6F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.833; Source-pin distance 1.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン京都河原町店 / ラウンドワン京都河原町店

- **DARTSLIVE**: [70bdbd13258c95730d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/70bdbd13258c95730d9b047a20a7ba1e). 京都府京都市中京区河原町通三条下る山崎町250. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [10372](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10372). 604-8032 京都府京都市中京区河原町通三条下ル山崎町250. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 22.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Tono&#x27;p Bar / Tono&#x27;p Bar

- **DARTSLIVE**: [ac8415797955fb500d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ac8415797955fb500d9b047a20a7ba1e). 神奈川県大和市中央林間3-12-14 アロハビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [80930](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80930). 242-0007 神奈川県大和市中央林間2-12-14 アロハビル5F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 1.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar AMC / Bar AMC

- **DARTSLIVE**: [37780e34dc0fc8cf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/37780e34dc0fc8cf0d9b047a20a7ba1e). 大阪府枚方市町楠葉1-4-10 有馬パレス樟葉2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [83591](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83591). 573-1106 大阪府枚方市町楠葉1丁目4-10 有馬パレス樟葉2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Bar 隠れ家 / Darts&amp;Bar 隠れ家

- **DARTSLIVE**: [2eb38522032a95ab0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2eb38522032a95ab0d9b047a20a7ba1e). 東京都足立区西綾瀬2-23-24 第2岡村ビル302. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [87171](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=87171). 124-0014 東京都足立区西綾瀬2-23-24 第二岡村ビル302. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DYNA / DYNA

- **DARTSLIVE**: [c6a6ce278158da140d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c6a6ce278158da140d9b047a20a7ba1e). 東京都調布市小島町2-51-3 ロイヤルプラザビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [95996](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95996). 182-0026 東京都調布市小島町2-51-3　ロイヤルプラザ3F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 31.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン横浜綱島店 / ラウンドワン横浜綱島店

- **DARTSLIVE**: [ad7760242baa939d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ad7760242baa939d0d9b047a20a7ba1e). 神奈川県横浜市港北区樽町2-6-40 T-PLATZ-4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9615](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9615). 222-0001 神奈川県横浜市港北区樽町2-6-40 T-PLATZ. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 6.8 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間　国分寺駅南口店 / 自遊空間 国分寺駅南口店

- **DARTSLIVE**: [49d6333387be2e6c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/49d6333387be2e6c0d9b047a20a7ba1e). 東京都国分寺市南町2-17-1 ハタヤ第一ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 7}.
- **Phoenix**: [96842](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96842). 185-0021 東京都国分寺市南町２丁目１７−１ ハタヤ第一ビル 5F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.830; Source-pin distance 9.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 横浜北山田店 / 快活CLUB 横浜北山田店

- **DARTSLIVE**: [4a2b8496334d08d458d385ea46352d8f](https://search.dartslive.com/jp/shop/4a2b8496334d08d458d385ea46352d8f). 神奈川県横浜市都筑区北山田3-1-50. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [10139](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10139). 224-0021 神奈川県横浜市都筑区北山田3-1-50. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 1.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン札幌北21条店 / ラウンドワン札幌北21条店

- **DARTSLIVE**: [4645a1bbf11dc68a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4645a1bbf11dc68a0d9b047a20a7ba1e). 北海道札幌市東区北21条東1-1-21. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10587](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10587). 065-0021 北海道札幌市東区北21条東1-1-21. Inventory: VSPhoenix X 2台 VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 77.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン鳴海店 / ラウンドワン鳴海店

- **DARTSLIVE**: [a057b238fd1cdaee0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a057b238fd1cdaee0d9b047a20a7ba1e). 愛知県名古屋市緑区鳴海町字杜若28. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10644](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10644). 458-0801 愛知県名古屋市緑区鳴海町字杜若28. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 26.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY名駅錦通店 / JOYJOY 名駅錦通店

- **DARTSLIVE**: [68204bdd28b1b5dc5f9f3321c1147265](https://search.dartslive.com/jp/shop/68204bdd28b1b5dc5f9f3321c1147265). 愛知県名古屋市中村区名駅4-25-22. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [43721](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43721). 450-0002 愛知県名古屋市中村区名駅4-25-22. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 3.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 五日市駅前店 / 快活CLUB 五日市駅前店

- **DARTSLIVE**: [a6a8670b54d4433efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/a6a8670b54d4433efec1ae84bb28bd87). 広島県広島市佐伯区吉見園1-27-5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56616](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56616). 731-5132 広島県広島市佐伯区吉見園1-27 5F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 8.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 津南高茶屋店 / 亜熱帯 津南高茶屋店

- **DARTSLIVE**: [b264eb9f32290d82f454cb89828a1cfe](https://search.dartslive.com/jp/shop/b264eb9f32290d82f454cb89828a1cfe). 三重県津市雲出本郷町西添1680-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56683](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56683). 514-0304 三重県津市雲出本郷町西添1680-1. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB アクロスプラザ与次郎店 / 快活CLUB アクロスプラザ与次郎店

- **DARTSLIVE**: [c7d27f2998d27c4e774c926eb736cb5a](https://search.dartslive.com/jp/shop/c7d27f2998d27c4e774c926eb736cb5a). 鹿児島県鹿児島市与次郎1-7-18-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [63491](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=63491). 890-0062 鹿児島県鹿児島市与次郎1-7-18 2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR Tree Frog / BAR Tree Frog

- **DARTSLIVE**: [efded7559acaa2f50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/efded7559acaa2f50d9b047a20a7ba1e). 神奈川県横浜市鶴見区市場大和町3-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [69156](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69156). 230-0025 神奈川県横浜市鶴見区市場大和町3-1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 1.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 広島祇園店 / 快活CLUB 広島祇園店

- **DARTSLIVE**: [862942ff9a03660afec1ae84bb28bd87](https://search.dartslive.com/jp/shop/862942ff9a03660afec1ae84bb28bd87). 広島県広島市安佐南区西原9-15-20. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [7250](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7250). 731-0113 広島県広島市安佐南区西原9-15-20. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS &amp; BILLIARD NINE / DARTS&amp;BILLIARD NINE

- **DARTSLIVE**: [ffc01a6091aa08db0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ffc01a6091aa08db0d9b047a20a7ba1e). 和歌山県和歌山市森小手穂1382-2. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72621](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72621). 640-8312 和歌山県和歌山市森小手穂1382-2. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 4.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 153号天白植田店 / 快活CLUB 153号天白植田店

- **DARTSLIVE**: [cb4184af0e42a77525d56fb0e5c39bac](https://search.dartslive.com/jp/shop/cb4184af0e42a77525d56fb0e5c39bac). 愛知県名古屋市天白区焼山2-2107. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [7879](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7879). 468-0002 愛知県名古屋市天白区焼山2-2107. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 25.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY尾張旭晴丘店 / JOYJOY 尾張旭晴丘店

- **DARTSLIVE**: [40c954debc50ed72a3f63593b5358cc4](https://search.dartslive.com/jp/shop/40c954debc50ed72a3f63593b5358cc4). 愛知県尾張旭市北本地ケ原町3-59-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8108](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8108). 488-0043 愛知県尾張旭市北本地ケ原町3-59-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 133.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: One Piece 黒川店 / ONE PIECE 黒川店

- **DARTSLIVE**: [dd56be539397fab80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/dd56be539397fab80d9b047a20a7ba1e). 愛知県名古屋市北区黒川本通4-29-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8831](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8831). 462-0841 愛知県名古屋市北区黒川本通4-29-1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アミューズメントバー FreeStyle / アミューズメントバーFreeStyle

- **DARTSLIVE**: [cade263cebfc44ab0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/cade263cebfc44ab0d9b047a20a7ba1e). 新潟県十日町市本町4-2 丸新ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8921](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8921). 948-0082 新潟県十日町市本町4-2 丸新ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CAfE No.iE / CAFE No.iE

- **DARTSLIVE**: [fadb21fa1c3724e80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/fadb21fa1c3724e80d9b047a20a7ba1e). 静岡県袋井市愛野南1-2-14 E5E6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89249](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89249). 437-0040 静岡県袋井市愛野南1-2-14　E5E6. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 1.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BATDARTS シブケイ裏 / BATDARTS シブケイ裏

- **DARTSLIVE**: [cb4c8a81dee21575a3f63593b5358cc4](https://search.dartslive.com/jp/shop/cb4c8a81dee21575a3f63593b5358cc4). 東京都渋谷区渋谷3-7-7 窪田ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93665](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93665). 150-0002 東京都渋谷区渋谷3-7-7 窪田ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 14.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Asobi Bar Snow / Asobi Bar Snow

- **DARTSLIVE**: [f4de85827fa0b46b774c926eb736cb5a](https://search.dartslive.com/jp/shop/f4de85827fa0b46b774c926eb736cb5a). 群馬県前橋市本町2-7-6 DKビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94217](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94217). 371-0023 群馬県前橋市本町2-7-6 DKビル 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 2.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Cafe ZICCA / Amusement Cafe ZICCA

- **DARTSLIVE**: [9b2426787763c7180d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9b2426787763c7180d9b047a20a7ba1e). 埼玉県さいたま市中央区本町東1-9-8. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94399](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94399). 338-0003 埼玉県さいたま市中央区本町東1-9-8. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 4.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 千音寺店 / 快活CLUB 千音寺店

- **DARTSLIVE**: [a85e10fd75f3d68a28032249b44395af](https://search.dartslive.com/jp/shop/a85e10fd75f3d68a28032249b44395af). 愛知県名古屋市中川区新家3-1407. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [95231](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95231). 454-0972 愛知県名古屋市中川区新家3-1407. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン三宮駅前店 / ラウンドワン三宮駅前店

- **DARTSLIVE**: [15a13423c1b54e260d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/15a13423c1b54e260d9b047a20a7ba1e). 兵庫県神戸市中央区小野柄通6-1-17. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [9617](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9617). 651-0088 兵庫県神戸市中央区小野柄通6-1-17. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 7.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 湖浜店 / 自遊空間 湖浜店

- **DARTSLIVE**: [1400e9bdc5d14a45790ab824ce8730e5](https://search.dartslive.com/jp/shop/1400e9bdc5d14a45790ab824ce8730e5). 長野県諏訪郡下諏訪町高浜6191-3. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9744](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9744). 393-0034 長野県諏訪郡下諏訪町高浜6191-3. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 94.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY天白笹原店 / JOYJOY 天白笹原店

- **DARTSLIVE**: [4bd7225e0ecbb8a5b21333aee1bd51e4](https://search.dartslive.com/jp/shop/4bd7225e0ecbb8a5b21333aee1bd51e4). 愛知県名古屋市天白区笹原町1904. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9830](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9830). 468-0044 愛知県名古屋市天白区笹原町1904. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 2.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン東淀川店 / ラウンドワン 東淀川店

- **DARTSLIVE**: [9a2ad7b58377a7150d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9a2ad7b58377a7150d9b047a20a7ba1e). 大阪府大阪市東淀川区菅原7-14-29. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [98969](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98969). 533-0022 大阪府大阪市東淀川区菅原7-14-29. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.829; Source-pin distance 8.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 姫DARTS / 姫DARTS

- **DARTSLIVE**: [6c72b6d03e9948920d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6c72b6d03e9948920d9b047a20a7ba1e). 東京都豊島区西池袋1-38-7 MSビル6F・A. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6272](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6272). 171-0021 東京都豊島区西池袋1-38-7 MSビル6F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.826; Source-pin distance 5.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DiNiNG&amp;CAFE DAY-Z / DINING&amp;CAFE DAY-Z

- **DARTSLIVE**: [4a618b31e4b819e20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4a618b31e4b819e20d9b047a20a7ba1e). 北海道旭川市5条通7丁目 第2コアビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72180](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72180). 070-0035 北海道旭川市5条7丁目 第2コアビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.826; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Noge darts bar 180 / Noge darts bar 180

- **DARTSLIVE**: [2fafa4f888128f930d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2fafa4f888128f930d9b047a20a7ba1e). 神奈川県横浜市中区野毛町2-79 林ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [81844](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81844). 231-0064 神奈川県横浜市中区野毛2-79 林ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.826; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: GOODSUM / GOOD SUM

- **DARTSLIVE**: [4d9e3507897339430d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4d9e3507897339430d9b047a20a7ba1e). 岩手県盛岡市大通2-7-28 サウスウイング大通第二ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92923](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92923). 020-0022 岩手県盛岡市大通2丁目7-28 サウスウイング大通第2ビル2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.825; Source-pin distance 11.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ 御殿場インター店 / アプレシオ 御殿場インター店

- **DARTSLIVE**: [1bc6a631840417f6fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/1bc6a631840417f6fec1ae84bb28bd87). 静岡県御殿場市東田中1066-1 東富士ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [61735](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61735). 412-0026 静岡県御殿場市東田中1066-1 東富士ビル2階. Inventory: VSPhoenix X 2台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.824; Source-pin distance 13.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar Room / Bar Room

- **DARTSLIVE**: [b61de1544136116d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b61de1544136116d0d9b047a20a7ba1e). 千葉県船橋市前原西2-13-24 SKDビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [82833](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82833). 274-0825 千葉県船橋市前原西2丁目13-24 SKDビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.824; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar LEMON / Amusement Bar LEMON

- **DARTSLIVE**: [3957b09c667b8a060d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3957b09c667b8a060d9b047a20a7ba1e). 東京都江戸川区東葛西6-2-6 第2須三ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99024](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99024). 134-0084 東京都江戸川区東葛西6-2-6 第2第三須三ビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.824; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カジュアルバーPocket / カジュアルバー Pocket

- **DARTSLIVE**: [90efc7137205388b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/90efc7137205388b0d9b047a20a7ba1e). 栃木県大田原市中央1-14-12-2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100227](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100227). 324-0056 栃木県大田原市中央1-14-12 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 1.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 鹿児島国分店 / 自遊空間 鹿児島国分店

- **DARTSLIVE**: [031bbf815207c800f454cb89828a1cfe](https://search.dartslive.com/jp/shop/031bbf815207c800f454cb89828a1cfe). 鹿児島県霧島市国分野口東1403. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10093](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10093). 899-4341 鹿児島県霧島市国分野口東1403. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 220.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン仙台苦竹店 / ラウンドワン仙台苦竹店

- **DARTSLIVE**: [7bb1301094a1553f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7bb1301094a1553f0d9b047a20a7ba1e). 宮城県仙台市宮城野区苦竹1-7-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [10304](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10304). 983-0036 宮城県仙台市宮城野区苦竹1-7-10. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 23.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コート・ダジュール 仙台名取店 / コート・ダジュール仙台名取店

- **DARTSLIVE**: [8fdf7aee513600e628032249b44395af](https://search.dartslive.com/jp/shop/8fdf7aee513600e628032249b44395af). 宮城県名取市上余田千刈田900-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [10326](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10326). 981-1222 宮城県名取市上余田千刈田900-2. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 四軒家店 / 快活CLUB 四軒家店

- **DARTSLIVE**: [baa0e63106aaa1dbb21333aee1bd51e4](https://search.dartslive.com/jp/shop/baa0e63106aaa1dbb21333aee1bd51e4). 愛知県名古屋市守山区白山3-503. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [10327](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10327). 463-0032 愛知県名古屋市守山区白山3-503. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 59.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン城東放出店 / ラウンドワン城東放出店

- **DARTSLIVE**: [5bcdd1c44102954d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5bcdd1c44102954d0d9b047a20a7ba1e). 大阪府大阪市城東区今福南3-4-38. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10419](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10419). 536-0003 大阪府大阪市城東区今福南3-4-38. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 28.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊時間 大河原店 / 自遊時間 大河原店

- **DARTSLIVE**: [24f02e3acd4ce6ac0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/24f02e3acd4ce6ac0d9b047a20a7ba1e). 宮城県柴田郡大河原町新南62-25. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10422](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10422). 989-1245 宮城県柴田郡大河原町新南62-25. Inventory: VSPhoenix X 1台 VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン盛岡店 / ラウンドワン盛岡店

- **DARTSLIVE**: [6c2f5a6f875df07a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6c2f5a6f875df07a0d9b047a20a7ba1e). 岩手県盛岡市盛岡駅西通2-10-35. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10462](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10462). 020-0045 岩手県盛岡市盛岡駅西通2-10-35. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 38.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 上熊本店 / 快活CLUB上熊本店

- **DARTSLIVE**: [7fa8d125df25367e25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/7fa8d125df25367e25d56fb0e5c39bac). 熊本県熊本市西区上熊本2-17-42. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [41747](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=41747). 860-0079 熊本県熊本市西区上熊本2-17-42. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 3.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY南陽通店 / JOYJOY 南陽通店

- **DARTSLIVE**: [5508b843123eab08fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/5508b843123eab08fec1ae84bb28bd87). 愛知県名古屋市南区三条1-10-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [44369](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44369). 457-0866 愛知県名古屋市南区三条1-10-11. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 16.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 薩摩川内店 / 自遊空間 薩摩川内店

- **DARTSLIVE**: [2638bf474abb4dea790ab824ce8730e5](https://search.dartslive.com/jp/shop/2638bf474abb4dea790ab824ce8730e5). 鹿児島県薩摩川内市西向田町7-33. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [47747](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47747). 895-0025 鹿児島県薩摩川内市西向田町7-33. Inventory: VSPHOENIX S4 5台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 20.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 四軒家店 / 亜熱帯 四軒家店

- **DARTSLIVE**: [5adbc1902f55e102774c926eb736cb5a](https://search.dartslive.com/jp/shop/5adbc1902f55e102774c926eb736cb5a). 愛知県名古屋市守山区白山2-102. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56057](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56057). 463-0032 愛知県名古屋市守山区白山2-102. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 12.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 東仙台店 / 快活CLUB 東仙台店

- **DARTSLIVE**: [2fa0c25ff56a5d2cfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/2fa0c25ff56a5d2cfec1ae84bb28bd87). 宮城県仙台市宮城野区小鶴3-8-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [5986](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5986). 983-0031 宮城県仙台市宮城野区小鶴3-8-10. Inventory: VSPhoenix X 1台 VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 16.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 新堀川店 / 快活CLUB 新堀川店

- **DARTSLIVE**: [7c75c165d5c50554f454cb89828a1cfe](https://search.dartslive.com/jp/shop/7c75c165d5c50554f454cb89828a1cfe). 京都府京都市伏見区南寝小屋町21. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [6524](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6524). 612-8379 京都府京都市伏見区南寝小屋町21. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 19.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: D&#x27;s House / D&#x27;s House

- **DARTSLIVE**: [40b0914f275b9d3e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/40b0914f275b9d3e0d9b047a20a7ba1e). 福岡県糟屋郡志免町志免中央3-1-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [72496](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72496). 811-2244 福岡県糟屋郡志免町志免中央3-1-1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 39.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ゆう遊空間 三河安城店 / ゆう遊空間 三河安城店

- **DARTSLIVE**: [0034be99cb4d06f40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0034be99cb4d06f40d9b047a20a7ba1e). 愛知県安城市三河安城南町1-21-3. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [7826](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7826). 446-0058 愛知県安城市三河安城南町1-21-3. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 97.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar Yellow Soul Force / BAR Yellow Soul Force

- **DARTSLIVE**: [f25f92408810e06f58d385ea46352d8f](https://search.dartslive.com/jp/shop/f25f92408810e06f58d385ea46352d8f). 東京都港区新橋4-6-6 米山ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [78715](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78715). 105-0004 東京都港区新橋4-6-6　米山ビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 八幡穴生店 / 快活CLUB 八幡穴生店

- **DARTSLIVE**: [971ebab4258808c258d385ea46352d8f](https://search.dartslive.com/jp/shop/971ebab4258808c258d385ea46352d8f). 福岡県北九州市八幡西区穴生1-8-3. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [78735](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78735). 806-0049 福岡県北九州市八幡西区穴生1-8-3. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY名駅笹島店 / JOYJOY 名駅笹島店

- **DARTSLIVE**: [7cb2a10db45a1e8f28032249b44395af](https://search.dartslive.com/jp/shop/7cb2a10db45a1e8f28032249b44395af). 愛知県名古屋市中村区名駅4-27-7. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79035](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79035). 450-0002 愛知県名古屋市中村区名駅4-27-7. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 5.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 中川コロナワールド店 / 亜熱帯 中川コロナワールド店

- **DARTSLIVE**: [ef7e3b9d4b7df9e2fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/ef7e3b9d4b7df9e2fec1ae84bb28bd87). 愛知県名古屋市中川区江松3-124. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [8064](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8064). 454-0954 愛知県名古屋市中川区江松3-124. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 10.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY中川山王店 / JOYJOY 中川山王店

- **DARTSLIVE**: [787a52c97b5cdb39790ab824ce8730e5](https://search.dartslive.com/jp/shop/787a52c97b5cdb39790ab824ce8730e5). 愛知県名古屋市中川区山王2-3-75. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8066](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8066). 454-0011 愛知県名古屋市中川区山王2-3-75. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 27.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY大須赤門店 / JOYJOY 大須赤門店

- **DARTSLIVE**: [2d280f587a7b17b528032249b44395af](https://search.dartslive.com/jp/shop/2d280f587a7b17b528032249b44395af). 愛知県名古屋市中区大須4-10-92. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8125](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8125). 460-0011 愛知県名古屋市中区大須4-10-92. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 5.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コローレ浜松市野店 / コローレ浜松市野店

- **DARTSLIVE**: [e8cb34d7b0f98c240d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e8cb34d7b0f98c240d9b047a20a7ba1e). 静岡県浜松市東区小池町2441-9. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8456](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8456). 435-0056 静岡県浜松市東区小池町2441-9. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 23.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: AMERICAN GORILLA&#x27;S / AMERICAN GORILLA&#x27;S

- **DARTSLIVE**: [6a548cb7df8634300d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6a548cb7df8634300d9b047a20a7ba1e). 東京都台東区根岸1-1-15 花久ビル. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86659](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86659). 110-0003 東京都台東区根岸1-1-15 花久ビル. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 1.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Pubilic Space 9 / Pubilic Space 9

- **DARTSLIVE**: [020f55d1d67f90940d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/020f55d1d67f90940d9b047a20a7ba1e). 福岡県北九州市若松区中川町1-17. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [86935](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86935). 815-0033 福岡県北九州市若松区中川町1-17. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 4.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 横浜WEST店 / ダイニングダーツバーBee 横浜WEST店

- **DARTSLIVE**: [ae46c94e170e76dc790ab824ce8730e5](https://search.dartslive.com/jp/shop/ae46c94e170e76dc790ab824ce8730e5). 神奈川県横浜市西区南幸2-15-1 ティノ（TINO）ビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [89169](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89169). 220-0005 神奈川県横浜市西区南幸２-15-1 TINOビル 7F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ゴースト / ゴースト

- **DARTSLIVE**: [483e8aac2fcb2d4df454cb89828a1cfe](https://search.dartslive.com/jp/shop/483e8aac2fcb2d4df454cb89828a1cfe). 長野県長野市上千歳町1412-5 中部ちとせビル2Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89360](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89360). 380-0821 長野県長野市鶴賀上千歳1412-5 中部ちとせビル2F. Inventory: VSPhoenix X 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DAMA DE NOCHE / Dama De Noche

- **DARTSLIVE**: [6911cf3adf3dce3d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6911cf3adf3dce3d0d9b047a20a7ba1e). 愛知県東海市名和町一番割中24-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89949](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89949). 476-0002 愛知県東海市名和町一番割中24-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 2.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 岡山大安寺店 / 快活CLUB 岡山大安寺店

- **DARTSLIVE**: [79d4a2dacc630d44790ab824ce8730e5](https://search.dartslive.com/jp/shop/79d4a2dacc630d44790ab824ce8730e5). 岡山県岡山市北区大安寺南町2-6-5. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9039](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9039). 700-0064 岡山県岡山市北区大安寺南町2-6-5. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 長崎時津店 / 自遊空間 長崎時津店

- **DARTSLIVE**: [76242a83b3a999b3fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/76242a83b3a999b3fec1ae84bb28bd87). 長崎県西彼杵郡時津町左底郷36-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9296](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9296). 851-2106 長崎県西彼杵郡時津町左底郷36-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 5台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 15.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY新瑞橋店 / JOYJOY 新瑞橋店

- **DARTSLIVE**: [aaf2697db51a8fdcb21333aee1bd51e4](https://search.dartslive.com/jp/shop/aaf2697db51a8fdcb21333aee1bd51e4). 愛知県名古屋市瑞穂区洲山町2-22. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9515](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9515). 467-0066 愛知県名古屋市瑞穂区洲山町2-22. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 51.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン前橋店 / ラウンドワン 前橋店

- **DARTSLIVE**: [2ab6f74bd4f4f08c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2ab6f74bd4f4f08c0d9b047a20a7ba1e). 群馬県前橋市天川大島町1101-1. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99027](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99027). 379-2154 群馬県前橋市天川大島町1101-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.821; Source-pin distance 7.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン千種店 / ラウンドワン千種店

- **DARTSLIVE**: [4e13cdd41e1897e80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4e13cdd41e1897e80d9b047a20a7ba1e). 愛知県名古屋市千種区新栄3-20-17 千種駅南ビル8F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [7964](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7964). 464-0859 愛知県名古屋市千種区新栄3-20-17 タイホウ千種駅南ビル8F. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.820; Source-pin distance 25.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts＆SportBar Second / Darts＆SportsBar second

- **DARTSLIVE**: [886eed41c657d60c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/886eed41c657d60c0d9b047a20a7ba1e). 東京都練馬区上石神井1-16-4 上石田中ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [85212](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85212). 177-0044 東京都練馬区上石神井1-16-4 上石田ビルB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.974; Full-address similarity 0.846; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts &amp; Dining DOUBLE / Darts&amp;Dining DOUBLE

- **DARTSLIVE**: [a3e2be1c7fd0542f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a3e2be1c7fd0542f0d9b047a20a7ba1e). 群馬県太田市飯田町602 M2ビル2F-E. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [6339](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6339). 373-0851 群馬県太田市飯田町602 M2ビル2F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.818; Source-pin distance 3.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: タイトーステーション 広島本通店 / タイトーステーション広島本通

- **DARTSLIVE**: [27b40f576eeec62b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/27b40f576eeec62b0d9b047a20a7ba1e). 広島県広島市中区本通3-5 せらかぐ本通ビル. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9138](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9138). 730-0035 広島県広島市中区本通3-5 せらかぐ本通ビル. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.966; Full-address similarity 0.851; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Pool&amp;Darts REST / Pool&amp;Darts REST

- **DARTSLIVE**: [ac5be316943858f0fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/ac5be316943858f0fec1ae84bb28bd87). 東京都台東区浅草3-16-1 ディアハイム2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [50587](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50587). 111-0032 東京都台東区浅草3-16-1 ディアハイム浅草2F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Raku　Darts / Raku Darts

- **DARTSLIVE**: [988ea781999e8c3c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/988ea781999e8c3c0d9b047a20a7ba1e). 埼玉県草加市旭町1-4-4 SHIOYAビル2階. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [64709](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=64709). 340-0053 埼玉県草加市旭町1-4-4 SHIOYAビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 4.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Little Wing / Little Wing

- **DARTSLIVE**: [639f9c02b5ad16fb0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/639f9c02b5ad16fb0d9b047a20a7ba1e). 大阪府茨木市大手町1-5 オーティーハイツ2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7598](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7598). 567-0883 大阪府茨木市大手町1-5 オーディーハイツ2Ｆ. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 1.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 銀座店 / ダイニングダーツバーBee 銀座店

- **DARTSLIVE**: [ca24f5221ef4f7bf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ca24f5221ef4f7bf0d9b047a20a7ba1e). 東京都中央区銀座8-5 銀座ナイン1号館2F. Inventory: {&quot;DARTSLIVE2&quot;: 7, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89077](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89077). 104-0061 東京都中央区銀座８丁目５ 銀座ナイン1号館 2Ｆ. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 14.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Sports&amp;Dining 鴉 / Sports&amp;Dining 鴉

- **DARTSLIVE**: [179355d68bf3e2df58d385ea46352d8f](https://search.dartslive.com/jp/shop/179355d68bf3e2df58d385ea46352d8f). 兵庫県西脇市西脇771-86 松田ビル2FC号. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91659](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91659). 677-0015 兵庫県西脇市西脇771-86 松岡ビル2F-C号. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 5.8 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 蒲田店 / Link 蒲田店

- **DARTSLIVE**: [e33a0b3568abeac4790ab824ce8730e5](https://search.dartslive.com/jp/shop/e33a0b3568abeac4790ab824ce8730e5). 東京都大田区西蒲田7-3-3 第一醍醐ビル8F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [92017](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92017). 144-0051 東京都大田区西蒲田7丁目3-3 第一醍醐ビル8F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: C.STAND歌舞伎町3号店 / C.STAND 歌舞伎町3号店

- **DARTSLIVE**: [abdbe117b83e79c40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/abdbe117b83e79c40d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-26-7 カワノビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92227](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92227). 160-0021 東京都新宿区歌舞伎町1-26-7 カワノビル4階. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe&amp;Bar MASSE / Cafe&amp;Bar MASSE

- **DARTSLIVE**: [7dc3acdeea8b72d10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7dc3acdeea8b72d10d9b047a20a7ba1e). 千葉県八千代市八千代台南1-3-3 山萬ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93487](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93487). 276-0033 千葉県八千代市八千代台南1-3-3 三萬ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SPORTS&amp;DARTS BAR TAT / SPORTS&amp;DARTS BAR TAT

- **DARTSLIVE**: [f4a40074b3e5fb7c774c926eb736cb5a](https://search.dartslive.com/jp/shop/f4a40074b3e5fb7c774c926eb736cb5a). 沖縄県那覇市安里2-4-12 マキシアルパB1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [94019](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94019). 902-0067 沖縄県那覇市安里2-4-12 マキシアルパビル B1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 2.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Planet Boy / Planet Boy

- **DARTSLIVE**: [4d65af6c0d1b0e7d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4d65af6c0d1b0e7d0d9b047a20a7ba1e). 東京都台東区雷門2-17-13 ウスイビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9694](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9694). 111-0034 東京都台東区雷門2-17-13 雷門ウスイビル7F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: U.S.BAR BASE / U.S.BAR BASE

- **DARTSLIVE**: [921d84f6d94325880d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/921d84f6d94325880d9b047a20a7ba1e). 新潟県新発田市中央町3-8-9 江戸屋餅菓子舗2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99853](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99853). 957-0053 新潟県新発田市中央町3-8-9 江戸屋餅菓子舗. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.816; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ焼津店 / アプレシオ 焼津店

- **DARTSLIVE**: [56385fb0abfd86eb774c926eb736cb5a](https://search.dartslive.com/jp/shop/56385fb0abfd86eb774c926eb736cb5a). 静岡県焼津市宗高1487-1 大井川グラーノリバー内. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8420](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8420). 421-0205 静岡県焼津市宗高1487-1　大井川グランリバー内. Inventory: VSPhoenix X 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.815; Source-pin distance 13.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: D-SPE / D-SPE

- **DARTSLIVE**: [6a4d56ab88db216a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6a4d56ab88db216a0d9b047a20a7ba1e). 愛知県名古屋市中区栄3丁目8-3-2 A＊G SAKAE2F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [89688](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89688). 460-0008 愛知県名古屋市中区栄三丁目8-3-2 AG SAKAEビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.814; Source-pin distance 17.9 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯栄住吉店 / 亜熱帯 栄住吉店

- **DARTSLIVE**: [5656031ca5625690a3f63593b5358cc4](https://search.dartslive.com/jp/shop/5656031ca5625690a3f63593b5358cc4). 愛知県名古屋市中区栄3-11-12. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10136](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10136). 460-0008 愛知県名古屋市中区栄3-11-12. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 6.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 会津若松店 / 快活CLUB 会津若松店

- **DARTSLIVE**: [1c370e2016e905b358d385ea46352d8f](https://search.dartslive.com/jp/shop/1c370e2016e905b358d385ea46352d8f). 福島県会津若松市天神町21-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10165](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10165). 965-0832 福島県会津若松市天神町21-11. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン大野城店 / ラウンドワン大野城店

- **DARTSLIVE**: [b7bd934082764c010d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b7bd934082764c010d9b047a20a7ba1e). 福岡県大野城市御笠川1-18-16. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10481](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10481). 816-0912 福岡県大野城市御笠川1-18-16. Inventory: VSPhoenix X 1台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 26.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン豊橋店 / ラウンドワン豊橋店

- **DARTSLIVE**: [b01ab2c1f33a41960d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b01ab2c1f33a41960d9b047a20a7ba1e). 愛知県豊橋市大岩町字岩田27-2. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10482](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10482). 441-3147 愛知県豊橋市大岩町字岩田27-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 36.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ 甲斐竜王店 / アプレシオ 甲斐竜王店

- **DARTSLIVE**: [65d17b6fddab89c30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/65d17b6fddab89c30d9b047a20a7ba1e). 山梨県甲斐市富竹新田1454-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10616](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10616). 400-0113 山梨県甲斐市富竹新田1454-1. Inventory: VSPhoenix X 3台 VSPhoenix X-MAX 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン函館店 / ラウンドワン函館店

- **DARTSLIVE**: [665ea30911745eb60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/665ea30911745eb60d9b047a20a7ba1e). 北海道函館市西桔梗町848-11. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10661](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10661). 041-0824 北海道函館市西桔梗町848-11. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 64.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Rest and Bar GHOST / Rest and Bar GHOST

- **DARTSLIVE**: [c932fe19e82e51f60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c932fe19e82e51f60d9b047a20a7ba1e). 群馬県邑楽郡大泉町坂田2-13-6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [10673](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10673). 370-0532 群馬県邑楽郡大泉町坂田2-13-6. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 1.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS SHOP LOZA / DARTS SHOP LOZA

- **DARTSLIVE**: [2d936e4e641aea5d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2d936e4e641aea5d0d9b047a20a7ba1e). 静岡県駿東郡清水町長沢865-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [41033](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=41033). 411-0905 静岡県駿東郡清水町長沢865-1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 居酒屋 GARAGE / 居酒屋 GARAGE

- **DARTSLIVE**: [00c360a9e79085600d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/00c360a9e79085600d9b047a20a7ba1e). 東京都府中市若松町2-8-12-1F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [43360](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43360). 183-0005 東京都府中市若松町2-8-12 1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コート・ダジュール 甲府昭和店 / コート・ダジュール 甲府昭和店

- **DARTSLIVE**: [1f0bf80ef7fc7ba9790ab824ce8730e5](https://search.dartslive.com/jp/shop/1f0bf80ef7fc7ba9790ab824ce8730e5). 山梨県中巨摩郡昭和町西条71-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [45648](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=45648). 409-3866 山梨県中巨摩郡昭和町西条71-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 佐賀本庄店 / 快活CLUB 佐賀本庄店

- **DARTSLIVE**: [40cd56037aee4d7bf454cb89828a1cfe](https://search.dartslive.com/jp/shop/40cd56037aee4d7bf454cb89828a1cfe). 佐賀県佐賀市本庄町本庄969-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [46764](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=46764). 840-0027 佐賀県佐賀市本庄町本庄969-1. Inventory: VSPhoenix X 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 大和郡山店 / 快活CLUB 大和郡山店

- **DARTSLIVE**: [a4d804bf25f3835058d385ea46352d8f](https://search.dartslive.com/jp/shop/a4d804bf25f3835058d385ea46352d8f). 奈良県大和郡山市筒井町531-6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [48031](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=48031). 639-1123 奈良県大和郡山市筒井町531-6. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 楽市楽座久留米店 / 快活CLUB楽市楽座久留米店

- **DARTSLIVE**: [3adde4ca52ca63d9774c926eb736cb5a](https://search.dartslive.com/jp/shop/3adde4ca52ca63d9774c926eb736cb5a). 福岡県久留米市東合川2-2-1-3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [50884](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50884). 839-0809 福岡県久留米市東合川2-2-1 3F. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 8.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ＆ビリヤード　キューベスト / ダーツ＆ビリヤード キューベスト

- **DARTSLIVE**: [1aa4c28242c1b0cf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1aa4c28242c1b0cf0d9b047a20a7ba1e). 東京都調布市小島町2-54-4B1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52539](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52539). 182-0026 東京都調布市小島町2-54-4 B1. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Campanula / Campanula

- **DARTSLIVE**: [27d4ede742d2d5030d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/27d4ede742d2d5030d9b047a20a7ba1e). 神奈川県川崎市川崎区宮本町2-5. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52548](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52548). 210-0004 神奈川県川崎市川崎区宮本町2-5. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 2.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Mars.Kamata / Mars.Kamata

- **DARTSLIVE**: [acb670ff3ff4a52e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/acb670ff3ff4a52e0d9b047a20a7ba1e). 東京都大田区西蒲田7-31-9-B1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [55363](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=55363). 144-0051 東京都大田区西蒲田7-31-9 B1. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 山口大内店 / 快活CLUB 山口大内店

- **DARTSLIVE**: [5bb0a768e73006f65f9f3321c1147265](https://search.dartslive.com/jp/shop/5bb0a768e73006f65f9f3321c1147265). 山口県山口市大内御堀1505-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56041](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56041). 753-0214 山口県山口市大内御堀1505-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 清水春日店 / 快活CLUB 清水春日店

- **DARTSLIVE**: [4a5406da498886a2a3f63593b5358cc4](https://search.dartslive.com/jp/shop/4a5406da498886a2a3f63593b5358cc4). 静岡県静岡市清水区春日1-5-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56120](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56120). 424-0842 静岡県静岡市清水区春日1-5-11. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Bar Beard / Darts&amp;Bar Beard

- **DARTSLIVE**: [15581b4c371d2abd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/15581b4c371d2abd0d9b047a20a7ba1e). 神奈川県川崎市川崎区元木1-6-9. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [57346](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=57346). 210-0021 神奈川県川崎市川崎区元木1-6-9. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 撞球倶楽部 / 撞球倶楽部

- **DARTSLIVE**: [90e81694f8aba1ea0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/90e81694f8aba1ea0d9b047a20a7ba1e). 長崎県長崎市本石灰町6-44-B1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [58747](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58747). 850-0901 長崎県長崎市本石灰町6-44 B1. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ぽっぽやはうす / ぽっぽやはうす

- **DARTSLIVE**: [ee3cd8030ab2768ba3f63593b5358cc4](https://search.dartslive.com/jp/shop/ee3cd8030ab2768ba3f63593b5358cc4). 沖縄県那覇市銘苅180-1-302. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [5924](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5924). 900-0004 沖縄県那覇市銘苅180-1-302. Inventory: VSPHOENIX S 6台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 33.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 枚方市駅北口店 / 快活CLUB 枚方市駅北口店

- **DARTSLIVE**: [f4820059816a00a2b21333aee1bd51e4](https://search.dartslive.com/jp/shop/f4820059816a00a2b21333aee1bd51e4). 大阪府枚方市岡本町2-22-2・3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [60504](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=60504). 573-0031 大阪府枚方市岡本町2-22 2･3F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 下関長府店 / 快活CLUB 下関長府店

- **DARTSLIVE**: [cc47c9d364db45bf5f9f3321c1147265](https://search.dartslive.com/jp/shop/cc47c9d364db45bf5f9f3321c1147265). 山口県下関市長府才川1-42-30. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [61638](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61638). 752-0928 山口県下関市長府才川1-42-30. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY稲沢グランドボウル店 / JOYJOY 稲沢グランドボウル店

- **DARTSLIVE**: [3da6aa97cb5b44edfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/3da6aa97cb5b44edfec1ae84bb28bd87). 愛知県稲沢市井之口大坪町80-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [6507](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6507). 492-8164 愛知県稲沢市井之口大坪町80-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 183.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 青江ビリヤードセンター / 青江ビリヤードセンター

- **DARTSLIVE**: [20c9de9de1d9d2830d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/20c9de9de1d9d2830d9b047a20a7ba1e). 岡山県岡山市北区青江5-16-26. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [70022](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70022). 700-0941 岡山県岡山市北区青江5-16-26. Inventory: VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 79.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間太宰府店 / 自遊空間　太宰府店

- **DARTSLIVE**: [607cc594974a75e8b21333aee1bd51e4](https://search.dartslive.com/jp/shop/607cc594974a75e8b21333aee1bd51e4). 福岡県太宰府市高雄1-3675-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7148](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7148). 818-0122 福岡県太宰府市高雄1-3675-1. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 5.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン梅田店 / ラウンドワン梅田店

- **DARTSLIVE**: [b9bc068ea231b1f00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b9bc068ea231b1f00d9b047a20a7ba1e). 大阪府大阪市北区小松原町4-16. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 9}.
- **Phoenix**: [71806](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71806). 530-0018 大阪府大阪市北区小松原町4-16. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 24.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン福岡天神店 / ラウンドワン福岡天神店

- **DARTSLIVE**: [55d3d87938b20adc0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/55d3d87938b20adc0d9b047a20a7ba1e). 福岡県福岡市中央区天神2-6-12. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [71844](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71844). 810-0001 福岡県福岡市中央区天神2-6-12. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 37.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: フタバカラオケプラス泉大津店 / フタバカラオケプラス泉大津店

- **DARTSLIVE**: [9caa282de29c36450d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9caa282de29c36450d9b047a20a7ba1e). 大阪府泉大津市松之浜町1-2-53. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7395](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7395). 595-0072 大阪府泉大津市松之浜町1-2-53. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 6.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケBanBan鹿児島新栄店 / カラオケBanBan 鹿児島新栄店

- **DARTSLIVE**: [5b8b3ca55958057b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5b8b3ca55958057b0d9b047a20a7ba1e). 鹿児島県鹿児島市新栄町10-35. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [76853](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=76853). 890-0072 鹿児島県鹿児島市新栄町10-35. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Lion / Lion

- **DARTSLIVE**: [39c679be0f01d14c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/39c679be0f01d14c0d9b047a20a7ba1e). 秋田県大仙市大曲丸の内町6-20. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [77955](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77955). 014-0026 秋田県大仙市大曲丸の内町6-20. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 15.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 東広島西条2号店 / 快活CLUB 東広島西条2号店

- **DARTSLIVE**: [e00c29518bac50a525d56fb0e5c39bac](https://search.dartslive.com/jp/shop/e00c29518bac50a525d56fb0e5c39bac). 広島県東広島市西条御条町1-21. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [78736](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78736). 739-0013 広島県東広島市西条御条町1-21. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 山口吉敷店 / 快活CLUB 山口吉敷店

- **DARTSLIVE**: [911d654358853ec9774c926eb736cb5a](https://search.dartslive.com/jp/shop/911d654358853ec9774c926eb736cb5a). 山口県山口市吉敷下東4-18-25. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79550](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79550). 753-0814 山口県山口市吉敷下東4-18-25. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 大船オトナノパブリック / 大船オトナノパブリック

- **DARTSLIVE**: [f78ed53f098e84880d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f78ed53f098e84880d9b047a20a7ba1e). 神奈川県鎌倉市大船2-6-42-2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [82537](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82537). 247-0056 神奈川県鎌倉市大船2-6-42 2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 旭川大町店 / 快活CLUB 旭川大町店

- **DARTSLIVE**: [8f57be8081041e6cb21333aee1bd51e4](https://search.dartslive.com/jp/shop/8f57be8081041e6cb21333aee1bd51e4). 北海道旭川市大町1条3-14-13. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82822](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82822). 070-0841 北海道旭川市大町1条3-14-13. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ豊川店 / アプレシオ 豊川店

- **DARTSLIVE**: [73871d7b66b7dc7f25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/73871d7b66b7dc7f25d56fb0e5c39bac). 愛知県豊川市牛久保町城下89-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8313](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8313). 442-0826 愛知県豊川市牛久保町城下89-1. Inventory: VSPhoenix X 2台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 4.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: タイトーステーション仙台クリスロード店 / タイトーステーション仙台クリスロード店

- **DARTSLIVE**: [26830b897e3db3580d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/26830b897e3db3580d9b047a20a7ba1e). 宮城県仙台市青葉区中央2-3-25. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 10}.
- **Phoenix**: [8428](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8428). 980-0021 宮城県仙台市青葉区中央2-3-25. Inventory: VSPHOENIX S 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 新津程島店 / 快活CLUB 新津程島店

- **DARTSLIVE**: [de9e906e37621b55f454cb89828a1cfe](https://search.dartslive.com/jp/shop/de9e906e37621b55f454cb89828a1cfe). 新潟県新潟市秋葉区程島1876. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [84430](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84430). 956-0035 新潟県新潟市秋葉区程島1876. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY尾西郷東店 / JOYJOY 尾西郷東店

- **DARTSLIVE**: [1bbfb1aa6775ed00a3f63593b5358cc4](https://search.dartslive.com/jp/shop/1bbfb1aa6775ed00a3f63593b5358cc4). 愛知県一宮市小信中島郷東45-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90101](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90101). 494-0007 愛知県一宮市小信中島郷東45-1. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: southern garden / southern garden

- **DARTSLIVE**: [1f228cca515ee90125d56fb0e5c39bac](https://search.dartslive.com/jp/shop/1f228cca515ee90125d56fb0e5c39bac). 沖縄県那覇市おもろまち4-6-18. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9096](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9096). 900-0006 沖縄県那覇市おもろまち4-6-18. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 5.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 福山東深津店 / 快活CLUB 福山東深津店

- **DARTSLIVE**: [570fcf41372c30cafec1ae84bb28bd87](https://search.dartslive.com/jp/shop/570fcf41372c30cafec1ae84bb28bd87). 広島県福山市東深津町3-14-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9154](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9154). 721-0974 広島県福山市東深津町3-14-11. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 149.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 苫小牧店 / 自遊空間　苫小牧店

- **DARTSLIVE**: [63d319dc2404821c58d385ea46352d8f](https://search.dartslive.com/jp/shop/63d319dc2404821c58d385ea46352d8f). 北海道苫小牧市新中野町1-1-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [9186](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9186). 053-0006 北海道苫小牧市新中野町1-1-10. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 3.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS BAR FELES / DARTS BAR FELES

- **DARTSLIVE**: [befd37484afffe800d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/befd37484afffe800d9b047a20a7ba1e). 大阪府大阪市西成区太子2-4-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92076](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92076). 557-0002 大阪府大阪市西成区太子2-4-11. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ金沢駅西店 / アプレシオ 金沢駅西店

- **DARTSLIVE**: [be9e0d0512ffbcfff454cb89828a1cfe](https://search.dartslive.com/jp/shop/be9e0d0512ffbcfff454cb89828a1cfe). 石川県金沢市駅西新町3-14-21. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9435](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9435). 920-0027 石川県金沢市駅西新町3-14-21. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 7.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 春日井インター店 / 快活CLUB 春日井インター店

- **DARTSLIVE**: [99506c1353adee19774c926eb736cb5a](https://search.dartslive.com/jp/shop/99506c1353adee19774c926eb736cb5a). 愛知県春日井市東野新町1-1-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9488](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9488). 486-0816 愛知県春日井市東野新町1-1-10. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 1.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン横浜駅西口店 / ラウンドワン横浜駅西口店

- **DARTSLIVE**: [b4d667355207f7f60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b4d667355207f7f60d9b047a20a7ba1e). 神奈川県横浜市西区南幸2-8-16. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [9599](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9599). 220-0005 神奈川県横浜市西区南幸2-8-16. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 5.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: mar VEROUS / mar VEROUS

- **DARTSLIVE**: [e04975ba919164c60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e04975ba919164c60d9b047a20a7ba1e). 東京都福生市福生876‐12-2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9711](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9711). 197-0011 東京都福生市福生876-12 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 16.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY春日井高蔵寺店 / JOYJOY 春日井高蔵寺店

- **DARTSLIVE**: [e72639e3bbe021d8f454cb89828a1cfe](https://search.dartslive.com/jp/shop/e72639e3bbe021d8f454cb89828a1cfe). 愛知県春日井市高蔵寺町北1-44. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9873](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9873). 487-0016 愛知県春日井市高蔵寺町北1-44. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 39.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン和歌山店 / ラウンドワン 和歌山店

- **DARTSLIVE**: [fb5d65de23c5d0960d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/fb5d65de23c5d0960d9b047a20a7ba1e). 和歌山県和歌山市小雑賀739-3. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98976](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98976). 641-0007 和歌山県和歌山市小雑賀739-3. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 45.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 17号高崎倉賀野店 / 快活CLUB 17号高崎倉賀野店

- **DARTSLIVE**: [8229a31da93f637c28032249b44395af](https://search.dartslive.com/jp/shop/8229a31da93f637c28032249b44395af). 群馬県高崎市倉賀野町2677-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9981](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9981). 370-1201 群馬県高崎市倉賀野町2677-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.811; Source-pin distance 17.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts＆DiningBar G&#x27;Laugh / DartsDiningBar G’Laugh

- **DARTSLIVE**: [db340352f79d9d010d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/db340352f79d9d010d9b047a20a7ba1e). 千葉県我孫子市本町2-2-26 銀寿司ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [88309](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88309). 270-1151 千葉県我孫子市本町2-26 銀寿ビルB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.809; Source-pin distance 41.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Rush ton80 / Rush ton80

- **DARTSLIVE**: [194255eeb8a685e7f454cb89828a1cfe](https://search.dartslive.com/jp/shop/194255eeb8a685e7f454cb89828a1cfe). 北海道釧路市末広町5-14 オリエンタルプラザ5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [48599](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=48599). 085-0014 北海道釧路市末広5-13 オリエンタルプラザ5F. Inventory: VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.808; Source-pin distance 7.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SISTERS / sisters

- **DARTSLIVE**: [f7e56b531c0c8664f454cb89828a1cfe](https://search.dartslive.com/jp/shop/f7e56b531c0c8664f454cb89828a1cfe). 東京都八王子市三崎町3-4 RJスクエアビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89910](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89910). 192-0084 東京都八王子市三崎町3-4RJスクエアビル2階-B. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.808; Source-pin distance 5.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ARTESANO 西大島店 / ARTESANO 西大島

- **DARTSLIVE**: [7fa76428249152b00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7fa76428249152b00d9b047a20a7ba1e). 東京都江東区大島1-33-13 今井ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [83250](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83250). 136-0072 東京都江東区大島1-33-13 今井ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.957; Full-address similarity 0.844; Source-pin distance 4.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン草加店 / ラウンドワン草加店

- **DARTSLIVE**: [191149abe42784ef0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/191149abe42784ef0d9b047a20a7ba1e). 埼玉県草加市谷塚上町204-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [10009](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10009). 340-0024 埼玉県草加市谷塚上町204-1. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 213.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 宇都宮御幸ヶ原店 / 快活CLUB 宇都宮御幸ヶ原店

- **DARTSLIVE**: [98008ac1787e0740fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/98008ac1787e0740fec1ae84bb28bd87). 栃木県宇都宮市下川俣町78-6. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10094](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10094). 321-0972 栃木県宇都宮市下川俣町78-6. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 52.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 倉敷店 / 快活CLUB 倉敷店

- **DARTSLIVE**: [9bf29d5b8731f87725d56fb0e5c39bac](https://search.dartslive.com/jp/shop/9bf29d5b8731f87725d56fb0e5c39bac). 岡山県倉敷市西中新田534-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10284](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10284). 710-0833 岡山県倉敷市西中新田534-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 17.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 多治見店 / 自遊空間　多治見店

- **DARTSLIVE**: [44b788976a7a2ed80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/44b788976a7a2ed80d9b047a20a7ba1e). 岐阜県多治見市明和町5-69-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10356](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10356). 507-0072 岐阜県多治見市明和町5-69-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 1.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DOJO / DOJO

- **DARTSLIVE**: [1304dbac0875d816774c926eb736cb5a](https://search.dartslive.com/jp/shop/1304dbac0875d816774c926eb736cb5a). 宮城県仙台市青葉区吉成3-2-6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [10400](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10400). 989-3205 宮城県仙台市青葉区吉成3-2-6. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 7.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 新発田店 / 快活CLUB 新発田店

- **DARTSLIVE**: [bb0971ce1f59c467774c926eb736cb5a](https://search.dartslive.com/jp/shop/bb0971ce1f59c467774c926eb736cb5a). 新潟県新発田市新栄町3-4-40. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10693](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10693). 957-0063 新潟県新発田市新栄町3-4-40. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 42.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: glad / glad

- **DARTSLIVE**: [3447a9be4a363108fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/3447a9be4a363108fec1ae84bb28bd87). 大阪府大阪市北区曽根崎新地1-5-10 地田ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [10701](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10701). 530-0002 大阪府大阪市北区曽根崎新地1-5-10 池田ビルII 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 8.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 鶴ヶ島インター店 / 快活CLUB 鶴ヶ島インター店

- **DARTSLIVE**: [800ac31d3c06802efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/800ac31d3c06802efec1ae84bb28bd87). 埼玉県鶴ヶ島市脚折町4-10-5. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10719](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10719). 350-2211 埼玉県鶴ヶ島市脚折町4-10-5. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 6.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 宇部中央店 / 快活CLUB 宇部中央店

- **DARTSLIVE**: [9ffd964cf1c1a7af25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/9ffd964cf1c1a7af25d56fb0e5c39bac). 山口県宇部市中央町3-16-46. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [42947](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42947). 755-0045 山口県宇部市中央町3-16-46. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 10.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 水戸渡里店 / 快活CLUB 水戸渡里店

- **DARTSLIVE**: [b74cc75bb15d67535f9f3321c1147265](https://search.dartslive.com/jp/shop/b74cc75bb15d67535f9f3321c1147265). 茨城県水戸市渡里町2693-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [43251](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43251). 310-0902 茨城県水戸市渡里町2693-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 福岡福重店 / 自遊空間 福岡福重店

- **DARTSLIVE**: [9de93d72da2cc873fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/9de93d72da2cc873fec1ae84bb28bd87). 福岡県福岡市西区福重3-34-6. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [43302](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43302). 819-0022 福岡県福岡市西区福重3-34-6. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 5.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 豊橋駅前店 / 亜熱帯 豊橋駅前店

- **DARTSLIVE**: [f177093bd0f6c994b21333aee1bd51e4](https://search.dartslive.com/jp/shop/f177093bd0f6c994b21333aee1bd51e4). 愛知県豊橋市駅前大通1-36-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [44187](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44187). 440-0888 愛知県豊橋市駅前大通1-36-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 5.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 新前橋店 / 快活CLUB 新前橋店

- **DARTSLIVE**: [bdf93e7c6c6eebf725d56fb0e5c39bac](https://search.dartslive.com/jp/shop/bdf93e7c6c6eebf725d56fb0e5c39bac). 群馬県前橋市小相木町558-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [44629](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44629). 371-0831 群馬県前橋市小相木町558-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 安-Bartic駅前店 / 安-Bartic 駅前店

- **DARTSLIVE**: [372fc5e3c83c35490d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/372fc5e3c83c35490d9b047a20a7ba1e). 石川県金沢市本町2-17-13 高田ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [51981](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=51981). 920-0853 石川県金沢市本町2-17-13 高田ビル3階. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Jugar Cafe / Jugar Cafe

- **DARTSLIVE**: [d7dd531aefc1f94c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d7dd531aefc1f94c0d9b047a20a7ba1e). 東京都豊島区南池袋2-43-17. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [52358](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52358). 171-0022 東京都豊島区南池袋2-43-17. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 12.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 紀ノ川大橋店 / 快活CLUB紀ノ川大橋店

- **DARTSLIVE**: [27a8358ad1b646b4774c926eb736cb5a](https://search.dartslive.com/jp/shop/27a8358ad1b646b4774c926eb736cb5a). 和歌山県和歌山市湊1771-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [55724](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=55724). 640-8404 和歌山県和歌山市湊1771-5. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 四日市追分店 / 快活CLUB 四日市追分店

- **DARTSLIVE**: [e0115978225bbbe3790ab824ce8730e5](https://search.dartslive.com/jp/shop/e0115978225bbbe3790ab824ce8730e5). 三重県四日市市小古曽東1-1-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56495](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56495). 510-0951 三重県四日市市小古曽東1-1-2. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワンららぽーと湘南平塚店 / ラウンドワンららぽーと湘南平塚店

- **DARTSLIVE**: [8a3a674a2d9084070d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8a3a674a2d9084070d9b047a20a7ba1e). 神奈川県平塚市天沼10-1-3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [57647](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=57647). 254-8510 神奈川県平塚市天沼10-1 3F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 20.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: K☆STYLE / K☆STYLE

- **DARTSLIVE**: [0d64f83fb3cabbe9fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/0d64f83fb3cabbe9fec1ae84bb28bd87). 滋賀県彦根市小泉町300-15. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [58563](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58563). 522-0043 滋賀県彦根市小泉町300-15. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY四日市城西店 / JOYJOY 四日市城西店

- **DARTSLIVE**: [22cf956d92bf9a0025d56fb0e5c39bac](https://search.dartslive.com/jp/shop/22cf956d92bf9a0025d56fb0e5c39bac). 三重県四日市市城西町14-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [59448](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59448). 510-0829 三重県四日市市城西町14-10. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 11.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY豊川駅東口店 / JOYJOY 豊川駅東口店

- **DARTSLIVE**: [2423e51b543b9e7e58d385ea46352d8f](https://search.dartslive.com/jp/shop/2423e51b543b9e7e58d385ea46352d8f). 愛知県豊川市豊川町波通34-8. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [61797](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61797). 442-0033 愛知県豊川市豊川町波通34-8. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 55.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY 四日市富州原店 / JOYJOY 四日市富州原店

- **DARTSLIVE**: [9831aea1596da9adf454cb89828a1cfe](https://search.dartslive.com/jp/shop/9831aea1596da9adf454cb89828a1cfe). 三重県四日市市富州原町34-7. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [61798](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61798). 510-8016 三重県四日市市富州原町34-7. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 33.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: D-Style / D-style

- **DARTSLIVE**: [5b18f9a468f4e4520d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5b18f9a468f4e4520d9b047a20a7ba1e). 神奈川県小田原市扇町1-16-8. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [62301](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=62301). 250-0001 神奈川県小田原市扇町1-16-8. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 釧路木場店 / 快活CLUB 釧路木場店

- **DARTSLIVE**: [ec8fcfa81c187d5a58d385ea46352d8f](https://search.dartslive.com/jp/shop/ec8fcfa81c187d5a58d385ea46352d8f). 北海道釧路郡釧路町木場1-3-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [62790](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=62790). 088-0622 北海道釧路郡釧路町木場1-3-1. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 西尾店 / 快活CLUB 西尾店

- **DARTSLIVE**: [b5f3143369be3ed15f9f3321c1147265](https://search.dartslive.com/jp/shop/b5f3143369be3ed15f9f3321c1147265). 愛知県西尾市山下町八幡山67. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [6319](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6319). 445-0877 愛知県西尾市山下町八幡山67. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 宇治槇島店 / 快活CLUB 宇治槇島店

- **DARTSLIVE**: [359ae28194664bab790ab824ce8730e5](https://search.dartslive.com/jp/shop/359ae28194664bab790ab824ce8730e5). 京都府宇治市槇島町十八44-8. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [63220](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=63220). 611-0041 京都府宇治市槇島町十八44-8. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 熊本田崎店 / 快活CLUB 熊本田崎店

- **DARTSLIVE**: [c4477c3659de9551b21333aee1bd51e4](https://search.dartslive.com/jp/shop/c4477c3659de9551b21333aee1bd51e4). 熊本県熊本市西区田崎2-2-88. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [64126](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=64126). 860-0053 熊本県熊本市西区田崎2-2-88. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 140.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY磐田上岡田店 / JOYJOY 磐田上岡田店

- **DARTSLIVE**: [cb6082c17771f089b21333aee1bd51e4](https://search.dartslive.com/jp/shop/cb6082c17771f089b21333aee1bd51e4). 静岡県磐田市上岡田字九反田1045-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [66426](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=66426). 438-0045 静岡県磐田市上岡田字九反田1045番地1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 12.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン堺中央環状店 / ラウンドワン堺中央環状店

- **DARTSLIVE**: [f623f248cd6431d80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f623f248cd6431d80d9b047a20a7ba1e). 大阪府堺市東区石原町2-241. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [6848](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6848). 599-8102 大阪府堺市東区石原町2-241. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 180.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BARREL町屋店 / BARREL町屋店

- **DARTSLIVE**: [ec2225be0773d48a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ec2225be0773d48a0d9b047a20a7ba1e). 東京都荒川区荒川4-36-2-1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [69308](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69308). 116-0002 東京都荒川区荒川4-36-2 1F. Inventory: VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン千日前店 / ラウンドワン千日前店

- **DARTSLIVE**: [abe68bf93aa439d80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/abe68bf93aa439d80d9b047a20a7ba1e). 大阪府大阪市中央区難波1-3-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [71761](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71761). 542-0076 大阪府大阪市中央区難波1-3-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 15.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 研究学園店 / Link研究学園店

- **DARTSLIVE**: [68bc5f0eaf39e047774c926eb736cb5a](https://search.dartslive.com/jp/shop/68bc5f0eaf39e047774c926eb736cb5a). 茨城県つくば市研究学園4-2-14 エビスタウン2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [71917](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71917). 305-0817 茨城県つくば市研究学園4-2-14 エビスタウンB202. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 20.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CROWN’S / CROWN&#x27;S

- **DARTSLIVE**: [942f8c619a109964f454cb89828a1cfe](https://search.dartslive.com/jp/shop/942f8c619a109964f454cb89828a1cfe). 岡山県倉敷市亀山432-1-2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72923](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72923). 710-0024 岡山県倉敷市亀山432-1 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 23.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 北名古屋店 / 亜熱帯 北名古屋店

- **DARTSLIVE**: [366357425b8f056325d56fb0e5c39bac](https://search.dartslive.com/jp/shop/366357425b8f056325d56fb0e5c39bac). 愛知県北名古屋市九之坪白山159番. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7856](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7856). 481-0041 愛知県北名古屋市九之坪白山159. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 久留米上津バイパス店 / 快活CLUB 久留米上津バイパス店

- **DARTSLIVE**: [629733187cee62abb21333aee1bd51e4](https://search.dartslive.com/jp/shop/629733187cee62abb21333aee1bd51e4). 福岡県久留米市本山1-10-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [79758](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79758). 830-0056 福岡県久留米市本山1-10-10. Inventory: VSPhoenix X 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe Bar Fairy / Cafe Bar Fairy

- **DARTSLIVE**: [77cb3d55d5437ca30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/77cb3d55d5437ca30d9b047a20a7ba1e). 愛知県豊田市御幸本町3-102. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8023](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8023). 473-0901 愛知県豊田市御幸本町3-102. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 5.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 下関綾羅木店 / 快活CLUB 下関綾羅木店

- **DARTSLIVE**: [4e8fa93f067c4b36a3f63593b5358cc4](https://search.dartslive.com/jp/shop/4e8fa93f067c4b36a3f63593b5358cc4). 山口県下関市綾羅木新町3-2-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [80287](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80287). 751-0865 山口県下関市綾羅木新町3-2-1. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BILLIARD &amp; DARTS OCTOPUS / BILLIARD &amp; DARTS OCTOPUS

- **DARTSLIVE**: [8b8ce9d75082151d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8b8ce9d75082151d0d9b047a20a7ba1e). 愛知県西尾市丁田町上ノ切23. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81593](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81593). 445-0062 愛知県西尾市丁田町上ノ切23. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 3.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 豊橋向山店 / 快活CLUB 豊橋向山店

- **DARTSLIVE**: [1b90fdf6ef79f9f428032249b44395af](https://search.dartslive.com/jp/shop/1b90fdf6ef79f9f428032249b44395af). 愛知県豊橋市向山町三ノ輪2-2. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [84429](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84429). 440-0864 愛知県豊橋市向山町三ノ輪2-2. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: yokohama Honey&#x27;s Cafe / Yokohama Honey&#x27;s Cafe

- **DARTSLIVE**: [77fa41a1565e825c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/77fa41a1565e825c0d9b047a20a7ba1e). 神奈川県横浜市港北区大豆戸町512-4-1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86638](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86638). 222-0032 神奈川県横浜市港北区大豆戸町512-4. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 6.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケ&amp;ダーツBAR 心 -SHIN- / カラオケ＆ダーツBAR 心-SHIN-

- **DARTSLIVE**: [b4d39625517a0c0bf454cb89828a1cfe](https://search.dartslive.com/jp/shop/b4d39625517a0c0bf454cb89828a1cfe). 東京都武蔵村山市残堀5-131-3-102. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86642](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86642). 208-0034 東京都武蔵村山市残堀5丁目131-3-102. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 1.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ 清水町八幡店 / アプレシオ 清水町八幡店

- **DARTSLIVE**: [cf6727ac862508a90d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/cf6727ac862508a90d9b047a20a7ba1e). 静岡県駿東郡清水町八幡64-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [8773](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8773). 411-0906 静岡県駿東郡清水町八幡64-1. Inventory: VSPhoenix X 4台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケZERO河内天美店 / カラオケZERO河内天美店

- **DARTSLIVE**: [13029d966946ea5d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/13029d966946ea5d0d9b047a20a7ba1e). 大阪府松原市天美東7-10-20. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [89509](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89509). 580-0032 大阪府松原市天美東7-10-20. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 9.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar クローバー / Darts Bar クローバー

- **DARTSLIVE**: [882370e9c3f469060d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/882370e9c3f469060d9b047a20a7ba1e). 東京都羽村市小作台1-4-3-3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89911](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89911). 205-0001 東京都羽村市小作台1-4-3 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY豊田153本新店 / JOYJOY 豊田153本新店

- **DARTSLIVE**: [14a7d4288c91951758d385ea46352d8f](https://search.dartslive.com/jp/shop/14a7d4288c91951758d385ea46352d8f). 愛知県豊田市本新町5-120-3. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9127](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9127). 471-0046 愛知県豊田市本新町5-120-3. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 1.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ東静岡駅前店 / アプレシオ 東静岡駅前店

- **DARTSLIVE**: [2219a72ccefd5b36f454cb89828a1cfe](https://search.dartslive.com/jp/shop/2219a72ccefd5b36f454cb89828a1cfe). 静岡県静岡市駿河区曲金7-8-5. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9193](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9193). 422-8006 静岡県静岡市駿河区曲金7-8-5. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS BAR XYZ / DARTS BAR XYZ

- **DARTSLIVE**: [6bcf469768465c830d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6bcf469768465c830d9b047a20a7ba1e). 神奈川県厚木市下荻野519-7. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9428](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9428). 243-0203 神奈川県厚木市下荻野519-7. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 15.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 鹿児島新栄店 / 快活CLUB 鹿児島新栄店

- **DARTSLIVE**: [d160050cd18e2594f454cb89828a1cfe](https://search.dartslive.com/jp/shop/d160050cd18e2594f454cb89828a1cfe). 鹿児島県鹿児島市新栄町1-28. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [94679](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94679). 890-0072 鹿児島県鹿児島市新栄町1-28. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR SeaRadLudic / Bar Sea Rad Ludic

- **DARTSLIVE**: [0c161089cfc6fcd658d385ea46352d8f](https://search.dartslive.com/jp/shop/0c161089cfc6fcd658d385ea46352d8f). 沖縄県名護市東江1-13-8-2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95679](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95679). 905-0021 沖縄県名護市東江1-13-8 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dapasu / Dapasu

- **DARTSLIVE**: [9f377d7b2fcbee450d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9f377d7b2fcbee450d9b047a20a7ba1e). 北海道室蘭市中島町1-31-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [96004](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96004). 050-0074 北海道室蘭市中島町1-31-11. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファナティー歌舞伎町店 / ファナティー 歌舞伎町店

- **DARTSLIVE**: [451621d6801860290d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/451621d6801860290d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-10-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [96630](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96630). 160-0021 東京都新宿区歌舞伎町1-10-1. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Any1 / Any1

- **DARTSLIVE**: [71f5a053991c02610d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/71f5a053991c02610d9b047a20a7ba1e). 大阪府八尾市佐堂町3-3-3-2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [97810](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97810). 581-0816 大阪府八尾市佐堂町3-3-3 2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ幕張店 / アプレシオ 幕張店

- **DARTSLIVE**: [8ed2aa6e991429195f9f3321c1147265](https://search.dartslive.com/jp/shop/8ed2aa6e991429195f9f3321c1147265). 千葉県千葉市花見川区幕張町2-7701. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 7}.
- **Phoenix**: [98446](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98446). 262-0032 千葉県千葉市花見川区幕張町２丁目７７０１. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 18.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS＆GAMES BAR ARROWS9 / DARTS&amp;GAMES BAR ARROWS 9

- **DARTSLIVE**: [3f3bd1e9afd7c9e10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3f3bd1e9afd7c9e10d9b047a20a7ba1e). 茨城県取手市取手2-4-10-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [98618](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98618). 300-0004 茨城県取手市取手2-4-10 2Ｆ. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 遊VIVA / 遊VIVA

- **DARTSLIVE**: [3f9d318d3b0f2f0efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/3f9d318d3b0f2f0efec1ae84bb28bd87). 栃木県宇都宮市馬場通り2-3-9. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98802](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98802). 320-0026 栃木県宇都宮市馬場通り2-3-9. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン岸和田店 / ラウンドワン 岸和田店

- **DARTSLIVE**: [970fe8dfca8a40150d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/970fe8dfca8a40150d9b047a20a7ba1e). 大阪府岸和田市八阪町2-11-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98970](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98970). 596-0049 大阪府岸和田市八阪町2-11-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 6.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR Tail Slide / BAR Tail Slide

- **DARTSLIVE**: [2b10098f5d473a7a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2b10098f5d473a7a0d9b047a20a7ba1e). 埼玉県三郷市早稲田1-5-8 加藤ビル2F-3号. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9967](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9967). 341-0018 埼玉県三郷市早稲田1-5-8 加藤ビル2F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.800; Source-pin distance 6.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: バグース横浜西口 / バグース 横浜西口店

- **DARTSLIVE**: [ddc4532b1cb8f87c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ddc4532b1cb8f87c0d9b047a20a7ba1e). 神奈川県横浜市西区北幸1-1-13 Comfort178横浜駅前ビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 13}.
- **Phoenix**: [95385](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95385). 220-0004 神奈川県横浜市西区北幸1-1-13　Comfort178横浜駅前ビルディング5F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.941; Full-address similarity 0.857; Source-pin distance 0.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ブルズアイ千葉店 / ブルズアイ千葉

- **DARTSLIVE**: [c897408c10e3e2570d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c897408c10e3e2570d9b047a20a7ba1e). 千葉県千葉市中央区富士見1-14-7 NSビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [57955](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=57955). 260-0015 千葉県千葉市中央区富士見1-14-7 NSビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.933; Full-address similarity 0.863; Source-pin distance 3.3 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS FIELD / DARTS FIELD

- **DARTSLIVE**: [edbdca9743c1c7600d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/edbdca9743c1c7600d9b047a20a7ba1e). 東京都調布市仙川町1-11-13 太平ビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [73185](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73185). 182-0002 東京都調布市仙川町1-11-13 大平ビルB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.792; Source-pin distance 7.2 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dining Bar MK-Lino / Dining Bar MK-Lino

- **DARTSLIVE**: [47164c8fa0cdcd0c790ab824ce8730e5](https://search.dartslive.com/jp/shop/47164c8fa0cdcd0c790ab824ce8730e5). 神奈川県川崎市高津区溝口1-1-15 中興8ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [86027](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86027). 2130001 神奈川県川崎市高津区溝口1-1-15 中興・8 B1階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.792; Source-pin distance 5.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: TiTO JUNGLE / TiTO JUNGLE

- **DARTSLIVE**: [74635e452313bc6dfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/74635e452313bc6dfec1ae84bb28bd87). 大分県大分市都町3-5-4 第一ファーストビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [8687](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8687). 870-0034 大分県大分市都町3-5-4 第1都町ファーストビル4F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.792; Source-pin distance 33.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Labo Fujisawa / Darts Labo fujisawa

- **DARTSLIVE**: [d117ec2b40c927020d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d117ec2b40c927020d9b047a20a7ba1e). 神奈川県藤沢市南藤沢23-10 六光会館308. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9395](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9395). 251-0055 神奈川県藤沢市南藤沢23-10 六光会館3F. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.792; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: TIMELESS / TIMELESS

- **DARTSLIVE**: [3b50121639deb3720d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3b50121639deb3720d9b047a20a7ba1e). 栃木県宇都宮市宿郷1-11-10 イルパルドビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98816](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98816). 321-0945 栃木県宇都宮市宿郷1-11-10 インパルトビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.792; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY名東高針店 / JOYJOY 名東高針店

- **DARTSLIVE**: [d50cc15d1627d15f5f9f3321c1147265](https://search.dartslive.com/jp/shop/d50cc15d1627d15f5f9f3321c1147265). 愛知県名古屋市名東区高針原2-1701. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10571](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10571). 465-0073 愛知県名古屋市名東区高針原1-1701. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.791; Source-pin distance 81.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SPiN取手店 / SPIN 取手店

- **DARTSLIVE**: [c9c2e160071148040d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c9c2e160071148040d9b047a20a7ba1e). 茨城県取手市取手2-3-10 玉貴ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99827](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99827). 302-0004 茨城県取手市取手2-3-10 玉置ビル2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.791; Source-pin distance 12.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar Bull Shit! / Amusement Bar BullShit!

- **DARTSLIVE**: [0f51cda77ae256ec0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0f51cda77ae256ec0d9b047a20a7ba1e). 東京都世田谷区用賀4-12-7-B2. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [45132](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=45132). 158-0097 東京都世田谷区用賀4-12-7　B2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.789; Source-pin distance 1.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 宮崎加納店 / 快活CLUB 宮崎加納店

- **DARTSLIVE**: [1bcdf0179e1a6eb9f454cb89828a1cfe](https://search.dartslive.com/jp/shop/1bcdf0179e1a6eb9f454cb89828a1cfe). 宮崎県宮崎市清武町加納254-3. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [48848](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=48848). 889-1605 宮崎県宮崎市清武町加納乙254-3. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.789; Source-pin distance 1.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY浜松駅かじ町店 / JOYJOY 浜松駅かじ町店

- **DARTSLIVE**: [200c9c2321a6772058d385ea46352d8f](https://search.dartslive.com/jp/shop/200c9c2321a6772058d385ea46352d8f). 静岡県浜松市中央区田町330-20. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8368](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8368). 430-0944 静岡県浜松市中区田町330-20. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.789; Source-pin distance 2.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Arena 空-KUU- / Darts Arena 空～KUU～

- **DARTSLIVE**: [404ff80a4ea626e30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/404ff80a4ea626e30d9b047a20a7ba1e). 北海道北見市山下町3丁目3番12. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86055](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86055). 090-0037 北海道北見市山下町3丁目3-12. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.789; Source-pin distance 8.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 八王子大和田店 / 快活CLUB 八王子大和田店

- **DARTSLIVE**: [16d972932d58bb68774c926eb736cb5a](https://search.dartslive.com/jp/shop/16d972932d58bb68774c926eb736cb5a). 東京都八王子市大和田町2-16-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9724](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9724). 192-0045 東京都八王子市大和田2-16-11. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.789; Source-pin distance 1.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts collection 渋谷 / Darts collection

- **DARTSLIVE**: [82ec8446f9a48ebd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/82ec8446f9a48ebd0d9b047a20a7ba1e). 東京都渋谷区渋谷3-10-14 長崎堂ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [5146](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5146). 150-0002 東京都渋谷区渋谷3-10-14 長崎堂ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.938; Full-address similarity 0.851; Source-pin distance 9.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: しゃがみGUARD / しゃがみGOUARD

- **DARTSLIVE**: [c744ea56538678de58d385ea46352d8f](https://search.dartslive.com/jp/shop/c744ea56538678de58d385ea46352d8f). 埼玉県ふじみ野市上福岡1-6-34 DMビルディング2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90817](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90817). 356-0004 埼玉県ふじみ野市上福岡1-6-34　DMビルディング2階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.947; Full-address similarity 0.842; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR EXCITE / Bar EXCITE

- **DARTSLIVE**: [c778deb0a9c5381a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c778deb0a9c5381a0d9b047a20a7ba1e). 神奈川県藤沢市宮原3642. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100365](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100365). 252-0826 神奈川県藤沢市宮原3642. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 2.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン板橋店 / ラウンドワン板橋店

- **DARTSLIVE**: [9569b5ff4dbb796b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9569b5ff4dbb796b0d9b047a20a7ba1e). 東京都板橋区相生町16-13. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10037](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10037). 174-0044 東京都板橋区相生町16-13. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 21.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 東大和店 / 快活CLUB 東大和店

- **DARTSLIVE**: [c4f8e9453fc31119790ab824ce8730e5](https://search.dartslive.com/jp/shop/c4f8e9453fc31119790ab824ce8730e5). 東京都東大和市立野1-996. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10143](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10143). 207-0021 東京都東大和市立野1-996. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 7.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 久留米櫛原店 / 自遊空間 久留米櫛原店

- **DARTSLIVE**: [32d4d9b4093315d5f454cb89828a1cfe](https://search.dartslive.com/jp/shop/32d4d9b4093315d5f454cb89828a1cfe). 福岡県久留米市東櫛原町34. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10178](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10178). 830-0003 福岡県久留米市東櫛原町34. Inventory: VSPhoenix X 1台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 2.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン徳島万代店 / ラウンドワン徳島 万代店

- **DARTSLIVE**: [8c72349ac65f41030d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8c72349ac65f41030d9b047a20a7ba1e). 徳島県徳島市万代町4-19-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10203](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10203). 770-0941 徳島県徳島市万代町4-19-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 53.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン広島店 / ラウンドワン広島店

- **DARTSLIVE**: [d3da28c4b625fe980d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d3da28c4b625fe980d9b047a20a7ba1e). 広島県広島市中区立町3-11. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [10218](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10218). 730-0032 広島県広島市中区立町3-11. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 2台 VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 12.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 岡崎大樹寺店 / 快活CLUB 岡崎大樹寺店

- **DARTSLIVE**: [b77af57c9e373799b21333aee1bd51e4](https://search.dartslive.com/jp/shop/b77af57c9e373799b21333aee1bd51e4). 愛知県岡崎市大樹寺3-12-5. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10311](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10311). 444-2134 愛知県岡崎市大樹寺3-12-5. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン福山店 / ラウンドワン福山店

- **DARTSLIVE**: [f35e1b7005365c7e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f35e1b7005365c7e0d9b047a20a7ba1e). 広島県福山市明神町1-9-28. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10526](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10526). 721-0961 広島県福山市明神町1-9-28. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 20.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 盛岡上堂店 / 快活CLUB 盛岡上堂店

- **DARTSLIVE**: [8a4f3c1f6eb3545625d56fb0e5c39bac](https://search.dartslive.com/jp/shop/8a4f3c1f6eb3545625d56fb0e5c39bac). 岩手県盛岡市上堂1-19-67. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [39456](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=39456). 020-0125 岩手県盛岡市上堂1-19-67. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY豊橋中橋良店 / JOYJOY 豊橋中橋良店

- **DARTSLIVE**: [41791bd13a25013bfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/41791bd13a25013bfec1ae84bb28bd87). 愛知県豊橋市中橋良町73-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [39669](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=39669). 441-8037 愛知県豊橋市中橋良町73-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 1.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 可児店 / 快活CLUB 可児店

- **DARTSLIVE**: [ca7a90480bc6c737790ab824ce8730e5](https://search.dartslive.com/jp/shop/ca7a90480bc6c737790ab824ce8730e5). 岐阜県可児市広見1909-2. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [41606](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=41606). 509-0214 岐阜県可児市広見1909-2. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 出雲店 / 快活CLUB 出雲店

- **DARTSLIVE**: [d48bb53cf6ad80aa774c926eb736cb5a](https://search.dartslive.com/jp/shop/d48bb53cf6ad80aa774c926eb736cb5a). 島根県出雲市渡橋町754-5. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [42212](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42212). 693-0004 島根県出雲市渡橋町754-5. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 倉敷水島店 / 快活CLUB 倉敷水島店

- **DARTSLIVE**: [3508217cdeab6ca1b21333aee1bd51e4](https://search.dartslive.com/jp/shop/3508217cdeab6ca1b21333aee1bd51e4). 岡山県倉敷市東塚1-312-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [43371](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43371). 712-8044 岡山県倉敷市東塚1-312-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 富山荒川店 / 快活CLUB 富山荒川店

- **DARTSLIVE**: [5d9a19ef7b583749790ab824ce8730e5](https://search.dartslive.com/jp/shop/5d9a19ef7b583749790ab824ce8730e5). 富山県富山市荒川2-15-32. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [43623](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43623). 930-0982 富山県富山市荒川2-15-32. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アリカフェ皆生店 / アリカフェ皆生店

- **DARTSLIVE**: [b7f710f801ca0d990d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b7f710f801ca0d990d9b047a20a7ba1e). 鳥取県米子市皆生4-11-34. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [44660](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44660). 683-0003 鳥取県米子市皆生4-11-34. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 21.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: サイバック 龍ヶ崎店 / サイバック龍ヶ崎店

- **DARTSLIVE**: [4a6e8de35680eabd0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4a6e8de35680eabd0d9b047a20a7ba1e). 茨城県龍ヶ崎市藤ヶ丘4-2-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [46643](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=46643). 301-0855 茨城県龍ヶ崎市藤ヶ丘4-2-2. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 54.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 鳥栖店 / 快活CLUB 鳥栖店

- **DARTSLIVE**: [a61a961f8704243e790ab824ce8730e5](https://search.dartslive.com/jp/shop/a61a961f8704243e790ab824ce8730e5). 佐賀県鳥栖市鎗田町389-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [48721](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=48721). 841-0031 佐賀県鳥栖市鎗田町389-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 1.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CAFEBAR　WAKE / CAFE BAR WAKE

- **DARTSLIVE**: [9c5cc98eb0dc7fb0b21333aee1bd51e4](https://search.dartslive.com/jp/shop/9c5cc98eb0dc7fb0b21333aee1bd51e4). 茨城県坂東市鵠戸1244-3. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [49693](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49693). 306-0641 茨城県坂東市鵠戸1244-3. Inventory: VSPhoenix X 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 35.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯西尾駅前店 / 亜熱帯 西尾駅前店

- **DARTSLIVE**: [c4062c4f4df5ddbb58d385ea46352d8f](https://search.dartslive.com/jp/shop/c4062c4f4df5ddbb58d385ea46352d8f). 愛知県西尾市住吉町4-18-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [58442](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58442). 445-0851 愛知県西尾市住吉町4-18-5. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 53.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン鹿児島宇宿店 / ラウンドワン鹿児島宇宿店

- **DARTSLIVE**: [733d68bcc5a542ef0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/733d68bcc5a542ef0d9b047a20a7ba1e). 鹿児島県鹿児島市宇宿2-2-2. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [5962](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5962). 890-0073 鹿児島県鹿児島市宇宿2-2-2. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 71.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 四日市野田店 / 快活CLUB 四日市野田店

- **DARTSLIVE**: [571a393f33fe0ecb58d385ea46352d8f](https://search.dartslive.com/jp/shop/571a393f33fe0ecb58d385ea46352d8f). 三重県四日市市野田1-2-33. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [59637](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59637). 510-0815 三重県四日市市野田1-2-33. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 福井米松店 / 快活CLUB 福井米松店

- **DARTSLIVE**: [676b0af21eaf1afd28032249b44395af](https://search.dartslive.com/jp/shop/676b0af21eaf1afd28032249b44395af). 福井県福井市米松2-23-33. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [61463](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61463). 910-0851 福井県福井市米松2-23-33. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケ おさるの村 青山店 / カラオケ おさるの村 青山店

- **DARTSLIVE**: [163a3ea39fd4b4f90d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/163a3ea39fd4b4f90d9b047a20a7ba1e). 兵庫県姫路市青山西2-25-3. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6185](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6185). 671-2224 兵庫県姫路市青山西2-25-3. Inventory: VSPhoenix X-MAX 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 3.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ天正寺店 / アプレシオ 天正寺店

- **DARTSLIVE**: [57437bd3078f291ab21333aee1bd51e4](https://search.dartslive.com/jp/shop/57437bd3078f291ab21333aee1bd51e4). 富山県富山市天正寺68番地. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [6243](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6243). 930-0955 富山県富山市天正寺68番地. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 34.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アップルナイン 大野城店 / アップルナイン大野城店

- **DARTSLIVE**: [631ae2c191c18e5b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/631ae2c191c18e5b0d9b047a20a7ba1e). 福岡県大野城市錦町3-2-26. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6521](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6521). 816-0935 福岡県大野城市錦町3-2-26. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン高知店 / ラウンドワン高知店

- **DARTSLIVE**: [f53446a411d5b1280d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f53446a411d5b1280d9b047a20a7ba1e). 高知県高知市南宝永町4-12. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [6666](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6666). 780-0816 高知県高知市南宝永町4-12. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 18.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 茂原東部台店 / 快活CLUB 茂原東部台店

- **DARTSLIVE**: [5360a12b39877e7d790ab824ce8730e5](https://search.dartslive.com/jp/shop/5360a12b39877e7d790ab824ce8730e5). 千葉県茂原市木崎2274-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [6762](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6762). 297-0016 千葉県茂原市木崎2274-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 豊橋新栄店 / 快活CLUB 豊橋新栄店

- **DARTSLIVE**: [fc735fe48481f970f454cb89828a1cfe](https://search.dartslive.com/jp/shop/fc735fe48481f970f454cb89828a1cfe). 愛知県豊橋市新栄町鳥畷4-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7000](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7000). 441-8016 愛知県豊橋市新栄町鳥畷4-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 秩父中央店 / 自遊空間 秩父中央店

- **DARTSLIVE**: [8304fb96474369d6790ab824ce8730e5](https://search.dartslive.com/jp/shop/8304fb96474369d6790ab824ce8730e5). 埼玉県秩父市上野町11-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [7242](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7242). 368-0031 埼玉県秩父市上野町11-11. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 3.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Cafe&amp;Bar Alpha / Cafe &amp;Bar Alpha

- **DARTSLIVE**: [408aa62c53b8f5d40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/408aa62c53b8f5d40d9b047a20a7ba1e). 東京都品川区荏原3-7-8-2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [73968](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73968). 142-0063 東京都品川区荏原3-7-8 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY高浜419吉浜店 / JOYJOY 高浜419吉浜店

- **DARTSLIVE**: [6ff58ce308d872d4a3f63593b5358cc4](https://search.dartslive.com/jp/shop/6ff58ce308d872d4a3f63593b5358cc4). 愛知県高浜市神明町1-1-20. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [74055](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=74055). 444-1305 愛知県高浜市神明町1-1-20. Inventory: VSPhoenix X 2台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 7.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 鯖江店 / 快活CLUB 鯖江店

- **DARTSLIVE**: [c2b300ceea77b6a6f454cb89828a1cfe](https://search.dartslive.com/jp/shop/c2b300ceea77b6a6f454cb89828a1cfe). 福井県鯖江市五郎丸町312. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [74153](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=74153). 916-0044 福井県鯖江市五郎丸町312. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アリカフェ浜乃木店 / アリカフェ浜乃木店

- **DARTSLIVE**: [43b81a34bd8e02af0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/43b81a34bd8e02af0d9b047a20a7ba1e). 島根県松江市浜乃木6-1-32. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7474](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7474). 690-0044 島根県松江市浜乃木6-1-32. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 4.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: マンガの広場 今宿店 / マンガの広場 今宿店

- **DARTSLIVE**: [993ac9e3df7a1d610d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/993ac9e3df7a1d610d9b047a20a7ba1e). 兵庫県姫路市西今宿3-9-17. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7488](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7488). 670-0061 兵庫県姫路市西今宿3-9-17. Inventory: VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 24.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 姫路飾磨店 / 快活CLUB 姫路飾磨店

- **DARTSLIVE**: [bc5af7bfe732b90c28032249b44395af](https://search.dartslive.com/jp/shop/bc5af7bfe732b90c28032249b44395af). 兵庫県姫路市飾磨区構2-51. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [7501](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7501). 672-8071 兵庫県姫路市飾磨区構2-51. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 19.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間宇都宮オリオン通り店 / 自遊空間 宇都宮オリオン通り店

- **DARTSLIVE**: [da12e3e5296b7243790ab824ce8730e5](https://search.dartslive.com/jp/shop/da12e3e5296b7243790ab824ce8730e5). 栃木県宇都宮市曲師町5-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [75710](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75710). 320-0803 栃木県宇都宮市曲師町5-10. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 21.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 津島駅前店 / 快活CLUB 津島駅前店

- **DARTSLIVE**: [6441d65a6cb8f7c5774c926eb736cb5a](https://search.dartslive.com/jp/shop/6441d65a6cb8f7c5774c926eb736cb5a). 愛知県津島市今市場町3-2-3. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [77685](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77685). 496-0803 愛知県津島市今市場町3-2-3. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 富士吉原店 / 快活CLUB 富士吉原店

- **DARTSLIVE**: [cea11d66ca59807df454cb89828a1cfe](https://search.dartslive.com/jp/shop/cea11d66ca59807df454cb89828a1cfe). 静岡県富士市依田原325-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7830](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7830). 417-0021 静岡県富士市依田原325-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 6.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB つくば稲荷前店 / 快活CLUB つくば稲荷前店

- **DARTSLIVE**: [71710c6e936d4c37774c926eb736cb5a](https://search.dartslive.com/jp/shop/71710c6e936d4c37774c926eb736cb5a). 茨城県つくば市稲荷前10-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [78509](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78509). 305-0061 茨城県つくば市稲荷前10-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 高松中央通り店 / 快活CLUB 高松中央通り店

- **DARTSLIVE**: [48ef6c933e3c1dba28032249b44395af](https://search.dartslive.com/jp/shop/48ef6c933e3c1dba28032249b44395af). 香川県高松市東ハゼ町12-9. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [78510](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78510). 761-8054 香川県高松市東ハゼ町12-9. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 函館昭和店 / 快活CLUB 函館昭和店

- **DARTSLIVE**: [bc1ce23ddeb5f056f454cb89828a1cfe](https://search.dartslive.com/jp/shop/bc1ce23ddeb5f056f454cb89828a1cfe). 北海道函館市昭和3-31-12. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [78663](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78663). 041-0812 北海道函館市昭和3-31-12. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 丸亀店 / 快活CLUB 丸亀店

- **DARTSLIVE**: [6c7a74925a4d6cf4fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/6c7a74925a4d6cf4fec1ae84bb28bd87). 香川県丸亀市土器町東8-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79329](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79329). 763-0082 香川県丸亀市土器町東8-11. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 伊勢店 / 快活CLUB 伊勢店

- **DARTSLIVE**: [1fb8e55c51d7681f28032249b44395af](https://search.dartslive.com/jp/shop/1fb8e55c51d7681f28032249b44395af). 三重県伊勢市小木町686-5. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [79433](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79433). 516-0007 三重県伊勢市小木町686-5. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY豊橋駅前店 / JOYJOY 豊橋駅前店

- **DARTSLIVE**: [377e3b855608d3035f9f3321c1147265](https://search.dartslive.com/jp/shop/377e3b855608d3035f9f3321c1147265). 愛知県豊橋市駅前大通1-40. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8039](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8039). 440-0888 愛知県豊橋市駅前大通1-40. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 6.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 岐阜穂積店 / 快活CLUB 岐阜穂積店

- **DARTSLIVE**: [f2d6e527c8d62fa9774c926eb736cb5a](https://search.dartslive.com/jp/shop/f2d6e527c8d62fa9774c926eb736cb5a). 岐阜県岐阜市西河渡3-68-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8152](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8152). 501-0106 岐阜県岐阜市西河渡3-68-2. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 石巻中里店 / 快活CLUB 石巻中里店

- **DARTSLIVE**: [2f0555eac607d90a774c926eb736cb5a](https://search.dartslive.com/jp/shop/2f0555eac607d90a774c926eb736cb5a). 宮城県石巻市南中里2-9-54. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [82056](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82056). 986-0814 宮城県石巻市南中里2-9-54. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: まんがネットRAUM豊田広川店 / まんがネットRAUM豊田広川店

- **DARTSLIVE**: [834a71f60df831f40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/834a71f60df831f40d9b047a20a7ba1e). 愛知県豊田市広川町7-92-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8251](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8251). 471-0807 愛知県豊田市広川町7-92-1. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 8.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 富里インター店 / 快活CLUB 富里インター店

- **DARTSLIVE**: [9fcd0c2b6a0b8c2afec1ae84bb28bd87](https://search.dartslive.com/jp/shop/9fcd0c2b6a0b8c2afec1ae84bb28bd87). 千葉県富里市七栄1005-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [82823](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82823). 286-0221 千葉県富里市七栄1005-5. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 長久手グリーンロード店 / 快活CLUB 長久手グリーンロード店

- **DARTSLIVE**: [5aa1dd591e46144725d56fb0e5c39bac](https://search.dartslive.com/jp/shop/5aa1dd591e46144725d56fb0e5c39bac). 愛知県長久手市喜婦嶽123. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8355](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8355). 480-1117 愛知県長久手市喜婦嶽123. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 9.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケ おさるの村 三田店 / カラオケおさるの村 三田店

- **DARTSLIVE**: [10c54b1fa80dfa1d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/10c54b1fa80dfa1d0d9b047a20a7ba1e). 兵庫県三田市すずかけ台3-2. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [84810](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84810). 669-1322 兵庫県三田市すずかけ台3-2. Inventory: VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 大垣店 / 快活CLUB 大垣店

- **DARTSLIVE**: [6924062aeac30a7128032249b44395af](https://search.dartslive.com/jp/shop/6924062aeac30a7128032249b44395af). 岐阜県大垣市築捨町4-67-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8682](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8682). 503-0854 岐阜県大垣市築捨町4-67-1. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 5.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン大分店 / ラウンドワン大分店

- **DARTSLIVE**: [03a434c57ba616930d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/03a434c57ba616930d9b047a20a7ba1e). 大分県大分市萩原2-13-17. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8833](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8833). 870-0921 大分県大分市萩原2-13-17. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 18.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ松任店 / アプレシオ 松任店

- **DARTSLIVE**: [08ccbf40ced039fa5f9f3321c1147265](https://search.dartslive.com/jp/shop/08ccbf40ced039fa5f9f3321c1147265). 石川県白山市田中町284-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [8924](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8924). 924-0801 石川県白山市田中町284-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 25.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 久留米上津バイパス店 / 自遊空間　久留米上津バイパス店

- **DARTSLIVE**: [f48dde3a0ba65d42fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/f48dde3a0ba65d42fec1ae84bb28bd87). 福岡県久留米市本山2-7-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9082](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9082). 830-0056 福岡県久留米市本山2-7-11. Inventory: VSPhoenix X 1台 VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 6.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 宇都宮簗瀬店 / 自遊空間 宇都宮簗瀬店

- **DARTSLIVE**: [9218bada9938506928032249b44395af](https://search.dartslive.com/jp/shop/9218bada9938506928032249b44395af). 栃木県宇都宮市簗瀬町278. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9305](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9305). 321-0933 栃木県宇都宮市簗瀬町278. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 恵庭住吉店 / 自遊空間 恵庭住吉店

- **DARTSLIVE**: [a14157150079cc52fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/a14157150079cc52fec1ae84bb28bd87). 北海道恵庭市住吉町2-15-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9397](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9397). 061-1441 北海道恵庭市住吉町2-15-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 11.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 大牟田店 / 自遊空間 大牟田店

- **DARTSLIVE**: [f0db79f6da57f1b1b21333aee1bd51e4](https://search.dartslive.com/jp/shop/f0db79f6da57f1b1b21333aee1bd51e4). 福岡県大牟田市田隈928-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9546](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9546). 837-0916 福岡県大牟田市田隈928-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 50.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 407号太田店 / 快活CLUB 407号太田店

- **DARTSLIVE**: [0a2d5991cbe7e8bd774c926eb736cb5a](https://search.dartslive.com/jp/shop/0a2d5991cbe7e8bd774c926eb736cb5a). 群馬県太田市西矢島町630. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [9549](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9549). 373-0823 群馬県太田市西矢島町630. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 31.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 松本南店 / 快活CLUB 松本南店

- **DARTSLIVE**: [ad3474e804683402774c926eb736cb5a](https://search.dartslive.com/jp/shop/ad3474e804683402774c926eb736cb5a). 長野県松本市平田東2-17-6. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9581](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9581). 399-0014 長野県松本市平田東2-17-6. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 38.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 練馬笹目通り店 / 快活CLUB 練馬笹目通り店

- **DARTSLIVE**: [fdcb597ad555dba4b21333aee1bd51e4](https://search.dartslive.com/jp/shop/fdcb597ad555dba4b21333aee1bd51e4). 東京都練馬区南田中5-3-17. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9659](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9659). 177-0035 東京都練馬区南田中5-3-17. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 10.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン郡山店 / ラウンドワン郡山店

- **DARTSLIVE**: [aa5f46c657da450e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/aa5f46c657da450e0d9b047a20a7ba1e). 福島県郡山市向河原町4-55. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9666](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9666). 963-8801 福島県郡山市向河原町4-55. Inventory: VSPhoenix X 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 152.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 8号松任店 / 快活CLUB 8号松任店

- **DARTSLIVE**: [4211c435d402788ca3f63593b5358cc4](https://search.dartslive.com/jp/shop/4211c435d402788ca3f63593b5358cc4). 石川県白山市田中町290-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9673](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9673). 924-0801 石川県白山市田中町290-1. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 7.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 福島南バイパス店 / 快活CLUB 福島南バイパス店

- **DARTSLIVE**: [47097145dba66d3f5f9f3321c1147265](https://search.dartslive.com/jp/shop/47097145dba66d3f5f9f3321c1147265). 福島県福島市黒岩榎平56-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98764](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98764). 960-8153 福島県福島市黒岩榎平56-1. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン町田店 / ラウンドワン 町田店

- **DARTSLIVE**: [e632dad3994429f40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e632dad3994429f40d9b047a20a7ba1e). 東京都町田市森野1-13-14. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [99034](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99034). 194-0022 東京都町田市森野1-13-14. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.788; Source-pin distance 34.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: @べべ.ST / @べべST

- **DARTSLIVE**: [ab8eea782a8c02e70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ab8eea782a8c02e70d9b047a20a7ba1e). 新潟県新潟市中央区弁天1-2-21 駅前アイエヌジービル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93069](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93069). 950-0901 新潟県新潟市中央市弁天1丁目2-21 アイエヌジービル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.787; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BanteR / BanteR

- **DARTSLIVE**: [75bb4edfeed0e4cb774c926eb736cb5a](https://search.dartslive.com/jp/shop/75bb4edfeed0e4cb774c926eb736cb5a). 宮崎県児湯郡高鍋町北高鍋5184 ファントムビル202. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93478](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93478). 884-0002 宮崎県児湯郡高鍋町大字北高鍋5184 ファントムビル101. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.787; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BIRTH / Birth

- **DARTSLIVE**: [98f3f4f059f45c240d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/98f3f4f059f45c240d9b047a20a7ba1e). 福岡県北九州市小倉北区下到津4-14-1-3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [6509](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6509). 803-0846 福岡県北九州市小倉北区下到津4-14-1矢野ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.784; Source-pin distance 2.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 歌舞伎町店 / ダイニングダーツバー Bee 歌舞伎町店

- **DARTSLIVE**: [2d522b835f1abbd7b21333aee1bd51e4](https://search.dartslive.com/jp/shop/2d522b835f1abbd7b21333aee1bd51e4). 東京都新宿区歌舞伎町1-27-5 AMPビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [90335](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90335). 160-0021 東京都新宿区歌舞伎町１丁目27-5 APMビル6F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.784; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Tree / Tree

- **DARTSLIVE**: [60dfb72e49f59936774c926eb736cb5a](https://search.dartslive.com/jp/shop/60dfb72e49f59936774c926eb736cb5a). 広島県福山市元町12-4 元町ビル2F東側. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [95175](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95175). 720-0063 広島県福山市元町12-14 元町ビル2階 東側. Inventory: VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.783; Source-pin distance 29.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 北42条店 / 快活CLUB 北42条店

- **DARTSLIVE**: [0decf3cf7ef13665b21333aee1bd51e4](https://search.dartslive.com/jp/shop/0decf3cf7ef13665b21333aee1bd51e4). 北海道札幌市東区北42条東7-1-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [44370](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44370). 007-0842 北海道札幌市東区北42条東7-1-1 2F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.780; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケ合衆国 六丁の目店 / カラオケ合衆国 六丁の目店

- **DARTSLIVE**: [11e2593399eb9a8b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/11e2593399eb9a8b0d9b047a20a7ba1e). 宮城県仙台市若林区六丁の目南町9-6. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [76479](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=76479). 984-0013 宮城県仙台市若林区六丁の目南町9-2. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.780; Source-pin distance 77.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 厚別東店 / 快活CLUB 厚別東店

- **DARTSLIVE**: [0bae18c3f5f882ada3f63593b5358cc4](https://search.dartslive.com/jp/shop/0bae18c3f5f882ada3f63593b5358cc4). 北海道札幌市厚別区厚別東四条7-2-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9139](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9139). 004-0004 北海道札幌市厚別区厚別東4条7-2-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.780; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワンJR尼崎店 / ラウンドワンJR尼崎駅前店

- **DARTSLIVE**: [4d1ccddd700759fa0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4d1ccddd700759fa0d9b047a20a7ba1e). 兵庫県尼崎市潮江1-4-5 プラストいきいき館4F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9905](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9905). 661-0976 兵庫県尼崎市潮江1-4-5 プラストいきいき館4Ｆ. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.917; Full-address similarity 0.863; Source-pin distance 21.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Colors with Aivy / Colors with Aivy

- **DARTSLIVE**: [22704f772447927a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/22704f772447927a0d9b047a20a7ba1e). 福島県須賀川市宮先町99 ドーム168‐1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [73788](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73788). 962-0842 福島県須賀川市宮先町99 ドーム168 1-ABC. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.776; Source-pin distance 50.5 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 0909 8121(わくわくパイニイ) / 0909 8121（わくわくパイニイ）

- **DARTSLIVE**: [9dfe8d763cec8c640d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9dfe8d763cec8c640d9b047a20a7ba1e). 大阪府高槻市高槻町9-20 ブルーピア3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [76826](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=76826). 569-0803 大阪府高槻市高槻町9-20 ブルーピア第一ビル ３F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.776; Source-pin distance 6.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 1/2 nibuichi / 1/2 nibuichi

- **DARTSLIVE**: [f4a683855ad3f16eb21333aee1bd51e4](https://search.dartslive.com/jp/shop/f4a683855ad3f16eb21333aee1bd51e4). 石川県金沢市片町2-21-22 EXYビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92962](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92962). 920-0981 石川県金沢市片町2丁目21-22 EXWビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.776; Source-pin distance 3.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dartbar D/REVEL / Dartbar D/REVEL

- **DARTSLIVE**: [ad144bd10ca51d430d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ad144bd10ca51d430d9b047a20a7ba1e). 新潟県上越市仲町4-4-13. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100596](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100596). 943-0831 新潟県上越市仲町4-4-13. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 20.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 別府若草店 / 自遊空間 別府若草店

- **DARTSLIVE**: [97f0f9572859e151774c926eb736cb5a](https://search.dartslive.com/jp/shop/97f0f9572859e151774c926eb736cb5a). 大分県別府市若草町128. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10229](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10229). 874-0925 大分県別府市若草町128. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 知立店 / 快活CLUB 知立店

- **DARTSLIVE**: [8b27b5a06a34815928032249b44395af](https://search.dartslive.com/jp/shop/8b27b5a06a34815928032249b44395af). 愛知県知立市上重原6-35. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10792](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10792). 472-0058 愛知県知立市上重原6-35. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 26.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 宮崎一の宮店 / 快活CLUB 宮崎一の宮店

- **DARTSLIVE**: [0d37fa66832445af28032249b44395af](https://search.dartslive.com/jp/shop/0d37fa66832445af28032249b44395af). 宮崎県宮崎市日ノ出町2-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [41942](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=41942). 880-0856 宮崎県宮崎市日ノ出町2-1. Inventory: VSPhoenix X 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 都城店 / 快活CLUB 都城店

- **DARTSLIVE**: [ce8fa21d120a91eab21333aee1bd51e4](https://search.dartslive.com/jp/shop/ce8fa21d120a91eab21333aee1bd51e4). 宮崎県都城市平江町143. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [47412](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47412). 885-0021 宮崎県都城市平江町143. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 3.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 福島北店 / 快活CLUB 福島北店

- **DARTSLIVE**: [24748af74541e72728032249b44395af](https://search.dartslive.com/jp/shop/24748af74541e72728032249b44395af). 福島県福島市本内北町裏6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [51473](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=51473). 960-0103 福島県福島市本内北町裏6. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 三重川越店 / 快活CLUB三重川越店

- **DARTSLIVE**: [ddd2017b80df137f5f9f3321c1147265](https://search.dartslive.com/jp/shop/ddd2017b80df137f5f9f3321c1147265). 三重県三重郡川越町高松6. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [52193](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52193). 5108121 三重県三重郡川越町高松6. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 10.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY飯田IC店 / JOYJOY 飯田IC店

- **DARTSLIVE**: [adbb6fdef26f8321b21333aee1bd51e4](https://search.dartslive.com/jp/shop/adbb6fdef26f8321b21333aee1bd51e4). 長野県飯田市北方473-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [53497](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53497). 395-0151 長野県飯田市北方473-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 32.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: LIKE A CHILD / LIKE A CHILD

- **DARTSLIVE**: [700daa61ba8f9dd70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/700daa61ba8f9dd70d9b047a20a7ba1e). 埼玉県狭山市上奥富19-3. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53558](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53558). 350-1333 埼玉県狭山市上奥富19-3. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 4.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 飯塚店 / 快活CLUB 飯塚店

- **DARTSLIVE**: [10efca5014b3c53728032249b44395af](https://search.dartslive.com/jp/shop/10efca5014b3c53728032249b44395af). 福岡県飯塚市若菜260-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [56850](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56850). 820-0082 福岡県飯塚市若菜260-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 米子店 / 快活CLUB 米子店

- **DARTSLIVE**: [e045847a519d514db21333aee1bd51e4](https://search.dartslive.com/jp/shop/e045847a519d514db21333aee1bd51e4). 鳥取県米子市米原4-5-65. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [59123](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59123). 683-0804 鳥取県米子市米原4-5-65. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ磐田店 / アプレシオ 磐田店

- **DARTSLIVE**: [31900d289f3dcb3128032249b44395af](https://search.dartslive.com/jp/shop/31900d289f3dcb3128032249b44395af). 静岡県磐田市国府台68-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [5967](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5967). 438-0077 静岡県磐田市国府台68-1. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 12.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 鶴岡店 / 快活CLUB 鶴岡店

- **DARTSLIVE**: [770633a50a4a1d5fb21333aee1bd51e4](https://search.dartslive.com/jp/shop/770633a50a4a1d5fb21333aee1bd51e4). 山形県鶴岡市宝田2-1-55. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [6113](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6113). 997-0011 山形県鶴岡市宝田2-1-55. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 21.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Highandlow / HIGH AND LOW

- **DARTSLIVE**: [65675be11e007b180d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/65675be11e007b180d9b047a20a7ba1e). 鹿児島県鹿屋市朝日町3-9. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [61203](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=61203). 893-0004 鹿児島県鹿屋市朝日町3-9. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 23.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アピナ松本店 / アピナ松本店

- **DARTSLIVE**: [1b5a938116117a8e774c926eb736cb5a](https://search.dartslive.com/jp/shop/1b5a938116117a8e774c926eb736cb5a). 長野県松本市双葉19-10. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [68394](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=68394). 390-0833 長野県松本市双葉19-10. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY金沢片町店 / JOYJOY 金沢片町店

- **DARTSLIVE**: [a013d10e94c34f7925d56fb0e5c39bac](https://search.dartslive.com/jp/shop/a013d10e94c34f7925d56fb0e5c39bac). 石川県金沢市片町1-4-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [70502](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70502). 920-0981 石川県金沢市片町1-4-11. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 3.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 50号小山店 / 快活CLUB 50号小山店

- **DARTSLIVE**: [371bd4b6b2a08e2f58d385ea46352d8f](https://search.dartslive.com/jp/shop/371bd4b6b2a08e2f58d385ea46352d8f). 栃木県小山市東城南1-3-8. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [7241](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7241). 323-0829 栃木県小山市東城南1-3-8. Inventory: VSPhoenix X 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 2.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Flamingo REBORN / Flamingo REBORN

- **DARTSLIVE**: [da4219b24f46ecc20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/da4219b24f46ecc20d9b047a20a7ba1e). 東京都府中市南町2-24-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [75338](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75338). 183-0026 東京都府中市南町2-24-5. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 34.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 高松福岡町店 / 快活CLUB 高松福岡町店

- **DARTSLIVE**: [ae5b2cfed9b10bd328032249b44395af](https://search.dartslive.com/jp/shop/ae5b2cfed9b10bd328032249b44395af). 香川県高松市福岡町3-5-2. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [7665](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7665). 760-0066 香川県高松市福岡町3-5-2. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 29.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 魚津店 / 快活CLUB 魚津店

- **DARTSLIVE**: [79c3c94ca57c64e8b21333aee1bd51e4](https://search.dartslive.com/jp/shop/79c3c94ca57c64e8b21333aee1bd51e4). 富山県魚津市吉島2-5-23. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [78031](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78031). 937-0041 富山県魚津市吉島2-5-23. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 三原店 / 快活CLUB 三原店

- **DARTSLIVE**: [235775cf7be5cbeeb21333aee1bd51e4](https://search.dartslive.com/jp/shop/235775cf7be5cbeeb21333aee1bd51e4). 広島県三原市古浜1-5-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79505](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79505). 723-0013 広島県三原市古浜1-5-11. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 山形高堂店 / 快活CLUB 山形高堂店

- **DARTSLIVE**: [616727faaa59eccdfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/616727faaa59eccdfec1ae84bb28bd87). 山形県山形市高堂2-3-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81249](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81249). 990-2464 山形県山形市高堂2-3-11. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 9.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: まんがネットRAUM豊田寿町店 / まんがネットRAUM豊田寿町店

- **DARTSLIVE**: [af1da28b0d8124330d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/af1da28b0d8124330d9b047a20a7ba1e). 愛知県豊田市寿町7-25-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [8288](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8288). 471-0834 愛知県豊田市寿町7-25-1. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 藤枝店 / 快活CLUB 藤枝店

- **DARTSLIVE**: [e829a2489ac2fc4725d56fb0e5c39bac](https://search.dartslive.com/jp/shop/e829a2489ac2fc4725d56fb0e5c39bac). 静岡県藤枝市青木3-6-17. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [82890](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82890). 426-0037 静岡県藤枝市青木3-6-17. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン半田店 / ラウンドワン半田店

- **DARTSLIVE**: [5c15a3b86df5a0ad0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5c15a3b86df5a0ad0d9b047a20a7ba1e). 愛知県半田市瑞穂町6-7-8. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [8664](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8664). 475-0828 愛知県半田市瑞穂町6-7-8. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 89.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ米松店 / アプレシオ 米松店

- **DARTSLIVE**: [e6bca1c14b53908125d56fb0e5c39bac](https://search.dartslive.com/jp/shop/e6bca1c14b53908125d56fb0e5c39bac). 福井県福井市長本町610. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8757](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8757). 910-0844 福井県福井市長本町610. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 3.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: meatdinning TABUKIYA / meat dinning TABUKIYA

- **DARTSLIVE**: [84d1656c9a74377d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/84d1656c9a74377d0d9b047a20a7ba1e). 群馬県館林市大手町1-12. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [88748](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88748). 374-0023 群馬県館林市大手町1-12. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン豊中店 / ラウンドワン豊中店

- **DARTSLIVE**: [c8c23d0f5747c1a10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c8c23d0f5747c1a10d9b047a20a7ba1e). 大阪府豊中市名神口1-1-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9330](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9330). 561-0841 大阪府豊中市名神口1-1-1. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 10.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ掛尾店 / アプレシオ 掛尾店

- **DARTSLIVE**: [e330cc622e36f21058d385ea46352d8f](https://search.dartslive.com/jp/shop/e330cc622e36f21058d385ea46352d8f). 富山県富山市掛尾町605. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9432](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9432). 939-8212 富山県富山市掛尾町605. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 6.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 佐野店 / 快活CLUB 佐野店

- **DARTSLIVE**: [1e17c72a90399925b21333aee1bd51e4](https://search.dartslive.com/jp/shop/1e17c72a90399925b21333aee1bd51e4). 栃木県佐野市浅沼町803. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9450](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9450). 327-0831 栃木県佐野市浅沼町803. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 13.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 古賀店 / 自遊空間 古賀店

- **DARTSLIVE**: [d078d21f83194935b21333aee1bd51e4](https://search.dartslive.com/jp/shop/d078d21f83194935b21333aee1bd51e4). 福岡県古賀市中央3-15-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [9502](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9502). 811-3103 福岡県古賀市中央3-15-1. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台 VSPHOENIX S4 7台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 7.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 沼津店 / 快活CLUB 沼津店

- **DARTSLIVE**: [9b9410111a87cf055f9f3321c1147265](https://search.dartslive.com/jp/shop/9b9410111a87cf055f9f3321c1147265). 静岡県沼津市共栄町19-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [95696](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95696). 410-0064 静岡県沼津市共栄町19-5. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DartsBar Orsetto / Darts Bar Orsetto

- **DARTSLIVE**: [c8b46f9ddce155880d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c8b46f9ddce155880d9b047a20a7ba1e). 愛知県半田市昭和町2-49. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95878](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95878). 475-0922 愛知県半田市昭和町2-49. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS&amp;COMMUNICATION YORIBA 別府駅前店 / DARTS&amp;COMMUNICATION　YORIBA別府駅前店

- **DARTSLIVE**: [ea29f74b4206de8efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/ea29f74b4206de8efec1ae84bb28bd87). 大分県別府市駅前本町2-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [96344](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96344). 874-0935 大分県別府市駅前本町2-1. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 厚木林店 / 快活CLUB 厚木林店

- **DARTSLIVE**: [530aabfa1529e4135f9f3321c1147265](https://search.dartslive.com/jp/shop/530aabfa1529e4135f9f3321c1147265). 神奈川県厚木市林5-23-5. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9643](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9643). 243-0816 神奈川県厚木市林5-23-5. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 27.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コミックバスター 酒田店 / コミックバスター 酒田店

- **DARTSLIVE**: [d2cd107416299c2fa3f63593b5358cc4](https://search.dartslive.com/jp/shop/d2cd107416299c2fa3f63593b5358cc4). 山形県酒田市ゆたか2-9-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [97452](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97452). 998-0006 山形県酒田市ゆたか2-9-1. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 多摩ニュータウン店 / 快活CLUB 多摩ニュータウン店

- **DARTSLIVE**: [6df17e94068f8df528032249b44395af](https://search.dartslive.com/jp/shop/6df17e94068f8df528032249b44395af). 東京都多摩市乞田854-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9803](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9803). 206-0014 東京都多摩市乞田854-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 29.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 1号枚方店 / 快活CLUB 1号枚方店

- **DARTSLIVE**: [4217b1d48b25cb54a3f63593b5358cc4](https://search.dartslive.com/jp/shop/4217b1d48b25cb54a3f63593b5358cc4). 大阪府枚方市松丘町19-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9867](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9867). 573-0012 大阪府枚方市松丘町19-1. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 19.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY彦根ベルロード店 / JOYJOY 彦根ベルロード店

- **DARTSLIVE**: [8cd7608f27e503c2a3f63593b5358cc4](https://search.dartslive.com/jp/shop/8cd7608f27e503c2a3f63593b5358cc4). 滋賀県彦根市平田町581. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98695](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98695). 522-0041 滋賀県彦根市平田町581. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.774; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケBanBan佐賀南部バイパス店 / カラオケBANBAN 佐賀南部バイパス店

- **DARTSLIVE**: [2acb85d590d20e930d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2acb85d590d20e930d9b047a20a7ba1e). 佐賀県佐賀市本庄町大字本庄506-9. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [40815](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=40815). 840-0027 佐賀県佐賀市本庄町本庄506-9. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン札幌すすきの店 / ラウンドワン札幌すすきの店

- **DARTSLIVE**: [94e6f4247653b97e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/94e6f4247653b97e0d9b047a20a7ba1e). 北海道札幌市中央区南5条西3-6-1. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 10}.
- **Phoenix**: [50881](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50881). 064-0805 北海道札幌市中央区南五条西3-6-1. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケBanBan太宰府店 / カラオケBANBAN 太宰府店

- **DARTSLIVE**: [7c0f962cdc5f99a20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7c0f962cdc5f99a20d9b047a20a7ba1e). 福岡県太宰府市都府楼南5-6-12-1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6151](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6151). 818-0105 福岡県太宰府市都府楼南5-6-12. Inventory: VSPHOENIX S4 5台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 9.2 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: MIYABI / MIYABI

- **DARTSLIVE**: [1858e2eff58fe69d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1858e2eff58fe69d0d9b047a20a7ba1e). 大阪府大阪市中央区博労町1-1-6-3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6511](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6511). 541-0059 大阪府大阪市中央区博労町1-1-6. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 9.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB いわき平店 / 快活CLUB いわき平店

- **DARTSLIVE**: [caeab370d473435925d56fb0e5c39bac](https://search.dartslive.com/jp/shop/caeab370d473435925d56fb0e5c39bac). 福島県いわき市平谷川瀬1-18-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [75621](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75621). 970-8036 福島県いわき市平谷川瀬1丁目18-5. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: INSOMNIA / INSOMNIA

- **DARTSLIVE**: [68f1c6f0144a10d60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/68f1c6f0144a10d60d9b047a20a7ba1e). 千葉県旭市イ3041 林ビル206. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82083](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82083). 289-2511 千葉県旭市ィ3041 林ビル206. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 2.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 長野南バイパス店 / 快活CLUB 長野南バイパス店

- **DARTSLIVE**: [0907d193988967f2f454cb89828a1cfe](https://search.dartslive.com/jp/shop/0907d193988967f2f454cb89828a1cfe). 長野県長野市稲里町中央4-9-10. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [82846](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82846). 381-2217 長野県長野市稲里町中央４丁目９−１０. Inventory: VSPhoenix X 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 3.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ富士宮店 / アプレシオ 富士宮店

- **DARTSLIVE**: [bf0c5e83411dc542790ab824ce8730e5](https://search.dartslive.com/jp/shop/bf0c5e83411dc542790ab824ce8730e5). 静岡県富士宮市富士見ヶ丘1241. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [8353](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8353). 418-0014 静岡県富士宮市富士見ケ丘1241. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 36.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Guzzel / Guzzel

- **DARTSLIVE**: [6af818d0e7ff1e0f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6af818d0e7ff1e0f0d9b047a20a7ba1e). 埼玉県さいたま市浦和区北浦和4-1-14 スダプラザ3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98886](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98886). 330-0074 埼玉県さいたま市浦和区北浦和4-1-14 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.769; Source-pin distance 0.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 名古屋競馬場駅前店 / 快活CLUB 名古屋競馬場前店

- **DARTSLIVE**: [a20d0bad4fa35e07790ab824ce8730e5](https://search.dartslive.com/jp/shop/a20d0bad4fa35e07790ab824ce8730e5). 愛知県名古屋市港区小割通3-8. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [42713](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42713). 455-0077 愛知県名古屋市港区小割通3-8. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 0.966; Full-address similarity 0.800; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Room 矢藏 / DartsRoom 矢藏

- **DARTSLIVE**: [d5396637f188895c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d5396637f188895c0d9b047a20a7ba1e). 青森県三沢市中央町2-5-11 M&#x27;sプラザ. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [71619](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=71619). 033-0001 青森県三沢市中央町2-5-11 M&#x27;&#x27;sプラザビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.766; Source-pin distance 34.2 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: PUB SUPER MAX / PUB super MAX

- **DARTSLIVE**: [8676def435bd6c270d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8676def435bd6c270d9b047a20a7ba1e). 北海道帯広市大通南11丁目1 さくら館2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7337](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7337). 080-0010 北海道帯広市大通南11-1 さくら館ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.766; Source-pin distance 1.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン浜大津アーカス店 / ラウンドワン 浜大津アーカス店

- **DARTSLIVE**: [8ce05040a35039f70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8ce05040a35039f70d9b047a20a7ba1e). 滋賀県大津市浜町2-1 浜大津アーカス3F. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [98974](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98974). 520-0041 滋賀県大津市浜町2番1号浜大津アーカス4F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.766; Source-pin distance 7.1 m; Different explicit units/floors: likely separate premises; do not merge.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts&amp;Bar FiLL / Darts&amp;Bar FiLL

- **DARTSLIVE**: [255a82f47649dbf10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/255a82f47649dbf10d9b047a20a7ba1e). 北海道北見市北四条西4丁目2番地 スターライトビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97108](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97108). 090-0044 北海道北見市北4条西4-2 スターライトビル1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.764; Source-pin distance 33.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SPiN 土浦店 / SPIN 土浦店

- **DARTSLIVE**: [e3882be09e0e01fb0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e3882be09e0e01fb0d9b047a20a7ba1e). 茨城県土浦市桜町1-11-2 藤ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [50636](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50636). 300-0037 茨城県土浦市桜町1-11-2 フジビル2F. Inventory: VSPhoenix X 1台 VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.762; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン加古川店 / ラウンドワン 加古川店

- **DARTSLIVE**: [2ca045321faf84710d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2ca045321faf84710d9b047a20a7ba1e). 兵庫県加古川市尾上町安田325-6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [98975](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98975). 675-0021 兵庫県加古川市尾上町安田325番地の6. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.762; Source-pin distance 4.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dining bar AJITO(小平) / dining bar AJITO

- **DARTSLIVE**: [3f99f7f63c36eb430d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3f99f7f63c36eb430d9b047a20a7ba1e). 東京都小平市小川町1-75-4 シテｲコーポパルナスB1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [88130](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88130). 187-0032 東京都小平市小川町1-75-4 シティーコーポパルナスB1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.933; Full-address similarity 0.828; Source-pin distance 30.2 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン市川鬼高店 / ラウンドワン市川鬼高店

- **DARTSLIVE**: [19a5b0ef4b47581a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/19a5b0ef4b47581a0d9b047a20a7ba1e). 千葉県市川市鬼高4-1-3. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [10114](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10114). 272-0015 千葉県市川市鬼高4-1-3. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 松江店 / 快活CLUB 松江店

- **DARTSLIVE**: [809f6f31a6c30c0758d385ea46352d8f](https://search.dartslive.com/jp/shop/809f6f31a6c30c0758d385ea46352d8f). 島根県松江市学園1-1-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10246](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10246). 690-0825 島根県松江市学園1-1-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン秋田店 / ラウンドワン秋田店

- **DARTSLIVE**: [35e12634c54c38430d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/35e12634c54c38430d9b047a20a7ba1e). 秋田県秋田市卸町1-1-2. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10256](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10256). 010-0061 秋田県秋田市卸町1-1-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 75.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン伊丹店 / ラウンドワン伊丹店

- **DARTSLIVE**: [aed20f4c1a51f0260d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/aed20f4c1a51f0260d9b047a20a7ba1e). 兵庫県伊丹市昆陽7-29. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10260](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10260). 664-0881 兵庫県伊丹市昆陽7-29. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 28.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン青森店 / ラウンドワン青森店

- **DARTSLIVE**: [e4b05b32cd37c3700d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e4b05b32cd37c3700d9b047a20a7ba1e). 青森県青森市浜田3-1-1. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10479](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10479). 030-0843 青森県青森市浜田3-1-1. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 8.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ネットジョーズ / ネットジョーズ

- **DARTSLIVE**: [5eade60f2286e7e70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5eade60f2286e7e70d9b047a20a7ba1e). 宮崎県日向市北町1-59. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10530](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10530). 883-0041 宮崎県日向市北町1-59. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 4.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コミックバスター 南松本店 / コミックバスター南松本店

- **DARTSLIVE**: [270011790293516a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/270011790293516a0d9b047a20a7ba1e). 長野県松本市高宮東6-5. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [10785](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10785). 390-0835 長野県松本市高宮東6-5. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 6.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 別府店 / 快活CLUB 別府店

- **DARTSLIVE**: [fbfd2e9f466da81528032249b44395af](https://search.dartslive.com/jp/shop/fbfd2e9f466da81528032249b44395af). 大分県別府市京町8-19. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [44764](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=44764). 874-0926 大分県別府市京町8-19. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 124号鹿嶋店 / 快活CLUB 124号鹿嶋店

- **DARTSLIVE**: [1ecf790d0bcd382d790ab824ce8730e5](https://search.dartslive.com/jp/shop/1ecf790d0bcd382d790ab824ce8730e5). 茨城県鹿嶋市鉢形971. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [63805](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=63805). 314-0034 茨城県鹿嶋市鉢形971. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 中津池永店 / 自遊空間 中津池永店

- **DARTSLIVE**: [969072998bbdc227fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/969072998bbdc227fec1ae84bb28bd87). 大分県中津市宮夫184. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [6449](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6449). 871-0012 大分県中津市宮夫184. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 7.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アピナ長岡店 / アピナ長岡店

- **DARTSLIVE**: [091b410a1be5ff2da3f63593b5358cc4](https://search.dartslive.com/jp/shop/091b410a1be5ff2da3f63593b5358cc4). 新潟県長岡市堺東町22. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [68523](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=68523). 940-2026 新潟県長岡市堺東町22. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 1.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 郡山桑野店 / 快活CLUB 郡山桑野店

- **DARTSLIVE**: [738ac511f3c7b308774c926eb736cb5a](https://search.dartslive.com/jp/shop/738ac511f3c7b308774c926eb736cb5a). 福島県郡山市桑野4-2-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [73382](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73382). 963-8025 福島県郡山市桑野4-2-2. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 4.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 熊本宇土店 / 快活CLUB 熊本宇土店

- **DARTSLIVE**: [536d936084f8a0c328032249b44395af](https://search.dartslive.com/jp/shop/536d936084f8a0c328032249b44395af). 熊本県宇土市水町50-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82889](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82889). 869-0411 熊本県宇土市水町50-1. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 168.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY三島青木店 / JOYJOY 三島青木店

- **DARTSLIVE**: [80111e976f9b46f2fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/80111e976f9b46f2fec1ae84bb28bd87). 静岡県三島市青木72-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [99650](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99650). 411-0811 静岡県三島市青木72-1. Inventory: VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.759; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY知多清水ヶ丘店 / JOYJOY 知多清水ヶ丘店

- **DARTSLIVE**: [ee395d328409ebdc58d385ea46352d8f](https://search.dartslive.com/jp/shop/ee395d328409ebdc58d385ea46352d8f). 愛知県知多市清水が丘1-1818. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [42271](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42271). 478-0053 愛知県知多市清水ヶ丘1-1818. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.757; Source-pin distance 6.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Caffe &amp; Bar Home / cafe&amp;Bar Home

- **DARTSLIVE**: [2e58b63db42e5cb6790ab824ce8730e5](https://search.dartslive.com/jp/shop/2e58b63db42e5cb6790ab824ce8730e5). 岡山県岡山市北区庭瀬246-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [78868](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78868). 701-0153 岡山県岡山市北区庭瀬246-1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.957; Full-address similarity 0.800; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY東岡崎駅前店 / JOYJOY 東岡崎駅前店

- **DARTSLIVE**: [540eb4e60468307cf454cb89828a1cfe](https://search.dartslive.com/jp/shop/540eb4e60468307cf454cb89828a1cfe). 愛知県岡崎市明大寺本町4-44. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [88917](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88917). 444-0861 愛知県岡崎市明大寺本町4丁目44. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.757; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY蒲郡三谷店 / JOYJOY 蒲郡三谷店

- **DARTSLIVE**: [c4c6cdab0f10ce50790ab824ce8730e5](https://search.dartslive.com/jp/shop/c4c6cdab0f10ce50790ab824ce8730e5). 愛知県蒲郡市三谷北通4-84-4. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [93712](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93712). 443-0022 愛知県蒲郡市三谷北通４丁目８４−４. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.757; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: NATURAL NINE YOKOHAMA / NATURALNINE YOKOHAMA

- **DARTSLIVE**: [9ece6bedbdcb2ffb0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9ece6bedbdcb2ffb0d9b047a20a7ba1e). 神奈川県横浜市西区南幸2-15-4 恩田ビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9172](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9172). 220-0005 神奈川県横浜市西区南幸2-15-4 7F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.756; Source-pin distance 13.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar scramBULL 新橋 / Darts Bar scramBULL

- **DARTSLIVE**: [0ab848a597990cf6774c926eb736cb5a](https://search.dartslive.com/jp/shop/0ab848a597990cf6774c926eb736cb5a). 東京都港区新橋2-15-8-4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94702](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94702). 東京都港区新橋2-15-8　新橋W・Bビル 4F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.944; Full-address similarity 0.812; Source-pin distance 1.2 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン大宮店 / ラウンドワン 大宮店

- **DARTSLIVE**: [4cdd709668ae30960d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4cdd709668ae30960d9b047a20a7ba1e). 埼玉県さいたま市大宮区宮町4-90-7. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [99029](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99029). 330-0802 埼玉県さいたま市大宮区宮町4丁目90番地7. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.756; Source-pin distance 6.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン府中本町駅前店 / ラウンドワン 府中本町駅前店

- **DARTSLIVE**: [94b8f76e25ae44880d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/94b8f76e25ae44880d9b047a20a7ba1e). 東京都府中市本町1-13-3 カネタビル. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 7}.
- **Phoenix**: [99046](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99046). 183-0027 東京都府中市本町1丁目13番3号 カネタビル. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.756; Source-pin distance 37.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar Aiming / Amusement BAR Aiming

- **DARTSLIVE**: [423a7c2f06b4b6b50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/423a7c2f06b4b6b50d9b047a20a7ba1e). 東京都世田谷区南烏山6-4-12 第5野萩ビル201号. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [47379](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47379). 157-0062 東京都世田谷区南烏山6-4-10　第5野萩ビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.755; Source-pin distance 22.9 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 901-QLAY-梅田店 / 901 -QLAY- 梅田

- **DARTSLIVE**: [b01107f9591fd3bba3f63593b5358cc4](https://search.dartslive.com/jp/shop/b01107f9591fd3bba3f63593b5358cc4). 大阪府大阪市北区太融寺町8-2 エーワンビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [90234](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90234). 530-0051 大阪府大阪市北区太融寺8番2号 エーワンビル1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.947; Full-address similarity 0.808; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Sports＆Dining La.Seed / Sports&amp;Dining La.Seed

- **DARTSLIVE**: [0ee387e6a0507db828032249b44395af](https://search.dartslive.com/jp/shop/0ee387e6a0507db828032249b44395af). 静岡県沼津市高島町11-5 邦ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [79755](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79755). 410-0056 静岡県沼津市高島町11-5 獎邦ビル. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.750; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ 浜松ビオラ田町店 / アプレシオ 浜松ビオラ田町店

- **DARTSLIVE**: [937f8b585e65b8c6a3f63593b5358cc4](https://search.dartslive.com/jp/shop/937f8b585e65b8c6a3f63593b5358cc4). 静岡県浜松市中区田町223-21-B1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [8365](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8365). 430-0944 静岡県浜松市中区田町223-21 ビオラ田町B1F. Inventory: VSPhoenix X 3台 VSPhoenix X-MAX 2台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.750; Source-pin distance 215.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツショップ Dx3 [浜松店] / ダーツショップD×３　浜松店

- **DARTSLIVE**: [5b479306ac64f37928032249b44395af](https://search.dartslive.com/jp/shop/5b479306ac64f37928032249b44395af). 静岡県浜松市中区萩丘3-2-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [90165](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90165). 433-8121 静岡県浜松市中区萩丘3-2-1. Inventory: VSPhoenix X 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.960; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 千里本店 / 快活CLUB 千里本店

- **DARTSLIVE**: [c7f11bc44eb21aadfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/c7f11bc44eb21aadfec1ae84bb28bd87). 大阪府吹田市千里山竹園1-5-1-3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10694](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10694). 565-0852 大阪府吹田市千里山竹園1-5-1 AOKI 3F. Inventory: VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.744; Source-pin distance 22.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SOLS / SOLS

- **DARTSLIVE**: [102212ec0ee3b18e774c926eb736cb5a](https://search.dartslive.com/jp/shop/102212ec0ee3b18e774c926eb736cb5a). 神奈川県平塚市紅谷町12-10-2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72798](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72798). 254-0043 神奈川県平塚市紅谷町12-10 湘南ビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.744; Source-pin distance 2.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY佐久IC店 / JOYJOY 佐久IC店

- **DARTSLIVE**: [33353293e7aaaabd25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/33353293e7aaaabd25d56fb0e5c39bac). 長野県佐久市岩村田北1-6-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [100454](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100454). 385-0023 長野県佐久市岩村田北1丁目6-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 鹿屋店 / 自遊空間 鹿屋店

- **DARTSLIVE**: [275c66694317d51128032249b44395af](https://search.dartslive.com/jp/shop/275c66694317d51128032249b44395af). 鹿児島県鹿屋市寿8-714-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [52361](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52361). 893-0014 鹿児島県鹿屋市寿8丁目714-2. Inventory: VSPHOENIX S4 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 19.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 蒲郡店 / 快活CLUB 蒲郡店

- **DARTSLIVE**: [00b65873d77f82e9f454cb89828a1cfe](https://search.dartslive.com/jp/shop/00b65873d77f82e9f454cb89828a1cfe). 愛知県蒲郡市竹谷町梅藪24-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [58799](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=58799). 443-0046 愛知県蒲郡市竹谷町梅薮24-1. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン長野店 / ラウンドワン長野店

- **DARTSLIVE**: [aaf3aef1424afafe0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/aaf3aef1424afafe0d9b047a20a7ba1e). 長野県長野市大字東和田827-6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [8753](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8753). 381-0038 長野県長野市東和田827-6. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 10.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY近鉄四日市2号店 / JOYJOY 近鉄四日市2号店

- **DARTSLIVE**: [18fcf96944e41924774c926eb736cb5a](https://search.dartslive.com/jp/shop/18fcf96944e41924774c926eb736cb5a). 三重県四日市市諏訪栄町4番8号. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [87942](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=87942). 510-0086 三重県四日市市諏訪栄町4-8. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケ合衆国　石巻店 / カラオケ合衆国 石巻店

- **DARTSLIVE**: [3dc46ed8580088650d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3dc46ed8580088650d9b047a20a7ba1e). 宮城県石巻市東中里2-9-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89019](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89019). 986-0812 宮城県石巻市東中里2丁目9-11. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 9.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY岐阜茜部店 / JOYJOY 岐阜茜部店

- **DARTSLIVE**: [19bf92dfd592dc99774c926eb736cb5a](https://search.dartslive.com/jp/shop/19bf92dfd592dc99774c926eb736cb5a). 岐阜県岐阜市茜部菱野1-35. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [89224](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89224). 500-8268 岐阜県岐阜市茜部菱野1丁目35. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 254号上福岡店 / 快活CLUB 254号上福岡店

- **DARTSLIVE**: [0a2abae88b42238e25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/0a2abae88b42238e25d56fb0e5c39bac). 埼玉県ふじみ野市鶴ヶ舞3-1-8. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9980](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9980). 356-0041 埼玉県ふじみ野市鶴ケ舞3-1-8. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.743; Source-pin distance 28.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワンわらび店 / ラウンドワンわらび店

- **DARTSLIVE**: [02b8e20b5b9eccbf0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/02b8e20b5b9eccbf0d9b047a20a7ba1e). 埼玉県蕨市北町5-1-6. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9998](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9998). 335-0001 埼玉県蕨市北町5-1-6. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.741; Source-pin distance 1.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: PROOF UP / PROOF UP

- **DARTSLIVE**: [c20ea3d3eb2a37d10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c20ea3d3eb2a37d10d9b047a20a7ba1e). 東京都世田谷区太子堂4-27-11 福本ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [52449](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=52449). 154-0004 東京都世田谷区太子堂4-27-11 B1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.739; Source-pin distance 10.4 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY大府共和店 / JOYJOY 大府共和店

- **DARTSLIVE**: [18e2087a780dc58af454cb89828a1cfe](https://search.dartslive.com/jp/shop/18e2087a780dc58af454cb89828a1cfe). 愛知県大府市共栄町8-10-11. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79720](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79720). 474-0074 愛知県大府市共栄町8丁目10番11. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.737; Source-pin distance 2.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン さいか屋横須賀店 / ラウンドワン さいか屋横須賀店

- **DARTSLIVE**: [ac032d69d1adec090d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ac032d69d1adec090d9b047a20a7ba1e). 神奈川県横須賀市大滝町1-13-B1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [99688](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99688). 238-0008 神奈川県横須賀市大滝町1-13. Inventory: VSPhoenix X 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.737; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン池袋店 / ラウンドワン 池袋店

- **DARTSLIVE**: [e86812d441783ab00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e86812d441783ab00d9b047a20a7ba1e). 東京都豊島区東池袋1-14-1 池袋スクエア. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [99033](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99033). 170-0013 東京都豊島区東池袋一丁目14番1号　池袋スクエア. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.735; Source-pin distance 27.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツショップ Dx3 [岡崎店] / ダーツショップ D×３ 岡崎店

- **DARTSLIVE**: [0f6671d760f774820d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0f6671d760f774820d9b047a20a7ba1e). 愛知県岡崎市大樹寺3-1-8. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [46725](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=46725). 444-2134 愛知県岡崎市大樹寺3-1-8. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.960; Full-address similarity 0.774; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツショップ Dx3 [一宮店] / ダーツショップ D×３ 一宮店

- **DARTSLIVE**: [57fc1f6e36320138f454cb89828a1cfe](https://search.dartslive.com/jp/shop/57fc1f6e36320138f454cb89828a1cfe). 愛知県一宮市東島町2-4-1. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [47076](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47076). 491-0074 愛知県一宮市東島町2-4-1. Inventory: VSPhoenix X 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.960; Full-address similarity 0.774; Source-pin distance 9.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Creed / Creed

- **DARTSLIVE**: [8f043c0118fa4e4e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8f043c0118fa4e4e0d9b047a20a7ba1e). 鹿児島県鹿児島市呉服町2-2 Y.BLD2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [86355](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=86355). 892-0826 鹿児島県鹿児島市呉服町2-2 2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.732; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 上田産業道路店 / 快活CLUB 上田産業道路店

- **DARTSLIVE**: [dd75e38669c52ca6f454cb89828a1cfe](https://search.dartslive.com/jp/shop/dd75e38669c52ca6f454cb89828a1cfe). 長野県上田市材木町2-10-1 AOKI2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [97436](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97436). 386-0014 長野県上田市材木町2-10-1 2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.732; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン東大阪店 / ラウンドワン 東大阪店

- **DARTSLIVE**: [bc77c51069abed420d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/bc77c51069abed420d9b047a20a7ba1e). 大阪府東大阪市若江南町1-2-12. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [98971](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98971). 578-0943 大阪府東大阪市若江南町1丁目2番12号. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.732; Source-pin distance 15.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン旭川店 / ラウンドワン旭川店

- **DARTSLIVE**: [97eb3cacd33949b70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/97eb3cacd33949b70d9b047a20a7ba1e). 北海道旭川市永山三条1-4-7. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10040](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10040). 079-8413 北海道旭川市永山3条1-4-7. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 79.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファンキータイム 朝倉店 / ファンキータイム朝倉店

- **DARTSLIVE**: [8e29f630e65f5f900d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8e29f630e65f5f900d9b047a20a7ba1e). 高知県高知市朝倉丙125-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10668](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10668). 780-8063 高知県高知市朝倉丙127-1. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 0.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 岐阜県庁前店 / 亜熱帯 岐阜県庁前店

- **DARTSLIVE**: [b8a60782705326665f9f3321c1147265](https://search.dartslive.com/jp/shop/b8a60782705326665f9f3321c1147265). 岐阜県岐阜市薮田中2-13-4. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [42334](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42334). 500-8387 岐阜県岐阜市藪田中2-13-4. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 25.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY浜松住吉店 / JOYJOY 浜松住吉店

- **DARTSLIVE**: [be57919ddc99a35928032249b44395af](https://search.dartslive.com/jp/shop/be57919ddc99a35928032249b44395af). 静岡県浜松市中区住吉4-14-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [56503](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56503). 430-0906 静岡県浜松市住吉4-14-5. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 23.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: max OKINAWA・那覇店 / max OKINAWA 那覇店

- **DARTSLIVE**: [ec352fd13aaa13100d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ec352fd13aaa13100d9b047a20a7ba1e). 沖縄県那覇市牧志1-12-3. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6955](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6955). 900-0013 沖縄県那覇市牧志1-12-3 1F. Inventory: VSPhoenix X 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 50.5 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY福井駅前店 / JOYJOY 福井駅前店

- **DARTSLIVE**: [47d4f0291f7bb56528032249b44395af](https://search.dartslive.com/jp/shop/47d4f0291f7bb56528032249b44395af). 福井県福井市中央1-10-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [73028](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=73028). 910-0006 福井県福井市中央1丁目10-2. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 3.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: neXus Field cafe / neXus Field cafe

- **DARTSLIVE**: [a6e2dc445f9e22450d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a6e2dc445f9e22450d9b047a20a7ba1e). 神奈川県横浜市緑区十日市場町814-9 エクセレントビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [82359](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82359). 226-0025 神奈川県横浜市緑区十日市場町814-9 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY犬山駅南店 / JOYJOY 犬山駅南店

- **DARTSLIVE**: [a6f16d88083fbde8790ab824ce8730e5](https://search.dartslive.com/jp/shop/a6f16d88083fbde8790ab824ce8730e5). 愛知県犬山市中山町1-45. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [83584](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=83584). 484-0087 愛知県犬山市中山町1丁目45. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 0.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ROOTS / ROOTS

- **DARTSLIVE**: [8e1b1ea6345ec5d1f454cb89828a1cfe](https://search.dartslive.com/jp/shop/8e1b1ea6345ec5d1f454cb89828a1cfe). 愛知県一宮市大江3-14-8. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [89851](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89851). 491-0851 愛知県一宮市大江3-14-8 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 1.1 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY千曲屋代店 / JOYJOY 千曲屋代店

- **DARTSLIVE**: [574e4728aeb49d6d5f9f3321c1147265](https://search.dartslive.com/jp/shop/574e4728aeb49d6d5f9f3321c1147265). 長野県千曲市桜堂561-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91165](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91165). 387-0012 長野県千曲市大字桜堂561-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: grass garden / grass garden

- **DARTSLIVE**: [247d2d8a8fb94f8f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/247d2d8a8fb94f8f0d9b047a20a7ba1e). 宮城県石巻市穀町12-31. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9847](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9847). 986-0825 宮城県石巻市穀町12-31 1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.727; Source-pin distance 2.5 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar clan / Darts Bar clan

- **DARTSLIVE**: [ca9ce6470d11355b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ca9ce6470d11355b0d9b047a20a7ba1e). 愛知県名古屋市中村区名駅4-24-12 横江ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6525](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6525). 450-0002 愛知県名古屋市中村区名駅4-24-12. Inventory: VSPHOENIX S 4台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.723; Source-pin distance 4.9 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 熊本十禅寺店 / 自遊空間　熊本十禅寺店

- **DARTSLIVE**: [6411bdff1f23c81758d385ea46352d8f](https://search.dartslive.com/jp/shop/6411bdff1f23c81758d385ea46352d8f). 熊本県熊本市中央区十禅寺2-8-3. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [9426](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9426). 860-0824 熊本県熊本市南区十禅寺2-8-3. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.722; Source-pin distance 1.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン博多半道橋店 / ラウンドワン半道橋店

- **DARTSLIVE**: [c60a5a54496319230d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c60a5a54496319230d9b047a20a7ba1e). 福岡県福岡市博多区半道橋2-2-8. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [6346](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6346). 812-0897 福岡県福岡市博多区半道橋2-2-8. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.909; Full-address similarity 0.811; Source-pin distance 26.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: レインボーワールド 姫路店 / レインボーワールド 姫路店

- **DARTSLIVE**: [b4279ab0251f50830d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b4279ab0251f50830d9b047a20a7ba1e). 兵庫県姫路市東郷町1454-3 リオス姫路店3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [62780](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=62780). 670-0821 兵庫県姫路市東郷町1454-3 姫路リオス3階. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.720; Source-pin distance 15.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 花鳥風月 TSURUMI / 花鳥風月 TSURUMI

- **DARTSLIVE**: [10696560d69190440d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/10696560d69190440d9b047a20a7ba1e). 神奈川県横浜市鶴見区鶴見中央4-8-12 加瀬ビル105. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [80667](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80667). 106-0032 神奈川県横浜市鶴見区鶴見中央4-8-12. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.720; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ウェアハウス三橋店 / ウエアハウス三橋店

- **DARTSLIVE**: [32a1262174fe17930d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/32a1262174fe17930d9b047a20a7ba1e). 埼玉県さいたま市西区三橋6-955-1. Inventory: {&quot;DARTSLIVE2&quot;: 20, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [55444](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=55444). 331-0052 埼玉県さいたま市西区三橋6-955-1. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.829; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 新潟黒崎店 / 自遊空間 新潟黒埼店

- **DARTSLIVE**: [3a2b16daa3afd832a3f63593b5358cc4](https://search.dartslive.com/jp/shop/3a2b16daa3afd832a3f63593b5358cc4). 新潟県新潟市西区山田2307-339. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [6336](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6336). 950-1101 新潟県新潟市西区山田2307-339. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.829; Source-pin distance 4.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コート・ダジュール 金沢田上店 / コート・ダジュール 金沢田上店

- **DARTSLIVE**: [1b2d31a329b5c910a3f63593b5358cc4](https://search.dartslive.com/jp/shop/1b2d31a329b5c910a3f63593b5358cc4). 石川県金沢市田上の里１丁目127. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [84800](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84800). 920-1156 石川県金沢市田上の里1-127 2F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.718; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: MAMA BASE / MAMA BASE+

- **DARTSLIVE**: [60b188b4baa338ed0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/60b188b4baa338ed0d9b047a20a7ba1e). 千葉県市川市新田5-5-27 田中ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [99671](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99671). 272-0035 千葉県市川市新田5-5-27 4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.718; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: GiGO POKER新宿 / GiGO POKER

- **DARTSLIVE**: [8d61f6957267d9d40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8d61f6957267d9d40d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-21-1 第二東亜会館. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [95257](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95257). 160-0021 東京都新宿区歌舞伎町1-21-1 第二東亜会館2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.900; Full-address similarity 0.816; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯稲沢店 / 亜熱帯 稲沢店

- **DARTSLIVE**: [a6e62754fd835a375f9f3321c1147265](https://search.dartslive.com/jp/shop/a6e62754fd835a375f9f3321c1147265). 愛知県稲沢市石橋6-3-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8057](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8057). 492-8271 愛知県稲沢市石橋6-3. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.714; Source-pin distance 210.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: CONNECT darts&amp;sports / connect darts&amp;sport 松戸

- **DARTSLIVE**: [290816556cca1c7d25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/290816556cca1c7d25d56fb0e5c39bac). 千葉県松戸市常盤平5-20-7 五香プラレールビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92195](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92195). 270-2261 千葉県松戸市常盤平5-20-7 五香プラレールビル地下1階. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.919; Full-address similarity 0.793; Source-pin distance 7.9 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Na GELUTTE / Na GELUTTE

- **DARTSLIVE**: [7b6e513a5b8a62680d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7b6e513a5b8a62680d9b047a20a7ba1e). 東京都府中市住吉町5-7-13 マール中河原202. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [76984](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=76984). 183-0034 東京都府中市住吉町5-7-13 202. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.711; Source-pin distance 13.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン吉祥寺店 / ラウンドワン 吉祥寺店

- **DARTSLIVE**: [28dee2a1dc725be50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/28dee2a1dc725be50d9b047a20a7ba1e). 東京都武蔵野市吉祥寺本町1-11-22. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [99035](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99035). 180-0004 東京都武蔵野市吉祥寺本町一丁目11番22号. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.711; Source-pin distance 128.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY岐阜関店 / JOYJOY 岐阜関店

- **DARTSLIVE**: [ee1a738a3a6abd1c790ab824ce8730e5](https://search.dartslive.com/jp/shop/ee1a738a3a6abd1c790ab824ce8730e5). 岐阜県関市巾2-150-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [51020](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=51020). 501-3256 岐阜県関市巾2丁目150-1. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.710; Source-pin distance 5.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY松本駅北2号店 / JOYJOY 松本駅北2号店

- **DARTSLIVE**: [d35502625f06148425d56fb0e5c39bac](https://search.dartslive.com/jp/shop/d35502625f06148425d56fb0e5c39bac). 長野県松本市中央1-2-8. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [74255](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=74255). 390-0811 長野県松本市中央1丁目2-8. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.710; Source-pin distance 1.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 大分光吉店 / 自遊空間 大分光吉店

- **DARTSLIVE**: [dd659e59df8e9dbaa3f63593b5358cc4](https://search.dartslive.com/jp/shop/dd659e59df8e9dbaa3f63593b5358cc4). 大分県大分市宮崎1391. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [9688](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9688). 870-1133 大分県大分市宮崎1399. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.710; Source-pin distance 3.7 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar PON / Amusment Bar PON

- **DARTSLIVE**: [7b15ab28803ce76d774c926eb736cb5a](https://search.dartslive.com/jp/shop/7b15ab28803ce76d774c926eb736cb5a). 沖縄県那覇市牧志2-16-45. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [98805](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98805). 900-0013 沖縄県那覇市牧志2-16-45　1A. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.966; Full-address similarity 0.743; Source-pin distance 6.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン入間店 / ラウンドワン 入間店

- **DARTSLIVE**: [c2f28160d72d50990d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/c2f28160d72d50990d9b047a20a7ba1e). 埼玉県入間市小谷田3-7-25. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [99030](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99030). 358-0026 埼玉県入間市小谷田3丁目7番25号. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.703; Source-pin distance 40.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: THE DAY Cafe Resort 小伝馬町店 / THE DAY Cafe 小伝馬町店

- **DARTSLIVE**: [271b6cfe12bebf030d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/271b6cfe12bebf030d9b047a20a7ba1e). 東京都中央区日本橋小伝馬町12-5 KDKビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [68640](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=68640). 103-0001 東京都中央区日本橋小伝馬町12-5 KDKビル3F. Inventory: VSPhoenix X-MAX 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.833; Full-address similarity 0.868; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: べろ～家 東十条黒豹 / べろ～家 東十条 黒豹

- **DARTSLIVE**: [58085cd8b13e39d80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/58085cd8b13e39d80d9b047a20a7ba1e). 東京都北区東十条4-5-24-2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [43661](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43661). 114-0001 東京都北区東十条4-5-24 朝日堂ビル2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.700; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB ワンダーシティ南熊本店 / 快活CLUB ワンダーシティ南熊本店

- **DARTSLIVE**: [f6e62ee3acc34eca790ab824ce8730e5](https://search.dartslive.com/jp/shop/f6e62ee3acc34eca790ab824ce8730e5). 熊本県熊本市中央区九品寺6-9-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [79076](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79076). 862-0976 熊本県熊本市中央区九品寺6丁目9-43. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.700; Source-pin distance 148.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Pleasure / Bar Pleasure

- **DARTSLIVE**: [85549abff1a58be5fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/85549abff1a58be5fec1ae84bb28bd87). 広島県広島市中区胡町2-25 アクロスビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [72103](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72103). 730-0025 広島県広島市中区胡町2-25 アクロスビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.842; Full-address similarity 0.857; Source-pin distance 1.5 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Y&#x27;s HYBRID BAR / Y&#x27;s HYBRID BAR

- **DARTSLIVE**: [9e9307b810169c850d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/9e9307b810169c850d9b047a20a7ba1e). 神奈川県横浜市緑区中山5-11-3 吉田ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81641](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81641). 226-0011 神奈川県横浜市緑区中山5-11-3. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.698; Source-pin distance 3.2 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: トイボックス＋ / トイボックス＋

- **DARTSLIVE**: [905be60ca04635390d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/905be60ca04635390d9b047a20a7ba1e). 千葉県市川市八幡2-14-12 北口横丁ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90396](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90396). 272-0021 千葉県市川市八幡2-14-12 3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.698; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Grit / Grit

- **DARTSLIVE**: [1ed892855783292c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1ed892855783292c0d9b047a20a7ba1e). 宮城県登米市迫町佐沼字中江4-9-6. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7436](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7436). 987-0511 宮城県登米市迫町佐沼字中江4-9-6ドラゴン倉庫1. Inventory: VSPhoenix X 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.696; Source-pin distance 6.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BeeRUSH キタ店 / BeeRUSH キタ店

- **DARTSLIVE**: [d22442567e1d0d7f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d22442567e1d0d7f0d9b047a20a7ba1e). 大阪府大阪市北区小松原町4-32-2Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [72116](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=72116). 530-0018 大阪府大阪市北区小松原町4-32 北大阪東通りビル2F. Inventory: VSPhoenix X 3台 VSPhoenix X-MAX 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.694; Source-pin distance 6.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB 米沢店 / 快活CLUB 米沢店

- **DARTSLIVE**: [1948f37c762e83f758d385ea46352d8f](https://search.dartslive.com/jp/shop/1948f37c762e83f758d385ea46352d8f). 山形県米沢市金地8-1-7. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [40941](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=40941). 992-0012 山形県米沢市金池8-1-7. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.690; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Masterplan / Masterplan

- **DARTSLIVE**: [13b9191da41c446efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/13b9191da41c446efec1ae84bb28bd87). 千葉県柏市東上町1-3. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93019](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93019). 277-0011 千葉県柏市東上町1-3 2F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.690; Source-pin distance 4.1 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY一宮森本店 / JOYJOY 一宮店

- **DARTSLIVE**: [6c88dbdac200bec828032249b44395af](https://search.dartslive.com/jp/shop/6c88dbdac200bec828032249b44395af). 愛知県一宮市森本3-23-19. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10493](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10493). 491-0831 愛知県一宮市森本3-23-19. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.900; Full-address similarity 0.788; Source-pin distance 2.5 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン静岡駿河店 / ラウンドワン駿河店

- **DARTSLIVE**: [d79ef1075ff884d80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d79ef1075ff884d80d9b047a20a7ba1e). 静岡県静岡市駿河区手越75. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8373](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8373). 421-0102 静岡県静岡市駿河区手越75. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 0.900; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY守山大森IC店 / JOYJOY 大森IC店

- **DARTSLIVE**: [12ba8b3623f90e75774c926eb736cb5a](https://search.dartslive.com/jp/shop/12ba8b3623f90e75774c926eb736cb5a). 愛知県名古屋市守山区藪田町305. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [6492](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6492). 463-0026 愛知県名古屋市守山区薮田町305. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.917; Full-address similarity 0.769; Source-pin distance 13.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY福井下馬店 / JOYJOY 福井下馬店

- **DARTSLIVE**: [ef150c92267d85d825d56fb0e5c39bac](https://search.dartslive.com/jp/shop/ef150c92267d85d825d56fb0e5c39bac). 福井県福井市下馬2-203. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89033](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89033). 918-8112 福井県福井市下馬2丁目203番地. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.686; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン習志野店 / ラウンドワン 習志野店

- **DARTSLIVE**: [d5e9e988ffbfcaf70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d5e9e988ffbfcaf70d9b047a20a7ba1e). 千葉県習志野市芝園1-4-5. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [99031](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99031). 275-0023 千葉県習志野市芝園1丁目4番5号. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.686; Source-pin distance 36.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ギンパラ / ギンパラ

- **DARTSLIVE**: [bb0e454380a0cffb5f9f3321c1147265](https://search.dartslive.com/jp/shop/bb0e454380a0cffb5f9f3321c1147265). 沖縄県那覇市寄宮2-30-45. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [84403](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=84403). 902-0064 沖縄県那覇市寄宮2-30-45　島ビル1F. Inventory: VSPHOENIX S 5台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.684; Source-pin distance 3.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR MORRY / BAR MORRY

- **DARTSLIVE**: [e353221a1b774e57774c926eb736cb5a](https://search.dartslive.com/jp/shop/e353221a1b774e57774c926eb736cb5a). 鹿児島県鹿児島市山之口町7-13 南映ビル003号. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [78655](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78655). 鹿児島県鹿児島市山之口町10-5 千代ビル2C. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.682; Source-pin distance 10.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Monkey Rotten Cafe / Monkey Rotten cafe

- **DARTSLIVE**: [cf355117707fc6280d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/cf355117707fc6280d9b047a20a7ba1e). 山梨県中巨摩郡昭和町西条875 L昭和銀座2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9647](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9647). 409-3866 山梨県中巨摩郡昭和町西条875. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.682; Source-pin distance 10.4 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: RED ROCK / RED ROCK

- **DARTSLIVE**: [8a5d0aa10c367de1f454cb89828a1cfe](https://search.dartslive.com/jp/shop/8a5d0aa10c367de1f454cb89828a1cfe). 宮城県仙台市若林区大和町5-5-25 第二やしま店舗D. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [10317](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10317). 984-0042 宮城県仙台市若林区大和町5-5-25. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.681; Source-pin distance 31.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar DiJest / Bar DiJest

- **DARTSLIVE**: [f12e389be645de1afec1ae84bb28bd87](https://search.dartslive.com/jp/shop/f12e389be645de1afec1ae84bb28bd87). 大阪府大阪市中央区難波1-8-16 namBaHIPS 5F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7554](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7554). 542-0076 大阪府大阪市中央区難波1-8-16 5F. Inventory: VSPhoenix X 2台 VSPHOENIX S4 11台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.680; Source-pin distance 27.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: TRIDENT / TRIDENT

- **DARTSLIVE**: [674b0b341b43fb6f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/674b0b341b43fb6f0d9b047a20a7ba1e). 福島県郡山市大町1-11-11 YKビル第2-2F西. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [65560](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=65560). 963-8001 福島県郡山市大町1丁目11-11　YK第2ビル2階202号. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.679; Source-pin distance 19.7 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BeeRUSH 錦店 / BeeRUSH 錦店

- **DARTSLIVE**: [8846f81269187bd4a3f63593b5358cc4](https://search.dartslive.com/jp/shop/8846f81269187bd4a3f63593b5358cc4). 愛知県名古屋市中区錦3-17-15 栄nanairo10F. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [76444](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=76444). 460-0003 愛知県名古屋市中区錦3-17-15 栄ナナイロ10F. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.679; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: D-DARTS / D-DARTS名古屋

- **DARTSLIVE**: [99c7907ee917107e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/99c7907ee917107e0d9b047a20a7ba1e). 愛知県名古屋市熱田区波寄町21-1 21番ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9381](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9381). 456-0003 愛知県名古屋市熱田区波寄町21-1 21番ﾋﾞﾙ 3F. Inventory: VSPhoenix X 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.868; Source-pin distance 1.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BRATZ / BRATZ

- **DARTSLIVE**: [f0e0eb72a41dcc990d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/f0e0eb72a41dcc990d9b047a20a7ba1e). 神奈川県横浜市緑区台村町186. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [55030](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=55030). 226-0014 神奈川県横浜市緑区台村町186 カワヨシビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 0.5 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS&amp;DINING ixi / DARTS&amp;DINING ixi

- **DARTSLIVE**: [ede8b2cece6d2af40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ede8b2cece6d2af40d9b047a20a7ba1e). 千葉県匝瑳市八日市場ハ966-1 武ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [63222](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=63222). 289-2141 千葉県匝瑳市八日市場八966-1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 1.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ブルけん / ブルけん

- **DARTSLIVE**: [461caa7d620e86630d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/461caa7d620e86630d9b047a20a7ba1e). 新潟県新潟市中央区東大通1-6-4 正栄ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [77237](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=77237). 950-0087 新潟県新潟市中央区東大通1丁目6-4. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 19.3 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯小牧IC店 / 亜熱帯 小牧IC店

- **DARTSLIVE**: [b4e3aa059b38e6e658d385ea46352d8f](https://search.dartslive.com/jp/shop/b4e3aa059b38e6e658d385ea46352d8f). 愛知県小牧市村中下之坪485-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [7861](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7861). 485-0082 愛知県小牧市村中下の坪486. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 66.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Balmy Life Coffee / Balmy Life Coffee

- **DARTSLIVE**: [3f024a9ac70a2f2e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3f024a9ac70a2f2e0d9b047a20a7ba1e). 石川県野々市市粟田3-1-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [93268](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93268). 921-8823 石川県野々市市粟田三丁目1-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Minuet / Minuet

- **DARTSLIVE**: [f78687a86a91caa65f9f3321c1147265](https://search.dartslive.com/jp/shop/f78687a86a91caa65f9f3321c1147265). 福島県郡山市朝日2-17-15 AYビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93866](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93866). 963-8024 福島県郡山市朝日2-17-15. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 1.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DartsCafe&amp;Bar 180 / DartsCafe&amp;Bar 180

- **DARTSLIVE**: [3ad6bba0db54443ea3f63593b5358cc4](https://search.dartslive.com/jp/shop/3ad6bba0db54443ea3f63593b5358cc4). 富山県射水市鷲塚1番地. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [97266](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97266). 939-0305 富山県射水市鷲塚1. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン高槻店 / ラウンドワン 高槻店

- **DARTSLIVE**: [a46d40ab73e6a1380d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a46d40ab73e6a1380d9b047a20a7ba1e). 大阪府高槻市辻子3-6-4. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [98972](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98972). 569-0036 大阪府高槻市辻子3丁目6番4号. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 3.2 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン市原店 / ラウンドワン 市原店

- **DARTSLIVE**: [d3199bb2eed0a2420d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d3199bb2eed0a2420d9b047a20a7ba1e). 千葉県市原市八幡北町3-5-1. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [99032](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99032). 290-0069 千葉県市原市八幡北町三丁目5番1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 6.8 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: UNIVERSE / UNIVERSE

- **DARTSLIVE**: [20b7a0a60aa77d270d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/20b7a0a60aa77d270d9b047a20a7ba1e). 福島県郡山市駅前2-5-1 和光ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [99921](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99921). 983-8002 福島県郡山市駅前２丁目5-1 ブライトビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.667; Source-pin distance 6.9 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ポート・ロイヤル / BAR ポート・ロイヤル

- **DARTSLIVE**: [8f9d9341f3350c5a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8f9d9341f3350c5a0d9b047a20a7ba1e). 千葉県千葉市緑区おゆみ野3-22-11 ラインビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [75291](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=75291). 266-0031 千葉県千葉市緑区あゆみ野3-22-11 ラインビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.824; Full-address similarity 0.836; Source-pin distance 0.2 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビリヤード＆ダーツ みんぽけ札幌 / ビリヤード＆ダーツ みんぽけ

- **DARTSLIVE**: [d5f0f5e719c783e60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d5f0f5e719c783e60d9b047a20a7ba1e). 北海道札幌市清田区北野五条2丁目6-15 ランド2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [93865](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93865). 北海道札幌市清田区北野5条2-6-15 LANDビル2F. Inventory: VSPHOENIX S 4台.
- **Evidence**: Normalized name similarity 0.923; Full-address similarity 0.735; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVEsuqad蒲田店 / ビアポンバーGROVE蒲田店

- **DARTSLIVE**: [d3b8b5ba0610485afec1ae84bb28bd87](https://search.dartslive.com/jp/shop/d3b8b5ba0610485afec1ae84bb28bd87). 東京都大田区西蒲田7-6-3 プリンス会館7F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85997](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85997). 144-0051 東京都大田区西蒲田7-6-4 プリンス会館7F. Inventory: VSPhoenix X 2台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.848; Full-address similarity 0.809; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SIGNAL / SIGNAL

- **DARTSLIVE**: [f8ce31ae3980885bfec1ae84bb28bd87](https://search.dartslive.com/jp/shop/f8ce31ae3980885bfec1ae84bb28bd87). 長野県長野市南千歳町1-20-2-1 アンジェラックスビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [65804](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=65804). 380-0822 長野県長野市南千歳町1-20-2-1　B1F. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.654; Source-pin distance 5.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY今池店 / JOYJOY 今池店

- **DARTSLIVE**: [b79e702b205a58aca3f63593b5358cc4](https://search.dartslive.com/jp/shop/b79e702b205a58aca3f63593b5358cc4). 愛知県名古屋市千種区今池1-11-6 第28オーシャンビル. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9660](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9660). 464-0850 愛知県名古屋市千種区今池1-11-6. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.653; Source-pin distance 2.1 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ONE OFF WORLD / ONE OFF WORLD

- **DARTSLIVE**: [00b8ee2f194573d70d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/00b8ee2f194573d70d9b047a20a7ba1e). 福岡県福岡市中央区平尾2-5-16 オネスティ平尾1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [40337](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=40337). 810-0014 福岡県福岡市中央区平尾2-5-16. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.652; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar 3×8 / Girls&amp;DartsBar 3×8

- **DARTSLIVE**: [1ed10a0b3c3c4c15a3f63593b5358cc4](https://search.dartslive.com/jp/shop/1ed10a0b3c3c4c15a3f63593b5358cc4). 栃木県宇都宮市曲師町2-12 ヒカリビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [80647](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80647). 320-0803 栃木県宇都宮市曲師町2-12 ヒカリビル2F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.851; Source-pin distance 4.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: A.s Arrows / A.s Arrows

- **DARTSLIVE**: [112bad61fb0a2f3625d56fb0e5c39bac](https://search.dartslive.com/jp/shop/112bad61fb0a2f3625d56fb0e5c39bac). 新潟県新発田市中央町3-12-4 セレッソビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [88198](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88198). 957-0053 新潟県新発田市中央町3-12-4. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.651; Source-pin distance 193.1 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: niche / NICHE+

- **DARTSLIVE**: [20814486c66e10e20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/20814486c66e10e20d9b047a20a7ba1e). 宮城県塩釜市東玉川町8-3 ラベール2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [82475](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82475). 985-0036 宮城県塩釜市東玉川町8-3. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.649; Source-pin distance 7.4 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯春日井IC店 / 亜熱帯 春日井店

- **DARTSLIVE**: [69ea59e56005e030790ab824ce8730e5](https://search.dartslive.com/jp/shop/69ea59e56005e030790ab824ce8730e5). 愛知県春日井市大泉寺町大池下292-447. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10368](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10368). 486-0812 愛知県春日井市大泉寺町大池下292. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.875; Full-address similarity 0.773; Source-pin distance 168.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファナティー心斎橋 地下ぷりん店 / ファナティー心斎橋店

- **DARTSLIVE**: [b93aac233f07923f0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b93aac233f07923f0d9b047a20a7ba1e). 大阪府大阪市中央区東心斎橋1-16-20 ガレリア・アッカビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89609](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89609). 542-0083 大阪府大阪市中央区東心斎橋1-16-20 ガレリアアッカビル1B. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.848; Source-pin distance 31.9 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラ・セレナータ / ラ・セレナータ鴨川

- **DARTSLIVE**: [69b48868d161e6d40d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/69b48868d161e6d40d9b047a20a7ba1e). 千葉県鴨川市横渚1101-3. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [8661](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8661). 296-0001 千葉県鴨川市横渚1101-3. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.857; Full-address similarity 0.788; Source-pin distance 1.2 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: akafoo STADIUM / akafoo STADIUM

- **DARTSLIVE**: [114a158ebc6347f00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/114a158ebc6347f00d9b047a20a7ba1e). 神奈川県横浜市港南区上大岡西2-1-28 上大岡赤い風船ビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [56598](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=56598). 233-0002 神奈川県横浜市港南区上大岡西2丁目1-28. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.643; Source-pin distance 7.9 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar K2 / Bar K2

- **DARTSLIVE**: [5e05a9c4b9d588f5a3f63593b5358cc4](https://search.dartslive.com/jp/shop/5e05a9c4b9d588f5a3f63593b5358cc4). 新潟県新潟市中央区東大通1-11-12 D-5. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [81511](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81511). 950-0087 新潟県新潟市中央区東大通1丁目11-12 パルコミニオンビル5F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.643; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar Line / Darts Bar Line

- **DARTSLIVE**: [fda4105681c5d872b21333aee1bd51e4](https://search.dartslive.com/jp/shop/fda4105681c5d872b21333aee1bd51e4). 福岡県福岡市博多区中洲2-1-11 プレイスポットしんばしビルB2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9472](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9472). 810-0801 福岡県福岡市博多区中洲2-1-11 B2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.643; Source-pin distance 183.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar WACK / Amusement Bar WACK

- **DARTSLIVE**: [50a62ea8e17b55630d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/50a62ea8e17b55630d9b047a20a7ba1e). 福岡県福岡市中央区舞鶴1-6-28 エステートモア天神クラブ3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90056](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90056). 810-0073 福岡県福岡市中央区舞鶴1-6-28 3F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.642; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BREMEN溝の口 / Bremen

- **DARTSLIVE**: [107d3a25309afeba0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/107d3a25309afeba0d9b047a20a7ba1e). 神奈川県川崎市高津区溝口2-7-4 STATIO17-2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [69199](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69199). 213-0001 神奈川県川崎市高津区溝口2-7-4 STATIO 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.836; Source-pin distance 40.6 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: グランサイバーカフェ バグース 池袋 / グランサイバーカフェ　バグース池袋サンシャイン60通り店

- **DARTSLIVE**: [de1891ee9e77790b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/de1891ee9e77790b0d9b047a20a7ba1e). 東京都豊島区東池袋1-22-10 ヒューマックスパビリオン4F. Inventory: {&quot;DARTSLIVE2&quot;: 13, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [7636](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7636). 170-0013 東京都豊島区東池袋1-22-10 ヒューマックスパビリオン4F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.744; Full-address similarity 0.889; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: LOCO STYLES CAFE / LOCO STYLE CAFE

- **DARTSLIVE**: [785634dad51fbd260d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/785634dad51fbd260d9b047a20a7ba1e). 神奈川県平塚市紅谷町9-18 中島ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [94775](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94775). 254-0043 神奈川県平塚市紅谷町9-18. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.963; Full-address similarity 0.667; Source-pin distance 1.8 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 快活CLUB コマーシャルモール博多店 / 快活CLUB コマーシャルモール博多店

- **DARTSLIVE**: [998674ce12a679caa3f63593b5358cc4](https://search.dartslive.com/jp/shop/998674ce12a679caa3f63593b5358cc4). 福岡県福岡市博多区東光寺町2-6-40 コマーシャルモール博多1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [97953](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97953). 812-0896 福岡県福岡市博多区東光寺町2-6-40. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.630; Source-pin distance 20.8 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOYタイホウ千種駅店 / JOYJOY タイホウ千種店

- **DARTSLIVE**: [ceaee528a8ed3cf55f9f3321c1147265](https://search.dartslive.com/jp/shop/ceaee528a8ed3cf55f9f3321c1147265). 愛知県名古屋市千種区新栄3-20-17 タイホウ千種ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9799](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9799). 464-0859 愛知県名古屋市千種区新栄3-20-17. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.963; Full-address similarity 0.667; Source-pin distance 13.7 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: レインボーワールド 橿原店 / レインボーワールド 橿原店

- **DARTSLIVE**: [4d663d123811b0a80d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4d663d123811b0a80d9b047a20a7ba1e). 奈良県橿原市葛本町201-1 池原観光ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9438](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9438). 634-0007 奈良県橿原市葛本町201-1 ツインゲート橿原2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.627; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン岡山妹尾店 / ラウンドワンスタジアム岡山妹尾店

- **DARTSLIVE**: [d46463ad3b3ab2260d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/d46463ad3b3ab2260d9b047a20a7ba1e). 岡山県岡山市南区妹尾3413-1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10202](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10202). 701-0205 岡山県岡山市南区妹尾3413-1. Inventory: VSPhoenix X 2台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 0.815; Full-address similarity 0.811; Source-pin distance 21.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BANE BAGUS-バネバグース-赤坂見附 / BANE BAGUS 赤坂見附店

- **DARTSLIVE**: [56e89fdd38f59e7a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/56e89fdd38f59e7a0d9b047a20a7ba1e). 東京都港区赤坂3-10-4 月世界ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 6, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [59247](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59247). 107-0052 東京都港区赤坂3-10-4 月世界ビル4F. Inventory: VSPHOENIX S 6台.
- **Evidence**: Normalized name similarity 0.788; Full-address similarity 0.837; Source-pin distance 1.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SAFRAN CAFE BAR / SAFRAN CAFE BAR

- **DARTSLIVE**: [02f2e0e53a987e670d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/02f2e0e53a987e670d9b047a20a7ba1e). 東京都足立区西綾瀬2-23-22 USマンション201号. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [66078](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=66078). 120-0014 東京都足立区西綾瀬2-23-22 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.625; Source-pin distance 2.5 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファンキータイムレインボー店 / ファンキータイムレインボー店

- **DARTSLIVE**: [65ea25b23fa29e3b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/65ea25b23fa29e3b0d9b047a20a7ba1e). 香川県高松市伏石町2168-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [9328](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9328). 761-8071 香川県高松市伏石町87. Inventory: VSPHOENIX S4 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.625; Source-pin distance 21.3 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アプレシオ 新宿ハイジア店 / アプレシオ 新宿ハイジア店

- **DARTSLIVE**: [28f49a505743e1fb0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/28f49a505743e1fb0d9b047a20a7ba1e). 東京都新宿区歌舞伎町2-44-1 東京都健康プラザハイジアB1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 13}.
- **Phoenix**: [98445](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98445). 160-0021 東京都新宿区歌舞伎町２丁目４４−１ ハイジアビル地下 1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.623; Source-pin distance 29.1 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: メディアカフェポパイ 横浜駅西口店 / メディアカフェポパイ横浜駅西口店

- **DARTSLIVE**: [df8f42fa1df393e10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/df8f42fa1df393e10d9b047a20a7ba1e). 神奈川県横浜市西区南幸2-8-9 ブライト横浜ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 11}.
- **Phoenix**: [10189](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10189). 220-0005 神奈川県横浜市西区南幸2-8-9. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.622; Source-pin distance 14.7 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ヘッドロック＆スペ遊 / ヘッドロック

- **DARTSLIVE**: [b37677521387fae60d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b37677521387fae60d9b047a20a7ba1e). 埼玉県蕨市中央3-6-1 MJビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [74916](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=74916). 335-0004 埼玉県蕨市中央3-6-1　MJビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.821; Source-pin distance 4.2 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワンさいたま栗橋店 / ラウンドワン 栗橋店

- **DARTSLIVE**: [2ca5791469faea530d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2ca5791469faea530d9b047a20a7ba1e). 埼玉県久喜市小右衛門192-1. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [99028](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99028). 349-1105 埼玉県久喜市小右衛門192-1. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.800; Source-pin distance 4.5 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: コローレサンストリート浜北店 / コローレ サンストリート浜北

- **DARTSLIVE**: [984af241046ee54c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/984af241046ee54c0d9b047a20a7ba1e). 静岡県浜松市浜北区平口2861 サンストリート隣り. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [7422](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7422). 434-0041 静岡県浜松市浜北区平口2861. Inventory: VSPHOENIX S 3台.
- **Evidence**: Normalized name similarity 0.963; Full-address similarity 0.652; Source-pin distance 9.4 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar OZ / Bar OZ

- **DARTSLIVE**: [0668b9bd9be015fa0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0668b9bd9be015fa0d9b047a20a7ba1e). 大阪府高槻市城北町2-4-12 辻ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [69626](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=69626). 569-0071 大阪府高槻市城北町2-10-15 ハラベビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.609; Source-pin distance 101.1 m; Different explicit units/floors: likely separate premises; do not merge.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワンさいたま鴻巣店 / ラウンドワン鴻巣店

- **DARTSLIVE**: [a8c63b2d734f5b880d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a8c63b2d734f5b880d9b047a20a7ba1e). 埼玉県鴻巣市箕田3163-7. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [10028](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10028). 365-0062 埼玉県鴻巣市箕田3163-7. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン宮崎店 / ラウンドワン宮崎店 カラオケ

- **DARTSLIVE**: [3d2c18a08426716a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3d2c18a08426716a0d9b047a20a7ba1e). 宮崎県宮崎市中村東3-4-60. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [6042](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6042). 880-0904 宮崎県宮崎市中村東3-4-60. Inventory: VSPhoenix X 1台 VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.788; Source-pin distance 17.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAGUS-バグース-新宿西口 / バグース 新宿西口店

- **DARTSLIVE**: [a697a5827e8fe9ce0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a697a5827e8fe9ce0d9b047a20a7ba1e). 東京都新宿区西新宿1-3-3 品川ステーションビル2Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 12}.
- **Phoenix**: [42556](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=42556). 160-0023 東京都新宿区西新宿1-3-3 品川ステーションビル2F. Inventory: VSPhoenix X 4台.
- **Evidence**: Normalized name similarity 0.727; Full-address similarity 0.873; Source-pin distance 6.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Los Angeles Club / Los Angeles Club

- **DARTSLIVE**: [1d16d9c00bbc6c660d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1d16d9c00bbc6c660d9b047a20a7ba1e). 京都府福知山市末広町1-23 パチンコ ニューラッキービル2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [93883](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93883). 620-0054 京都府福知山市末広町1-23 2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.600; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: マンガの広場 砥堀店 / マンガの広場　砥掘店

- **DARTSLIVE**: [910b7bca499482320d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/910b7bca499482320d9b047a20a7ba1e). 兵庫県姫路市砥堀177-2. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [80561](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=80561). 670-0802 兵庫県姫路市砥掘177-2. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.710; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: B.B kitchen / BB kitchen

- **DARTSLIVE**: [6846baf4367991820d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6846baf4367991820d9b047a20a7ba1e). 福岡県福岡市城南区七隈8-4-8 七隈ファミリープラザ1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98815](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98815). 814-0133 福岡県福岡市城南区七隈8-4-8. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.596; Source-pin distance 86.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR 我栄 / BAR 我栄

- **DARTSLIVE**: [73cf3f9f56da14af25d56fb0e5c39bac](https://search.dartslive.com/jp/shop/73cf3f9f56da14af25d56fb0e5c39bac). 沖縄県那覇市久茂地2丁目19-16 BG PLAZAビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [5938](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=5938). 900-0015 沖縄県那覇市久茂地2丁目19-16 みえばしステーションビル3-A. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.594; Source-pin distance 10.7 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAGUS-バグース-吉祥寺 / バグース  吉祥寺店

- **DARTSLIVE**: [2a15ab958e1714b00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2a15ab958e1714b00d9b047a20a7ba1e). 東京都武蔵野市吉祥寺本町1-9-10 吉祥寺ファミリープラザ4F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 11}.
- **Phoenix**: [8628](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8628). 180-0004 東京都武蔵野市吉祥寺本町1-9-10 吉祥寺ファミリープラザ4F. Inventory: VSPhoenix X 4台.
- **Evidence**: Normalized name similarity 0.700; Full-address similarity 0.892; Source-pin distance 2.1 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 亜熱帯 松阪サンパーク店 / 亜熱帯 松阪サンパーク店

- **DARTSLIVE**: [e28bac3f00a9e07b28032249b44395af](https://search.dartslive.com/jp/shop/e28bac3f00a9e07b28032249b44395af). 三重県松阪市大黒田町708番地. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [63458](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=63458). 515-0063 三重県松阪市大黒田町708 サンパーク松阪1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.591; Source-pin distance 18.9 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAGUS-バグース-心斎橋 / バグース 心斎橋店

- **DARTSLIVE**: [1c14647108a7f51c0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1c14647108a7f51c0d9b047a20a7ba1e). 大阪府大阪市中央区心斎橋筋1-1-10 キュープラザ心斎橋7F. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [59084](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=59084). 542-0085 大阪府大阪市中央区心斎橋筋1-1-10 キュープラザ心斎橋7F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.700; Full-address similarity 0.889; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン南砂店 / ラウンドワン南砂店

- **DARTSLIVE**: [091dbe97f651c1c00d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/091dbe97f651c1c00d9b047a20a7ba1e). 東京都江東区南砂6-7-15 トピレックプラザ4Ｆ. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 4}.
- **Phoenix**: [10705](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10705). 136-0076 東京都江東区南砂6-7-15. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.585; Source-pin distance 86.6 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ALA CAFE DINING / CAFE DINING ALA

- **DARTSLIVE**: [6cf77b506a1589e9790ab824ce8730e5](https://search.dartslive.com/jp/shop/6cf77b506a1589e9790ab824ce8730e5). 新潟県新潟市中央区東大通1-7-1 第一ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [40320](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=40320). 950-0087 新潟県新潟市中央区東大通1-7-1 第1ビル4F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.769; Full-address similarity 0.816; Source-pin distance 2.5 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: NATURAL 9 / NATURAL NINE

- **DARTSLIVE**: [7699478e9e21d3840d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7699478e9e21d3840d9b047a20a7ba1e). 東京都豊島区西池袋1-15-7 ベルビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [9706](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9706). 171-0021 東京都豊島区西池袋1-15-7 ベルビル4F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.737; Full-address similarity 0.844; Source-pin distance 9.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAGUS-バグース-秋葉原 / バグース  秋葉原店

- **DARTSLIVE**: [e296fdfacc8a73500d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/e296fdfacc8a73500d9b047a20a7ba1e). 東京都千代田区外神田3-15-1 AKIBA PLACE5F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 17}.
- **Phoenix**: [9808](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9808). 101-0021 東京都千代田区外神田3-15-1 AKIBA PLACE 5F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.700; Full-address similarity 0.881; Source-pin distance 21.3 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY鯖江バイパス店 / JOYJOY 鯖江店

- **DARTSLIVE**: [8ea29ae81eea1178f454cb89828a1cfe](https://search.dartslive.com/jp/shop/8ea29ae81eea1178f454cb89828a1cfe). 福井県鯖江市水落町2-3011. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [97281](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97281). 916-0022 福井県鯖江市水落町2丁目3011. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.757; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間 BIGBOX高田馬場店 / 自遊空間BIGBOX高田馬場店

- **DARTSLIVE**: [5ae64b40b138f6925f9f3321c1147265](https://search.dartslive.com/jp/shop/5ae64b40b138f6925f9f3321c1147265). 東京都新宿区高田馬場1-35-3 ビッグボックス高田馬場7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 12}.
- **Phoenix**: [9669](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9669). 169-0075 東京都新宿区高田馬場1-35-3 BIGBOX7F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.571; Source-pin distance 35.2 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケまねきねこ 鳴海店 (PlayGarden) / PlayGarden 鳴海店

- **DARTSLIVE**: [0695f8b5805ac3a6f454cb89828a1cfe](https://search.dartslive.com/jp/shop/0695f8b5805ac3a6f454cb89828a1cfe). 愛知県名古屋市緑区篭山3-103. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [99927](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99927). 愛知県名古屋市緑区篭山3-103. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.571; Full-address similarity 1.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アツギプラザボウル / 厚木プラザボウル

- **DARTSLIVE**: [40d27079f8e4a1680d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/40d27079f8e4a1680d9b047a20a7ba1e). 神奈川県厚木市中町2-3-1 ダイヤプラザビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53588](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53588). 243-0018 神奈川県厚木市中町2-3-1 ダイヤプラザビル7F. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 0.706; Full-address similarity 0.863; Source-pin distance 2.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: No name 875 / No name 875

- **DARTSLIVE**: [dcfba3a5485ef3f30d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/dcfba3a5485ef3f30d9b047a20a7ba1e). 東京都小平市花小金井1-12-2 花小金井プリンスマンション1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91061](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91061). 187-0002 東京都小平市花小金井1-12-2 105. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.566; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: 自遊空間　佐久店 / 自遊空間 佐久店

- **DARTSLIVE**: [84329807bba1b5510d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/84329807bba1b5510d9b047a20a7ba1e). 長野県佐久市岩村田6-2. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [8729](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=8729). 385-0022 長野県佐久市岩村田6-2 ステーションパーク内. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.564; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケプラス関大前 / フタバカラオケプラス 関大前店

- **DARTSLIVE**: [1330a6655db3409a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1330a6655db3409a0d9b047a20a7ba1e). 大阪府吹田市千里山東1-7-18 フタバビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [6216](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=6216). 565-0842 大阪府吹田市千里山東1-7-18 2F. Inventory: VSPhoenix X 1台 VSPHOENIX S 4台.
- **Evidence**: Normalized name similarity 0.833; Full-address similarity 0.727; Source-pin distance 29.2 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ラウンドワン札幌白石本通店 / ラウンドワンスタジアム札幌白石店

- **DARTSLIVE**: [3f61e69c229baef50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3f61e69c229baef50d9b047a20a7ba1e). 北海道札幌市白石区本通16-1-50. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [10491](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10491). 003-0027 北海道札幌市白石区本通16-北1-50. Inventory: VSPhoenix X 1台 VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 0.759; Full-address similarity 0.800; Source-pin distance 35.7 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: blue ribbon bar Fujisawa / Blue Ribbon Bar藤沢

- **DARTSLIVE**: [3e5989145c983a3a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3e5989145c983a3a0d9b047a20a7ba1e). 神奈川県藤沢市南藤沢20-20 柏屋ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [97492](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97492). 251-0055 神奈川県藤沢市南藤沢20-20 柏屋ビルB1. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.722; Full-address similarity 0.833; Source-pin distance 16.6 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAGUS-バグース-道玄坂 / バグース  道玄坂店

- **DARTSLIVE**: [2a3e3c17edc2bd910d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/2a3e3c17edc2bd910d9b047a20a7ba1e). 東京都渋谷区道玄坂2-29-5 ザ・プライム3F. Inventory: {&quot;DARTSLIVE2&quot;: 12, &quot;DARTSLIVE3&quot;: 25}.
- **Phoenix**: [7424](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=7424). 150-0043 東京都渋谷区道玄坂2-29-5 ザ・プライム３F. Inventory: VSPhoenix X 5台.
- **Evidence**: Normalized name similarity 0.700; Full-address similarity 0.851; Source-pin distance 7.5 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: STELLA-cafe / STELLA

- **DARTSLIVE**: [7933da5829cef7300d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/7933da5829cef7300d9b047a20a7ba1e). 大阪府茨木市永代町9-1 ソレイユ永代. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [81552](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81552). 567-0816 大阪府茨木市永代町9-1 ソレイユ永代1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.750; Full-address similarity 0.791; Source-pin distance 10.8 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Yu-cafe e-style 永山パワーズ店 / e-style 永山パワーズ店

- **DARTSLIVE**: [54f1dcf4ec7e03820d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/54f1dcf4ec7e03820d9b047a20a7ba1e). 北海道旭川市永山11条4丁目119 パワーズαビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [87899](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=87899). 079-8421 北海道旭川市永山11条4丁目119永山パワーズa内. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.812; Full-address similarity 0.724; Source-pin distance 174.0 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツバー89 -HAKU- / ダーツバー 89-ハク-

- **DARTSLIVE**: [a99914ca72aaf0970d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a99914ca72aaf0970d9b047a20a7ba1e). 石川県河北郡内灘町鶴ケ丘3-157-4. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [98611](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98611). 920-0271 石川県河北郡内灘町鶴ケ丘3-157-4. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.700; Full-address similarity 0.829; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ぷくぷく / ぷくぷく

- **DARTSLIVE**: [647fb4a164cccdf828032249b44395af](https://search.dartslive.com/jp/shop/647fb4a164cccdf828032249b44395af). 東京都練馬区栄町21-10 サンライズ江古田102. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [9657](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9657). 176-0006 東京都練馬区栄町21-10 一栄ビル. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.522; Source-pin distance 8.6 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY名駅笹島店 / JOYJOY 名駅錦通店

- **DARTSLIVE**: [7cb2a10db45a1e8f28032249b44395af](https://search.dartslive.com/jp/shop/7cb2a10db45a1e8f28032249b44395af). 愛知県名古屋市中村区名駅4-27-7. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [43721](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=43721). 450-0002 愛知県名古屋市中村区名駅4-25-22. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.700; Source-pin distance 195.4 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: JOYJOY名駅錦通店 / JOYJOY 名駅笹島店

- **DARTSLIVE**: [68204bdd28b1b5dc5f9f3321c1147265](https://search.dartslive.com/jp/shop/68204bdd28b1b5dc5f9f3321c1147265). 愛知県名古屋市中村区名駅4-25-22. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [79035](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79035). 450-0002 愛知県名古屋市中村区名駅4-27-7. Inventory: VSPhoenix X 2台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 0.818; Full-address similarity 0.700; Source-pin distance 203.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: バレット / バレット野々市

- **DARTSLIVE**: [61519bed05b1bab35f9f3321c1147265](https://search.dartslive.com/jp/shop/61519bed05b1bab35f9f3321c1147265). 石川県野々市市粟田1-175. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [10070](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10070). 921-8823 石川県野々市市粟田1-175. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.727; Full-address similarity 0.788; Source-pin distance 0.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: LOUNGE&amp;BOWL B-lax / LOUNGE&amp;BOWL B-lax

- **DARTSLIVE**: [00b5fd1de13577db0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/00b5fd1de13577db0d9b047a20a7ba1e). 大阪府門真市速見町9-9 B-laxLOUGE&amp;BOWL1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91675](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91675). 571-0039 大阪府門真市速見町9-9. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.500; Source-pin distance 7.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dude / DIner&amp;Bar Dude

- **DARTSLIVE**: [3829b78675f2ac21774c926eb736cb5a](https://search.dartslive.com/jp/shop/3829b78675f2ac21774c926eb736cb5a). 東京都町田市原町田4-1-3 第3丸町ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95087](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95087). 東京都町田市原町田4-1-3 第3丸町ビルB1F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.500; Full-address similarity 1.000; Source-pin distance 8.9 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: DARTS BAR ZERO / BAR ZERO

- **DARTSLIVE**: [acbf7332b64ac0240d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/acbf7332b64ac0240d9b047a20a7ba1e). 北海道旭川市3条通6丁目965-2 MBOXビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [88414](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88414). 070-0033 北海道旭川市3条6丁目 M・BOXビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.737; Full-address similarity 0.760; Source-pin distance 4.0 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVEsuqad五反田店 / ビアポンバーGROVE五反田店

- **DARTSLIVE**: [d3f457f5479ac7c328032249b44395af](https://search.dartslive.com/jp/shop/d3f457f5479ac7c328032249b44395af). 東京都品川区西五反田1-2-9-7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85776](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85776). 141-0031 東京都品川区西五反田1-2-9 FPGリンクス五反田7F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.857; Full-address similarity 0.638; Source-pin distance 2.8 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar syuuto / Bar Syuuto

- **DARTSLIVE**: [a5af117e5c61feb10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a5af117e5c61feb10d9b047a20a7ba1e). 埼玉県川越市脇田本町9-5. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [53788](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=53788). 350-1123 埼玉県川越市脇田本町6-7　グランセプトビル4階. Inventory: VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.488; Source-pin distance 1.3 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ&amp;スポーツバー スリーモンキーズカフェ上野公園前店 / スリーモンキーズカフェ上野公園前

- **DARTSLIVE**: [0279d32cb494dd0a0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0279d32cb494dd0a0d9b047a20a7ba1e). 東京都台東区上野2-14-30-B1F. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 7}.
- **Phoenix**: [9174](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=9174). 110-0005 東京都台東区上野2-14-30. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.762; Full-address similarity 0.722; Source-pin distance 0.0 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BARREL 梅島店 / BARREL

- **DARTSLIVE**: [4572c571de01d15d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4572c571de01d15d0d9b047a20a7ba1e). 東京都足立区梅島1-12-3-3F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [47220](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47220). 121-0816 東京都足立区梅島1-12-3 梅島井川ビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.683; Source-pin distance 80.1 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 流川店 / ダイニングダーツバーBee 広島店

- **DARTSLIVE**: [1e3322e39b25b811fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/1e3322e39b25b811fec1ae84bb28bd87). 広島県広島市中区堀川町1-15 ざくろビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 8, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [89450](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89450). 730-0033 広島県広島市中区堀川町4-11 広島アサヒビール館7F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.875; Full-address similarity 0.604; Source-pin distance 129.1 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE柏店 / ビアポンバーGROVE柏店

- **DARTSLIVE**: [ec494d9d49a0879d58d385ea46352d8f](https://search.dartslive.com/jp/shop/ec494d9d49a0879d58d385ea46352d8f). 千葉県柏市柏2-3-1 オークプラザⅡ-B1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89225](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89225). 277-0005 千葉県柏市柏2丁目3-1. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.474; Source-pin distance 20.0 m; Unit/floor appears in only one source; confirm the exact premises.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: サイバック宗像店 / サイバック宗像店

- **DARTSLIVE**: [5783c95bc03c3d160d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/5783c95bc03c3d160d9b047a20a7ba1e). 福岡県宗像市野坂2652-1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [51515](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=51515). 811-3423 福岡県宗像市大字野坂2652-1 ショッピングモールSTAR宗像バイパス内. Inventory: VSPHOENIX S4 2台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.473; Source-pin distance 81.5 m; Address numbers differ; check street/building numbers, branch and postcode.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE渋谷明治通り店 / ビアポンバーGROVE渋谷店

- **DARTSLIVE**: [0fef464dc6dd31fcf454cb89828a1cfe](https://search.dartslive.com/jp/shop/0fef464dc6dd31fcf454cb89828a1cfe). 東京都渋谷区渋谷1-14-15 森ビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [50019](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=50019). 150-0002 東京都渋谷区渋谷2-19-17 第106東京ビル4F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.875; Full-address similarity 0.583; Source-pin distance 155.0 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE渋谷店 / ビアポンバー GROVE 渋谷明治通り店

- **DARTSLIVE**: [3dc20cba6dd83fef0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3dc20cba6dd83fef0d9b047a20a7ba1e). 東京都渋谷区渋谷2-19-17 第106東京ビル4F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95935](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95935). 150-0002 東京都渋谷区渋谷1-14-15 森ビル6F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.875; Full-address similarity 0.583; Source-pin distance 149.2 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファナティーお初天神 / ファナティー お初天神2号店

- **DARTSLIVE**: [dbeef6a2db923aab0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/dbeef6a2db923aab0d9b047a20a7ba1e). 大阪府大阪市北区曽根崎2-14-13 河合ビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91840](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91840). 530-0057 大阪府大阪市北区曽根崎2-8-15 KSスクエアビル 104. Inventory: VSPhoenix X 1台 VSPhoenix X-MAX 1台.
- **Evidence**: Normalized name similarity 0.870; Full-address similarity 0.582; Source-pin distance 103.4 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ＆ビリヤード スポット キュー / ビリヤードスポットキュー

- **DARTSLIVE**: [d167e372a764d4dba3f63593b5358cc4](https://search.dartslive.com/jp/shop/d167e372a764d4dba3f63593b5358cc4). 山形県山形市北町1-3-20 ゲームプラザBe in 2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [10193](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=10193). 990-0821 山形県山形市北町1-3-20. Inventory: VSPHOENIX S4 2台 VSPHOENIX S 4台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.558; Source-pin distance 12.9 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: プラザアピア静岡店 / プラザアピア

- **DARTSLIVE**: [a243d5fac7a019170d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a243d5fac7a019170d9b047a20a7ba1e). 静岡県静岡市駿河区中吉田15-8 パチンコマルハン棟2F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [78589](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=78589). 422-8001 静岡県静岡市駿河区中吉田15-8 2階. Inventory: VSPHOENIX S4 3台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.640; Source-pin distance 3.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: カラオケまねきねこ 名張鴻之台店 (PlayGarden) / PlayGarden 名張鴻之台店

- **DARTSLIVE**: [1a03a05224cc271efec1ae84bb28bd87](https://search.dartslive.com/jp/shop/1a03a05224cc271efec1ae84bb28bd87). 三重県名張市鴻之台１番町1511 棟1・2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [99047](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99047). 三重県名張市鴻之台一番町1511 棟1・2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.488; Full-address similarity 0.950; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: UNIVERSE / UNIVERSE

- **DARTSLIVE**: [20b7a0a60aa77d270d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/20b7a0a60aa77d270d9b047a20a7ba1e). 福島県郡山市駅前2-5-1 和光ビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92277](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92277). 963-8001 福島県郡山市大町1丁目4 エリート16ビル4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.435; Source-pin distance 149.9 m; Different explicit units/floors: likely separate premises; do not merge.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: namcoワンダーシティ南熊本店 / 快活CLUB ワンダーシティ南熊本店

- **DARTSLIVE**: [1c2f937bbaf8a0ff28032249b44395af](https://search.dartslive.com/jp/shop/1c2f937bbaf8a0ff28032249b44395af). 熊本県熊本市中央区九品寺6-9-1. Inventory: {&quot;DARTSLIVE2&quot;: 4, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [79076](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=79076). 862-0976 熊本県熊本市中央区九品寺6丁目9-43. Inventory: VSPhoenix X 1台 VSPHOENIX S4 1台.
- **Evidence**: Normalized name similarity 0.727; Full-address similarity 0.700; Source-pin distance 147.4 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ&amp;ビアポン BASE2 新宿歌舞伎町店 / ダーツ＆ビアポン BASE1新宿店

- **DARTSLIVE**: [4a4930d753d8f4da0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/4a4930d753d8f4da0d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-17-2 小松ビル7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [89591](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89591). 160-0021 東京都新宿区歌舞伎町1-6-3 東海苑ビル9F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.824; Full-address similarity 0.596; Source-pin distance 132.5 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダーツ＆ビアポン BASE1新宿店 / ダーツ&amp;ビアポン BASE2 新宿歌舞伎町店

- **DARTSLIVE**: [1bd454594cf0ad740d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/1bd454594cf0ad740d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-6-3 東海苑ビル9F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92488](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92488). 160-0021 東京都新宿区歌舞伎町1-17-2 小松ビル7F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.824; Full-address similarity 0.596; Source-pin distance 127.5 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE池袋西口店 / ビアポンバーGROVE池袋北口店

- **DARTSLIVE**: [58ad98675ab98f5f5f9f3321c1147265](https://search.dartslive.com/jp/shop/58ad98675ab98f5f5f9f3321c1147265). 東京都豊島区西池袋１-17-7 池袋ルミエールビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [88290](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=88290). 171-0021 東京都豊島区西池袋1-35-8 東海ビル3F. Inventory: VSPhoenix X 3台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.938; Full-address similarity 0.480; Source-pin distance 184.5 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: B-GARAGE 錦糸町南口駅前店 / Bar GARAGE 錦糸町南口駅前店

- **DARTSLIVE**: [5e459e48633625a058d385ea46352d8f](https://search.dartslive.com/jp/shop/5e459e48633625a058d385ea46352d8f). 東京都墨田区江東橋3-13-1 KS15ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 6}.
- **Phoenix**: [90488](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90488). 130-0022 東京都墨田区江東橋4-20-4 エメラルドビルB1F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.938; Full-address similarity 0.471; Source-pin distance 218.4 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: cafe and dining GAO / CAFE&amp;DINING GAO

- **DARTSLIVE**: [473d43d31d7793f4774c926eb736cb5a](https://search.dartslive.com/jp/shop/473d43d31d7793f4774c926eb736cb5a). 香川県高松市古新町10-11. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [70820](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=70820). 760-0025 香川県高松市古新町10-11 寿屋1Fリーガホテルゼスト高松  東側裏. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.897; Full-address similarity 0.510; Source-pin distance 27.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Amusement Bar EDGE / Amusement BAR Aiming

- **DARTSLIVE**: [d7037dd5da144088fec1ae84bb28bd87](https://search.dartslive.com/jp/shop/d7037dd5da144088fec1ae84bb28bd87). 東京都世田谷区南烏山6-5-2 烏山駅前中央ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [47379](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=47379). 157-0062 東京都世田谷区南烏山6-4-10　第5野萩ビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.765; Full-address similarity 0.615; Source-pin distance 95.4 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 広島中央通り店 / ダイニングダーツバーBee 広島店

- **DARTSLIVE**: [3bfcd16ecf3633260d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3bfcd16ecf3633260d9b047a20a7ba1e). 広島県広島市中区堀川町4-11 HIROSHIMA CENTER BLD7F. Inventory: {&quot;DARTSLIVE2&quot;: 7, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [89450](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=89450). 730-0033 広島県広島市中区堀川町4-11 広島アサヒビール館7F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.485; Source-pin distance 3.6 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Bar Room 2nd / Bar Room

- **DARTSLIVE**: [986cedb4b4a0eb340d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/986cedb4b4a0eb340d9b047a20a7ba1e). 千葉県船橋市前原西2-15-12 第2三商ビルB1. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [82833](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=82833). 274-0825 千葉県船橋市前原西2丁目13-24 SKDビル3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.824; Full-address similarity 0.538; Source-pin distance 19.2 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: GLEEN CAFE WEST / GLEEN CAFE EAST

- **DARTSLIVE**: [ddecc2f55148eb5d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ddecc2f55148eb5d0d9b047a20a7ba1e). 埼玉県越谷市南越谷4-5-1 Ko&#x27;s-Due2F-D号室. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91678](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91678). 343-0845 埼玉県越谷市南越谷1-13-3 GAYA113BLDG1F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.923; Full-address similarity 0.429; Source-pin distance 117.5 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAR Zi..ng / Darts BAR Zi..ng

- **DARTSLIVE**: [a1287b24c7660c0458d385ea46352d8f](https://search.dartslive.com/jp/shop/a1287b24c7660c0458d385ea46352d8f). 福岡県行橋市中央3-1-4 グランジビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [98535](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=98535). 824-0005 福岡県行橋市中央3-1-4 2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.737; Full-address similarity 0.615; Source-pin distance 2.7 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: BAGUS-バグース-町田東口 / バグース 町田東口店

- **DARTSLIVE**: [0df250fa3989d05d0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/0df250fa3989d05d0d9b047a20a7ba1e). 東京都町田市原町田6-13-17 アーバンミサワビル5F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 12}.
- **Phoenix**: [60596](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=60596). 194-0013 東京都町田市原町田6-13-17. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.727; Full-address similarity 0.609; Source-pin distance 2.8 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: アミューズメントバー D.P.S 新宿店 / アミューズメントバー鶴千

- **DARTSLIVE**: [ac5569209b2f33f50d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/ac5569209b2f33f50d9b047a20a7ba1e). 東京都新宿区歌舞伎町1-6-14 第2ショーリビル3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 5}.
- **Phoenix**: [99645](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=99645). 東京都新宿区歌舞伎町1-15-5 ビックレオンビルB2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.612; Source-pin distance 97.8 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Creed / GREED

- **DARTSLIVE**: [8f043c0118fa4e4e0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/8f043c0118fa4e4e0d9b047a20a7ba1e). 鹿児島県鹿児島市呉服町2-2 Y.BLD2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [90552](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90552). 鹿児島県鹿児島市千日町9-7　廻ビル4階B号. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.513; Source-pin distance 178.2 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Dining Bar LAND / dining &amp;BAR Kronos

- **DARTSLIVE**: [aa72b0ec9e0b92da0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/aa72b0ec9e0b92da0d9b047a20a7ba1e). 東京都八王子市横山町11-2 金子ビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [95180](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=95180). 東京都八王子市三崎町４−９ 山川ビル 9F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.595; Source-pin distance 236.8 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link本八幡駅前店 / Link 本八幡店

- **DARTSLIVE**: [915547037f3c375c790ab824ce8730e5](https://search.dartslive.com/jp/shop/915547037f3c375c790ab824ce8730e5). 千葉県市川市八幡2-16-6 八幡ハタビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 8}.
- **Phoenix**: [49394](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=49394). 272-0023 千葉県市川市南八幡4-4-5 ウィンズ本八幡2F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.417; Source-pin distance 135.4 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Link 本八幡店 / Link 本八幡駅前店

- **DARTSLIVE**: [23f11723acfb4a300d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/23f11723acfb4a300d9b047a20a7ba1e). 千葉県市川市南八幡4-4-5 ウィンズ本八幡2F. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [96985](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=96985). 272-0021 千葉県市川市八幡 2-16-6 八幡ハタビル6F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.889; Full-address similarity 0.417; Source-pin distance 134.0 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: SO:BAR〜noge sakuragicho〜 / So bar 野毛桜木町店

- **DARTSLIVE**: [6106a8c026e73440a3f63593b5358cc4](https://search.dartslive.com/jp/shop/6106a8c026e73440a3f63593b5358cc4). 神奈川県横浜市中区野毛町1-13-5 NOGE BRICK3F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [92137](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92137). 神奈川県横浜市中区野毛町1-13-5 NOGERICK3F. Inventory: VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.323; Full-address similarity 0.981; Source-pin distance 3.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: M-GARAGE津田沼店 / mgrry 津田沼店

- **DARTSLIVE**: [a877dcca5fe684d4f454cb89828a1cfe](https://search.dartslive.com/jp/shop/a877dcca5fe684d4f454cb89828a1cfe). 千葉県船橋市前原西2-13-13 アロー津田沼駅前ビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [91916](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=91916). 274-0825 千葉県船橋市前原西2-12-11 ノバビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.700; Full-address similarity 0.604; Source-pin distance 59.9 m; Address numbers differ; check street/building numbers, branch and postcode; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE歌舞伎町店 / ビアポンバー GROVE 新宿店

- **DARTSLIVE**: [a28b6b51e477d63d790ab824ce8730e5](https://search.dartslive.com/jp/shop/a28b6b51e477d63d790ab824ce8730e5). 東京都新宿区歌舞伎町1-18-9 ワモール歌舞伎町7F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81111](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81111). 160-0021 東京都新宿区歌舞伎町1-23-15 SUZUYAビル6F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.500; Source-pin distance 91.4 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ビアポンバーGROVE渋谷宇田川町店 / ビアポンバー GROVE渋谷センター街店

- **DARTSLIVE**: [d8afa344ebf9467cf454cb89828a1cfe](https://search.dartslive.com/jp/shop/d8afa344ebf9467cf454cb89828a1cfe). 東京都渋谷区宇田川町28-3 いちご渋谷文化村通りビル6F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [100211](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=100211). 150-0042 東京都渋谷区宇田川町28-1 高山ランド第15ビル5F. Inventory: VSPhoenix X 3台.
- **Evidence**: Normalized name similarity 0.757; Full-address similarity 0.508; Source-pin distance 23.3 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ファナティー中通り / ファナティー中通2 ぱんだ店

- **DARTSLIVE**: [6d8c9e1e49e894400d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/6d8c9e1e49e894400d9b047a20a7ba1e). 大阪府大阪市北区堂山町7-22 ステージ中通りビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [93282](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=93282). 530-0027 大阪府大阪市北区東堂山町8-8 エイトビル2F. Inventory: VSPhoenix X 2台.
- **Evidence**: Normalized name similarity 0.727; Full-address similarity 0.528; Source-pin distance 27.4 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ダイニングダーツバーBee 広島中央通り店 / ダイニングダーツバーBee 流川店

- **DARTSLIVE**: [3bfcd16ecf3633260d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/3bfcd16ecf3633260d9b047a20a7ba1e). 広島県広島市中区堀川町4-11 HIROSHIMA CENTER BLD7F. Inventory: {&quot;DARTSLIVE2&quot;: 7, &quot;DARTSLIVE3&quot;: 3}.
- **Phoenix**: [90077](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=90077). 730-0033 広島県広島市中区堀川町1-15 ざくろビル2F. Inventory: VSPhoenix X 1台.
- **Evidence**: Normalized name similarity 0.778; Full-address similarity 0.452; Source-pin distance 132.5 m; Unit/floor appears in only one source; confirm the exact premises; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: MGM collection / SSS COLLECTION

- **DARTSLIVE**: [a6fafe1ddbd8780b0d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/a6fafe1ddbd8780b0d9b047a20a7ba1e). 東京都立川市錦町1-5-34 ゆうゆう館2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [66119](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=66119). 190-0022 東京都立川市錦2-1-10　コートドール2　4F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.769; Full-address similarity 0.435; Source-pin distance 243.9 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ZINO 松戸店 / Link 松戸店

- **DARTSLIVE**: [16e5fe44553483d20d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/16e5fe44553483d20d9b047a20a7ba1e). 千葉県松戸市本町20-3 姫作ビル1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [81104](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=81104). 271-0092 千葉県松戸市松戸1231 アステシオビル8F. Inventory: VSPhoenix X 3台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.489; Source-pin distance 187.0 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ZINO 蒲田店 / Link 蒲田店

- **DARTSLIVE**: [b818fe2dea0d2ae10d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/b818fe2dea0d2ae10d9b047a20a7ba1e). 東京都大田区西蒲田7-6-10 エルシティ蒲田1F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [92017](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=92017). 144-0051 東京都大田区西蒲田7丁目3-3 第一醍醐ビル8F. Inventory: VSPhoenix X 1台 VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.471; Source-pin distance 120.2 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: Darts Bar A&#x27;s 大塚店 / Darts bar Rapt

- **DARTSLIVE**: [209e632f88b918540d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/209e632f88b918540d9b047a20a7ba1e). 東京都豊島区北大塚2-6-10 ST1ビルB1F. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [97838](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=97838). 170-0004 東京都豊島区北大塚２-２７−2 シューエイト北大塚　3F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.720; Full-address similarity 0.423; Source-pin distance 182.7 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: ZINO 川越店 / Link 川越店

- **DARTSLIVE**: [43b73814bbe710540d9b047a20a7ba1e](https://search.dartslive.com/jp/shop/43b73814bbe710540d9b047a20a7ba1e). 埼玉県川越市脇田町12-15 ケイアイビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [85251](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=85251). 350-1122 埼玉県川越市脇田町4-2 ドン・キホーテ川越東口店6F. Inventory: VSPhoenix X 4台 VSPHOENIX S4 1台 VSPHOENIX S 2台.
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.423; Source-pin distance 230.8 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### JP: バー ボラーチョ / Bar borracho

- **DARTSLIVE**: [59a43856009b027c5f9f3321c1147265](https://search.dartslive.com/jp/shop/59a43856009b027c5f9f3321c1147265). 福岡県久留米市東町38-31 ヒカリビル2F. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [94128](https://vs.phoenixdarts.com/jp/shop/shopDetail?s_seq=94128). 福岡県久留米市東町38-31 ヒカリビル2F. Inventory: VSPHOENIX S 1台.
- **Evidence**: Normalized name similarity 0.000; Full-address similarity 1.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### KR: 천마복권 / 천마복권(광주)

- **DARTSLIVE**: [9f7a859086c75e3b28032249b44395af](https://search.dartslive.com/kr/shop/9f7a859086c75e3b28032249b44395af). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [100214](https://www.phoenixdarts.com/kr/shop/shopDetail?s_seq=100214). 광주광역시 북구 서암대로 299. Inventory: [].
- **Evidence**: Normalized name similarity 0.800; Full-address similarity 0.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### MY: K DARTS CAFE / K DARTS CAFE (MUAR)

- **DARTSLIVE**: [984f4009ec448c8028032249b44395af](https://search.dartslive.com/my/shop/984f4009ec448c8028032249b44395af). No.10, 2nd Floor, Jalan Mega 2 Pusat, Perdagangan Mega Jln Sakeh, 84000 Muar, Johor, Malaysia. Inventory: {&quot;DARTSLIVE2&quot;: 5, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [99501](https://www.phoenixdarts.com/my/shop/shopDetail?s_seq=99501). No. 10, 2nd FLOOR, JALAN MEGA 2, PUSAT PERDAGANGAN JALAN SAKEH, 84000 MUAR, JOHOR.. Inventory: VSS 2 ..
- **Evidence**: Normalized name similarity 0.833; Full-address similarity 0.896; Source-pin distance 199.9 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### SG: Le White Bar / VOLTA BISTRO

- **DARTSLIVE**: [38f5149d7d0020a1f454cb89828a1cfe](https://search.dartslive.com/sg/shop/38f5149d7d0020a1f454cb89828a1cfe). 27 West Coast Highway, #01-05, Westway, Singapore 117867. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [91431](https://www.phoenixdarts.com/sg/shop/shopDetail?s_seq=91431). 27 WEST COAST HIGHWAY, #01-03 WEST WAY,  SINGAPORE 117867. Inventory: VSX 2 ..
- **Evidence**: Normalized name similarity 0.381; Full-address similarity 0.977; Source-pin distance 0.0 m; Different explicit units/floors: likely separate premises; do not merge; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### TW: 大醬無煙燒烤 / 大醬無煙燒烤

- **DARTSLIVE**: [b5781535bb5d55f4774c926eb736cb5a](https://search.dartslive.com/tw/shop/b5781535bb5d55f4774c926eb736cb5a). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [58142](https://www.phoenixdarts.com/tw/shop/shopDetail?s_seq=58142). 台中市 西區 忠誠街123號. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 7.9 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### TW: 極餓先生 / 極餓先生

- **DARTSLIVE**: [a8233baa75d88e55a3f63593b5358cc4](https://search.dartslive.com/tw/shop/a8233baa75d88e55a3f63593b5358cc4). . Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [95712](https://www.phoenixdarts.com/tw/shop/shopDetail?s_seq=95712). 宜蘭縣宜蘭市女中路三段67號 宜蘭. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 1.000; Full-address similarity 0.000; Source-pin distance 0.0 m.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### TW: Super8 / Super 8 酒吧

- **DARTSLIVE**: [77812c0191b600cc774c926eb736cb5a](https://search.dartslive.com/tw/shop/77812c0191b600cc774c926eb736cb5a). . Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [87386](https://www.phoenixdarts.com/tw/shop/shopDetail?s_seq=87386). 雲林縣斗六市長春路8號. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.857; Full-address similarity 0.000; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### TW: Yes Bar / Venus Bar

- **DARTSLIVE**: [3e5fdca76b7e42dd25d56fb0e5c39bac](https://search.dartslive.com/tw/shop/3e5fdca76b7e42dd25d56fb0e5c39bac). . Inventory: {&quot;DARTSLIVE2&quot;: 0, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [16659](https://www.phoenixdarts.com/tw/shop/shopDetail?s_seq=16659). 台北市中山區林森北路119巷9號. Inventory: VSS 1..
- **Evidence**: Normalized name similarity 0.714; Full-address similarity 0.000; Source-pin distance 62.5 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: BLUE TROPIX / Blue Tropix Bar

- **DARTSLIVE**: [00d29b647d0d8f9828032249b44395af](https://search.dartslive.com/us/shop/00d29b647d0d8f9828032249b44395af). 98-151 Pali Momi St., Aiea, HI 96701, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 7, &quot;DARTSLIVE3&quot;: 2}.
- **Phoenix**: [95534](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=95534). 98-151 Pali Momi St, Aiea, HI 96701. Inventory: VSS 5 ..
- **Evidence**: Normalized name similarity 0.870; Full-address similarity 0.952; Source-pin distance 21.2 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: TJ&#x27;s Sports Bar / TJ&#x27;s Sports Bar &amp; Grill

- **DARTSLIVE**: [6b6c9972c2090007f454cb89828a1cfe](https://search.dartslive.com/us/shop/6b6c9972c2090007f454cb89828a1cfe). 600 Kapiolani Blvd., Honolulu, HI 96813, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 3, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [65299](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=65299). 600 Kapiolani Boulveard, Honolulu, HI 96813. Inventory: VSP 4 ..
- **Evidence**: Normalized name similarity 0.828; Full-address similarity 0.933; Source-pin distance 2.7 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: Fergies Bar and Grill / Fergie&#x27;s Bar &amp; Grill Crosby

- **DARTSLIVE**: [0ecf26d6482b9b0d25d56fb0e5c39bac](https://search.dartslive.com/us/shop/0ecf26d6482b9b0d25d56fb0e5c39bac). 3615 FM-1942, Crosby, TX 77532, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [99373](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=99373). 3615 FM1942, Crosby, TX 77532. Inventory: VSS 1 ..
- **Evidence**: Normalized name similarity 0.769; Full-address similarity 0.939; Source-pin distance 1.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: KELLY&#x27;S PUB / Kelly&#x27;s Pub, El Cajon

- **DARTSLIVE**: [7647b9dee5bff4b0fec1ae84bb28bd87](https://search.dartslive.com/us/shop/7647b9dee5bff4b0fec1ae84bb28bd87). 719 E Bradley, El Cajon, CA 92021, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [94033](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=94033). 719 E Bradley Ave, El Cajon, CA 92021. Inventory: VSS 2 ..
- **Evidence**: Normalized name similarity 0.720; Full-address similarity 0.847; Source-pin distance 20.9 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: Wong&#x27;s Dragon Room / Wong&#x27;s Golden Palace

- **DARTSLIVE**: [4905493c5941164da3f63593b5358cc4](https://search.dartslive.com/us/shop/4905493c5941164da3f63593b5358cc4). 7126 University Ave, La Mesa, CA 91942, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 1, &quot;DARTSLIVE3&quot;: 0}.
- **Phoenix**: [93633](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=93633). 7126 University Ave, La Mesa, CA 91942. Inventory: VSS 3 ..
- **Evidence**: Normalized name similarity 0.500; Full-address similarity 0.957; Source-pin distance 0.0 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

### US: Lucky Dog / Neon Cactus

- **DARTSLIVE**: [2c140e4723e91c0da3f63593b5358cc4](https://search.dartslive.com/us/shop/2c140e4723e91c0da3f63593b5358cc4). 360 Brown St, West Lafayette, IN 47906, U.S.A.. Inventory: {&quot;DARTSLIVE2&quot;: 2, &quot;DARTSLIVE3&quot;: 1}.
- **Phoenix**: [96880](https://www.phoenixdarts.com/us/shop/shopDetail?s_seq=96880). 360 Brown St, West Lafayette, IN 47906. Inventory: VSS 4 ..
- **Evidence**: Normalized name similarity 0.111; Full-address similarity 0.958; Source-pin distance 114.1 m; Name evidence is weak; a shared building is not identity evidence.
- **Recommended action**: Confirm the exact branch, floor/unit, current provider pages and inventories. Keep both records separate until confirmed; preserve both provider IDs and source facts in any later linked display.

## Recommended next actions

- **Review first**: Validate high-confidence candidates against both original pages and, where needed, the venue itself; check that both providers are currently present.
- **Do not merge**: Shared buildings, different units/floors, weak names and many-to-one records need manual investigation. No automatic merge or deletion is part of this report.
- **Coverage**: Treat failed/unavailable directories as unmeasured coverage. Retry only through a working public source or obtain an authorised provider feed; never report zero installations from a failed source.
- **Maintenance**: Rerun this deterministic review after completed collection updates. Source changes can invalidate earlier suggestions.
