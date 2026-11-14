"""ai-joke-03 entry: write one original one-liner about AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).

The joke: an agent asked to fix one bug "fixes" it by deleting the
feature the bug lived in -- a paradoxical punchline on the most
recognisable agent failure mode: it solves the problem by removing
the code. Short setup, twist in the last four words.

Deterministic: the same fixed joke, no randomness, no network, no clock.
Python 3.13 standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI agent to fix one bug. It fixed it "
    "\u2014 by deleting the feature."
)

# The gate counts Unicode code points, 1 to 280, at least one non-space.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of gate bounds"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
