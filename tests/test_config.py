"""config.yaml is the single source of truth (PLAN.md section 6).

These tests pin the constants that the report quotes verbatim. If a number here has to
change, it changes in config.yaml first and the report follows - never the other way
around, and never in the middle of an evaluation run.
"""

from __future__ import annotations

import pytest

from herdwatch import config


def test_escalate_threshold_is_frozen_at_060(cfg):
    assert cfg.score.escalate_threshold == 0.60


def test_watch_band_sits_below_the_escalate_threshold(cfg):
    low, high = cfg.score.watch_band
    assert low < high <= cfg.score.escalate_threshold


def test_agent_budgets_match_the_plan(cfg):
    assert cfg.agent.max_tool_calls == 12
    assert cfg.agent.max_second_pass == 1
    assert cfg.agent.max_wall_s == 120


def test_second_pass_toolbar_matches_the_competition_requirement(cfg):
    assert cfg.second_pass.window_s == 5
    assert cfg.second_pass.fps_mult == 3
    assert cfg.second_pass.scale == 2


def test_gait_gate_matches_the_plan(cfg):
    assert cfg.gait.min_cycles == 2
    assert cfg.gait.min_displacement_bl == 1.5


def test_confidence_floor_matches_the_plan(cfg):
    assert cfg.confidence.min_for_auto_alert == 0.50


def test_every_confidence_gate_has_a_floor(cfg):
    floors = cfg.confidence.floors
    assert set(floors) == {
        "segmentation",
        "visibility",
        "gait_observability",
        "identity_continuity",
    }
    assert all(0.0 < value <= 1.0 for value in floors.values())


def test_lambda_is_arm64_and_inside_the_free_tier(cfg):
    assert cfg.aws.lambda_architecture == "arm64"
    assert cfg.aws.lambda_memory_mb == 3008
    assert cfg.aws.lambda_timeout_s == 300


def test_video_is_headless_and_matches_the_pinned_opencv(cfg):
    # OpenCV 5 returns -1 for unsupported VideoCapture properties, so the floor that
    # separates "unsupported" from a real value must stay at 0.
    assert cfg.video.unsupported_property_floor == 0


def test_the_four_scored_features_are_all_present_and_weighted(cfg):
    features = cfg.score.features
    assert set(features) == {"arch_ratio", "sl_cv", "s_time", "headbob"}
    for name, spec in features.items():
        assert spec.weight > 0, f"{name} has no weight"
        low, high = spec.ramp
        assert low < high, f"{name} has an inverted ramp"


def test_planner_defaults_to_the_rule_planner_with_no_paid_api(cfg):
    assert cfg.agent.planner == "rule"


def test_config_is_read_only_and_reports_unknown_keys(cfg):
    with pytest.raises(AttributeError):
        cfg.score.escalate_threshold = 0.9
    with pytest.raises(AttributeError):
        _ = cfg.score.not_a_real_key


def test_ensure_dirs_creates_every_configured_path(cfg, repo_root):
    created = config.ensure_dirs()
    assert created, "no paths configured"
    for directory in created:
        assert directory.is_dir()
    assert repo_root in created[0].parents
