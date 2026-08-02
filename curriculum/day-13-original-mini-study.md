# Day 13: Run an original mini-study

**Date:** 2026-08-15  
**Mission:** Convert one observed LLM behaviour into a falsifiable, controlled and causally probed research question.  
**Source:** Primary backbone: preregistration, controls and causal intervention.

## Definition of done

Preregistered protocol, ≥30 examples, held-out evaluation, negative control, results table and mini-study.md with no causal overclaim.

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

- A research question must define behaviour, model, input distribution and measurable outcome.
- Competing hypotheses prevent an attractive story from becoming the default conclusion.
- Preregistered predictions reduce hindsight bias.
- Discovery examples and evaluation examples must be separated.
- A negative result is useful when the intervention had power to distinguish the hypotheses.

## You must do yourself

- Choose one narrow behaviour, preferably coding-error persistence, constraint tracking, refusal or prompt-pressure reversal.
- Complete research/MINI_STUDY_PROTOCOL.md before running the main experiment.
- Use at least thirty examples, with discovery and held-out sets.
- Perform one internal causal intervention if using an open model; otherwise run the strongest behavioural intervention possible.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- What exact observation would support each hypothesis?
- What exact observation would falsify your favourite hypothesis?
- What confound is most likely to produce a convincing but false result?
- What result would remain unknown even after your planned experiment?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Run the preregistered primary test before exploratory analyses.
- Repeat across prompts, seeds and at least one model/checkpoint contrast where feasible.
- Perform one negative control and one intervention-strength check.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- State the question, hypotheses and discriminating prediction in under ninety seconds.
- Explain why your intervention is causally informative.
- Identify the earliest point where your study could have become invalid.
- Give the strongest conclusion justified by the evidence, then name the remaining unknowns.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=13
```

Complete the generated files under `evidence/day-13/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
No automated unit gate; use the evidence checks and oral defense.
make check DAY=13
make complete DAY=13
```

## Bad-day floor

Define one behaviour precisely, write two competing hypotheses, construct ten examples and run one discriminating behavioural intervention.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
