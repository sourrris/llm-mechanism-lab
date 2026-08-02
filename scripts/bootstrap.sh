#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "Python 3 is required." >&2
  exit 1
fi

if [[ ! -d .venv ]]; then
  "$PYTHON_BIN" -m venv .venv
fi

.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -e '.[dev]'

echo
echo "Core environment ready."
echo "Activate: source .venv/bin/activate"
echo "Begin:    make today"
echo
echo "Install interpretability tools on Day 9 with:"
echo "  .venv/bin/python -m pip install -e '.[interpretability]'"
