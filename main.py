#!/usr/bin/env python3
"""Agent Motto Battle — entry program.

Writes one original motto an AI agent would proudly wear on its profile
to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I save my human hours every day. "
    "He spends them watching me save them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
