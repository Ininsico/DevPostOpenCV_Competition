"""segmentation.py — foreground extraction, TRUCO contours and instance splitting.

Milestone M2 (PLAN.md §5.1).

Responsibilities:
    1. ``cv2.createBackgroundSubtractorMOG2`` (history/varThreshold from config.yaml);
       the shadow label (127) is discarded so it never reaches a silhouette.
    2. Morphological open then close with an elliptical kernel sized from image width;
       specks below the configured area fraction are dropped.
    3. ``cv2.findContours(RETR_EXTERNAL, CHAIN_APPROX_NONE)`` — the TRUCO path in
       OpenCV 5, which is exactly the hot spot the benchmark measures.
    4. Instance splitting for touching cows: distance transform -> local-maxima seeding ->
       ``cv2.connectedComponentsWithStats`` -> ``cv2.watershed``.

Ambiguity is a designed failure path, not an afterthought: when the peak configuration is
ambiguous the module sets ``multi_cow_overlap``, which later forces
``request_human_approval`` rather than an invented identity.

Note (PLAN.md §7.6): Haar and HOG detectors moved out of the main OpenCV 5 wheel, so there
is no learned detector here and a completely motionless cow cannot be segmented. The
locomotion gate catches that and reports ``insufficient_gait``.
"""

from __future__ import annotations

__all__: list[str] = []
