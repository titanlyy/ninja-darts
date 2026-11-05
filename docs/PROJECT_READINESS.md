# Ninja Darts Project Readiness

Snapshot: 6 November 2026, Singapore time. The web directory and its recovery pipeline have been improved and deployed, but global Phoenix collection is not yet complete. This is a project status report, not the final cross-provider duplicate audit.

## Live project

- **Public directory:** [Ninja Darts](https://titanlyy.github.io/ninja-darts/).
- **Source and commits:** [titanlyy/ninja-darts](https://github.com/titanlyy/ninja-darts).
- **Current coverage:** [Phoenix collection audit](https://github.com/titanlyy/ninja-darts/blob/main/docs/PHOENIX_COVERAGE.md). This is the ongoing coverage record; counts below are a snapshot rather than a worldwide installation census.
- **Japan recovery:** [Run 42062735942](https://github.com/titanlyy/ninja-darts/actions/runs/42062735942), resumed from the saved checkpoint. Its last checked state was in progress, not complete.

## Published data snapshot

| Measure | Published records |
|---|---:|
| Original DARTSLIVE listings retained | 6,853 |
| Phoenix records collected | 10,534 |
| Phoenix records eligible for map pins | 10,441 |
| Total mapped provider listings | 17,294 |
| Phoenix country directories complete | 28 of 33 |

These are provider-listing counts, not a verified count of unique physical venues. The Phoenix snapshot also retains 75 public coordinate-held records without map pins and 18 excluded non-public/administrative records; missing coordinates are never replaced with invented positions.

- **Spain:** Complete, with 2,137 collected records and 2,133 eligible map records.
- **Japan:** Recovery is active. The published country snapshot still says failed, so it must not be represented as complete until the recovery publishes a complete country status.
- **China:** The official route redirects to an unavailable/DNS-failing source.
- **Brunei, United Arab Emirates and Ireland:** The official directories returned no usable venue rows. These remain explicit coverage gaps, not evidence of zero machines.

## Implemented and verified

- **Provider discovery:** Compact square brand-logo pins retain pointed location tips. Provider filters update country/global counts and rankings; the approximate IP country is pinned first, with Singapore as fallback.
- **Map navigation:** Search brings matching venues into view. Country and available regional/locality filters compose with provider selection; absent locality information is not fabricated.
- **Selection and Near me:** Street-level focus, a gold-highlighted unclustered selected pin and a name label remain visible above the mobile venue card. Mobile selection collapses the sidebar, including when an already-open desktop selection is resized into a narrow layout.
- **Clustering:** The existing 28-pixel grouping radius is retained. Cluster badges are smaller, large counts use compact labels with full counts available on hover, and conflicting cluster animations are disabled.
- **Venue details:** Provider IDs, source URLs and machine inventory remain attached to source records. Published hours/telephone facts are displayed when present; unsafe links and known corporate-policy footer links are not presented as venue websites.
- **Resilience:** An unavailable country feed does not erase the working feeds. Offline data fallback does not cache HTTP failures as good data, intercept external map tiles or delete unrelated app caches.
- **Preview compatibility:** The normal public site keeps its OpenStreetMap basemap. The embedded preview uses OpenFreeMap with a reproducibly bundled, versioned classic MapLibre worker, including support for opaque browser origins; it does not disguise or proxy requests to bypass OpenStreetMap restrictions.
- **Google Sheets:** All 33 configured country workbook connections were checked. Phoenix Live and Collection status imports are enabled, and existing source tabs are retained. Google controls external-data refresh timing, so updates are not instantaneous.

## Collection and review safeguards

Checkpoint saving now happens independently of publication and website deployment. A hosting failure cannot discard collection progress, and country-level completion is checked rather than inferred from a green orchestration step. Budget-limited continuations require saved progress; source access blocks are not bypassed.

An event-driven GitHub review workflow is installed. It runs the final duplicate review only when no collection is active/queued, Spain and Japan are complete, and no country remains pending, collecting or partial. Other failed/unavailable sources are reported as coverage gaps.

Matching is restricted to the same country and considers normalized names, full addresses, unit/floor conflicts, geographic distance, competing branches and potentially stale coordinates. Existing explicit dual-provider links, high-confidence candidates and uncertain candidates are separated. Each candidate preserves both providers' IDs, source URLs and inventories; proximity or a shared building alone does not establish a match.

The workflow publishes a Markdown report plus JSON/CSV evidence to the repository when ready. It does not merge or delete listings, change production counts, or invent coordinates. No final duplicate findings are asserted in this status report.

## Quality checks and application readiness

The latest local suite passed 36 Python tests and 7 Node tests, with JavaScript syntax checks and no reported npm audit vulnerabilities. GitHub CI repeats the tests, dependency audit, reproducible vendor check and public-build checks using Node 22.

Browser checks covered desktop and phone layouts, provider counts, search and empty results, source links, Near me and location denial, selected-pin visibility, country defaults, feed failures, offline recovery and responsive transitions. The hosted preview was inspected for actual streets/coastlines, not just a canvas element; the live public site's normal OpenStreetMap requests returned HTTP 200.

The public build uses an explicit asset allowlist so source tooling, git metadata, scraper checkpoints and private configuration are not deployed. A relative-scope PWA manifest and Capacitor configuration prepare the current web UI for a future Android/iOS wrapper.

Signed native applications, app-store submissions, account systems, venue claims, reviews, billing and a Supabase-backed application service have not been implemented. The current directory is a read-only web application; no Supabase schema migration was required or performed.

## Remaining work and limits

- **Finish Japan:** Let the existing recovery publish its country result; investigate any failed country result rather than treating the run's overall colour as proof of completion.
- **Complete the gated review:** Generate and inspect the final report only after the completion conditions are met. Candidate review does not authorize automatic merging.
- **Resolve external coverage gaps:** China, Brunei, United Arab Emirates and Ireland require usable official sources or separately verified replacement data. No zero-installation claim is justified.
- **Maintain provenance:** Provider listings and coordinates can be stale or misplaced, and a listing is not a guarantee of public access or current operation. Public visibility of facts does not by itself establish unrestricted redistribution or commercial-use permission.

The existing GitHub collection, continuation, deployment and completion-gated review workflows can proceed without another manual dispatch from the user. No additional Computer follow-up check has been scheduled.
