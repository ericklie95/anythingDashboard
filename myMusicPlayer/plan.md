# myMusicPlayer — Project Plan (Draft v0.1)

> Status: **Planning / partly answered.** Decisions so far are in §0. Every item marked **[Q]** still needs your decision before it gets built. Sections marked **[Proposed]** are my recommendation only.

---

## 0. Decisions log

| # | Topic | Decision | Date |
|---|---|---|---|
| D1 | Repository | **Standalone project** in its own GitHub repo (not inside anythingDashboard). This plan stays here temporarily and will be removed later | 2026-10-27 |
| D2 | Build approach | **Fork vivi-music** and customise it (Q2 option a). The project inherits **GPL-3.0**. The proprietary `musixmatch` module must be removed or replaced | 2026-10-27 |
| D3 | Sign-in | **Same as vivi-music:** WebView Google login, session cookie stored on device (§3.4 option A) | 2026-10-27 |
| D4 | Sync direction | **Two-way.** Likes and playlist edits in the app are written back to YouTube Music | 2026-10-27 |
| D5 | Accounts | **Single Google account only.** No account switching. The user picks which email to sign in with on Google's own login page; the app doesn't need to know the account in advance. Account risk (§3.2) accepted on that basis | 2026-10-27 |
| D6 | Repo setup | **Private** repo `ericklie95/myMusicPlayer` for **personal use only**. It contains vivi-music's full commit history (not a GitHub fork, because forks of public repos can't be private). vivi-music is added as the `upstream` remote; pull in its fixes with `git fetch upstream` then `git merge upstream/main` | 2026-10-27 |

| D7 | Lyrics | **All kinds:** plain, line-synced and word-by-word (karaoke). Use vivi-music's non-Musixmatch providers (LRCLIB, KuGou, YouLyPlus, Paxsenix, Unison, BetterLyrics, YouTube). **Musixmatch is removed** because of its licence restriction | 2026-10-27 |
| D8 | Minimum Android | **Android 14 (API 34)**: `minSdk = 34`, raised from vivi-music's 26 | 2026-10-27 |
| D9 | Source scope | **YouTube Music only.** No regular YouTube videos (Q4b) | 2026-10-27 |
| D10 | History reporting | **Report plays to YouTube history**, with an on/off toggle in settings (Q4c) | 2026-10-27 |
| D11 | Features | Yes / Later / No marked per feature in §5 | 2026-10-27 |

| D12 | Devices | **Phone only** (Q10) | 2026-10-27 |
| D13 | Design | **Keep vivi-music's look**: Material You, colours from album art (Q11) | 2026-10-27 |
| D14 | Name / package | App name **myMusicPlayer**, package ID **`com.ericklie.mymusicplayer`** (Q12) | 2026-10-27 |
| D15 | Distribution | **Build locally** for now; no release pipeline yet (Q13) | 2026-10-27 |
| D16 | Testing | Tested on **your physical Android phone** (Q14) | 2026-10-27 |
| D17 | Timeline | **Ongoing hobby project**, no target date (Q15) | 2026-10-27 |
| D18 | Musixmatch | **Removed from the current code** (commit "Remove Musixmatch lyrics provider"). It stays in old history so vivi-music updates still merge cleanly | 2026-10-27 |

| D19 | Existing vivi features | Features vivi-music already has are **kept and available now**, including ones marked Later in §5 | 2026-10-27 |
| D20 | Removed integrations | **JioSaavn and Spotify removed** (commits "Remove JioSaavn streaming", "Remove Spotify integration"). This also drops Spotify playlist import, Spotify lyrics and Spotify Canvas. Motionartwork animated backgrounds are unaffected | 2026-10-27 |
| D21 | Settings | Keep vivi-music's settings screen now; trim it as features are removed | 2026-10-27 |
| D22 | Local playlists | **Choose per playlist** whether it syncs with YouTube Music. vivi already has this: the "Create playlist" dialog has a "Sync playlist" switch | 2026-10-27 |
| D23 | Phase order | Confirmed as listed in §5 | 2026-10-27 |
| D24 | Downloads | Save downloaded songs to a **phone folder the user picks** (Android folder picker). **New work:** vivi only keeps downloads in app-private storage | 2026-10-27 |
| D25 | Building | No Android Studio. The repo's GitHub Actions workflow (`CI & Debug Build`) builds a debug APK on every push; download it from the run's Artifacts and install on the phone | 2026-10-27 |

