"""features/headbob.py — head/neck vertical oscillation amplitude.

Milestone M2 (PLAN.md §5.1).

Tracks the vertical oscillation of the head/neck band — the front
``features.headbob.head_band_fraction`` of body length — and normalises the amplitude by
``L_px``. Head-bob is a well-known lameness correlate and costs almost nothing once the
track and the body axis already exist.
"""

from __future__ import annotations

__all__: list[str] = []
