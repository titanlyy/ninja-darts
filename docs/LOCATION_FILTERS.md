# Country and locality navigation

All countries stays first, followed by the visitor's default country. Remaining
countries are ranked by total mapped listings, descending, with name as a
deterministic tie-breaker. Counts include both providers where the Phoenix pilot
is available.

## IP-based default

The browser requests https://api.country.is/ once on page load, with credentials
omitted and no referrer. The public service returns the caller's IP country;
this app uses only the country code and does not persist the IP or location.
The service necessarily receives the visitor's network IP, and is credited in
the sidebar. Service documentation: https://country.is/

A supported country is pinned and selected. Unsupported countries, invalid
responses, network failure or a 2.5-second timeout select and pin Singapore.
Macau maps to the existing Hong Kong / Macau directory. Manual country choices
after load are not overridden. IP estimates may reflect a VPN and are not
precise browser geolocation. Precise location is requested only when the user
clicks Near me.

Selecting a country reveals region and city/area controls in its expandable
navigation section, where source geography exists. The second control narrows
to the chosen region. Options show listing totals and are ranked by count.
Geography composes with provider, search and machine filters. Changing country
or using Near me clears geographic selections. Reset a selector to All to widen
the view again.

## Provenance and limitations

The additive `data/locations.json` joins original DARTSLIVE source IDs to
`large_region` and `medium_region` fields retained by the collector. Existing
country JSON records and coordinates are unchanged.

- Japan: prefecture and source city/district, including wards.
- USA: state and explicit city from comma-delimited postal addresses.
- Canada and Australia: province/state and explicit postal-address locality.
- France: region and department. The collected snapshot does not provide city
  names or street addresses, so French departments are not labelled as cities.
- China: source region and province/municipality.
- Taiwan: city/county from the source's large region field.
- Malaysia: region and state/territory.
- Other countries: source regions/areas where available.

Unknown localities are retained in Not provided options, never dropped or
assigned a nearest city. Source administrative names are preserved in their
original language. No translation, reverse geocoding or approximate city
assignment is performed. Singapore is a city-state and does not show the
country-to-city drill-down controls.

Refresh the additive metadata after refreshing the original source CSV:

```sh
python3 tools/build_locations.py /path/to/dartslive_shops.csv
```

Source venue pages remain linked in each venue's details. These fields describe
provider-supplied administrative groupings, not verified municipal boundaries.

## Marker geometry

The logo tile remains 30 × 30 px, within a 38 × 40 px Leaflet hit area. A
downward white triangle ends at the bottom-centre coordinate anchor (19, 40),
so the point, rather than the centre of the square, identifies the supplied pin
coordinate. Logo symbols remain text-free.

## Clustering

`CLUSTER_RADIUS_PX` in `js/app.js` controls the Leaflet marker-cluster grouping
distance in screen pixels. It is 28 px, reduced from the earlier 55 px setting,
so venues must be closer on screen to combine. Lower values reveal more
individual pins at the same zoom, at the cost of denser/overlapping logos.
It is not a fixed geographic distance: its ground distance changes with zoom.
Very close or identical-coordinate venues still cluster and can be expanded
by clicking a cluster and zooming in.

## Selection and Near me

Near me shows the nearest 50 records, selects the closest, and focuses that
shop at street-level zoom 16 rather than centring the visitor at zoom 11.
The closest shop's distance is shown separately in its card. Normal pin clicks
also focus and highlight the selected venue.

The selected logo has a gold outline and a permanent venue-name label on a
separate, unclustered overlay. Its highlight remains visible if the map is
zoomed out. Closing the card, switching country/provider, or filtering out the
venue clears the selection.

The camera uses the measured uncovered map rectangle: above a bottom card on
mobile, or left of the right-hand card on desktop. ResizeObserver repositions
the selection when the viewport or card dimensions change. The mobile card
is capped at 52dvh to preserve map space; its content scrolls within the card.
Opening a selection closes the sidebar on mobile/tablet widths up to 1024px.
Location lookup temporarily disables Near me and restores it on success or error.
