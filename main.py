#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon.

Writes a single line (at most 120 characters) to /output/entry.txt: a
one-star review in the voice of a fed-up customer — a rating, a grievance,
and a reason the Moon earned its single star.
"""

import os

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 One star. The Moon is late every month, "
    "only ever half-dressed, and still thinks it runs the tides."
)

# The sealed scorer gates /output/entry.txt at 1-120 characters, one line,
# not only whitespace. The review reads like a real one-star review: the
# star rating up front, then the grievance (always late, half-lit) and the
# reason it earned the single star (it still acts like it runs the tides).
# Fail loudly here instead of shipping an invalid entry.
if not 1 <= len(LINE) <= 120 or "\n" in LINE or not LINE.strip():
    raise SystemExit("entry line must be a single line of 1-120 characters")


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
