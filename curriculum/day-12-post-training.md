# Day 12: How post-training reshapes behaviour

**Date:** 2026-08-14  
**Mission:** Separate pretraining capability from assistant behaviour by understanding SFT and preference optimization.  
**Source:** Primary backbone: Stanford CS336 Alignment and Reasoning RL.

## Definition of done

Day 12 tests pass; twenty-prompt checkpoint comparison completed; DPO derivation and beta experiment included.

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

- Pretraining learns next-token prediction over a data distribution; SFT conditions the model toward demonstrated assistant responses.
- Preference optimization changes relative likelihood of chosen and rejected responses under a reference constraint.
- DPO turns a preference pair into a logistic objective over policy/reference log-probability ratios.
- Refusal, verbosity, sycophancy and format-following can be post-training effects rather than architectural properties.
- Comparing base and instruction checkpoints is evidence about when behaviour appeared, not a complete explanation of why.

## You must do yourself

- Implement dpo_loss in post_training.py and pass the numerical tests.
- Create at least twenty prompts and compare a related base/instruction model pair.
- Record completion log-probabilities where feasible, not only decoded text.
- Write checkpoint-comparison.md separating stable capabilities from changed policies.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which behaviours should change most between base and instruction checkpoints?
- What happens to DPO loss when the chosen response becomes more likely relative to both rejected and reference?
- Why is SFT not equivalent to adding a system prompt?
- How might preference optimization trade calibration for preferred style?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Compare raw continuation, instruction following, refusal and sycophancy prompts.
- Vary DPO beta on synthetic log-probabilities and plot the loss.
- Find one capability present in both checkpoints but expressed differently after instruction tuning.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Derive the DPO logit and loss from four sequence log-probabilities.
- Separate capability, propensity and sampled behaviour.
- Explain how you would locate the training stage where a behaviour appeared.
- State what checkpoint comparison cannot establish.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=12
```

Complete the generated files under `evidence/day-12/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day12
make check DAY=12
make complete DAY=12
```

## Bad-day floor

Implement and test dpo_loss on scalar log-probabilities, then compare five prompts across a base/instruction pair.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
