"""make_synthetic.py -- procedural gait clips with KNOWN ground-truth parameters.

Milestone M1 (PLAN.md section 5.4).

Renders cows with parameterized stride length, near/far asymmetry, back arch and head-bob
amplitude, so the recovery error of every measurement can be reported as MAE / MAPE / R^2
against the true parameter. This is the evidence that the OpenCV numbers are *correct*,
not merely discriminative -- the part most submissions will not have.

Output goes to data/synthetic/ (git-ignored).
"""

from __future__ import annotations

import sys

MILESTONE = "M1"


def main() -> int:
    print(
        f"make_synthetic.py: not implemented yet (milestone {MILESTONE}) - see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
