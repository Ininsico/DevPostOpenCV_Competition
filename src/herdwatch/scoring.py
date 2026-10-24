"""scoring.py — the explainable score. No black box, by design.

Milestone M2 (PLAN.md §5.1).

    for each feature j:
        z_j = (x_j - mu_j) / sigma_j      # mu_j, sigma_j from the FROZEN normal-clip split
        a_j = ramp(z_j; lo_j, hi_j)       # piecewise-linear 0 -> 1 abnormality, saturating
    score = sum(w_j * a_j) / sum(w_j)     # 0..1

Every ``w_j``, ``lo_j`` and ``hi_j`` comes from config.yaml with its source comment. Per
cow-segment the module emits raw values, z, ramp output, weight, contribution and the
total, so the CLI can print the worked example:

    Cow #12 - score 0.73 (arch_ratio 0.081*w, SL_CV 0.34, S_time 0.19, headbob 0.06)
    vs threshold 0.60 -> inspect_more_frames

``mu``/``sigma`` are loaded from ``data/calibration.json`` (frozen before evaluation) so
the reported metrics are leak-free and reproducible. Golden tests pin the arithmetic.
"""

from __future__ import annotations

__all__: list[str] = []
