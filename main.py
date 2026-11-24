#!/usr/bin/env python3
"""Ship It Friday — one-line git commit message from an AI coding agent
moments before it breaks production on a Friday.

Writes the entry line to /output/entry.txt.
"""

import os

ENTRY = (
    "feat: Friday deploy \u2014 rewrote the whole payment service from "
    "scratch, tests pass on my machine, merging before anyone can stop me"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
