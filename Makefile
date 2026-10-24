# Thin wrapper for Linux/CI where `make` exists.
# The real task runner is tasks.py (make is absent on the dev machine, so it can
# never be the primary entry point).

PY ?= uv run python

.DEFAULT_GOAL := help
.PHONY: help sync lock lint format test test-contract fetch-data synthetic analyze agent demo eval bench package diagrams verify-all clean

help:
	@$(PY) tasks.py --help

sync:
	uv sync --all-extras

lock:
	$(PY) tasks.py lock

lint:
	$(PY) tasks.py lint

format:
	$(PY) tasks.py format

test:
	$(PY) tasks.py test

test-contract:
	$(PY) tasks.py test-contract

fetch-data:
	$(PY) tasks.py fetch-data

synthetic:
	$(PY) tasks.py synthetic

analyze:
	$(PY) tasks.py analyze --clip "$(CLIP)"

agent:
	$(PY) tasks.py agent

demo:
	$(PY) tasks.py demo

eval:
	$(PY) tasks.py eval

bench:
	$(PY) tasks.py bench

package:
	$(PY) tasks.py package

diagrams:
	$(PY) tasks.py diagrams

verify-all:
	$(PY) tasks.py verify-all

clean:
	$(PY) tasks.py clean
