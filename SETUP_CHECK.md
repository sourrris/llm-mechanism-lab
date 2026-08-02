# Setup verification

The repository is ready when all commands below succeed:

```bash
python3 -m json.tool curriculum/index.json >/dev/null
python3 -m json.tool progress.json >/dev/null
python3 -m compileall -q src scripts labs
bash -n scripts/bootstrap.sh scripts/publish_to_github.sh scripts/setup_github_issues.sh
python3 scripts/forge.py status
python3 scripts/forge.py ci
```

The starter implementation contains intentional `NotImplementedError` and TODO gates. Tests for an uncompleted day are expected to fail until you implement that day. CI validates only days recorded as completed in `progress.json`.

The dashboard reads `docs/progress.json`, which `forge.py` mirrors whenever progress changes. Run it through `make dashboard`, not by opening the HTML file directly.
