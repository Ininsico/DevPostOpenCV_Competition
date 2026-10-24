"""identity.py — optional ORB/BFMatcher gallery re-identification.

Off by default (PLAN.md §10.7). Wired in M4; not on the evaluation critical path.

Responsibilities:
    * Build an ORB descriptor gallery from confirmed cow crops and match a new track
      against it, so the same animal can be recognised across clips.
    * When the gallery is empty or a match is ambiguous, fall back to the track-scoped
      ``cow_key`` from tracking.py rather than guessing.
"""

from __future__ import annotations

__all__: list[str] = []
