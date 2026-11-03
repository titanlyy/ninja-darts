# ninja-darts

🎯 A darts directory made by dart lovers, for dart lovers — listing all places to play darts around the world.

**Live map:** [https://titanlyy.github.io/ninja-darts/](https://titanlyy.github.io/ninja-darts/)

## What is this?

A map-based global directory of darts venues, with DARTSLIVE source data across 18 regions and a Singapore Phoenix Darts pilot. Counts reflect collected provider listings, not a guarantee of completeness or current operation.

## Phoenix Singapore pilot

- Official DARTSLIVE and Phoenix logo markers; both logos on matched dual-brand venues.
- Provider filters: All, DARTSLIVE, Phoenix and Both.
- Independent, provider-attributed machine inventories and source links.
- Conservative duplicate matching. The original DARTSLIVE data remains unchanged.
- Singapore opens by default. Country browsing still covers the global dataset.
- See [pilot collection and matching notes](docs/PHOENIX_PILOT.md).

## Features

- 🗺️ Full-screen interactive dark map with marker clustering
- 🔍 Search by venue name, city or address
- 🌏 Browse by country with venue counts
- 🎯 Filter: official league venues, venues with DARTSLIVE3 machines
- 📍 "Near me" — geolocation, nearest 50 venues with distances
- 📱 Installable PWA (works offline once loaded)
- 🤖 Android/iOS ready — see [docs/MOBILE.md](docs/MOBILE.md)

## Data pipeline

```
tools/DartsliveScraper.py   →  dartslive_shops.csv   →  tools/build_data.py  →  data/*.json
 (scrapes DARTSLIVE)            (raw venue rows)        (CSV → compact JSON)   (app data)
```

Refresh the data:

```bash
python3 tools/build_data.py dartslive_shops.csv data/
```

Per-country source spreadsheets are also kept in Google Drive → "Ninja Darts — DARTSLIVE Venues".

## Repository layout

```
├── index.html            # SPA shell
├── css/style.css         # dark night-darts-bar theme
├── js/app.js             # Leaflet map, search, filters, detail panel
├── data/                 # index.json + <country>.json venue files
├── tools/                # scraper + data build script
├── icons/                # PWA icons (dartboard)
├── manifest.webmanifest  # PWA manifest
├── sw.js                 # service worker (offline caching)
└── docs/                 # requirements (ARD) + mobile guide
```

## Roadmap

See [docs/APP_REQUIREMENTS.md](docs/APP_REQUIREMENTS.md) for the full plan: venue claiming, reviews, events, subscriptions. This map is Phase 1's public directory front-end.

## Attribution

- Venue data: [DARTSLIVE](https://search.dartslive.com/) (scraped for community, non-commercial use)
- Singapore pilot data: [Phoenix Darts](https://www.phoenixdarts.com/sg/shop/shopSearch). Source rights and terms remain applicable; this pilot does not establish permission for commercial reuse.
- Map tiles: © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright) © [CARTO](https://carto.com/attributions)
