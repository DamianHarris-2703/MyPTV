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

The next audit completed UK Music, UK News and UK Sports Extra, bringing the private checklist to five of 60 groups. The audit distinguishes working and failed streams from schedule confidence: a decodable feed can still be marked NO GUIDE when its content does not match an approved source, or UNCONFIRMED when its identity changes between checks. Confirmed schedule mappings remain private and require three observations.

## 19. Native VOD search and documentary audit

The native Android guide now gives on-demand titles their own VOD destination in the bottom navigation. Live Search is limited to channels and scheduled programmes, while VOD searches movies, series and documentaries through separate authenticated, paginated requests. Both views retain the same private-data allowlist and never return playback addresses or provider identifiers.

The DStv Documentary group became the sixth completed visual-audit group. Repeated stream checks, visible network identification and approved schedule comparison were completed before publication. The private repository retains the feed-level evidence and guide associations; the public project records only the method and overall progress.

The DStv General and Music groups brought the checklist to eight of 60. Every entry received three live checks, working feeds were compared with approved schedules, and consistently inaccessible feeds received explicit status records. One consistently mislabelled music feed was corrected only after three matching observations in private cloud storage; the public repository contains no feed identifiers, viewing addresses or correction payloads.

## 20. DStv Movies and Entertainment audit

The DStv Movies and Entertainment groups brought the private checklist to ten of 60. All 62 entries received three live-media checks. Working feeds were visually identified and compared with approved schedules, missing schedule associations were restored privately, and feeds that repeatedly failed were given explicit availability states.

One correctly labelled service consistently displayed its expected off-air slate but had no approved schedule, so it is reported as NO GUIDE rather than receiving guessed listings. No feed-identity correction was needed. The public repository retains only this sanitised result; feed identifiers, upstream addresses, private configuration and audit evidence remain private.

## 21. DStv Sports and News audit

The DStv Sports and News groups brought the private checklist to twelve of 60. All 85 entries received three live-media checks, with sequential retries used to separate transient decoding errors from stable failures. Working services were visually identified and compared with approved schedules before four missing official associations were restored privately.

Regional and online services without exact approved schedules remain explicitly NO GUIDE instead of borrowing listings from similar channels. One provider-labelled news entry consistently displayed a different network in all three observations; the correction was confirmed in private Cloudflare storage and the feed remains NO GUIDE because an exact schedule is unavailable. The public repository contains no feed identifiers, viewing addresses, screenshots or correction payloads.

## 22. UK Locals and Movies audit

The UK Locals and Movies groups brought the private checklist to fourteen of 60. All 92 entries received three live-media checks. Seventy-six working feeds were visually compared with their guide data, while sixteen feeds unavailable throughout all three attempts received explicit status records.

The review also handled current channel renames and several repeatedly mislabelled services through the existing three-confirmation process. Exact schedule associations and three NO GUIDE decisions were stored privately so neither client presents a confident but incorrect schedule. The public repository records the audit outcome without provider identifiers, upstream addresses, screenshots, correction payloads, credentials or private configuration.

The authenticated mobile API was also tightened so category and channel requests process only the requested page and group. This keeps the larger refreshed guide responsive without changing opaque identifiers or exposing private catalogue data.

## 23. UK and African Radio audit

The UK and African Radio groups received three local live-audio checks across 127 stations. One hundred and eighteen stations decoded successfully in at least one round; nine were unavailable in all three rounds and have explicit private availability states prepared for the next batched publication. Transient timeouts did not turn otherwise working stations into false failures.

The audit also requested ICY metadata, inspected timed stream-title blocks and checked ID3 artist/title fields. The provider relay exposed no usable now-playing metadata during these checks, so the clients will not guess artist or song names. The audit tooling is ready to retain that information when a feed supplies it, while stations without embedded metadata require a separately reviewed source.

This audit was deliberately local and did not start a cloud guide build or create a GitHub Actions artifact. Raw observations, provider identifiers, stream addresses and private state records remain outside the public repository.

## 24. UK Entertainment and Documentary audit

The UK Entertainment and Documentary groups received three local live-media checks across 92 exact feeds. Seventy-six working services were visually reviewed, while sixteen feeds that remained unavailable or displayed a provider unavailable slate received explicit private failure states for the next batched publication. Temporary failures recovered in another pass and were not misclassified.

The review found two provider labels carrying Travelxp, corrected a television-versus-radio name collision affecting U&GOLD schedules, and isolated several feeds carrying a different regional service. Exact approved UK schedule aliases were prepared where a matching source exists, and six corrections were confirmed through the private three-observation store. Feeds with an unknown, switching or unsupported regional identity remain NO GUIDE or UNCONFIRMED instead of borrowing a convenient schedule.

This audit also remained local and did not trigger a guide build, deployment or Actions artifact. Correction evidence, provider identifiers, raw frames, private schedules and access details remain outside the public repository.

## 25. UK Sports and Subtitles audit

The UK Sports and Subtitles groups received three local media checks across 96 feeds. Sixty-three decoded in at least one pass, while 33 remained unavailable through all three checks. Seven of the eight subtitle feeds worked and visibly carried subtitles.

