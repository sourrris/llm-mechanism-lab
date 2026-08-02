# Repository validation

Validated before delivery on 2026-08-03.

## Structural checks

- Clean Git repository on `main` with committed history.
- Python source, lab and CLI files compile.
- Shell scripts pass `bash -n`.
- Curriculum and progress JSON parse.
- GitHub issue forms parse as YAML.
- Dashboard JavaScript passes Node syntax checking.
- Dashboard HTML parses and CSS delimiters balance.
- All local Markdown links resolve.
- Dashboard assets return HTTP 200 when served locally.
- `git fsck --full` passes.

## Behavioural checks

- Day 2 cannot start before Day 1 is complete.
- A bad-day floor cannot be recorded for a future gate.
- Empty evidence templates count as zero evidence.
- CSV evidence starts with a valid schema and requires actual data rows.
- PNG evidence must have a real PNG signature.
- Clean-state CI validates zero completed days without pretending TODOs are finished.

## Exercise-test validation

The learner repository intentionally contains TODOs and therefore its future-day unit tests fail until implemented. To validate the tests themselves, a separate temporary reference implementation was created outside this repository and run against the full suite:

```text
31 passed
```

Coverage includes stable softmax, causal masking, cross-entropy, deterministic byte-level BPE, scaled attention, RMSNorm, SwiGLU, RoPE integration, multi-head attention, mini-GPT causality, AdamW, shifted next-token loss, joint gradient clipping, a complete train step, temperature/top-k/top-p filtering, generation and DPO loss.

The reference implementation is deliberately not included. The tests are the teacher; the first implementation remains yours.

## Validation environment

```text
Python 3.13.5
PyTorch 2.10.0+cpu
pytest 9.0.2
```

The supported learner target remains Python 3.11 or 3.12 because interpretability libraries can lag the newest Python release.
