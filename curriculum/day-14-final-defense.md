# Day 14: Final defense and mechanism atlas

**Date:** 2026-08-16  
**Mission:** Demonstrate closed-book command of the complete stack and convert the sprint into a durable research system.  
**Source:** Primary backbone: your own accumulated evidence.

## Definition of done

Final atlas, blank-file implementation, three unseen diagnoses, adversarial oral defense and a concrete next 30-day research cycle.

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

- Expertise is the ability to predict, derive, build, diagnose and intervene, not merely recognize terminology.
- A complete explanation links behaviour to context, tokenization, computation, training origin, decoding and runtime where relevant.
- Mechanistic confidence should track causal evidence and generalization, not explanatory fluency.
- The two-week sprint creates a foundation and operating method; top-tier standing requires repeated original contributions.
- The next cycle should narrow around one mechanism rather than restart the entire curriculum.

## You must do yourself

- Write mechanism-atlas/final-atlas.md covering at least twenty mechanisms with equations, shapes, interventions and failure modes.
- Complete final-defense.md without notes before checking any answer.
- Reimplement stable softmax, attention and one transformer block in a blank file under time pressure.
- Present the mini-study as a five-minute research talk and record a transcript or audio link.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which three areas are still weakest, based on failed evidence rather than feeling?
- Which one research direction has the best combination of novelty, access and personal advantage?
- What intervention would most increase confidence in your mini-study?
- What will you stop doing to protect depth during the next cycle?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Diagnose three unseen behaviours using the full seven-layer stack.
- Repair three deliberately broken components without external code.
- Ask an AI examiner to challenge every causal claim in the mechanism atlas.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Derive the transformer forward pass and training objective from memory.
- Explain one behaviour from observation through causal intervention.
- Distinguish Known, Inferred, Speculative and Unknown in your study.
- Defend why your next research question is narrow enough to answer.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=14
```

Complete the generated files under `evidence/day-14/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
No automated unit gate; use the evidence checks and oral defense.
make check DAY=14
make complete DAY=14
```

## Bad-day floor

Complete the closed-book forward-pass derivation, diagnose one unseen case, and write the next research question with two hypotheses.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
