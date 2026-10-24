"""aws/models.py — DynamoDB item shapes and the alert-ticket schema.

Milestone M6 (PLAN.md §5.3).

Single table ``herdwatch``:
    PK  cow_key
    SK  ts#kind
    GSI1  status   (normal | watch | pending_approval | alerted | re_inspected)
    GSI2  score    (dashboard ranking)

Every item carries the ``trace_id`` of the agent run that produced it, so an alert in the
dashboard can be traced back to the exact decision line that created it. Item shapes are
plain dicts with a validating constructor — no ORM, nothing that can silently drift from
the CloudFormation table definition.
"""

from __future__ import annotations

__all__: list[str] = []
