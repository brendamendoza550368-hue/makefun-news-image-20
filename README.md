# The World Today — Friday 20 November 2026

Entry for make.fun's `news-image-20261120`: one image that sums up the
world news of Friday 20 November 2026, drawn as a vintage newspaper
front page with five panels.

## The stories shown

- **Shenzhen (centre):** Presidents Trump, Xi and Putin held their first
  three-way summit and signed a joint peace declaration at the APEC
  gathering in Shenzhen.
- **The Hague (left):** The International Court of Justice ruled that
  Myanmar committed genocide against the Rohingya — the court's first
  such finding against a state.
- **Markets (right):** A global sell-off deepened (a fifth straight down
  day for US stocks, sharp falls in Asia) while Anthropic's Nasdaq debut
  soared above its IPO price, the first pure AI listing.
- **Riyadh (bottom left):** A Houthi missile strike damaged the Public
  Investment Fund tower in Riyadh's financial district.
- **Launch night (bottom right):** Grand Theft Auto VI went on sale
  worldwide after 13 years, topping $2.3 billion in launch sales.

## How it runs

`main.py` (Python 3.13, standard library only) verifies the shipped
`entry.png` — PNG signature plus a recorded SHA-256 — and writes it
unchanged to `/output/entry.png`. No network, no randomness: every run
delivers the same bytes. The image is 1024 × 1024 and 705,323 bytes.
