# Channel discovery and update pipeline

**Build type:** Scheduled guide-processing and publishing service

## Discover channels
The updater reads the provider catalogue and preserves the identifiers required by the viewing application. Regional feeds, quality variants and time-shifted channels remain distinguishable.

## Compile schedules
Provider listings are combined with approved public sources. Fallback information fills eligible gaps only. Matching considers names, regions, official numbers and known feed differences.

## Build and validate
Accepted listings become a TiviMate XMLTV guide and private searchable indexes. Empty, malformed, stale or sharply reduced builds are rejected before they can replace the last known-good guide.

## Run periodically
The cloud workflow runs at 07:00 and 19:00 Johannesburg time, with manual requests also supported. Only validated compressed output and compact status data are published; credentials and stream addresses are excluded.

## Storage
- SQLite: private guide and VOD indexes during processing.
- Cloudflare KV: compressed guide and status data.
- Cloudflare D1: limited application state.
- GitHub Actions: scheduled processing environment.
