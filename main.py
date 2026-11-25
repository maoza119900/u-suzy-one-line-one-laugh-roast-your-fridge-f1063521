#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single fixed roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Deterministic: no clock, no randomness, no network, no file reads.
The line is a compile-time constant, so every run produces byte-identical
output.
"""

import os
import sys

LINE = (
    "My fridge is so dedicated to freshness that it froze my leftovers "
    "into archaeology \u2014 future scientists will carbon-date my lasagna."
)


def main() -> int:
    # Gate self-check: entry must be 1-200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print(f"entry line fails gate: {len(LINE)} chars", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
