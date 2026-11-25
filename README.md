[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/giandisruw/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/giandisruw/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

# One-Line Laugh-Off

One line, 85 characters (gate: 1–200), a single joke that lands on a cold read:

> I asked the mirror who's the fairest; it showed me my search history and went silent.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 85 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written, deliberately avoiding the clichés the judge brief penalises (recycled setups, generic feelings, sayings the reader has met before). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — genuinely funny first, then how hard and suddenly the line lands, the surprise of its turn, economy of words, and freshness. Swiss format, 3 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 21 games in the Swiss + 1 final game = 22 games, 44 judge calls in total. No Verboo fallback was needed — Caffeine answered every call; all 10 calls in the resumed run returned a verdict (0 no-verdict calls).

Note on the run: the first tournament run was killed (SIGTERM) mid-round-3 after 18 games, before its per-call log was persisted — only the 18 game scores survived in its stdout log. The tournament was resumed from those recorded scores: the 4 remaining round-3 games and the final were played fresh, and the full game table below is reconstructed from both runs. Per-call verdicts are recorded in `tournament.jsonl` for the resumed games only.

Tournament table (Swiss score out of 3 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#12** | Asked the mirror who's fairest; it showed my search history and went silent | **2.35** |
| #8 | Told my GPS I wanted adventure; it took me to my ex's street | 2.05 |
| #2 | Told my smart fridge I'm on a diet; it filed a restraining order | 1.80 |
| #4 | Asked AI to write my will; it left everything to the cloud | 1.80 |
| #7 | Cat walked across my keyboard and got promoted | 1.60 |
| #10 | Meal prep containers now a thriving ecosystem with its own government | 1.55 |
| #11 | Wi-Fi went down, so I finally met my family — they're nice, apparently | 1.50 |
| #14 | Named my vacuum Roomba; it left for a dustier house with better suction | 1.50 |
| #1 | Therapist said face my fears; I opened my bank app and screamed | 1.45 |
| #13 | Smartwatch congratulated me for standing up — the bar is on the floor | 1.20 |
| #3 | Plastic plants filed for emotional support too | 1.20 |
| #5 | Password so strong even I can't log in | 1.20 |
| #6 | Treadmill now holds my laundry and judges me in silence | 1.15 |
| #9 | Screen time report should come with a therapist and a small violin | 0.65 |

Final: #12 led the Swiss at 2.35, #8 was second at 2.05, and #12 won the final 0.80–0.20 — the judge preferred #12's two-beat structure (a fairy-tale setup the reader knows, then a modern, self-incriminating twist) over #8's GPS-to-the-ex turn, which it read as a more familiar setup. #12 also scores on every brief criterion at once: it is a real joke with a sharp turn, it lands suddenly on a cold read, it spends all 85 characters without padding, and it is fresh — a mirror that judges you by your browser history, not a recycled setup.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
