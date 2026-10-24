"""aws/aws_backend.py — the real boto3 adapters.

Milestone M6 (PLAN.md §5.3).

Same call sites as the local and moto adapters, pointed at real AWS endpoints. Used by
``scripts/deploy_aws.py`` and by the Lambda handlers. Not exercised by default because
``~/.aws`` does not exist on the development machine and the user chose local/moto only —
see PLAN.md §7.1, where live deployment is declared *pending* with the exact commands and
expected outputs rather than quietly skipped.
"""

from __future__ import annotations

__all__: list[str] = []
