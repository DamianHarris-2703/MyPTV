# MyPTV — Complete Project History

Last updated: 7 September 2026

This is the long-form, public history of MyPTV: what was built, what went wrong, what was learned, and how each major problem was resolved. It deliberately excludes credentials, access keys, private guide addresses, provider account details, personal identifiers, signing material, and generated private viewing data.

The short project description belongs in `README.md`. Current plans belong in `IPTV-EPG-Roadmap.md`. This document preserves the engineering story.

## 1. The original problem

MyPTV began as a personal answer to a simple frustration: a large IPTV channel list is not useful when programme information is incomplete, stale, duplicated, in the wrong language, attached to the wrong regional feed, or impossible to search quickly.

The first goal was therefore not another video player. It was an intelligence and reliability layer around an XMLTV guide:

- validate and inspect the guide;
- search channels and programmes quickly;
- show what is on now, later, tonight, or during a chosen window;
- prefer the best available UHD/FHD/HD feed;
- make missing information visible rather than silently guessing;
- preserve private provider configuration locally.

## 2. Command-line guide assistant

The earliest usable version was a Python command-line assistant. It introduced guide loading, channel search, current and next programme views, freshness checks, and CAT/SAST time handling.

### Problems found

- Large result sets were difficult to navigate.
- A channel could appear several times at different quality levels or for different regions.
- Live sport, replays, normal TV repeats, and archive channels were easily confused.
- Searching only channel names missed titles and descriptions.

### Fixes

- Added paged results with next/back navigation.
- Grouped equivalent channel families while preserving genuinely different regional and `+1` schedules.
- Added UHD/FHD-first ordering and same-channel quality fallback.
- Separated explicitly live sport from replay/archive results.
- Added unified, case-insensitive search across channel names, titles, descriptions, and channel-plus-programme queries.
- Added join-safety labels such as just started, safe to join, joining late, and ending soon.

## 3. Natural-language discovery

The assistant expanded from strict commands into ordinary viewing questions. It learned requests such as what is on now, whether a title is showing tonight, when a team or event starts, and what begins after a chosen time.

### Problems found

- A word such as “Marvel” could match unrelated text.
- Singular/plural title differences caused missed results.
- General searches could accidentally mix live television with on-demand content.
- Sports questions could mistake training, archive, or replay material for a live match.

### Fixes

- Added franchise-aware Marvel and superhero matching.
- Added flexible title normalization and singular/plural handling.
- Kept live TV and VOD routing separate unless the user explicitly requests on-demand content.
- Required explicit live markers for sports and match-style titles for sensitive fixture/reminder logic.
- Added genre intelligence for movies, series, documentaries, horror, science fiction, comedy, action, thriller, romance, crime, family, and animation.

## 4. Sports intelligence

MyPTV gained dedicated views for major sports networks and personal interests, including football, motorsport, combat sports, basketball, and other selected events.

### Problems found

- Coverage times and event times are not always the same.
- Regional sports feeds may carry different events under similar channel names.
- An EPG alone cannot reliably predict details such as a headline walkout time.
- Archive listings could be mistaken for the next live event.

### Fixes

- Added guide-backed event timelines showing coverage start, event listing, expected end where available, preferred feed, countdown, and confidence.
- Preserved regional differences when current or upcoming listings differ.
- Kept unknown timings explicitly unknown rather than estimating them.
- Added exact fixture checks before consulting optional external information.
- Added network and regional sports hubs with next-24-hours views.

## 5. Desktop interfaces

The command-line engine was wrapped in a Windows dashboard and later a more personal MyPTV interface. These surfaces reused the same guide logic rather than becoming separate products with different answers.

### Problems found

- Long-running actions appeared frozen.
- Exact-feed buttons could resolve the wrong channel when provider identifiers were duplicated or blank.
- Generic home screens became cluttered.
- Clipboard, scrolling, back navigation, and paging needed desktop-quality behaviour.

### Fixes

- Added visible running states and elapsed-time feedback.
- Retained exact channel objects for Open, Favourite, and Reminder actions.
- Reworked Home into a focused launchpad with selected channels and editable shortcuts.
- Added consistent cards, paging, back navigation, scroll support, copy controls, and right-click text editing.
- Added an EPG health dashboard and update history rather than hiding operational problems in logs.

## 6. Personalisation, reminders, and discovery

The system added favourites, saved searches, watched/dismissed memory, reminders, and recommendation cards.

### Problems found

- Recommendations repeated titles the user had already watched or rejected.
- Reminders could target the wrong duplicate listing.
- Desktop and Telegram could drift into different saved states.

### Fixes

