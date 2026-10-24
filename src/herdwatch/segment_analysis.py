"""segment_analysis.py — one analysis pass over one cow segment.

Milestone M2 (PLAN.md §5.1).

Parameterised so the *same* code runs the first pass and the second pass triggered by
``inspect_more_frames``: the only difference is the sampling parameters
(``second_pass.window_s`` / ``fps_mult`` / ``scale`` from config.yaml). That is what makes
the closed loop genuinely closed — the second pass is not a different code path.

Returns a per-cow-segment record: measurements, confidences, reason codes, score and the
full contribution table, which scoring.py and the agent kernel both consume.
"""

from __future__ import annotations

__all__: list[str] = []
