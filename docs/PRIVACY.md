# Privacy and external services

This describes the current read-only Ninja Darts implementation, not a legal certification or a policy for future account features.

## Location

The page requests an approximate country from `https://api.country.is/` when it loads. That provider receives the request's IP address. The directory uses only the returned country code, does not store the IP, and falls back to Singapore if the lookup fails or the country is unsupported.

Precise browser geolocation is requested only when the visitor presses Near me. The code compares that position against the public venue dataset locally in the browser; it does not send it to a Ninja Darts backend or save it in an account.

Opening Directions sends the selected venue coordinates to Google Maps. Map tile requests reveal the viewed map area to the tile provider, which can indirectly reveal the area a visitor is exploring.

## External services

GitHub Pages hosts the public directory. OpenStreetMap supplies the normal live basemap; embedded previews use OpenFreeMap/OpenMapTiles through MapLibre instead, without proxying or disguising requests to OpenStreetMap's tile server. Country.is supplies the country hint and Fontshare supplies fonts. These services receive normal network request information and apply their own policies, including [OpenFreeMap's privacy policy](https://openfreemap.org/privacy/).

Links to provider venue pages, social profiles and Google Maps leave this site. Their privacy terms apply after navigation.

## Storage and data

The service worker caches public app assets and venue data on the visitor's device for offline fallback. The app has no account system, ad tracker, first-party analytics, stored location history or payment collection.

Public venue facts come from provider directories and may be stale. Coordinates and opening/access details are not independently verified. Source attributions and collection dates are preserved where available; collecting public facts does not establish unlimited redistribution rights.

Adding accounts, reviews, venue claims, analytics, payments or a database will require a new data-flow and privacy review before those features launch.
