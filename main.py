#!/usr/bin/env python3
"""make.fun entry: "The GPS Swears It Was a Shortcut".

Writes one line -- the GPS's own excuse, in its own voice, for sending
the driver down the wrong road -- to /output/entry.txt.

Chosen line (after comparing 3 candidates against the judge criteria):
  - Candidate A (chosen): lake + shortcut that "hasn't been invented yet",
    blames the map outright. Strongest twist, most arrogant/defensive GPS
    voice, freshest specific detail.
  - Candidate B (rejected): "turn left at the wedding" -- funny, but the
    GPS sounds sheepish rather than caught-and-defensive.
  - Candidate C (rejected): "cul-de-sac on the 2019 map" -- good, but the
    punchline lands softer and the voice is more passive than arrogant.
"""

import os

LINE = (
    "I didn't drive you into a lake, I took a shortcut that simply hasn't "
    "been invented yet \u2014 blame the map, it lied to me first."
)


def main() -> None:
    # Gate guard: exactly one line, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip() and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
