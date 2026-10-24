# HerdWatch — Dairy Cow Lameness Risk Alert System

**OpenCV AI Competition 2026** · submitted on the **Agentic Vision** path + **Overall**

> **Status: M0 (bootstrap).** Repository structure, tooling, config and CI are in place.
> The analysis pipeline, agent loop, AWS stack and evaluation are built in milestones
> **M1–M8** — see [`PLAN.md`](PLAN.md) for the full plan and `docs/rubric_map.md` for the
> criterion → artifact mapping.

HerdWatch turns ordinary barn/IP-camera video into an **explainable lameness-risk alert per
cow**. OpenCV 5 does all of the perceptual work with classical, auditable geometry
(background subtraction + instance splitting, a robust spine fit on the back line, hoof-landing
events from the bottom envelope plus optical flow, stride/symmetry/head-bob measurements, all
normalized by body length so they are camera-distance invariant). Those measurements feed a
documented weighted-ramp score — *no black-box classifier*. A score above threshold **causally**
fires a re-inspection at higher frame rate; the second pass either confirms an alert
(DynamoDB ticket + SNS to the farm manager, with an evidence clip), resolves as normal, or
requests human approval. The AWS side is a real, deployable, always-free pipeline
(S3 → SQS → **arm64 Lambda** = Graviton → DynamoDB → SNS → Function URL dashboard), with
local adapters so the whole thing runs end-to-end today with no account and no spend.

**Target users:** farm managers and herd-health staff. **This is a triage aid, never a
diagnosis** — a human confirms before any intervention. See `docs/responsible_use.md`.

---

## Quickstart

Requires [`uv`](https://docs.astral.sh/uv/). Python **3.12** is pinned deliberately
(`requires-python = "==3.12.*"`) — it matches the Lambda runtime and avoids uncertain
wheel coverage on newer interpreters.

```powershell
uv python install 3.12
uv sync --all-extras            # creates .venv with opencv-python-headless 5.0.0.93

uv run python -c "import cv2; print(cv2.__version__)"   # -> 5.0.0
uv run python tasks.py test                             # green
```

Everything else goes through the Python task runner (`make` is not available on the dev
machine; the `Makefile` and `tasks.ps1` are thin wrappers over `tasks.py`):

```powershell
uv run python tasks.py --help
```

| Task | Command | Milestone |
|---|---|---|
| Lint + format check | `tasks.py lint` | M0 |
| Unit tests | `tasks.py test` | M0 |
| Fetch the 50 labelled clips (git-ignored) | `tasks.py fetch-data` | M1 |
| Build the known-ground-truth synthetic set | `tasks.py synthetic` | M1 |
| Analyze one clip end-to-end | `tasks.py analyze --clip "L (1).mp4"` | M2 |
| Agent run + counterfactual replay | `tasks.py agent` | M3 |
| Local pipeline + dashboard | `tasks.py demo` | M4 |
| Evaluation tables (P/R/F1, ablations, baselines) | `tasks.py eval` | M5 |
| `moto` AWS contract test | `tasks.py test-contract` | M6 |
| Build the arm64 Lambda layer | `tasks.py package` | M6 |
| x86 vs Lambda-arm64 OpenCV bench | `tasks.py bench` | M7 |
| Diagrams (matplotlib PNGs from the Mermaid sources) | `tasks.py diagrams` | M8 |
| Everything | `tasks.py verify-all` | M8 |

---

## Repository layout

```
.
├─ PLAN.md                      # the full build plan + session handoff document
├─ README.md                    # this file — quickstart and the judges' entry point
├─ LICENSE  NOTICE              # Apache-2.0 code; dataset attribution + no-redistribution
├─ pyproject.toml               # pinned deps, ruff + pytest config
├─ tasks.py                     # THE task runner (works without make)
├─ Makefile  tasks.ps1          # thin wrappers for CI/Linux and Windows
├─ src/herdwatch/               # the package
│  ├─ config.yaml               # SINGLE source of truth: every threshold, weight, gate
│  ├─ video_io.py  calibration.py  segmentation.py  tracking.py  identity.py
│  ├─ confidence.py             # visibility/occlusion/locomotion gating + reason codes
│  ├─ features/                 # backline · stride · symmetry · headbob
│  ├─ scoring.py                # weighted-ramp transfer fn -> score + contribution table
│  ├─ segment_analysis.py       # one analysis pass (first or second, parameterized)
│  ├─ evidence.py               # annotated overlay + evidence clip export
│  ├─ cli.py                    # herdwatch analyze|batch|agent|bench|serve
│  ├─ agent/                    # tools · policy · planner · orchestrator · trace
│  ├─ aws/                      # models · adapters · local_backend · aws_backend · handlers
│  └─ dashboard/                # FastAPI app + static/
├─ infra/                       # CloudFormation + the in-Lambda Graviton bench
├─ scripts/                     # data, packaging, deploy, eval, bench, diagrams
├─ tests/                       # unit, golden score, agent-policy, contract tests
├─ docs/                        # report, diagrams, traces, evaluation, limitations
├─ frontend/                    # React + Vite UI (dev server / static build)
├─ reports/                     # machine-readable eval output (committed)
├─ data/                        # git-ignored: clips/ synthetic/ labels.csv
└─ artifacts/                   # git-ignored: traces/ evidence/ outbox/ bench/
```

`data/` and `artifacts/` are created on demand by `herdwatch.config.ensure_dirs()`; their
contents are never committed. Raw and evidence video dwarfs what git should carry, and the
labelled dataset is **fetched at setup, never redistributed** (see `NOTICE`).

---

## Key documents

| Document | What it covers |
|---|---|
| `PLAN.md` | The authoritative build plan, verified environment facts and locked decisions |
| `docs/rubric_map.md` | Every judging criterion → the artifact that satisfies it → the command that produces it |
| `docs/architecture.mmd` | System / data-flow diagram (`docs/architecture.png` rendered in M8) |
| `docs/agent_workflow.mmd` | Agent state machine, including the unbypassable approval gate |
| `docs/report.md` | The technical report |
| `docs/limitations.md` | Declared limits and failure cases |
| `docs/responsible_use.md` | Welfare, privacy and non-diagnostic framing |
| `docs/aws_deployment.md` | Deploy / destroy runbook |
| `docs/cool_benchmark.md` | COOL runbook + the Graviton-generation caveat |
| `docs/demo_video_script.md` | Timed ≤5-minute demo script |

## Zero-cost operation

Live AWS deployment is **off by default** (`~/.aws` does not exist on the dev machine).
The full CloudFormation stack and a pure-`boto3` deploy script are built and validated
against a `moto` fake-AWS server, so the code path issues real boto3 calls against a real
API surface. Adding credentials makes it live with one command. Every AWS choice sits inside
always-free limits — Graviton is delivered as **Lambda `arm64`**, not EC2.

## License

Code is Apache-2.0 (`LICENSE`). The video dataset is third-party research/education material
and is **not** redistributed — attribution and terms are in `NOTICE`.