Still open: whether features marked **No** in §5 that vivi already has (animated artwork, Listen Together, video playback, tablet layouts, other languages) should be removed, hidden or left as they are.

---

## 1. Goal (as given)

- Android music player.
- Source platform: **YouTube Music** and/or **YouTube**.
- **No ads, no trackers/telemetry.**
- Optional **sign-in with an official YouTube/Google account** to sync library and playlists.
- Inspiration: [vivizzz007/vivi-music](https://github.com/vivizzz007/vivi-music).

---

## 2. Evaluation of the reference app (vivi-music)

I cloned and reviewed the repo (README, Gradle setup, module layout).

| Area | What vivi-music does |
|---|---|
| Language / UI | Kotlin, Jetpack Compose, Material 3 / Material You (colours from album art) |
| Playback | AndroidX Media3 (ExoPlayer + MediaSession), background playback, notification controls, Android Auto |
| Data source | `innertube` module — talks to YouTube Music's **private InnerTube API** (the same API the official web/app uses). Also uses **NewPipe Extractor** for stream URLs |
| Account | Logs in via a WebView and reuses the Google session cookie to read/write library, likes, playlists, history |
| Storage | Room (local SQLite DB), all local — no cloud backend |
| DI / Network | Hilt, Ktor/OkHttp, Coil for images |
| Extras | Synced/word-by-word lyrics (multiple providers), equaliser, downloads/offline cache, SponsorBlock, animated "canvas" artwork, Last.fm scrobbling, Discord rich presence (`kizzy`), Shazam-style recognition, Spotify/JioSaavn importers, Listen Together, home-screen widget, in-app OTA updater |
| Min / target SDK | minSdk 26 (Android 8.0), targetSdk 37 |
| Licence | **GPL-3.0**, plus a proprietary `musixmatch` module that **may not be copied** into other projects |

Lineage: vivi-music is part of the InnerTune → OuterTune → Metrolist family of open-source YouTube Music clients. Those projects share most of the `innertube` code.

### Takeaways

1. It's a very large app. Copying its whole feature set into an MVP isn't realistic. We should choose a core subset (see §5).
2. **Licence:** if we copy or fork any vivi-music / Metrolist / InnerTune code, **myMusicPlayer must also be GPL-3.0** (open source if distributed). The Musixmatch module is off-limits either way.
3. The "ad-free" part isn't really ad *blocking*. The app fetches audio streams directly, so ads never get requested.

---

## 3. Important constraints and risks (please read)

### 3.1 No official API for playback
- The **official YouTube Data API v3** can read/write playlists, likes and subscriptions with OAuth. It **can't stream audio**, has no YouTube Music–specific endpoints (no Music library, no "Liked Music" song metadata, no radio/mixes) and has a daily quota.
- Every app in this category (vivi, Metrolist, ViMusic, NewPipe) uses the **unofficial InnerTube API** plus stream extraction. YouTube changes this regularly (signature/"PO token" changes, client blocks), so **ongoing maintenance is required**. Breakages every few weeks or months are normal.

### 3.2 Terms of Service
- Playing YouTube content without ads in a third-party client **breaches YouTube's Terms of Service**.
- Consequences:
  - The app **can't be published on the Google Play Store**. Distribution would be sideloaded APK / GitHub Releases / F-Droid-style.
  - Signing in with a Google account carries a **small but real risk of the account being flagged or restricted**. Some users of similar apps use a secondary account for this reason.
- This document doesn't give legal advice. You should be comfortable with this before we proceed.

### 3.3 "Official account link" vs "no tracking"
These two goals are in some tension:
- When signed in, YouTube still sees your requests and can record **watch/listen history** against your account. Our app wouldn't add any trackers of its own, but it can't stop Google seeing what you stream from Google.
- **[Proposed]** Provide toggles: *Send playback to YouTube history* (on/off), and *Use account only for library sync* versus *Use account for everything (recommendations too)*.

### 3.4 Sign-in method options
| Option | How it works | Pros | Cons |
|---|---|---|---|
| A. WebView cookie login (what vivi does) | User logs into Google in an embedded WebView; app stores session cookie | Full YT Music access: library, likes, history, personalised home | Unofficial; Google sometimes blocks WebView logins; cookie stored on device |
| B. Official OAuth + YouTube Data API v3 | Standard Google OAuth consent screen | "Official", lower account risk for sync | Needs Google Cloud project and OAuth client; app verification needed for >100 users; no YT Music-specific data; quota limits; can't drive playback |
| C. Hybrid | OAuth (B) for playlist sync; anonymous InnerTube for search and playback | Account is never used for the unofficial API | Loses personalised home, Music library, "Liked Music" fidelity |

### 3.5 Device-only, no backend
**[Proposed]** No server of our own, so there's nothing to host, pay for or leak. All data stays on the device (Room DB), with an optional manual backup/restore file.

---

## 4. Proposed technical stack [Proposed]

| Layer | Choice | Notes |
|---|---|---|
| Language | Kotlin | |
| UI | Jetpack Compose + Material 3 (dynamic colour) | |
| Playback | Media3 ExoPlayer + MediaSessionService | Background play, lock-screen and notification controls, Bluetooth, Android Auto-ready |
| YouTube access | InnerTube client (fork of the GPL `innertube` module **or** written from scratch) + NewPipe Extractor for stream deciphering | See Q2 |
| Local DB | Room | Library, playlists, history, cache index |
| DI | Hilt | |
| Networking | OkHttp / Ktor | |
| Images | Coil | |
| Build | Gradle (Kotlin DSL), version catalog | |
| CI | GitHub Actions: build + lint + unit tests, signed release APK | |
| minSdk | 26 (Android 8.0) | **[Q]** see Q9 |

**Zero third-party analytics or crash SDKs.** No Firebase, Crashlytics, Sentry, AdMob, etc. Crash logs stay local and can be exported manually.

---

## 5. Proposed feature list and phasing

Marked by you on 2026-10-27: **Yes** = build/keep now, **Later** = after the Yes items, **No** = not wanted. Phase ordering not yet confirmed (Q5).

### Phase 1 — MVP (usable daily player)
- **Yes** — Search (songs, albums, artists, playlists)
- **Yes** — Album, artist and playlist pages
- **Yes** — Streaming playback, ad-free
- **Yes** — Background playback + notification and lock-screen controls
- **Yes** — Queue: play next, add to queue, reorder, shuffle, repeat
- **Yes** — Local library: like songs, create/edit local playlists
- **Later** — Playback history (local)
- **Yes** — Audio quality setting (e.g. Low / Normal / High; Wi-Fi vs mobile data)
- **Later** — Settings screen; no telemetry anywhere

### Phase 2 — Account sync
- **Yes** — Sign in with YouTube/Google account (WebView login, D3)
- **Yes** — Import/sync: Liked songs, saved playlists, own playlists, subscribed artists, saved albums
- **Yes** — Two-way sync (D4)
- **Yes** — Personalised home feed (Quick picks, Mixes) if signed in
- **Yes** — History reporting toggle (see §3.3)

### Phase 3 — Comfort features
- **Yes** — Offline downloads + smart cache with size limit
- **Yes** — Lyrics: plain, line-synced and word-by-word (non-Musixmatch providers, see D7)
- **Later** — Sleep timer
- **Yes** — Radio / "start mix from this song" (autoplay similar tracks)
- **Yes** — Equaliser (system audio-effect based)
- **Yes** — SponsorBlock: skip non-music intros/outros in music videos
- **Yes** — Skip silence, audio normalisation (loudness)
- **Later** — Home-screen widget

### Phase 4 — Optional extras (from vivi-music; confirm if wanted)
- **Later** — Android Auto
- **Later** — Last.fm scrobbling
- **Yes** — Discord rich presence
- **Removed** — Import from Spotify (playlists) (D20)
- **Later** — Song recognition (Shazam-like)
- **No** — Animated "canvas" artwork
- **No** — Listen Together (shared sessions)
- **Later** — In-app updater (checks GitHub Releases)
- **Yes** — Backup / restore local data to a file
- **No** — Video playback mode (watch the music video, not just audio)
- **No** — Tablet / landscape layouts
- **No** — Localisation (multiple languages)

---

## 6. Proposed architecture (high level) [Proposed]

```
app/                    Android app (UI, ViewModels, navigation)
core/playback/          Media3 service, queue, audio focus, equaliser
core/data/              Room DB, repositories, sync engine
core/youtube/           InnerTube client, stream resolver, account session
core/lyrics/            Lyrics providers (Phase 3)
core/common/            Shared models and utilities
```

- MVVM + unidirectional data flow (StateFlow), Compose-only UI.
- Repositories merge **remote (YouTube)** and **local (Room)** sources so the app still works offline with the cached library.
- The YouTube layer is isolated behind interfaces. When YouTube breaks something, only `core/youtube` needs fixing.

---

## 7. Questions for you

Please answer inline (e.g. `A:` under each), or reply in chat.

### Project setup
- **Q1. Repository location.** This plan currently sits in `anythingDashboard/myMusicPlayer/`. Should myMusicPlayer:
  - (a) stay as a subfolder of this repo,
  - (b) move to a **new dedicated GitHub repo** (my recommendation, since an Android/Gradle project is unrelated to the Python dashboard), or
  - (c) something else?
- **Q2. Build approach.**
  - (a) **Fork** vivi-music or Metrolist and customise it. Fastest; inherits GPL-3.0 and a large codebase.
  - (b) **Build from scratch** but reuse their GPL `innertube` module. Cleaner and smaller; still GPL-3.0.
  - (c) **Fully from scratch** with no copied code. Licence is your choice, but it's much slower, especially the stream-deciphering part.
- **Q2b. Licence.** Are you happy for the project to be GPL-3.0 (required for options a/b)? Will it be public/open source or private?
- **Q2c. Audience.** Is this for **personal use only**, or do you plan to distribute it to others? This affects sign-in option B (Google verification) and how much polish and docs are needed.

### Source and account
- **Q3. Sign-in method:** A (WebView cookie), B (official OAuth), or C (hybrid)? See §3.4.
- **Q4. Sync direction:**
  - (a) one-way, YouTube → app only (read-only import), or
  - (b) two-way: liking a song or editing a playlist in the app also updates YouTube?
  - And should **local-only playlists** (never uploaded) also be supported?
- **Q4b. Source scope:** YouTube **Music** only, or also regular **YouTube** videos (podcasts, covers, live sets that aren't on YT Music)?
- **Q4c. Playback history:** should plays be reported back to your YouTube history (improves YT recommendations) or kept local only? Or should this be a toggle?
- **Q4d. Multiple accounts:** single account, or allow switching between several Google accounts or brand accounts?

### Features
- **Q5.** Go through §5 and mark each feature **Yes / No / Later**. Is the phase ordering right?
- **Q6. Offline downloads:** required? If yes, should downloaded files be playable outside the app (exported to device music storage) or kept private to the app cache?
- **Q7. Lyrics:** wanted? Synced (line-by-line) enough, or do you want word-by-word karaoke style?
- **Q8. "Skip ads and trackers"** — besides YouTube ads, did you also mean:
  - SponsorBlock-style skipping of non-music segments in videos?
  - Blocking YouTube's own tracking parameters/endpoints where possible?
  - Anything else you've seen in other apps that you want removed?

### Platform and design
- **Q9. Minimum Android version:** what's the oldest phone/Android version you need to support? (Proposed: Android 8.0 / API 26.)
- **Q10. Devices:** phone only, or also tablet, Android Auto, Wear OS, Android TV?
- **Q11. Visual style:** follow vivi-music's look (Material You, colours from album art), or do you have another design in mind? Dark mode only, or light and dark?
- **Q12. App name / package ID:** is "myMusicPlayer" the final display name? Proposed package: `com.<yourname>.mymusicplayer`. Which `<yourname>` should I use?

### Delivery
- **Q13. Distribution:** how will you install it — build locally, GitHub Releases APK, or F-Droid-style repo? Do you want an in-app updater?
- **Q14. Your environment:** do you have Android Studio and a physical Android device for testing? (I can build APKs in CI, but can't run them on a real phone.)
- **Q15. Timeline / priority:** is there a target date for the MVP, or is this an ongoing hobby project?
- **Q16. Risk acceptance:** do you accept the ToS / account-risk trade-off in §3.2? Would you prefer to use a secondary Google account for sign-in?

---

## 8. Next steps (once questions are answered)

1. Finalise feature scope and phases in this document.
2. Set up the repo (per Q1) with Gradle skeleton, CI build, lint and licence file.
3. Build Phase 1 MVP in small, reviewable PRs:
   1. Project skeleton + navigation + theme
   2. YouTube client: search + stream resolution
   3. Playback service + mini/full player + queue
   4. Local library (Room): likes, playlists, history
   5. Settings (quality, privacy toggles)
4. Then Phase 2 (account sync), and so on.
