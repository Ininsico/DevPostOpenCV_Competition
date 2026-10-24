"""agent/orchestrator.py — the loop, and the causal proof it produces.

Milestone M3 (PLAN.md §5.2).

Runs perceive -> decide -> act over a clip, propagating ``trace_id`` into the DynamoDB
items and the SNS message so a trace line can be joined to a stored ticket.

The artifact this exists to produce: ``herdwatch agent run`` on a triggering clip yields a
trace where step 1's first-pass score ``0.73 >= 0.60`` is the *recorded* reason step 2 is
``inspect_more_frames``, whose result ``0.68 >= 0.60`` is the recorded reason step 3 is
``escalate_alert``. Then ``herdwatch agent replay --force-first-score 0.42`` on the *same*
clip produces ``close_no_action`` — same code, same video, only the OpenCV-derived score
differs. Both traces ship in docs/.
"""

from __future__ import annotations

__all__: list[str] = []
