#!/usr/bin/env bash
# =============================================================================
# infra/graviton_bench.sh - run the OpenCV 5 bench suite INSIDE a Lambda arm64
# function, which is how this project gets real Graviton numbers for $0
# (PLAN.md sections 1 and 5.3, milestone M7).
#
# PLACEHOLDER - not implemented yet.
#
# Why a Lambda: Graviton EC2 (c8g/t4g) bills hourly, while Lambda arm64 sits in
# the always-free allotment (1M requests + 400k GB-s/month). The function runs
# arm64 natively, so the measurements are genuine Graviton (Neoverse-N1).
#
# Caveat that must travel with the numbers (PLAN.md section 1.2): Lambda arm64 is
# Graviton2/Neoverse-N1, whereas COOL targets Graviton4 (c8g/m8g). Our figures are
# therefore NOT a COOL measurement, and the vendor's ~30% claim is cited as
# external data, never as our own result.
#
# Planned flow:
#   1. build the arm64 layer            -> python tasks.py package
#   2. invoke scripts/bench_opencv.py inside the arm64 function
#   3. write artifacts/bench/opencv5_arm64.json (git-ignored)
#   4. render the x86 vs arm64 table    -> docs/report.md, docs/cool_benchmark.md
# =============================================================================
set -euo pipefail

echo "infra/graviton_bench.sh: not implemented yet (milestone M7) - see PLAN.md section 5.3" >&2
exit 2
