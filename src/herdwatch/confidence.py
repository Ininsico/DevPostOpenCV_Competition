"""confidence.py — gating and reason codes: the module that makes failure handling real.

Milestone M2 (PLAN.md §5.1, §5.4).

Four separate 0-1 confidences, each with a configurable floor:

    segmentation        mask stability / area coefficient of variation
    visibility          mean local contrast + illumination level (night-time IR collapses)
    gait_observability  >= gait.min_cycles stride cycles, net displacement
                        >= gait.min_displacement_bl body lengths, both limb pairs seen
    identity_continuity track not fragmented or swapped

Any confidence below its floor emits a reason code — ``insufficient_gait``,
``low_visibility``, ``multi_cow_overlap``, ``occlusion`` — and the segment goes to human
review instead of an alert. Reason codes are part of the JSONL trace and the dashboard.
"""

from __future__ import annotations

__all__: list[str] = []
