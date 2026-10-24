"""agent/policy.py — the deterministic decision kernel.

Milestone M3 (PLAN.md §5.2, §3.2). This module owns the guarantees.

Budgets and guardrails, all from config.yaml:
    max_tool_calls=12          breach -> budget_exceeded -> human review
    max_second_pass=1          per cow
    max_wall_s=120
    identical (tool, args) twice  -> abort with ``no_progress``
    hysteresis band 0.50-0.60  -> "watch", stops alert flapping

The escalation predicate: ``escalate_alert`` is **unreachable** unless a confirming second
pass agrees AND confidence >= ``confidence.min_for_auto_alert``. A bad planner decision
therefore cannot bypass the human-in-the-loop gate — that property is unit-tested, not
asserted in prose.

This kernel is a table of rules. There is no model in here, by design (reproducibility,
zero per-inference cost, auditable orchestration).
"""

from __future__ import annotations

__all__: list[str] = []
