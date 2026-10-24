"""aws/api_handler.py — Lambda Function URL backend for the dashboard.

Milestone M6 (PLAN.md section 5.3). Deployed as ``herdwatch-api`` on **arm64** with a
Function URL: free, and the same HTML/JSON contract as the local FastAPI dashboard, so
nothing in the UI changes between local and cloud.

Routes: ranked cows, per-cow score breakdown with feature contributions, evidence clip
retrieval, and ``POST /approve`` (``approve`` / ``reject`` / ``re-inspected``) which writes
the DynamoDB item. The approval endpoint is a first-class API, not a mock - it is the
human-in-the-loop action.

Access is a shared-secret query token (``dashboard.api_token_env``). HTTP-only with no
ALB/TLS is a deliberate free-tier choice, stated as a production gap in the report
(PLAN.md section 10.5).
"""

from __future__ import annotations

MILESTONE = "M6"


def handler(event, context):  # pragma: no cover - implemented in M6
    """AWS Lambda handler (Function URL)."""
    raise NotImplementedError(f"milestone {MILESTONE} - see PLAN.md section 5.3")


__all__ = ["handler"]
