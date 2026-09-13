# Android controller build

**Build type:** Android APK

The Android app is a lightweight controller. A configured private installation can request a cloud update, display progress and confirm completion while processing runs remotely.

The public APK contains a safe demonstration mode with no provider credentials. Its SHA-256 value is a verification fingerprint: a matching value confirms a downloaded file is complete and unchanged.

## MyPTV TiviMate Controls

The private production Android project also includes **MyPTV TiviMate Controls**, a native Kotlin app for Android 9 and later. It provides a draggable six-button D-pad overlay above a user-selected installed TiviMate edition.

The user must explicitly enable Android's “Display over other apps” permission and the app's accessibility service. Direction buttons move accessibility focus, OK clicks the focused item, and Back invokes Android's supported accessibility global Back action. The app does not claim to inject arbitrary hardware key events and requires no root access.

Android 13 and newer may label a sideloaded copy's accessibility service **Controlled by restricted setting**. The user can open **Settings > Apps > MyPTV TiviMate Controls**, use the three-dot menu to choose **Allow restricted settings**, authenticate, and then return to **Settings > Accessibility > Installed apps**. This operating-system safeguard is not bypassed or silently changed by MyPTV.

The overlay remembers separate portrait and landscape positions, supports adjustable transparency and button size, can collapse from its drag handle, and has a persistent notification with a Stop action. An optional calibrated gesture fallback is available for custom-rendered screens, but it is less reliable and disabled by default. Screens that expose neither navigable accessibility nodes nor useful gesture behavior may remain incompatible.

Only genuine TiviMate launcher packages are considered as overlay targets. One detected edition is selected automatically with no chooser shown; the edition chooser appears only when multiple valid TiviMate editions are installed. MyPTV's controller itself is excluded from the results.

Controller processing and preferences remain on the device. The app does not collect screen contents, accessibility data, usage analytics, provider details, credentials, or private service endpoints.

The Android apps remain independently installable and visually distinct: TiviMate Controls uses a D-pad/OK launcher icon, EPG Remote uses straight red/yellow/green guide lines, and MyPTV Guide uses a TV GUIDE badge. Their stable application identities let a correctly signed update install over the matching earlier release without replacing either of the other apps.

# MyPTV Guide for Android

MyPTV Guide is a native Kotlin and Jetpack Compose companion for Android 9 and newer, including Android 15. It is a separate app that can coexist with the existing MyPTV controller and floating-controls apps. Playback remains in the viewer's chosen player.

The navy-and-mint interface has Home, Channels, Search, Following, Favourites and Tools. Home focuses on current movie listings and explicitly live major sporting competitions over the next three days. Following applies to whole competitions. Channels include current/next programmes, schedules, favourites, reminders and guide-status explanations.

Compact category and channel cards reduce scrolling. Page controls remain above the bottom navigation. Wider tablet and unfolded-phone windows show two columns, adapting back to one in narrow windows or with larger text settings.

The companion uses authenticated paginated JSON from the existing cloud guide. Telegram and Android share the same healthy published guide. Android keeps personal favourites, following and reminders locally and provides optional password-encrypted backup files. The controller key is entered by the user and encrypted using Android Keystore; it is excluded from backups and builds.

The app retains healthy pages for offline viewing with visible timestamps. Android notifications cover saved reminders, followed/favourite schedule changes and manually requested cloud-update completion. Background notification timing follows Android permissions and battery restrictions.

Production source, signing material, live channel identifiers, provider URLs, private configuration and release APKs stay in the private operations repository. Public demonstrations remain fictional; existing public demo downloads are not this production companion.

