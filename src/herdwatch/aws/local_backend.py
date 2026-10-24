"""aws/local_backend.py — filesystem + SQLite + ``artifacts/outbox/`` adapters.

Milestone M6 (PLAN.md §5.3). The default ``aws.adapter = local``.

Alerts that would go to SNS are rendered into ``artifacts/outbox/`` instead, and
DynamoDB items land in a local SQLite file — so the entire pipeline (ingest -> worker ->
score -> agent -> alert -> dashboard -> approve) demonstrably runs on a laptop with no
account, no credentials and no spend. This is what ``tasks.py demo`` exercises.
"""

from __future__ import annotations

__all__: list[str] = []
