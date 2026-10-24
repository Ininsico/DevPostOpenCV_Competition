"""aws/worker.py — the Lambda entrypoint that runs the OpenCV 5 pipeline.

Milestone M6 (PLAN.md section 5.3). Deployed as ``herdwatch-worker`` on **arm64** = real
AWS Graviton (Neoverse-N1), always-free.

Flow: SQS batch -> download the clip from S3 -> segmentation -> features -> score ->
DynamoDB first-pass item -> when ``score >= score.escalate_threshold`` invoke
``herdwatch-agent``. Batch failures go to the DLQ rather than being dropped.

The identical code runs locally through the local adapters, which is what makes
``tasks.py demo`` a real end-to-end run instead of a mock.
"""

from __future__ import annotations

MILESTONE = "M6"


def handler(event, context):  # pragma: no cover - implemented in M6
    """AWS Lambda handler (SQS trigger)."""
    raise NotImplementedError(f"milestone {MILESTONE} - see PLAN.md section 5.3")


__all__ = ["handler"]
