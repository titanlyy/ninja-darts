# Android and iOS preparation

Ninja Darts is a responsive static PWA. A Capacitor configuration and a reproducible public-asset build are included so the web directory can become the shared UI for future native wrappers.

## Current implementation

- `npm run build` generates `www/` from an explicit public-asset allowlist.
- `capacitor.config.json` points to that output with app ID `com.titanlee.ninjadarts`.
- PWA manifest uses relative scope/start URLs and includes normal/maskable icons.
- Geolocation uses the browser API, with denial handling and no guessed position.
- App/data fallback uses successfully cached visits after service-worker installation. A first-time visit may need an additional online reload before all country data is available offline; uncached map tiles still require connectivity.

This preparation is not a signed Android/iOS app. Native permissions, device testing, signing, store review and store accounts remain necessary.

## Create native projects when ready

```bash
npm install @capacitor/core @capacitor/android @capacitor/ios
npm install --save-dev @capacitor/cli
npm run build
npx cap add android
npx cap add ios
npx cap sync
```

Android needs Android Studio/SDK tooling. Building iOS requires macOS and Xcode. Configure location usage descriptions/permissions and verify geolocation on physical devices; if using the native geolocation plugin, adapt the web call explicitly rather than assuming plugin installation changes it.

Do not publish a thin wrapper without checking the relevant store's current policies. Review icons, accessibility, privacy disclosures, navigation, offline behaviour and source data rights before submission.

## Data updates

The build bundles the collected public dataset. A native release can ship updated data, or a future reviewed configuration can fetch trusted HTTPS feeds. The current static app does not silently install native updates or use a remote-code server.

Never bulk-download OpenStreetMap tiles for offline packs. Use a tile provider and licence that explicitly permits the intended native/offline usage.

The web tile layer sends an accurate origin referrer where the browser permits it, as required by [OpenStreetMap's tile policy](https://operations.osmfoundation.org/policies/tiles/). Embedded previews/privacy filters may suppress it and receive blocked tiles; do not work around that by spoofing identification or proxying anonymous traffic. Recheck the tile provider and identification requirements before a native release.

Embedded previews use the separate, public [OpenFreeMap](https://openfreemap.org/) vector service, which permits website/app and commercial usage without an API key. It is rendered through pinned, vendored MapLibre GL and its Leaflet adapter; source attribution is retained. `?basemap=vector` exercises this renderer on a normal host. No offline tile download is implemented, and that service's current terms still apply.
