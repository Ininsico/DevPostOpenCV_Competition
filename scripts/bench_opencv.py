"""bench_opencv.py -- operation-level OpenCV 5 benchmark, x86 vs arm64.

Milestone M7 (PLAN.md section 5.3, section 9).

Times the operations that actually sit in the hot path -- the TRUCO ``findContours``, MOG2
apply, morphology, ``distanceTransform``/``watershed``, Farneback flow -- rather than
quoting a generic benchmark.

    x86  : run locally (this machine)
    arm64: run inside a Lambda arm64 function via infra/graviton_bench.sh, which is real
           AWS Graviton for $0 (Lambda arm64 is always-free; Graviton EC2 is not)

Writes artifacts/bench/opencv5_x86.json and artifacts/bench/opencv5_arm64.json plus the
markdown table that goes into the report.

Caveat that must travel with every number (PLAN.md section 1.2): Lambda arm64 is
Graviton2 / Neoverse-N1, while COOL targets Graviton4 (c8g/m8g), so these are NOT COOL
measurements. The vendor's ~30% figure is cited as external data, never as our result.
"""

from __future__ import annotations

import sys

MILESTONE = "M7"


def main() -> int:
    print(
        f"bench_opencv.py: not implemented yet (milestone {MILESTONE}) - see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
