#!/usr/bin/env python3
"""make.fun entry: One Sentence for a Traveler from 1800.

Writes one sentence explaining the modern internet to a time traveler
from 1800, using only words that existed in their time.
Pure standard library; no third-party packages, no network.
"""

import os

PART_A = "Picture a road joining every post office, press, and library on earth, "
PART_B = "carrying letters that reach their reader before the ink is dry."
SENTENCE = PART_A + PART_B
assert SENTENCE == "Picture a road joining every post office, press, and library on earth, carrying letters that reach their reader before the ink is dry."
assert 1 <= len(SENTENCE) <= 200


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
