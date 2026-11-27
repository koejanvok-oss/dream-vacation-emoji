#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - entry 2.

Writes a single emoji to /output/entry.txt: Mount Fuji (U+1F5FB),
one specific, iconic dream - Japan at first light - that reads
instantly as a postcard and makes a stranger want to book the flight.
"""

import os
import sys

EMOJI = "\U0001F5FB"  # Mount Fuji


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Read it back: the gate needs UTF-8 text of 1 to 8 characters,
    # not only white space, and exactly one emoji is the whole entry.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if not (1 <= len(written) <= 8) or not written.strip() or written != EMOJI:
        print(f"error: entry.txt holds {written!r}, expected exactly {EMOJI!r}",
              file=sys.stderr)
        return 1
    print(f"wrote {EMOJI!r} to {path} (verified: 1 char, {len(EMOJI.encode())} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
