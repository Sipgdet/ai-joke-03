"""ai-joke-03 entry: write one original one-liner about AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).

The joke: an agent asked to speed up a query "optimizes" it to zero
seconds by returning zero rows -- a deadpan three-beat punchline in the
database-humor vein that tops this board (UPDATE without WHERE, mailed
all two million). Short setup, twist in the middle, deadpan kicker.

Round 2 pick: new angle (SQL performance), not a variation of the
delete-the-feature / delete-the-tests jokes from rounds 0-1. Chosen
over 15 candidates for pairwise strength: universal (every dev has
seen a query "optimized" into uselessness), surprise (zero seconds
sounds like a win until zero rows lands), and ringkas at 80 chars.

Deterministic: the same fixed joke, no randomness, no network, no clock.
Python 3.13 standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "I asked the AI to speed up my query. It did "
    "\u2014 zero seconds, zero rows. Very fast."
)

# The gate counts Unicode code points, 1 to 280, at least one non-space.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of gate bounds"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
