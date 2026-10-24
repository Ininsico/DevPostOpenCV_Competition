"""video_io.py — decode/encode wrappers with the OpenCV 5 property semantics.

Milestone M2 (PLAN.md §5.1 step 1).

Responsibilities:
    * ``cv2.VideoCapture`` / ``cv2.VideoWriter`` wrappers.
    * OpenCV 5 changed ``VideoCapture.get()`` to return ``-1`` for unsupported properties
      (it returned ``0`` in 4.x), so every property read must check
      ``< video.unsupported_property_floor`` from config.yaml and fall back explicitly.
    * The container is written with ``avc1`` and falls back to ``mp4v``; the machine has
      no ffmpeg, so ``cv2.VideoWriter`` is the only encoder available.
"""

from __future__ import annotations

__all__: list[str] = []
