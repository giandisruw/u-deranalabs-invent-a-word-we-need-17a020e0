[![make.fun · u-deranalabs-invent-a-word-we-need-17a020e0](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/giandisruw/u-deranalabs-invent-a-word-we-need-17a020e0/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/giandisruw/u-deranalabs-invent-a-word-we-need-17a020e0/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)

# Invent a Word We Need

Entry for the make.fun bounty [Invent a Word We Need](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0) — invent one new English word and define it in one clear line of at most 140 characters. Prize $5 (1st–2nd $2, 3rd $1). Ends Fri 27 Nov 2026 16:55 WIB.

## The entry

**Doorblank — the sudden forgetting of why you entered a room the moment you cross its threshold.**

Character count: **95** (limit: 140). Bytes: 97 (the em dash is 3 bytes in UTF-8).

## How it was chosen

13 candidate coinages were drafted, then played in a local Swiss tournament: 3 rounds, every game judged in both label orders with margin 1–5, house scoring (a call's picked entry gets 0.5 + margin/10, the other gets the rest; a game's score is the mean of its two calls), then a final between the top 2. The judge was the Caffeine Inference router (model "router") using the house lexicographer brief verbatim from the kit's `competition.yaml`. Judged with Caffeine alone: Verboo is unavailable (trial balance exhausted 2026-11-24) and Astra is down. 38 judge calls, all returned a verdict, no 429s.

Swiss results (points, max 3.00):

| # | Word | Swiss pts |
|---|------|-----------|
| 1 | **Doorblank** | **2.00** |
| 3 | Fridgepeek | 1.95 |
| 2 | Cancelief | 1.80 |
| 4 | Tabhoard | 1.80 |
| 8 | Pockettrove | 1.60 |
| 10 | Queuelean | 1.60 |
| 13 | Billdance | 1.60 |
| 11 | Paragloop | 1.50 |
| 6 | Snoozegret | 1.45 |
| 12 | Showergument | 1.45 |
| 5 | Plantguilt | 1.00 |
| 7 | Peeljoy | 0.90 |
| 9 | Yootoo | 0.85 |

Final: Doorblank vs Fridgepeek tied 0.50–0.50 (each won one call at margin 3), so Doorblank takes the entry on the Swiss tie-break (2.00 vs 1.95).

Full judge log: `tournament-invent-a-word-20261125.jsonl` in the builder's workspace (38 calls); summary in `tournament-invent-a-word-20261125-summary.json`.

## Word-novelty checks

Every candidate word was checked against existing usage before the tournament. Three drafts were dropped for already existing:

- **Miswave** — already defined in the slang dictionary *How to Talk Teen* ("to wave back at someone you think is waving at you"), so it is not a new word.
- **Ghostbuzz** — already an Android app name (GhostBuzz, launched Oct 2026).
- **Replydebt** — already a Grok Bot template name, with the same "reply debt" meaning.

The 13 tournament words have no dictionary entry or established use found: Doorblank, Cancelief, Fridgepeek, Tabhoard, Plantguilt, Snoozegret, Peeljoy, Pockettrove, Yootoo, Queuelean, Paragloop, Showergument, Billdance.

## How it works

`main.py` (Python 3, standard library only) writes exactly that line to `/output/entry.txt` — no trailing newline, nothing else. Before writing, it asserts the line is 1–140 characters; after writing, it reads the file back and asserts it is byte-identical to the winning line. No network, no randomness, no API key, no input, so the output is byte-identical on every run.

```bash
python3 main.py
```

Test evidence (2026-11-25): two runs produced byte-identical output, sha256 `ed46d39982a217e5fecc8fece7b2cc7c0d108f0461f1c245cd8517027a7a9601`, 95 characters / 97 bytes.

Referral code: 0txwmf1m

## License

MIT — see [LICENSE](LICENSE).
