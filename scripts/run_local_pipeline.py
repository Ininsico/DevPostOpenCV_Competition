"""run_local_pipeline.py -- the whole cloud pipeline, offline, on one clip.

Milestone M4 (PLAN.md section 5.3). This is what ``python tasks.py demo`` runs.

S3 upload -> SQS -> worker (OpenCV 5 pipeline) -> DynamoDB first-pass score -> agent
(re-inspection when the score crosses the threshold) -> alert + evidence clip -> outbox ->
dashboard read and approve, all through the ``local`` adapters (filesystem + SQLite +
artifacts/outbox/).

The point is that this is not a mock: it is the same orchestrator and the same adapters
that run in the cloud, with the storage and notification backends swapped. It needs no AWS
account and costs nothing, which is what makes the end-to-end claim checkable today.
"""

from __future__ import annotations

import sys

MILESTONE = "M4"


def main() -> int:
    print(
        f"run_local_pipeline.py: not implemented yet (milestone {MILESTONE}) - "
        f"see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
