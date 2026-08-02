# Day 08: Diagnose behaviour without storytelling

**Date:** 2026-08-10  
**Mission:** Learn the seven-layer diagnostic stack and apply it to controlled failure cases.  
**Source:** Primary backbone: controlled evaluation and causal-science practice.

## Definition of done

Twelve cases completed; each has competing hypotheses, a proposed intervention and an uncertainty label; one unseen case is defended orally.

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

- Observed output may be caused by input construction, tokenization, forward computation, training, post-training, decoding or runtime scaffolding.
- A fluent explanation invented after seeing an output is not mechanistic evidence.
- Reproduction requires fixing model version, prompt template, context, sampling parameters, seed and tools.
- Closed-model behaviour often cannot be localized internally, so the correct answer may stop at a constrained causal hypothesis.
- Personal intent is not established by anthropomorphic output; distinguish objective, instruction and observable behaviour.

## You must do yourself

- Use research/BEHAVIOR_DIAGNOSTIC.md to analyze all twelve supplied cases.
- For each case, write at least two competing hypotheses and one discriminating intervention.
- Run the interventions that are possible locally.
- Write diagnosis.md with Known, Inferred, Speculative and Unknown separated.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- How would you distinguish a tokenizer failure from a learned-knowledge failure?
- How would you distinguish sampling variance from prompt sensitivity?
- How would you determine whether a refusal appeared during post-training?
- What evidence would justify saying a tool result, rather than model weights, caused an answer?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Paraphrase prompts while preserving content and record stability.
- Fix all sampling parameters, then vary one variable at a time.
- Compare a base and instruction-tuned checkpoint on the same raw continuation task.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Recite the seven-layer stack in order and justify the order.
- Diagnose one unseen failure live using competing hypotheses.
- Explain the difference between behavioural, representational and mechanistic claims.
- State when “unknown” is the strongest scientific answer.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=8
```

Complete the generated files under `evidence/day-08/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
No automated unit gate; use the evidence checks and oral defense.
make check DAY=8
make complete DAY=8
```

## Bad-day floor

Diagnose three cases using the seven-layer stack and propose one intervention for each.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
