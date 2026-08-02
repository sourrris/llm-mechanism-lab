# Day 09: See inside: activations and the logit lens

**Date:** 2026-08-11  
**Mission:** Use hooks and cached activations to locate where output-relevant information becomes decodable.  
**Source:** Primary backbone: TransformerLens and ARENA Intro to Mechanistic Interpretability.

## Definition of done

activation-summary.md, logit-lens.csv and one plot exist; claims are tested across at least ten examples; decodability is not mislabeled as causation.

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

- The residual stream accumulates component updates across layers.
- A hook exposes or modifies an intermediate tensor; its semantic meaning depends on the exact hook point.
- The logit lens projects intermediate residual states through a normalization/unembedding approximation.
- Decodability does not prove that the model causally uses the decoded representation.
- Direct logit attribution decomposes contributions under specific linear assumptions and must be interpreted accordingly.

## You must do yourself

- Install the interpretability extra and load GPT-2 small or another supported small open model with TransformerLens.
- Cache residual, attention and MLP activations for at least five prompts.
- Produce a layer-by-layer logit-lens table for one target token.
- Write activation-summary.md describing exact hook names and tensor shapes.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- At which layers should a factual completion become decodable? State a hypothesis before running.
- Why might the ordinary logit lens misrepresent an intermediate computation?
- Can information be decodable in one layer and later disappear?
- What changes if the beginning-of-sequence token is added or omitted?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Compare clean prompts with paraphrases and corrupted prompts.
- Compare residual-pre, attention-output, MLP-output and residual-post contributions.
- Test whether your layer-level claim survives at least ten examples.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Explain precisely what run_with_cache records.
- Explain why a probe or logit lens is correlational by default.
- Trace one candidate token’s logit through component updates.
- Name three hook-related implementation errors that could invalidate a conclusion.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=9
```

Complete the generated files under `evidence/day-09/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
No automated unit gate; use the evidence checks and oral defense.
make check DAY=9
make complete DAY=9
```

## Bad-day floor

Load one supported model, cache residual activations, record their shapes, and compute one layer-wise target logit.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
