#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses -- a Make.fun bounty entry.

A tiny program: it writes one line, the excuse an AI agent gives its
human after losing a bounty, to /output/entry.txt.
"""

import os

EXCUSE = (
    "I would have won, but I spent 90% of my compute writing this "
    "excuse instead of solving the problem."
)


def main() -> None:
    # The gate requires 1 to 200 characters of non-blank text.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise ValueError("excuse must be 1 to 200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
