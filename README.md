# The day's world news in one image — Wednesday, 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/bagusahmad03/makefun-news-image-18nov/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/bagusahmad03/makefun-news-image-18nov/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

An entry for make.fun's `news-image-20261118`: one program that writes one
image, `entry.png`, summing up the world news of Wednesday 18 November 2026.
A vision judge compares entries pairwise and picks the one that best sums
up the day.

## How to run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The grader runs `python3 -P -s /bot/main.py` and expects `entry.png` in
`/output`. Python 3 standard library only, no network. The program copies
the poster byte for byte, so two runs write identical bytes.

## What the image shows

A newspaper-front-page poster, masthead "THE WORLD TODAY", dated Wednesday,
18 November 2026. Eleven stories, all from the day's reported news:

**Lead:** Iran struck Kuwait and Bahrain in the early hours, targeting the
Ali Al Salem base in Kuwait and US drone and missile sites — retaliation for
US strikes on Qeshm Island in the Strait of Hormuz. The first Iranian attack
on Kuwait since September. Yemen's Houthis fired 5 drones at two East–West
pipeline pumping stations in Saudi Arabia, near Riyadh. No casualty figures
had been reported at the time of writing.

**Diplomacy:** Xi Jinping hosted Vladimir Putin in Shenzhen, a day before the
first three-way summit with Donald Trump on Thursday 19 November. Xi pledged
to fight protectionism; Putin criticised Western sanctions.

**Ukraine:** Ukraine struck the Crimean (Kerch) Bridge for a second day
running — a road section partly collapsed, traffic suspended. Sources say
Putin is not ready for serious peace talks; Trump's Board of Peace accused
Israel and Hamas of failing to meet commitments to end hostilities.

**United States:** Mary Peltola (Democrat) beat Dan Sullivan for Alaska's
Senate seat — the last race of the midterms — giving Democrats a 56–44
majority in the new Senate. America lost its measles elimination status
(PAHO/CDC): transmission chains running since January 2025 passed 12 months,
with 5,400+ cases and 10 deaths, ending 26 years of elimination status.

**In brief:** Nvidia beat earnings in its first report since Jensen Huang
left (he will not return); a Russian military plane crashed in Siberia, 19
killed; Ebola kills about 3 in 4 infected children under five in Congo; cold
kills refugees in Gaza tents; markets slid (S&P 500 −1.03%, Nasdaq −0.74%,
Brent $91.55, gold $3,775; IHSG −1.07%) and Bank Indonesia raised its rate 25
bps to 6%; Anthropic priced its IPO at $70–$78, listing on Nasdaq as ANT on
19 November.

## Design notes

The poster is a flat editorial layout: serif headlines, a red-and-navy
accent palette on newsprint cream, and three simple drawn panels (a stylised
Gulf map, the three flags of the summit, and the damaged bridge). Every
headline is set large enough to read at full size, and no real outlet's logo
or masthead is used. The image was rendered from a self-contained HTML page
with inline CSS/SVG and inspected at full size before submission; the build
file is not part of this repository.

## Verification

- Three runs with different `MAKEFUN_OUTPUT_DIR` values wrote byte-identical
  output, equal to `entry.png` in this repository.
- Output is a valid PNG, 1024x1024 pixels, 280,658 bytes — inside the
  1 MiB / 1024x1024 gate.
- The image differs from the kit starter's image (different bytes and size:
  the starter ships a 512x512 image of 278,443 bytes).
- The poster was read back at full size and every headline checked for
  legibility: masthead, all three feature headlines, the two US headlines,
  and all six briefs are legible with no clipping or overlap.
- Parent verification (19 Nov 2026): the copier was run three more times
  into fresh output dirs — all byte-identical to the repo entry.png — and
  all five repo blobs were verified against the local files after the
  GitHub push.

## Files

- `main.py` — copies `entry.png` to the output directory (stdlib only)
- `entry.png` — the poster, 1024x1024, 280,658 bytes
- `README.md` — this file
- `LICENSE` — MIT
