#!/usr/bin/env bash
set -euo pipefail

OWNER="${GITHUB_OWNER:-sourrris}"
REPO="${1:-llm-mechanism-lab}"
VISIBILITY="${2:-private}"
DESCRIPTION="A proof-driven 14-day forge for building, diagnosing and causally interpreting language models."

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is missing. Install it, then run: gh auth login" >&2
  exit 1
fi

gh auth status >/dev/null

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Run this script from the repository root." >&2
  exit 1
fi

if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  echo "$OWNER/$REPO already exists."
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$OWNER/$REPO.git"
  fi
  git push -u origin main
else
  case "$VISIBILITY" in
    public|private) ;;
    *) echo "Visibility must be public or private." >&2; exit 1 ;;
  esac
  gh repo create "$OWNER/$REPO" "--$VISIBILITY" --source=. --remote=origin --push --description "$DESCRIPTION"
fi

"$(dirname "$0")/setup_github_issues.sh" "$OWNER/$REPO"

echo "Published: https://github.com/$OWNER/$REPO"
