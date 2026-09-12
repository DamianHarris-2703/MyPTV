# Android controller build

**Build type:** Android APK

The Android app is a lightweight controller. A configured private installation can request a cloud update, display progress and confirm completion while processing runs remotely.

The public APK contains a safe demonstration mode with no provider credentials. Its SHA-256 value is a verification fingerprint: a matching value confirms a downloaded file is complete and unchanged.

## MyPTV TiviMate Controls

The private production Android project also includes **MyPTV TiviMate Controls**, a native Kotlin app for Android 9 and later. It provides a draggable six-button D-pad overlay above a user-selected installed TiviMate edition.

The user must explicitly enable Android's “Display over other apps” permission and the app's accessibility service. Direction buttons move accessibility focus, OK clicks the focused item, and Back invokes Android's supported accessibility global Back action. The app does not claim to inject arbitrary hardware key events and requires no root access.

The overlay remembers separate portrait and landscape positions, supports adjustable transparency and button size, can collapse from its drag handle, and has a persistent notification with a Stop action. An optional calibrated gesture fallback is available for custom-rendered screens, but it is less reliable and disabled by default. Screens that expose neither navigable accessibility nodes nor useful gesture behavior may remain incompatible.

Controller processing and preferences remain on the device. The app does not collect screen contents, accessibility data, usage analytics, provider details, credentials, or private service endpoints.
