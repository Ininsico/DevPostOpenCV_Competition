"""agent/tools.py — the validated tool registry.

Milestone M3 (PLAN.md §5.2).

Six tools, each with a JSON schema, strict argument validation and a declared cost:

    analyze_segment          run one analysis pass over a segment window
    inspect_more_frames      re-extract +/- second_pass.window_s at fps_mult and scale
    escalate_alert           ticket + evidence clip + DynamoDB + SNS
    request_human_approval   queue for a human; never auto-alerts
    close_no_action          resolve as normal
    record_observation       append a note to the trace

Argument validation happens *before* dispatch, so an invalid call is a recorded
``no_progress`` observation rather than an exception in the middle of the loop.
"""

from __future__ import annotations

__all__: list[str] = []