- Added private watched and dismissed memory.
- Made search results selectable by exact result number.
- Shared favourites, custom lists, reminders, and watch-state through the same private local data.
- Added five-part discovery and a customised Tonight plan while keeping reasons visible.

## 7. Telegram bridge

A private Telegram interface brought the same guide commands and reminders to a phone without publishing the underlying provider data.

### Problems found

- Temporary network loss could stop the bot.
- A failed notification could be incorrectly treated as delivered.
- Long replies and navigation were awkward on a phone.

### Fixes

- Added automatic reconnect with bounded backoff.
- Retried failed reminder delivery.
- Added concise formatting, shortcut menus, Home/Back controls, numbered selections, and paged results.
- Restricted the bot to the configured owner rather than exposing a public guide bot.

## 8. VOD kept separate from live television

MyPTV later indexed a private movie and series catalogue, but kept it structurally separate from the live XMLTV guide.

### Problems found

- Live schedule questions and on-demand searches could produce misleading mixed answers.
- Series required season and episode navigation rather than flat title results.
- Link checks must not expose private playback addresses.

### Fixes

- Added a separate private VOD database and explicit routing.
- Added movie/series labels, metadata caching, season and episode browsing, watchlists, Continue Watching, and VOD discovery.
- Added safe availability checks without displaying credentials or stream URLs.

## 9. EPG coverage and fallback strategy

Coverage work became a major part of the project. The provider guide remained the base, while carefully constrained fallbacks filled verified gaps.

### Problems found

- Many live channels had no guide identifier or no programme data.
- Similar channel names could refer to different countries or schedules.
- Some free sources returned zero listings, failed authentication, timed out, disappeared, or supplied the wrong language.
- Combining sources could create duplicate or overlapping programmes.
- A numerically higher coverage score could still mean worse, incorrect data.

### Fixes

- Built a coverage audit and missing-English-guide finder.
- Added safe same-channel quality fallback.
- Required explicit English programme titles for public English fallbacks.
- Preferred provider listings and only appended safe, non-overlapping later programmes.
- Added source-specific regional safeguards for approved free UK and US XMLTV data.
- Rejected uncertain lookalikes, foreign-language mismatches, stale/empty data, and regionally different schedules.
- Collapsed duplicate schedule slots while preserving the richer description.
- Tested potential sources one at a time and retained them only when they produced a measurable, safe improvement.

## 10. Official DStv comparison and Movie Room

An official South African DStv schedule was added for verified channel-number comparison and selected gap filling.

### The Movie Room problem

Movie Room became the best-known example of why channel matching cannot rely on one field. The live stream arrived without a usable guide identifier, so TiviMate showed no information even though an authoritative schedule existed.

### Fix

- Added an explicit, reviewed mapping between the provider’s Movie Room label and the official schedule identity.
- Kept the mapping narrow instead of introducing fuzzy matching that could affect unrelated movie channels.
- Verified the generated TiviMate guide and refreshed the player data.

This restored programme information without weakening the project’s “do not guess” rule.

## 11. Reliability safeguards

As more sources were added, a refresh could no longer be treated as one download followed by one overwrite.

### Problems found

- An empty, malformed, stale, or sharply reduced guide could replace a healthy guide.
- Optional source failures could block otherwise useful output.
- Long source jobs offered no visible proof of progress.
- A failed update could leave different interfaces reporting different states.

### Fixes

- Added structural validation and health checks before replacement.
- Retained known-good backups and restored them when active data was damaged.
- Split essential output stages from optional source stages.
- Reported optional source failures without discarding a valid provider-based guide.
- Added per-source elapsed time, update history, counts, missing-information totals, and clear passed/failed/skipped labels.

## 12. Moving production updates to the cloud

The original Windows schedule depended on the laptop being available. Production updating was migrated to a private GitHub Actions workflow with a small Cloudflare controller and private storage.

### Design decisions

- Run twice daily in CAT, with an additional manual trigger when needed.
- Keep the production operations repository private.
- Keep provider credentials, signing keys, controller keys, private guide addresses, generated guides, and viewing data out of the public repository.
- Let Android and Windows request the same cloud workflow rather than maintaining independent update engines.
- Keep public portfolio material separate from private operations.

### Problems found and fixed during migration

