"""agent/trace.py — the JSONL trace writer and its human-readable renderer.

Milestone M3 (PLAN.md §5.2).

Every step is appended as one JSON object per line with ``trace_id``, monotonic
timestamps, the tool name, its arguments, a result summary and ``decision_reason`` — the
field that makes the loop auditable. ``agent.trace_format = jsonl``.

Traces land in ``artifacts/traces/`` (git-ignored); the curated pair that proves the causal
claim is rendered into ``docs/trace_example.md`` and ``docs/trace_counterfactual.md``.

The renderer turns a trace into the markdown table used in the report, so the document and
the machine artifact cannot drift apart.
"""

from __future__ import annotations

__all__: list[str] = []
