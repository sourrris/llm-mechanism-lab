# Day 01: Text → logits → probabilities

**Date:** 2026-08-03  
**Mission:** Build the numerical atoms of an autoregressive language model and trace one next-token prediction end to end.  
**Source:** Primary backbone: Stanford CS336 Assignment 1 and the original Transformer paper.

## Definition of done

All Day 01 tests pass; explanation.md contains a complete forward-path trace; oral-defense.md answers all four questions without copied wording.

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

- An autoregressive LM models a conditional distribution: p(x_t | x_<t), not a database lookup.
- Token IDs are discrete addresses; embeddings turn addresses into trainable vectors.
- Logits are unnormalized evidence. Softmax converts relative logit differences into probabilities.
- Subtracting the maximum logit prevents overflow without changing the distribution.
- Cross-entropy is the negative log-probability assigned to the correct next token.
- The causal mask changes which earlier positions may influence each prediction.

## You must do yourself

- Implement stable_softmax in src/llm_mechanism_lab/tensor_ops.py.
- Implement causal_attention_mask for a decoder-only model.
- Implement cross_entropy_from_logits without calling torch.nn.functional.cross_entropy.
- Write a tensor-shape trace for: text → IDs → embeddings → hidden states → logits → probabilities.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- What happens to a softmax distribution when the same constant is added to every logit?
- What happens to entropy when every logit is multiplied by 0.2? By 5?
- Which entries of a 4×4 causal mask must be blocked?
- Why can a model have low training loss while still generating poor text?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Compare your stable_softmax with torch.softmax on ordinary and extreme logits.
- Measure entropy while scaling the same logit vector from 0.1× to 10×.
- Visualize a causal mask and prove that changing a future token cannot affect an earlier logit.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Explain why logits, probabilities and sampled tokens are three different objects.
- Derive the cross-entropy for one target token from a five-token vocabulary.
- Explain the exact causal role of the mask. Do not say only “it prevents cheating.”
- State every major tensor shape from a batch of token IDs to vocabulary logits.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=1
```

Complete the generated files under `evidence/day-01/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day01
make check DAY=1
make complete DAY=1
```

## Bad-day floor

Compute one three-logit softmax by hand, implement stable_softmax, and write 150 words explaining logits versus probabilities.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