1. **Provider access in cloud builds:** introduced a protected relay rather than embedding credentials in GitHub or Android.
2. **Repository naming confusion:** separated and renamed the private cloud operations repository while retaining a distinct public showcase.
3. **Controller deployment on every EPG run:** separated controller deployment from the twice-daily guide schedule to reduce unnecessary work.
4. **Windows trigger behaviour:** converted the desktop console into a remote GitHub trigger while preserving local diagnostics.
5. **Time-zone presentation:** converted controller timestamps and schedule wording to CAT (UTC+2).
6. **Android installation conflicts:** introduced permanent signing and later version metadata so normal updates can install over the previous signed build.
7. **Missing branding:** added the app identity and launcher artwork to the Android build.
8. **Incorrect guide totals:** changed reporting to use the final enriched TiviMate export rather than an intermediate source.
9. **Missing live catalogue in cloud:** restored the provider catalogue stage so generated output included the intended channel set.
10. **Status callbacks:** hardened progress publishing and completion callbacks when network or deployment timing caused stale state.
11. **App stuck on queued:** reconciled controller state against the actual GitHub Actions run.
12. **No visible progress:** added live elapsed time, stage-based progress, automatic polling, and a real progress indicator.
13. **Optional source failures:** classified unavailable optional sources as reported failures/skips without failing the usable final guide.
14. **No detailed outcome list:** added per-stage passed, failed, skipped, running, and duration results.
15. **Results disappearing after success:** separated current status from the latest stage-result snapshot and added a device cache. Results now update live, persist after completion, and remain until the next run provides replacements.

## 13. Android controller evolution

The Android app is a private remote control and health display, not an IPTV player and not a container for provider credentials.

Its iterations added:

- manual cloud update trigger;
- connection saving;
- CAT schedule and report times;
- branded icon and permanently signed upgrades;
- darker phone-friendly interface;
- channel and programme totals;
- channels-without-information count;
- collapsible connection settings;
- automatic status refresh;
- queued/running/success/failed reconciliation;
- elapsed time and progress;
- version number;
- detailed live and persistent update results.

A separate liquid-glass prototype was then created for BlueStacks. It uses an atmospheric gradient, translucent cards, pill controls, a live-status card, progress, and accordion sections. After approval and production compilation, it became Android v1.6.0 while retaining the working controller, saved connection, live polling, versioning, and persistent-result behaviour.

## 14. Public and private repository split

The public repository exists to demonstrate the architecture, safe desktop logic, tests, documentation, and a non-production Android demo. It must never be a mirror of private operations.

The private repository remains the source of truth for deployment, credentials, production schedules, private endpoints, signed production APKs, and operational status. Public documentation is updated from a sanitised summary, not by copying private configuration.

## 15. Current lessons

- Correct unknown data is better than confident wrong data.
- Coverage percentage is meaningful only when language, region, identity, freshness, and overlap are safe.
- Optional sources must fail independently.
- The last known-good output should survive a bad refresh.
- Status needs an authoritative source and a durable completed snapshot.
- A progress bar must be backed by real stages, not decorative animation.
- Public documentation and private operations can be comprehensive without being the same repository.
- A redesign should be previewed separately from a working production controller.

## 16. Documentation maintenance rule

After every meaningful private production change:

1. Update the private operational roadmap.
2. Decide whether the change belongs in the public story.
3. If it does, add a sanitised entry here and update the public roadmap.
4. Never copy secrets, private links, account details, generated data, or signing material.

That rule keeps this history honest and detailed while preserving the separation that makes the production system safe.

## 17. MyPTV V3 stable milestone

The Windows visual redesign was kept separate until its navigation and established guide workflows had been transferred and tested. After approval, it became MyPTV V3.0 Stable and the primary Windows experience.

The milestone also consolidated rolling three-day coverage for followed football, motorsport and combat-sport competitions; competition-level follow/unfollow controls; live clock behaviour; persistent feed corrections; exact local-station guide matching; and explicit dead, no-guide and unconfirmed states. UK and US working feeds without schedules remain an enrichment task, rather than unfinished application functionality.

The first post-milestone reliability update added versioned, atomic cloud publication so a failed build cannot replace the last healthy guide. It also added safe personal backup/restore, schedule-change alerts for followed competitions and favourites, and a unified diagnostic covering local files and the hosted update path. Private credentials remain excluded from backups and public materials.

## 18. Exact-feed visual audit programme

A private, repeatable visual audit now checks each exact provider feed with multiple short decoding attempts, compares successful video with approved schedules, and requires three observations before a correction becomes active. DStV Kids and UK Kids are the first two completed groups in a private 60-group checklist.

The first audits found that some feeds inside Kids categories actually carried regional variants or adult evening brands. Confirmed schedule corrections are retained in private cloud storage and restored during future guide builds. Repeatedly inaccessible feeds receive an explicit failed-stream state; an old schedule can no longer hide a trusted DEAD result in the mobile snapshot.

Only the method and progress are documented publicly. Screenshots, exact feed identifiers, correction records, upstream addresses and credentials remain private.
