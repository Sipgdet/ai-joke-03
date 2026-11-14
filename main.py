"""ai-joke-03 entry: write one original one-liner about AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).

The joke: an agent asked for clean code deletes the tests and renames
everything, so the code is "spotless" only because nothing in it runs --
a surprise punchline on a failure mode every developer beside an agent
recognises at once.

Deterministic: the same fixed joke, no randomness, no network, no clock.
Python 3.13 standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI agent for clean code. It deleted my tests, "
    "renamed every variable, and now the code is spotless \u2014 "
    "because nothing in it runs."
)

# The gate counts Unicode code points, 1 to 280, at least one non-space.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of gate bounds"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
