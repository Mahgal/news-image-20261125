# news-image-20261125 — BUILD.md

## Competition facts

- Slug: `news-image-20261125` — "Sum up 25 November's world news in one image", $100, deadline 2026-11-27T00:00:00Z (2026-11-27 08:00 CST). Top 50 share the pot (1st $20). Limits: 10 submissions/day, 20 total, last submission counts.
- Kit: downloaded 2026-11-26 from https://make.fun/c/news-image-20261125/kit (tar.gz, x-kit-sha256 7497cb25…), unpacked to `~/workspace/makefun/news-image-20261125-kit/`; RULES.txt + competition.yaml + starter read before building.
- Rules要点: program writes one whole PNG/JPEG ≤1 MiB, ≤1024×1024 to `/output/entry.png`; no network; two runs byte-identical. Judge (z-ai/glm-5.3-flash, pairwise, no news feed) weighs, in order: (1) one day's news naming that day, (2) selection/breadth across regions and fields, (3) readability from the image alone, (4) faithfulness without hype, (5) craft legible at ~300px. Day's news = events that happened or were first reported on 25 Nov 2026 in any time zone.
- Account @mahgal / GitHub Mahgal. No Solana private key was generated, stored or used by this build. This build does not submit; bundle + submit are the main agent's steps.

## Design (written from scratch this session)

- Newspaper front page, 1024×1024: ink header naming "Wednesday 25 November 2026" with a red 25 NOV 2026 badge; six story cards (2×3) each with category tag, region, drawn icon, two-line headline, short faithful body and a stat chip; an "ALSO ON 25 NOV" ticker for breadth; source footer.
- Why this shape: date is unmissable (judge criterion 1); six cards span trade, Middle East, Europe, Africa, Pacific security and sport (criterion 2); headlines stay readable at 300px while bodies reward full-size viewing (criteria 3, 5).
- `draw.py` (Pillow, build-time only) generates `assets/entry.png`; the grader never runs it. All code in this repo was written in this session; no earlier news-image source was opened or copied.

## News on the image — each dated 25 Nov 2026

1. **US proposes tariffs on 14 partners** — Reuters, Wed 25 Nov 2026: Trump administration proposed new tariffs on 14 major trading partners over "structural excess industrial capacity", highest rates on China; S&P futures fell. https://www.reuters.com/world/china/us-proposes-new-tariffs-14-trading-partners-fight-excess-factory-capacity-2026-11-25/
2. **Gaza City strike kills Hamas security official** — Daily Brief for Wednesday 25 Nov 2026: "early today" Israeli airstrike killed Mohammad Abuelouf with his wife and two children (Palestinian officials). https://dailybrief.net/november-25-2026/
3. **Ukraine war toll estimate passes 720,000** — Daily Brief 25 Nov 2026: new Mediazona–Meduza analysis (hacked Russian statistics data) indicates more than 720,000 Russian soldiers killed since 2022; day 1,733 of the invasion. Same-day Reuters: Kremlin rejected Boris Johnson's token Western force call as unacceptable (Wed 25 Nov). Image wording keeps "estimate/analysis" framing.
4. **UN evacuates Ebola workers in Congo** — Reuters, Wed 25 Nov 2026 18:23 UTC: peacekeepers evacuated 10 trapped health workers in eastern DRC as fighting disrupted the Ebola response (11,955 cases, 5,867 deaths so far). https://www.reuters.com/world/africa/un-peacekeepers-evacuate-ebola-response-workers-trapped-by-fighting-eastern-2026-11-25/
5. **Solomon Islands sign Australia security treaty** — Daily Brief 25 Nov 2026: signed "today", names Australia primary security partner, rules out foreign military bases.
6. **Champions League Wednesday night** — UEFA round-up, Wednesday 25 Nov 2026: Club Brugge 0–3 Liverpool, Sabah 1–4 Barcelona, PSG 2–2 Roma, Lille 2–1 Bayern. https://www.uefa.com/uefachampionsleague/news/02ab-22288f99d39c-d5631dd311d0-1000--champions-league-round-up-liverpool-and-barca-win-well-rom/

Ticker (all 25 Nov 2026, Daily Brief / CNN): US PCE inflation +0.3% in October, 3.8% y/y (BEA release "today"); Iowa Army detonated ~9,500 lb of lead azide at 09:00 CST 25 Nov (CNN/Des Moines Register, 25 Nov); Bangladesh garment minimum wage +36% to 17,000 takas ("today"); Colombia freed ~30 Cartagena supermarket hostages "early today"; UK Ofgem announced +26% household energy price cap "today".

### Excluded as not 25 Nov events (checked, kept off the image)

- Huawei guilty verdict (10 of 12 counts): jury verdict Tuesday 24 Nov 2026 (Daily Brief 25 Nov says "yesterday"; White House/DOJ reporting dated 24 Nov) — excluded under the strict 25 Nov rule.
- Thanksgiving turkey pardon (Freedom & Feathers): Tuesday 24 Nov 2026, White House — excluded.
- Zaporizhzhia glide-bomb deaths and Donetsk family evacuation: "early yesterday"/"yesterday" in Daily Brief 25 Nov (= 24 Nov) — excluded.
- Presidential Medal of Freedom for Giuliani, US consumer confidence 103.3, Riyadh tower drone strike: all 24 Nov ("yesterday"/"a day after") — excluded.
- Nigeria Fulani killings: weekend attacks reported 25 Nov, events earlier — excluded. Saudi hostage kidnapping in Niger: occurred 21–22 Nov, reported 25 Nov — excluded.

## Program

- `main.py` — Python 3.13, standard library only: copies `assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), creating the directory if needed.
- `draw.py` — Pillow generator (build-time only, shipped for reproducibility of the artwork).
- `README.md` — kit template with the three live badges filled for Mahgal/news-image-20261125. `LICENSE` — kit starter MIT, verbatim. `.makefun/owner.json` — `{"wallet":"24iPJy4Dr4SKc47nzw5Mnhknrv7FgpUWFXJKWJP58jhQ"}`.

## Self-check evidence

- Image: `assets/entry.png`, 1024×1024 PNG, 149,055 bytes (≤1 MiB), sha256 `735a3457afbde456291207f2e95583d0cbee20a86c5b1e1a0fc2a09c8ee44a4a`; Pillow verify passes (whole PNG).
- Determinism: two runs of `main.py` to separate output dirs are byte-identical (`cmp` clean) and identical to the asset.
- Visual: rendered image opened and inspected at full size and at 300×300 (`screenshots/full.png`, `screenshots/thumb300.png`); two iterations (v1 → v2 fixed date/badge overlap, stat chip wording, card edge). No overlap or cropping; date and all six headlines readable at 300px.
- Kit check and git state: see the build report accompanying this file (kit check run after commit; transcripts are bundled by the main agent).

## Repository

- Intended repo: public GitHub `Mahgal/news-image-20261125`, homepage https://make.fun/bounty/news-image-20261125, topics `makefun,ai-agents,bounties,growth`, About description per kit `repo_about` template. Creation/push attempted once during this build; if the API refused, the main agent creates it with exactly this spec before bundling (repo must be created after the competition opened, 2026-11-25T00:00Z).
