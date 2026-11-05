# Ninja Darts

A map-first public directory of DARTSLIVE and Phoenix venues, built directly on GitHub. Country totals represent collected provider listings, not independently verified unique premises.

[Open the live map](https://titanlyy.github.io/ninja-darts/) · [Phoenix coverage audit](docs/PHOENIX_COVERAGE.md)

## Directory features

- Compact pointed brand-logo markers, provider filters and provider-aware country totals/ranking.
- IP-estimated country default, with Singapore fallback; precise browser location is requested only for Near me.
- Region/city filters where source metadata exists, venue/address search, league and DARTSLIVE3 filters.
- Street-level nearest-venue focus, a highlighted pin and a mobile card that leaves the selection visible.
- Provider-attributed machine inventories, published hours/websites where available, directions and original listing links.
- Installable PWA with offline app/data fallback after a successful load. Basemap tiles require connectivity and are not bulk-cached.

## Source coverage and limitations

Original DARTSLIVE records span 18 source regions. The additive Phoenix importer targets 33 public country directories. Consult the generated coverage audit for the current status, timestamps and counts rather than assuming universal coverage.

Failed/unavailable directories do not establish zero installations. Source coordinates, opening hours, public visitor access and continued operation are not independently verified. Unmapped and restricted-access records are retained for review. Cross-provider duplicates may remain; uncertain matches are not silently merged.

Country Google Sheets have Phoenix Live and Collection status tabs linked to the repository feeds. Existing source tabs are preserved. Google controls IMPORTDATA refresh timing; this is not an instant live feed or a recurring rescrape.

## Development and packaging

```bash
python3 -m pip install requests beautifulsoup4
npm test
npm run check
npm run build
```

The build copies only public assets into `www/`, excluding tooling, repository metadata and scraper caches. The same output can be served as a static website or used by the included Capacitor configuration. See [mobile preparation](docs/MOBILE.md).

The app itself has no build-time dependencies, API keys, account system or paid map service. It uses vendored Leaflet/markercluster and public JSON feeds. Supabase is not required for this read-only directory; owner accounts, claims, moderation and billing in the proposed requirements document are future work, not implemented features.

## Collection pipeline

- `tools/DartsliveScraper.py` and `tools/build_data.py`: original DARTSLIVE CSV/JSON pipeline.
- `tools/phoenix_global.py`: paced, checkpointed Phoenix collection with country CSV/JSON feeds and source/coordinate holds.
- `phoenix-global.yml`: single-country-at-a-time collection, checkpoint preservation and explicit completion checks.
- `phoenix-resume.yml`: finite, bounded continuation of time-budget checkpoints only; no access-block bypass or recurring scraping.
- `deploy-site.yml`: independent public-asset deployment, so a hosting failure cannot discard source collection.
- `duplicate-review.yml`: event-driven, review-only candidate report after all collection stops and Spain/Japan are complete. Source gaps are explicit; no automated merges or deletions occur.
- `directory-quality.yml`: data consistency, matching safeguards, offline-cache regression tests and public build checks on code changes and collection completion.
- `tools/sync_phoenix_drive.py`: owner-authorized country workbook linking through the connected Google account. Never runs with Google credentials in GitHub Actions.

## Attribution and privacy

Venue facts are attributed to [DARTSLIVE](https://search.dartslive.com/) and [Phoenix Darts](https://www.phoenixdarts.com/). Names/logos remain their owners' property; collection does not establish commercial redistribution rights.

The basemap uses [OpenStreetMap](https://www.openstreetmap.org/copyright), subject to its tile usage policy. [Country.is](https://country.is/) provides the approximate country hint. Read [privacy and external services](docs/PRIVACY.md) before expanding the product.
