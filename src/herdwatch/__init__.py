"""HerdWatch — dairy cow lameness risk alerts from barn video.

OpenCV 5 does the perceptual work with classical, auditable geometry; a documented
weighted-ramp scoring function turns the measurements into one gait abnormality score
per cow per segment (no black-box classifier); a self-built planner decides whether to
re-inspect, alert, close or escalate to a human.

See PLAN.md for the full build plan and every locked decision.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
