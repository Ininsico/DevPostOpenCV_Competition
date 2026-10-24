"""dashboard/app.py — the FastAPI app serving the local dashboard.

Milestone M4 (PLAN.md section 5.3).

Server-rendered HTML plus ``fetch()`` JS, no build step, so ``tasks.py serve`` works with
nothing but the pinned Python dependencies:

    GET  /                      cows ranked by score, with status chips
                                (normal | watch | pending_approval | alerted | re_inspected)
    GET  /api/cows              the same data as JSON
    GET  /api/cows/{cow_key}    score breakdown with per-feature raw value, z, ramp,
                                weight and contribution
    GET  /evidence/{clip}       evidence clip playback
    POST /approve               approve | reject | re-inspected -> writes DynamoDB

Every request carries the shared-secret query token (``dashboard.api_token_env``); a
missing or wrong token is rejected. This is the human-in-the-loop surface, so it is the
one place where the token matters most.
"""

from __future__ import annotations

MILESTONE = "M4"


def create_app():  # pragma: no cover - implemented in M4
    """Build and return the FastAPI application."""
    raise NotImplementedError(f"milestone {MILESTONE} - see PLAN.md section 5.3")


__all__ = ["create_app"]
