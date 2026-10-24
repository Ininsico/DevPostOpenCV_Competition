"""Feature extractors — one module per required measurement.

Every extractor returns a value already normalised by body length (``L_px`` from
calibration.py), so the numbers are camera-distance invariant and comparable across clips
and cameras.

    backline   back-line curvature / arch ratio        (required metric 1)
    stride     stride length, variation, duty factor   (required metric 2)
    symmetry   near/far timing and duty asymmetry      (required metric 3)
    headbob    head/neck vertical oscillation amplitude (extra evidence)
"""

from __future__ import annotations

__all__ = ["backline", "headbob", "stride", "symmetry"]
