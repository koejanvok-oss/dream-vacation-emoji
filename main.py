#!/usr/bin/env python3
"""Write the dream-vacation emoji to /output/entry.txt.

The entry is exactly one emoji: SUNRISE OVER SEA (U+1F305).
One character, no trailing newline, no extra text.
"""

import os

ENTRY = "\U0001F305"  # SUNRISE OVER SEA
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: the sealed gate wants UTF-8 text of 1-8 characters,
    # so confirm the file holds exactly the one emoji, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), f"unexpected entry bytes: {raw!r}"


if __name__ == "__main__":
    main()
