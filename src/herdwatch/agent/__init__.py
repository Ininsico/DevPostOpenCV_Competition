"""The agentic closed loop — our own planner, no paid LLM anywhere.

PLAN.md §5.2. The interesting property of this package is that the perception output
*causally* drives the action, and that the human-in-the-loop gate cannot be bypassed even
by a misbehaving planner.

    tools         six tools, each with a JSON schema, arg validation and a declared cost
    policy        the deterministic decision kernel: thresholds, hysteresis, confirmation
    planner       our utility/rule planner (+ an off-by-default local-LLM hook)
    orchestrator  the loop; trace_id propagation
    trace         JSONL trace writer + human-readable renderer
"""

from __future__ import annotations

__all__ = ["orchestrator", "planner", "policy", "tools", "trace"]
