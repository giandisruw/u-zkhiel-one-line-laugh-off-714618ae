#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Deterministic and self-contained:
stdlib only, no network calls, no web search, no randomness, no
environment secrets. The line was picked by a local pairwise tournament
of 14 original candidates, judged with the bounty's published judge
brief (see README.md).
"""

import os

LINE = "I asked the mirror who's the fairest; it showed me my search history and went silent."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
