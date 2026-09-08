# MyPTV — Public Roadmap

Last updated: 7 September 2026

This is the sanitised public roadmap. The private operations repository contains deployment-specific information, private endpoints, credentials, generated data, and production release details that are intentionally excluded here.

For the full engineering journey, including problems and fixes across every major iteration, read [PROJECT-HISTORY.md](PROJECT-HISTORY.md).

## What is working

- XMLTV validation, health reporting, backups, and safe replacement.
- Channel, programme, title, description, genre, network, region, and time-window search.
- UHD/FHD-first channel families with regional and `+1` differences preserved.
- English-first fallback policy and safe non-overlapping schedule enrichment.
- Missing-information and coverage auditing.
- Official DStv comparison and reviewed channel mappings, including Movie Room.
- Sports hubs, live-event filtering, timelines, countdowns, and reminders.
- Desktop dashboard, personal MyPTV interface, command-line assistant, and private Telegram bridge.
- Favourites, saved searches, discovery, watched/dismissed memory, and Tonight planning.
- Separate private VOD indexing, series/episode browsing, watchlist, and discovery.
- Cloud-based twice-daily guide generation with Android and Windows remote triggers.
- Android status, progress, elapsed time, version display, guide totals, missing-information count, collapsible settings, and persistent per-stage results.
- Approved liquid-glass Android interface, first validated as a separate BlueStacks preview before production integration.
- MyPTV V3.0 Stable Windows interface, promoted after its complete navigation and guide workflows were validated as a preview.
- Rolling three-day Premier League, Champions League, Formula 1 and UFC coverage with competition-level following controls.
- Explicit dead, working-without-guide and awaiting-confirmation guide states.
- Persistent reviewed feed corrections and exact station/callsign matching for safe guide enrichment.
- Atomic publication that keeps the previous healthy cloud guide active if a build or upload fails.
- Credential-safe personal backup/restore, self-diagnostics and followed/favourite schedule-change alerts.

## Current priorities

### 1. Android experience

- Continue checking the liquid-glass interface at phone and larger-screen sizes.
- Preserve readability, accessibility, live progress, and persistent stage results in future releases.

### 2. Missing guide coverage

- Re-audit channels without programme information after each source refresh.
- Treat working UK and US feeds without programme information as the critical remaining enrichment queue.
- Ignore channels absent from a provider catalogue; they are outside the product's purpose.
- Evaluate rights-compliant free sources individually.
- Keep only sources that measurably improve correct coverage.
- Add explicit aliases only after channel identity and regional schedule are verified.

### 3. Reliability

- Observe scheduled and manual cloud runs for accurate queued/running/completed/failed transitions.
- Strengthen duplicate-trigger protection and active-run warnings.
- Expand regression tests for status persistence, duplicate schedule removal, and channel matching.
- Track source performance without exposing private operational data.

### 4. Public demonstration

- Keep the public Android build as a safe demo with no production credentials or private controller access.
- Publish clearer demo releases rather than expecting visitors to find temporary Actions artifacts.
- Add screenshots and a concise architecture overview.
- Keep this roadmap and `PROJECT-HISTORY.md` updated from sanitised private release notes.

## Later improvements

- Richer artwork and channel logos.
- More search aliases and event intelligence.
- Better update-history and source-health visualisation.
- Additional desktop accessibility and layout polish.
- Optional hosted notification mode, kept separate from the core guide updater.

## Non-negotiable safety rules

- Never publish provider credentials, controller keys, private guide URLs, personal identifiers, signing keys, generated private databases, stream addresses, or viewing history.
- Never attach an uncertain or regionally different schedule merely to raise a coverage percentage.
- Never let a failed optional source destroy a valid provider-based guide.
- Never replace the working production UI with an unapproved preview.
