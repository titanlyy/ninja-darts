# Country and locality navigation

Countries are ranked by the total number of currently mapped listings, descending,
with name as a deterministic tie-breaker. All countries remains above the ranking.
Counts include both providers where the Phoenix pilot is available.

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
