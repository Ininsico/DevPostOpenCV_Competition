"""aws/agent_handler.py — the Lambda entrypoint for the agentic loop.

Milestone M6 (PLAN.md section 5.3). Deployed as ``herdwatch-agent`` on **arm64**.

Invoked by the worker when a first-pass score crosses the threshold. Runs the same
``herdwatch.agent.orchestrator`` loop as the CLI, so the trace written to
``artifacts/traces/`` locally and the trace emitted in the cloud are the same artifact.
The ``trace_id`` is propagated into the DynamoDB items and the SNS message.
"""

from __future__ import annotations

MILESTONE = "M6"


def handler(event, context):  # pragma: no cover - implemented in M6
    """AWS Lambda handler (invoked by herdwatch-worker)."""
    raise NotImplementedError(f"milestone {MILESTONE} - see PLAN.md section 5.3")


__all__ = ["handler"]
