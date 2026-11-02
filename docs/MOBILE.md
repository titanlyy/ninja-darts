# Mobile Apps (Android & iOS)

Ninja Darts is built as a fully static, installable PWA with no server-side dependencies. That makes it trivially wrappable as a native app later using [Capacitor](https://capacitorjs.com/) — the same codebase ships to Android (Play Store) and iOS (App Store).

## Why this app is mobile-ready

- **Static SPA** — plain HTML/CSS/JS, no server, no SSR, no backend calls. Host anywhere (GitHub Pages, CDN, or bundle in the app).
- **PWA manifest + service worker** — already installable on Android/iOS home screens, with offline caching of the app shell.
- **Responsive layout** — collapsible sidebar, bottom-sheet detail panel, touch targets ≥ 34px, safe-area insets handled via `viewport-fit=cover`.
- **Geolocation "Near me"** — uses the standard Web Geolocation API, which Capacitor exposes natively.
- **No API keys** — map tiles are free OSM/CARTO with attribution; no billing surprises.

## Wrapping with Capacitor (when you're ready)

```bash
npm install @capacitor/core @capacitor/cli @capacitor/geolocation
npx cap init "Ninja Darts" com.titanlee.ninjadarts --web-dir=www

# Put the site into www/ (or point --web-dir at the repo root if you keep
# index.html at the top level and exclude tooling files):
mkdir www
cp index.html manifest.webmanifest sw.js css js data icons www/ -r

npx cap add android
npx cap add ios        # requires macOS with Xcode
npx cap sync
npx cap open android   # opens Android Studio — build & sign there
```

### Recommended native plugins

| Need | Plugin |
|---|---|
| Fused/native location | `@capacitor/geolocation` (replace `navigator.geolocation` calls) |
| Native map performance | Keep Leaflet, or swap to `@capacitor/google-maps` later |
| Offline map tiles | `@capacitor-community/capacitor-offline` or pre-cache tiles for target cities |
| Push notifications | `@capacitor/push-notifications` (Phase 4: event alerts) |

### Data updates inside the app

`data/*.json` are fetched at runtime over HTTP. In a native app you can either:

1. Keep fetching from the GitHub Pages URL (auto-updates, needs network), or
2. Bundle the JSON in `www/data/` at build time (fully offline, update via app release).

## Google Play / App Store notes

- Add privacy policy URLs (geolocation permission requires justification on both stores).
- iOS requires `NSLocationWhenInUseUsageDescription` in Info.plist.
- Data is sourced from DARTSLIVE's public search site — attribute it in the app description and settings screen.
