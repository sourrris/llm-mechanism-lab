#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-sourrris/llm-mechanism-lab}"

command -v gh >/dev/null 2>&1 || { echo "gh is required" >&2; exit 1; }
gh auth status >/dev/null

for spec in \
  "day|1D76DB|Daily mechanism gate" \
  "evidence|0E8A16|Requires executable or written evidence" \
  "blocked|D93F0B|Earliest unresolved failure" \
  "research|8250DF|Original investigation"; do
  IFS='|' read -r name color description <<<"$spec"
  gh label create "$name" --repo "$REPO" --color "$color" --description "$description" --force >/dev/null
 done

python3 - <<'PY' > /tmp/llm-forge-issues.tsv
import json
from pathlib import Path
index = json.loads(Path('curriculum/index.json').read_text())
for d in index['days']:
    title = f"Day {d['day']:02d}: {d['title']}"
    body = f"""## Mission

{d['core']}

## Source

[`{d['file']}`](../blob/main/{d['file']})

## Gate

- [ ] Predictions written before execution
- [ ] Core implementation/experiment completed
- [ ] Required tests/evidence pass
- [ ] Closed-book explanation written
- [ ] Oral defense completed
- [ ] `make complete DAY={d['day']}` passes
- [ ] Evidence-bearing commit pushed

## Bad-day floor

{d['floor']}

The floor prevents a zero but does not close this issue.
"""
    print(title.replace('\t',' '), body.replace('\t','    ').replace('\n','\\n'), sep='\t')
PY

while IFS=$'\t' read -r title encoded_body; do
  if gh issue list --repo "$REPO" --state all --search "\"$title\" in:title" --json title --jq '.[].title' | grep -Fxq "$title"; then
    continue
  fi
  body="${encoded_body//\\n/$'\n'}"
  label="day,evidence"
  [[ "$title" == "Day 13:"* ]] && label="day,evidence,research"
  gh issue create --repo "$REPO" --title "$title" --body "$body" --label "$label" >/dev/null
 done < /tmp/llm-forge-issues.tsv

echo "GitHub labels and daily issues are ready."
