# Global Phoenix importer

The map preserves the original DARTSLIVE feeds and adds public Phoenix business facts by country. The [country selector](https://www.phoenixdarts.com/sg/main/sel_language) is the discovery scope, not evidence that every selectable country has a working public venue directory.

## Collection and publication

- The manually dispatched `phoenix-global.yml` workflow processes one country at a time, with a minimum 1.2-second gap after each source response. Each country job has a six-hour maximum.
- Public directory pagination is followed, then individual public venue pages supply coordinates and available factual inventory. Native-script names are preserved. Japan uses its separately linked directory template.
- Checkpoints and partial facts are retained. HTTP 403/429 stops the workflow without bypass. Unavailable, failed, blocked and pending sources remain explicit in the [coverage audit](PHOENIX_COVERAGE.md).
- Each finished country is committed with GitHub's authenticated application identity and published through GitHub Pages. No user git identity is impersonated.
- Facts include provider URLs and timestamps. No player data, photos or promotional descriptions are copied.
- Coordinates are taken from source listings, not independently geocoded. Range checks reject impossible coordinates, with tighter checks for the reviewed Singapore pilot. Public visitor access and current operation are not guaranteed.
- Uncertain cross-brand duplicates are not silently merged. Listing counts are source listings, not a certified count of unique physical premises or machines.

## Live country spreadsheets

The owner explicitly approved workbook-level external-URL imports for the directory spreadsheets. The `sync_phoenix_drive.py` helper uses the already-authorised Google Workspace CLI; credentials and private folder identifiers are not committed.

Existing DARTSLIVE and Singapore pilot tabs are preserved. Each Phoenix market gets a `Phoenix Live` tab linked to the public country CSV and a `Collection status` tab linked to its audit row. Stable header-only CSVs allow pending feeds to exist without claiming any venue records.

Google controls `IMPORTDATA` refresh timing; changes are not guaranteed to appear instantly. A temporary import failure is shown explicitly. Formula-like source strings are escaped in generated CSVs, while canonical JSON keeps the original factual text.

```bash
python tools/phoenix_global.py --countries kh --cache .phoenix-cache
python tools/phoenix_global.py --build-only
python tools/sync_phoenix_drive.py --folder YOUR_DIRECTORY_FOLDER_ID --allow-external-imports
```

Use the last command only after the workbook owner approves Google's external-URL import permission. It does not change Google Drive sharing permissions.

## Rights and limitations

The [Phoenix terms](https://www.phoenixdarts.com/us/help/clause) restrict unauthorised redistribution and commercial use, and include restrictions on automated access inconsistent with intended use. Public availability is not a licence or proof of permission. Obtain a permission review before a full commercial directory launch, and honour provider removal or correction requests.

Coverage reflects what the public sources exposed at collection time. It must not be described as a guaranteed global installation census.
