"""features/backline.py — back-line curvature and arch ratio.

Milestone M2 (PLAN.md §5.1, required metric 1).

Algorithm:
    1. Take the cow mask's upper boundary ordered along the body axis: ``y_top(s)`` for
       ``s`` in ``[0, 1]``.
    2. Fit a polynomial of order ``features.backline.fit_order`` with iterative
       reweighted least squares and Huber weights. The robust fit is what suppresses the
       head/neck discontinuity and single-frame segmentation noise.
    3. Report, per frame and as a time median:
         arch_ratio = max_s |spine(s) - chord(s)| / chord_length
         spine_curvature_k = |y''| / (1 + y'^2)^(3/2) at mid-back
       ``s`` is normalised by the chord length, so ``k`` is dimensionless and
       scale-invariant.

The fitted spine, the withers->hips chord and the deviation shading go into the evidence
overlay.
"""

from __future__ import annotations

__all__: list[str] = []
