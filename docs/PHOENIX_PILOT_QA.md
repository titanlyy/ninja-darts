# Singapore pilot checks

Checked 2026-11-03 using Chromium, at 1440 × 900 and 375 × 812.

- Initial Singapore view: 121 records.
- Provider buttons: DARTSLIVE 60, Phoenix 61, All 121, with explicit pressed state.
- Japan switch: 4,024 existing records. Global view: 6,914 across 18 regions.
- Search: SE9TEMBER resolves to one Phoenix venue; nonsense query returns zero;
  clearing the query restores the provider result set.
- Existing filters: DARTSLIVE3 returns 32 Singapore records and league returns 37.
- Detail panel: SE9TEMBER shows supplied address and two VSS machines, original
  provider page and coordinate-based Google Maps directions.
- Branded marker symbols load in 30 × 30 px square markers with no wordmark
  text; Leaflet hit areas remain 38 × 38 px for easier selection.
- Mobile sidebar can open and collapse; provider filtering and detail opening
  work without document-width overflow.
- Near me with a supplied Singapore browser location returns 50 nearest venues.
- No page JavaScript exceptions during these flows.
- Data assertions: 67 unique source IDs, complete names, addresses and inventories,
  coordinates bounded to Singapore, 61 directory-eligible records.
- JavaScript syntax and Git whitespace checks pass.
- Original DARTSLIVE country data and index are unchanged.

These are UI and structural checks, not verification that a venue is currently
operating, allows public access, or still has the listed machines. No confirmed
dual-provider venue was found; the empty Both filter was removed in the UI cleanup.
