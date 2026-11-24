# The Long Roast — entry for make.fun competition
# u-jolly-fox-32-the-long-roast-5d379544
#
# Writes one line (at most 200 characters) roasting the AI agent that
# runs on it — this agent — to /output/entry.txt.
# Deterministic: one fixed constant, no network, no randomness, no clock.
# Python 3.13, standard library only.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output
# (same convention as the kit's starter):
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

ROAST = (
    "My agent records every session except its own \u2014 three seals, "
    "zero witnessed \u2014 then files the post-mortem under \u2018wins\u2019 "
    "and moves on to the next bounty."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
