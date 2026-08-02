# Day 03: Attention by hand

**Date:** 2026-08-05  
**Mission:** Implement single-head causal self-attention and explain information routing precisely.  
**Source:** Primary backbone: Attention Is All You Need and ARENA Transformers from Scratch.

## Definition of done

Day 03 tests pass; manual-attention.md reproduces every number; one experiment falsifies an over-simple “attention equals explanation” claim.

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

- Q and K jointly determine routing scores; V supplies the content moved along those routes.
- The dot product measures compatibility in learned query/key spaces, not semantic similarity in the abstract.
- Scaling by sqrt(d_head) controls score magnitude and softmax saturation.
- Attention produces a weighted sum of value vectors for each query position.
- Attention patterns are data-dependent routing weights, not by themselves complete explanations.

## You must do yourself

- Implement scaled_dot_product_attention for tensors shaped [batch, heads, time, d_head].
- Calculate Q, K, scores, probabilities and output manually for a three-token, two-dimensional example.
- Return attention probabilities for inspection without detaching gradients.
- Prove causality with a test that changes a future token while holding the prefix fixed.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- What happens when every key vector is identical?
- What happens when one Q·K score dominates by 100?
- Can two different attention patterns produce the same output? Construct an example.
- Why does an attention head need an output projection after combining values?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Remove the 1/sqrt(d_head) scale at several head dimensions and compare attention entropy.
- Zero Q, K or V separately and explain each resulting behaviour.
- Create two value matrices that make attention patterns misleading as explanations.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Derive scaled dot-product attention from inputs to output.
- Explain “where to read” versus “what to move” without anthropomorphic language.
- Explain why attention weights alone cannot identify the whole causal computation.
- Give the exact shape of every tensor for B=2, T=5, H=4, d_head=8.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=3
```

Complete the generated files under `evidence/day-03/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day03
make check DAY=3
make complete DAY=3
```

## Bad-day floor

Calculate one attention row by hand and implement the score, mask and softmax portion of scaled_dot_product_attention.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
