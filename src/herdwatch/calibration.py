"""calibration.py — pixel -> body-length normalisation and body-axis estimation.

Milestone M2 (PLAN.md §5.1).

Responsibilities:
    * ``cv2.PCACompute2`` on each cow mask for the body axis: every measurement is taken
      along the animal, not along image-x, so a cow crossing the frame at an angle is
      measured consistently.
    * Body length ``L_px`` = mask extent along that axis (withers height is a secondary
      scale). Everything downstream is normalised by ``L_px``, which is what makes
      stride length, arch ratio and head-bob amplitude camera-distance invariant.
"""

from __future__ import annotations

__all__: list[str] = []
