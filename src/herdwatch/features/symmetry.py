"""features/symmetry.py — gait symmetry as a vector, not one opaque number.

Milestone M2 (PLAN.md §5.1, required metric 3).

    S_time = 2 * |T_near - T_far| / (T_near + T_far)

and the same construction for ``SL_norm`` and duty factor, giving a symmetry *vector*.

Declared limitation (PLAN.md §7.5): anatomical left/right requires a known camera side, so
by default this module measures the **near/far limb pair**. The ``camera_side`` config key
relabels them as left/right when the barn geometry is known.
"""

from __future__ import annotations

__all__: list[str] = []
