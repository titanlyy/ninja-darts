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
  text; a downward tip anchors the supplied coordinate within a 38 × 40 px hit area.
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

## Country and locality navigation regression

- Country counts are numerically descending with All countries pinned first.
- Japan → Tokyo prefecture: 1,084 records; Shinjuku district: 102.
- USA → Hawaii → Honolulu: 30 records. Washington → Seattle: 15.
- France → Bretagne → Côtes-d'Armor: 122 records, correctly labelled Department.
- Region reset clears the city selection. Country switch clears both selections.
- Provider filters compose with geography; Phoenix in Shinjuku returns zero,
  and returning to All restores 102.
- City-scoped nonsense search returns zero, then clearing restores city count.
- Near me resets geographic/provider selections and returns 50 nearby venues;
  denied location permission displays an explanatory message.
- Singapore provider, DARTSLIVE3 and league totals remain 61/60, 32 and 37.
- Mobile 375 px city controls fit inside the scrolling country navigation;
  collapsing the drawer restores the full map with no horizontal overflow.
- No application exceptions, JavaScript syntax failures or whitespace errors.
- Venue snapshots and original coordinate fields remain unchanged.

## Lighter clustering

- `CLUSTER_RADIUS_PX` reduced from 55 to 28 screen pixels.
- Same 1440 × 900 Singapore zoom-11 view: 2 individual pins / 12 clusters
  before, 11 individual pins / 18 smaller groups after.
- All 121 Singapore listings remain included; clustering changes representation,
  not the number of listings.
- Cluster click-to-zoom, DARTSLIVE/Phoenix buttons, machine filters, search,
  venue details and Japan prefecture/district filtering pass regression checks.
- Mobile map and provider filtering remain usable.

## Selected venue focus and IP default

- Mobile Near me with a granted Ang Mo Kio coordinate selects iDarts X (Big Mac
  Centre), opens the card with a separate 0.2 km distance, collapses the drawer,
  and loads zoom-16 map tiles.
- At 375 × 812, the selected pin ends at y=219, above the card starting at
  y≈382. The permanent selected-venue label is fully within the visible map.
- Gold selection stays unclustered when zooming out. Card close, Escape and
  provider switch remove the overlay.
- Mobile short viewport 375 × 640 and landscape 812 × 375 preserve the pin
  and label outside the card. Desktop selection fits left of the card.
- Ordinary Phoenix pin selection uses the same highlight and camera.
- Denied geolocation restores Near me and shows an explanatory message with
  no invented marker.
- Mocked IP defaults: USA→USA, France→France, unsupported GB→Singapore,
  Macau→Hong Kong / Macau, HTTP 503→Singapore, timeout→Singapore.
- Every IP-default case pins the selected country after All countries and
  sorts the remaining countries by count. Manual Japan/Tokyo/Shinjuku selection
  stays selected after initial load.
- Real browser integration received HTTP 200 from https://api.country.is/ and
  selected the sandbox IP's USA country without precise-location permission.
- IP API purpose and privacy behaviour are documented in LOCATION_FILTERS.md.

## Provider navigation counts

- All / DARTSLIVE / Phoenix global badges: 6,914 / 6,853 / 61.
- Singapore badges: 121 / 60 / 61. Japan: 4,024 / 4,024 / 0.
- Selected Tokyo / Shinjuku retain their options with zero Phoenix counts and
  restore to 1,084 / 102 for DARTSLIVE.
- Mobile badges follow the same provider selection. Near me resets global
  badges to all-provider totals.
- Core Leaflet and markercluster assets are served locally after an external
  CDN failure was reproduced; subsequent page checks had no app exceptions.
