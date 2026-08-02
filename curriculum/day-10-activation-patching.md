# Day 10: Causal tracing with activation patching

**Date:** 2026-08-12  
**Mission:** Replace internal activations between clean and corrupted runs to identify causally important locations.  
**Source:** Primary backbone: TransformerLens/NNsight activation-patching documentation.

## Definition of done

At least twenty prompt pairs, preregistered predictions, heatmap, negative control and replicated localization; all limitations stated.

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

- Activation patching is an interchange intervention: run a corrupted input but substitute an activation from a clean input.
- A patching metric must measure the behaviour of interest, often through a logit difference rather than raw accuracy.
- Patch location, granularity and corruption choice define the causal question being asked.
- Restoration under a patch supports causal relevance but does not automatically identify a complete circuit.
- Negative controls and matched prompt pairs are necessary to reject trivial explanations.

## You must do yourself

- Construct at least twenty clean/corrupted prompt pairs with aligned token positions.
- Define a signed logit-difference metric before inspecting results.
- Patch residual-stream activations across every layer and position.
- Save patching-result.png and patching-analysis.md.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which position/layer region should restore the answer and why?
- What result would falsify your preferred localization hypothesis?
- How can token misalignment create a false patching result?
- Why might patching a broad residual vector restore behaviour without identifying the responsible feature?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Repeat with two different corruption types.
- Run a random-activation or unrelated-prompt negative control.
- Patch attention and MLP outputs separately in the highest-impact layers.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Define the clean run, corrupted run, intervention and metric mathematically.
- Explain what a bright heatmap cell does and does not establish.
- Explain why causal relevance is weaker than a complete mechanism.
- Design a patching experiment for one unseen behaviour.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=10
```

Complete the generated files under `evidence/day-10/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
No automated unit gate; use the evidence checks and oral defense.
make check DAY=10
make complete DAY=10
```

## Bad-day floor

Patch residual state at one layer across five aligned clean/corrupted pairs and compute the change in logit difference.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
