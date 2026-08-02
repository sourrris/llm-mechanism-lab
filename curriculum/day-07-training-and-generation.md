# Day 07: Train, sample and explain generation

**Date:** 2026-08-09  
**Mission:** Train the mini-GPT on a small corpus and separate learned logits from decoding behaviour.  
**Source:** Primary backbone: Stanford CS336 minimal LM training and generation.

## Definition of done

Day 07 tests pass; checkpoint saved; decoding-grid.md predicts and explains twelve samples; week-one-defense.md reconstructs the machine without notes.

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

- The model produces logits; the decoding algorithm chooses how those logits become a token.
- Temperature rescales relative logit differences and therefore changes entropy, not stored knowledge.
- Top-k and nucleus sampling truncate the candidate distribution in different ways.
- Autoregressive errors alter future context, so generation is a feedback process.
- A KV cache avoids recomputing past key/value projections during incremental decoding.

## You must do yourself

- Implement temperature, top-k, top-p and sampling in generation.py.
- Complete `labs/day07_train_and_sample.py`; train on `data/tiny_corpus.txt` or another legally usable small corpus and save a checkpoint.
- Generate from the same prompt under at least twelve decoding settings.
- Write a conceptual KV-cache shape and memory trace; implementing the cache is a stretch task.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which settings make generation deterministic?
- Can top-p retain more tokens than top-k? Give a concrete distribution.
- Why can temperature 0.2 improve factual consistency but also preserve a wrong high-logit answer?
- Which computations are reused by a KV cache and which still occur for the new token?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Hold logits fixed and compare the empirical sampling frequency with the theoretical distribution.
- Generate with identical settings and different seeds, then identical seed and different temperature.
- Measure generation time as context grows, with and without any available cache implementation.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Separate weights, context, logits, decoding and sampled token in one explanation.
- Explain top-p with a six-token numerical example.
- Explain exposure through autoregressive feedback without saying “the model gets confused.”
- Give KV-cache tensor shapes for B, layers, KV heads, time and d_head.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=7
```

Complete the generated files under `evidence/day-07/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day07
make check DAY=7
make complete DAY=7
```

## Bad-day floor

Implement greedy and temperature sampling, generate two contrasting samples, and explain why the weights were unchanged.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
