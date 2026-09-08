# MyPTV

MyPTV turns incomplete provider information into a clearer, searchable and regularly refreshed television guide.

MyPTV V3.0 is the completed stable Windows experience. Its approved top-navigation design, rolling sports view, competition following, guide-state reporting, feed correction and cloud-update controls now sit on the same mature guide engine.

The stable reliability toolkit now includes atomic last-healthy cloud recovery, credential-safe personal backup/restore, followed and favourite schedule-change alerts, and one-screen self-diagnostics.

## Project documentation

- **[Complete project history](PROJECT-HISTORY.md):** every major iteration, problem, diagnosis, fix, cloud-migration lesson, and Android-controller improvement, written without private operational data.
- **[Public roadmap](IPTV-EPG-Roadmap.md):** what works now, current priorities, later work, and the safety rules governing public/private separation.

The repository intentionally does not contain the private production Android controller or production credentials. The downloadable Android build is a safe demonstration app; production releases remain in the private operations repository.

## Public demonstrations

- **Interactive demo hub:** https://damianharris-2703.github.io/MyPTV/
- **Demo downloads:** see the latest release.

All public demonstrations use fictional sample records. Credentials, stream addresses, production databases and private guides are not included.

## Build types

| Build | Purpose | Demo |
|---|---|---|
| Windows desktop | Visual guide, discovery, favourites and guide health | Browser simulation and Windows download |
| Android controller | Requests an update and displays progress | Safe-demo APK |
| Telegram assistant | Conversational guide browsing, search and reminders | Browser simulation |
| Update service | Finds channels, combines schedules, validates and publishes | Pipeline explanation |

## Detailed build notes

- [Windows desktop build](WINDOWS-DESKTOP.md)
- [Android controller build](ANDROID.md)
- [Telegram assistant build](TELEGRAM.md)
- [Channel discovery and update pipeline](UPDATE-PIPELINE.md)

Release SHA-256 values are file-verification fingerprints, not passwords or activation codes.
