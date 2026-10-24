"""build_lambda_package.py -- build the aarch64 OpenCV layer from an x86 Windows box.

Milestone M6 (PLAN.md section 5.3).

    pip download --platform manylinux_2_28_aarch64 --python-version 3.12 --only-binary=:all:
        opencv-python-headless==5.0.0.93 numpy

then strip the shared objects and print the measured unzipped size against Lambda's
250 MB limit. If it ever exceeds the limit the script fails loudly and names the
container-image fallback rather than shipping something that cannot deploy.

Building the arm64 layer from x86 is the trick that makes the Graviton path verifiable
without owning an Arm machine.
"""

from __future__ import annotations

import sys

MILESTONE = "M6"


def main() -> int:
    print(
        f"build_lambda_package.py: not implemented yet (milestone {MILESTONE}) - "
        f"see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
