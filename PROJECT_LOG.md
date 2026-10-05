# THE RIZEN — Project Log

## 2026-10-04 — Adam's Pocket foundation

- Added the **Pocket Tools** wall without replacing the original eight content worlds.
- Added device-only Screen Light, rear-camera flashlight request, compass/level request, a countdown timer, floor-area/coverage calculator, dilution calculator, private device note, and personal Google Calendar launch links.
- Updated the installable PWA manifest for **THE RIZEN / Adam's Pocket** and refreshed the offline cache generation.
- The Pocket tool page follows the approved palette: deep purple, burnt orange, turquoise/green, cream, and black.
- No personal calendar, notes, contact information, credentials, product ratios, tracks, inventory, prices, or live channel details were added or invented.
- Notes remain in browser-local storage. Camera/motion access only occurs after a user presses the relevant tool.

## Hosting status

- GitHub Pages API reports no active Pages site as of this entry; GitHub Actions cannot create one with its current token permission (`Resource not accessible by integration`).
- A self-contained public fallback is maintained in `THE_RIZEN_LIVE.html` while GitHub Pages is fixed.

## 2026-10-04 — Nearby places and open-art redesign

- Added **Nearby & Favorite Spots** inside Adam's Pocket using official, user-triggered Google Maps URLs. It can request the visitor's device location only after pressing **Use my location**, then opens a Maps search near the current coordinates.
- Added a browser-local field for the owner's Google Maps saved-list share link. The static public site does not read Google Maps Saved places, Google account data, or location history.
- The Google Maps connector was inspected; it remains disabled. The implemented Maps URL approach requires no API key or connector and reveals no private credential in the site source.
- Replaced the muted generated mural shell with a restored, high-resolution copy of the owner-supplied ADAN UNFILTERED desktop art. The redesign makes the artwork visible behind the full application and removes the heavy boxed-card treatment in favor of open translucent content areas.
- Validated the Google Maps search handoff, browser-local favorite-list save/clear behavior, JavaScript syntax, and the self-contained public fallback. The active GitHub Pages address still returns 404 because a Pages site has not been created for the repository yet.

### Next launch step

- In GitHub **Settings → Pages**, choose **Deploy from a branch**, select **main** and **/(root)**, then save. This will activate the permanent `privateaz9898-tech.github.io/the-rizen-public-site` address directly from the published static site source.

## 2026-10-04 — Dark tactical command-center redesign

- Replaced the bright, playful mural treatment with original high-resolution dark tactical creator artwork: desert-night command station, chrome and weathered-metal materials, mature tactical shadows, and restrained purple/red signal color.
- The creator reference was preserved on the right-side workstation with a deep-purple tactical shirt, chrome eyewear, and subtle silver accents in hair and goatee.
- Artwork uses original masked-ranger, warlord, aerospace-sentinel, feline-warrior, and machine silhouettes—not branded or copied franchise characters, logos, or uniforms.
- Rethemed the public shell, home hero, Pocket command wall, buttons, navigation, and cache to use the darker asset without changing published tools, Maps handoff, music links, or private-on-device behavior.

## 2026-10-04 — Gold-frame command center and field tools

- Shifted text-heavy content into a thick antique-gold, tattoo-shop-style frame with a clean dark-suede interior; original dark artwork remains a surrounding background rather than an illustration behind operational text.
- Added a command rail visible at the top of every route: Phoenix time/date, live weather, wind speed and bearing, precipitation, surface pressure, sunrise, sunset, browser-only location option, and a clearly labeled fuel-search fallback.
- Added a browser-local tactical map console. Users can save a nickname plus address/place, choose an active marker, remove it, use temporary current location, and hand off to Google Maps. No custom spot is published or sent to THE RIZEN.
- Replaced the default editorial rap prompt with owner-stated West Coast / Bay Area, punk, and classic western Spotify search launch points. Added a persistent browser-local Spotify dock and an optional original Web Audio ambient synth; autoplay and unlicensed tracks are not used.
- Fuel-price rows are deliberately not fabricated. Live price ranking remains a setup item because no verified gas-price provider is connected.

## 2026-10-04 — Top CB radio listener

- Added a persistent **CB RADIO** control to the top command bar and a privacy-safe MyCB Radio listener panel with an official external launch button.
- Verified that `https://mycbradio.org/app/sdr` is a free SDR listening application with receiver, channel, and AM / LSB / USB controls, but it blocks embedding through `X-Frame-Options: DENY` and `frame-ancestors 'none'`. THE RIZEN therefore does not frame, proxy, scrape, or simulate its interface.
- Added local quick-reference cards for CH 19 (27.185 MHz AM), CH 9 (27.065 MHz AM), and CH 38 (27.385 MHz LSB). Copy buttons only copy references; they cannot tune or transmit.
- The panel states its receive-only boundary, opens the official provider in a new tab, requests no radio-related location, microphone, or account access, and is not presented as an emergency-service replacement.
