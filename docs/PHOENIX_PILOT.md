# Phoenix Darts Singapore pilot

## Scope and provenance

The Singapore pilot reads public shop-listing and shop-detail pages at
[Phoenix Darts](https://www.phoenixdarts.com/sg/shop/shopSearch).
Source IDs, URLs, collection timestamps, supplied coordinates and machine
inventories are retained in `data/phoenix-sg.json` and `data/phoenix-sg.csv`.
Only venue facts are collected, not player profiles, venue descriptions or photos.
Missing inventories are unknown, not zero. Public listings can be stale.

The snapshot contains 67 source listings with supplied Singapore coordinates
and machine counts. Of these, 61 are included as venue candidates; six test,
provider office, workplace or camp listings are held for visitor-access review.
There are no confirmed cross-brand matches in this snapshot. Same-building
records with different unit numbers or names remain separate. The Singapore
map therefore contains 60 original DARTSLIVE venues and 61 Phoenix candidates,
121 total, while the global map contains 6,914 records across 18 regions.

The collector is sequential and paced, checkpoints each parsed record, and stops
on HTTP 403 or 429. It neither authenticates nor bypasses access controls.

## Matching and data safety

Original `data/sg.json` and other DARTSLIVE files are not overwritten. The
browser adds the Phoenix pilot feed, using a reviewed `dartslive_id` to attach
provider inventories and links to an existing venue. Unmatched venues get
provider-prefixed IDs. Runtime marker keys include country to avoid ID collisions.

Exact normalized names with coordinates within 100 m can match automatically.
Other candidates require an explicit source-ID mapping and rationale.
Candidate proximity alone is never sufficient. See
`docs/phoenix-sg-match-review.json` for candidates and decisions.

## Refresh

Install `requests` and `beautifulsoup4`. Keep cache outside the published folder.

```sh
python3 tools/phoenix_pilot.py \
  --output /tmp/phoenix-sg.json --cache /tmp/phoenix-cache
python3 tools/build_phoenix_pilot.py /tmp/phoenix-sg.json \
  --matches docs/phoenix-sg-reviewed-matches.json
```

Cached facts are reused on resume. To deliberately refresh the source snapshot,
use a new cache folder after allowing appropriate time between collection runs.
Review generated candidates and invalid coordinates before publishing.

## Identification and rights

Official brand logos identify machine providers, not an affiliation or
endorsement. Local logo assets and original asset URLs are recorded in
`icons/providers/README.md`. Do not interpret public accessibility or robots.txt
as a licence. [Phoenix terms](https://www.phoenixdarts.com/sg/help/clause)
restrict unauthorised reproduction, distribution and commercial use of service
information; permission review is needed before wider/commercial reuse.

Numbered clusters aggregate venues; zoom in to see individual logo pins.
Phoenix currently covers Singapore only. The Both filter means confirmed
cross-provider matches, not inferred co-location.
