"""run_eval.py -- the evaluation harness.

Milestone M5 (PLAN.md section 5.4). Writes reports/eval_results.json and
docs/eval_results.md.

Produces:
    1. The 50-clip labelled set driven through the ACTUAL agent policy: confusion matrix,
       precision, recall, F1, accuracy, a 0.30-0.90 threshold sweep and ROC/AUC.
       Metrics are implemented with numpy -- no sklearn -- so the math is inspectable and
       the dependency surface stays tight.
    2. Ablations: drop each feature in turn and re-run, proving which geometric
       measurements carry the signal.
    3. Baselines: motion-energy-only (no geometry) and single-feature scoring, to quantify
       what the extra measurements buy.
    4. Measurement accuracy on the synthetic set with known ground truth: MAE / MAPE / R^2
       per feature.
    5. Three or more documented failure cases with frame grabs and reason codes:
       occlusion, night-time low contrast, and multi-cow overlap.

mu/sigma come from the frozen calibration split (data/calibration.json), never from the
evaluation clips, so the reported numbers are leak-free.
"""

from __future__ import annotations

import sys

MILESTONE = "M5"


def main() -> int:
    print(
        f"run_eval.py: not implemented yet (milestone {MILESTONE}) - see PLAN.md section 8",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
