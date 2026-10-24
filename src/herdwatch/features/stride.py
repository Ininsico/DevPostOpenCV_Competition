"""features/stride.py — stride length, stride-length variation and duty factor.

Milestone M2 (PLAN.md §5.1, required metric 2).

Algorithm:
    1. Lower band of the cow mask -> bottom envelope ``y_bot(s)``.
    2. Contact candidates = local minima with a prominence test and a minimum separation
       of ``features.stride.min_contact_separation_fraction`` body lengths.
    3. Limb association: near pair vs far pair by the vertical ordering rule (the near
       hoof projects lower for an elevated side-view camera) plus temporal continuity
       through the cycle.
    4. A landing event = a candidate whose dense Farneback flow in a small patch has
       ``|v_x|`` below the configured threshold while sitting at the envelope minimum,
       with hysteresis so contacts do not chatter.
    5. From the contact timeline:
         SL_norm     = |x_land(k) - x_land(k-1)| / L_px
         stride_time = t_k - t_(k-1)
         SL_CV       = sigma(SL_norm) / mu(SL_norm)      <- stride-length variation
         duty factor = from contact-timeline overlap
"""

from __future__ import annotations

__all__: list[str] = []
