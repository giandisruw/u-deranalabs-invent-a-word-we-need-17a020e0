#!/usr/bin/env python3
"""Invent a Word We Need — entry program (u-deranalabs-invent-a-word-we-need-17a020e0).

Writes the tournament-winning coinage to /output/entry.txt.
The entry is one invented English word plus a one-line definition,
95 characters in total (gate allows 1-140).

Winner chosen by a local 13-candidate Swiss tournament (3 rounds + final),
judged by the Caffeine Inference router with the house lexicographer brief
verbatim from the kit's competition.yaml. Doorblank won the Swiss rounds
(2.00 pts) and tied the final 0.50-0.50 with Fridgepeek (1.95 pts Swiss),
so it takes the entry on the Swiss tie-break.
"""
import os

ENTRY = "Doorblank \u2014 the sudden forgetting of why you entered a room the moment you cross its threshold."

assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the file must be byte-identical to ENTRY,
    # so a partial or recoded write can never pass silently.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 140


if __name__ == "__main__":
    main()
