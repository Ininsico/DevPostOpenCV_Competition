"""evidence.py — annotated overlays and evidence clips.

Milestone M2 (PLAN.md §5.1).

Draws, on the original frames:
    * the cow mask outline and the fitted spine + chord with deviation shading, so a judge
      can *see* the measurement rather than trust a number;
    * hoof landing markers and the contact-timeline strip;
    * the score-breakdown panel;
    * a banner with ``cow_key``, window and score — and no farm-identifying text.

Text uses OpenCV 5's new ``cv2.FontFace("sans")`` + the new ``putText`` overload for crisp
labels (the legacy ``FONT_HERSHEY_*`` path still works and is the fallback). Clips are
written with ``cv2.VideoWriter`` (``avc1`` -> ``mp4v``), never ffmpeg.
"""

from __future__ import annotations

__all__: list[str] = []