The sports review found several numbered services attached to schedules for different channel numbers, along with placeholder listings and unstable feeds that changed to unrelated programming. Seventeen exact mappings met the three-observation rule and were stored privately. Regional services without an approved exact source remain NO GUIDE, and incomplete or changing identities remain UNCONFIRMED instead of receiving a guessed schedule.

The competition recogniser was tightened after a sports listing exposed “Premier League Darts” with an EPL tag. Darts can no longer enter the English Premier League section on Home. This audit stayed local and did not start a guide build or create an Actions artifact; private identifiers, stream addresses, raw images, controller details and correction records were not copied here.

## 26. Canadian Kids and Music audit

The Canadian Kids and Music groups received three local media checks across 17 feeds. Eleven decoded in at least one pass, while six remained unavailable through all three checks. Temporary failures did not turn otherwise working feeds into false DEAD results.

Six channel identities met the three-observation rule. Four exact Canadian schedule associations are prepared privately for the next batched publication, while two confirmed channels remain NO GUIDE because the approved sources contain no exact schedule. Five intermittent or insufficiently identified feeds remain UNCONFIRMED rather than receiving guessed regional listings.

One music-labelled entry consistently carried a different established Canadian network and was corrected only after three matching observations. This audit did not start a cloud guide build or create a GitHub Actions artifact. Provider identifiers, upstream addresses, screenshots, controller details, schedule mappings and correction records remain private.

## 27. Canadian Documentary and Entertainment audit

The Canadian Documentary and Entertainment groups received three local media checks across 46 feeds. Thirty-one decoded in at least one pass, while 15 remained unavailable through all three checks. A single temporary timeout recovered in another pass and did not create a false DEAD result.

Twenty identities met the three-observation rule. Eighteen exact schedule associations are prepared privately for the next batched publication, two confirmed services remain NO GUIDE, and seven feeds remain UNCONFIRMED because their visible identity did not reach the required threshold. Several provider labels were found carrying different established networks, including one former Canadian channel name that now carries its replacement service.

The authenticated correction endpoint’s bounded request ceiling was increased to retain the growing reviewed history. Backend tests verify that the expected history is accepted while oversized requests remain rejected. Only the controller was deployed; no guide build or XMLTV publication was started. Private identifiers, mappings, observations, addresses, credentials and raw images remain outside this repository.

## 28. Canadian Movies and General audit

The Canadian Movies and General groups received three local media checks across 74 feeds. Sixty decoded in at least one pass, while 14 remained unavailable through all three checks. Intermittent failures recovered in another pass and were not marked dead.

Eleven identities met the three-observation rule. Six exact Canadian schedule associations are prepared privately for the next batched publication, and five confirmed services remain NO GUIDE because no usable exact approved schedule exists. Forty working feeds remain UNCONFIRMED where the exact regional market, channel number or stable service identity could not be established safely.

The audit found one movies entry consistently carrying another established Canadian service and corrected it through the existing private confirmation process. Regional network branding was not treated as proof of a city-specific schedule, and numbered premium feeds did not borrow listings from adjacent channels.

This audit stayed local and did not start a guide build, Worker deployment or GitHub Actions guide artifact. Provider identifiers, stream addresses, raw frames, controller details, schedule mappings and correction records remain private.

## 29. Canadian News and Sports audit

The Canadian News and Sports groups received three valid local media checks across 64 feeds. Forty-one decoded in at least one pass, while 23 remained unavailable through all three checks. A local decoder-access problem invalidated an earlier attempt; that attempt was discarded and repeated rather than being counted as channel evidence.

Ten identities met the three-observation rule. Four exact schedule associations are prepared privately for the next batched publication, and six confirmed services remain NO GUIDE because the approved index lacks a usable unambiguous match. Eleven working or intermittent feeds remain UNCONFIRMED where the exact network, regional variant or stable recovery did not meet the required threshold.

The review corrected several provider labels that consistently carried other established services. Regional news listings were attached only when the pictures established the market, and a Canadian sports service did not borrow a schedule from its numbered sibling. An intermittent sports feed that recovered once remains UNCONFIRMED instead of being falsely marked dead.

This audit stayed local and did not start a guide build, Worker deployment or GitHub Actions guide artifact. Provider identifiers, stream addresses, raw frames, controller details, schedule mappings and correction records remain private.

## 30. Canadian TV and Ultra audit

The final two Canadian groups received three local media checks across 344 feeds. Two hundred and sixty-one decoded in at least one pass, while 83 remained unavailable through all three checks. Intermittent errors recovered in another pass and were not marked dead.

Thirty-five exact identities met the three-observation rule. Fourteen replacement-service associations are prepared privately for the next batched publication, 21 confirmed services remain NO GUIDE because no exact approved schedule exists, and 39 working or intermittent feeds remain UNCONFIRMED where recovery or visible identity did not satisfy the required threshold.

The broad catalogues repeat many channels from the smaller Canadian groups under different feed identifiers, so every duplicate was checked independently. Several recurring provider-label errors were confirmed again, including news, nature, children's and weather services carrying another established channel. The Ultra category also proved to be a provider catalogue label rather than a guarantee of 4K delivery; successful samples ranged from standard definition to 1080p.

This completes all ten Canadian groups in the private checklist. The audit stayed local and did not start a guide build, Worker deployment or GitHub Actions guide artifact. Provider identifiers, stream addresses, raw frames, controller details, schedule mappings and correction records remain private.
