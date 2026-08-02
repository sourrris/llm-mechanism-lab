# Day 11: From locations to circuits

**Date:** 2026-08-13  
**Mission:** Narrow a behaviour from layer/position localization to attention-head and MLP components using ablation and path hypotheses.  
**Source:** Primary backbone: induction-head and IOI circuit work plus ARENA circuit exercises.

## Definition of done

A replicated causal effect, at least two ablation methods, held-out templates and a circuit report with explicit uncertainty.

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

- A circuit is a causally relevant subgraph of model components for a defined behaviour and distribution of inputs.
- Ablation can reveal necessity, but distributed redundancy may hide important components.
- Induction heads implement a pattern-completion operation of the form [A][B] … [A] → [B] in suitable settings.
- QK circuits determine attention destinations; OV circuits determine the output written when attention occurs.
- Mechanisms may be prompt-local, model-specific or only partially faithful to a sparse approximation.

## You must do yourself

- Replicate either a small induction-head result or an IOI-style head-ablation result.
- Rank heads by causal effect using ablation or patching.
- Inspect QK and OV evidence for the most important head.
- Write circuit-report.md containing a proposed graph and falsifying experiments.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which head properties distinguish induction from generic previous-token attention?
- What would redundancy look like under single-head versus multi-head ablation?
- How can mean ablation introduce an off-distribution state?
- What evidence is needed before calling a set of heads “the circuit”?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Compare zero, mean and resample ablation.
- Ablate combinations of top heads and test for non-additive effects.
- Test the circuit on prompt templates not used for discovery.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Explain QK versus OV circuits with equations.
- Distinguish necessity, sufficiency and redundancy.
- Explain why one successful ablation is not a universal mechanism.
- Defend your circuit graph against two alternative hypotheses.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=11
```

Complete the generated files under `evidence/day-11/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
No automated unit gate; use the evidence checks and oral defense.
make check DAY=11
make complete DAY=11
```

## Bad-day floor

Rank all heads in one small model by one ablation metric and explain the top three without claiming completeness.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
