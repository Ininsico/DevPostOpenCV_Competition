"""fetch_dataset.py -- download the 50 labelled clips and write data/labels.csv.

Milestone M1 (PLAN.md section 5.4).

Dataset: fahimsohan/CattleLameness
    Data/Lame/L (1..25).mp4    25 clips
    Data/Normal/N (1..25).mp4  25 clips
    42 cows, indoor and outdoor, labelled by visual gait characteristics.

The dataset's README states the material is research/education only and that the source
videos must not be redistributed, so this script writes into data/clips/ (git-ignored) and
nothing here is ever committed. Attribution lives in NOTICE.

Labels are video-level, not per-stride and not clinical lameness scores -- that limit is
declared in docs/limitations.md rather than papered over.
"""

from __future__ import annotations

import sys

MILESTONE = "M1"


def main() -> int:
    print(
        f"fetch_dataset.py: not implemented yet (milestone {MILESTONE}) - see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
