# Day 06: Make the model learn

**Date:** 2026-08-08  
**Mission:** Understand how prediction error becomes weight change and prove the full training path by overfitting one batch.  
**Source:** Primary backbone: Stanford CS336 optimization and training material.

## Definition of done

Day 06 tests pass; one batch is overfit; training-curve.csv exists; bug-autopsy.md traces a deliberately introduced failure to its earliest cause.

## Timebox

| Block | Time | Output |
|---|---:|---|
| Closed-book retrieval + predictions | 25 min | `predictions.md` before any experiment |
| Learn only what blocks the build | 35 min | equations and shapes in your own words |
| Build | 90 min | working implementation or experiment |
| Break + measure | 45 min | controlled ablations and results |
| Explain + oral defense | 25 min | mechanism note and adversarial answers |

Take a ten-minute break between long blocks. Stop adding resources once the next executable step is known.

## You must understand

- Backpropagation applies the chain rule through the exact computational graph used in the forward pass.
- A gradient is local sensitivity, not a direct instruction about the globally best parameter value.
- Adam tracks first and second moments; bias correction matters early in training.
- AdamW decouples parameter shrinkage from the adaptive gradient update.
- Overfitting one tiny batch is a diagnostic for plumbing, not evidence of useful generalization.

## You must do yourself

- Implement AdamW in optim.py, including moments, bias correction and decoupled weight decay.
- Implement the training primitives in `training.py`, then complete `labs/day06_overfit_batch.py` with gradient zeroing, clipping, evaluation and checkpoint saving.
- Overfit one fixed batch until loss falls dramatically.
- Save step, loss, gradient norm and learning rate to evidence/day-06/training-curve.csv.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- What symptom appears if gradients are never zeroed?
- What happens when learning rate is 100× too large?
- Which parameters should generally avoid weight decay and why?
- Why can loss decrease while generated samples remain incoherent?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Run learning rates spanning at least two orders of magnitude.
- Disable bias correction and compare the first ten update magnitudes.
- Deliberately introduce one training bug, diagnose it from metrics, then repair it.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Trace one scalar loss backward to one weight.
- Derive the first AdamW update for a scalar parameter.
- Explain exactly what an overfit-one-batch test establishes.
- Distinguish optimization failure, underfitting and data failure.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=6
```

Complete the generated files under `evidence/day-06/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day06
make check DAY=6
make complete DAY=6
```

## Bad-day floor

Make loss fall on a two-parameter toy problem and derive the first Adam update by hand.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
