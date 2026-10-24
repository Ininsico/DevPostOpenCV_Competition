"""tracking.py — per-segment identity by centroid + IoU association.

Milestone M2 (PLAN.md §5.1).

Responsibilities:
    * Associate detections across frames with an IoU gate plus centroid distance.
    * ``cv2.KalmanFilter`` (constant velocity on centre and size) so a dropped
      segmentation frame does not break the track or the stride timeline.
    * Emit the per-cow ``cow_key``. Without an ear-tag/RFID gallery this is a
      *track-scoped* identity — stated as a limitation in docs/limitations.md, not hidden.
"""

from __future__ import annotations

__all__: list[str] = []
