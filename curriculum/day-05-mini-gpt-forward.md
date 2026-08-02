# Day 05: Assemble a mini-GPT

**Date:** 2026-08-07  
**Mission:** Build the complete decoder-only forward pass from token IDs to next-token logits.  
**Source:** Primary backbone: Stanford CS336 Assignment 1.

## Definition of done

Day 05 tests pass; shape trace is complete; parameter-count estimate is within 1% of the programmatic count.

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

- Embedding lookup, repeated blocks, final normalization and unembedding form the core decoder-only path.
- The final-position hidden state contains context-dependent features used to score every vocabulary token.
- Weight tying reuses the embedding geometry for unembedding but does not make input and output roles identical.
- Parameter count, activation memory and compute scale differently with width, depth, vocabulary and context.
- Causality is a property of the complete computation, not merely a triangular mask in one function.

## You must do yourself

- Implement ModelConfig, TransformerBlock and MiniGPT.forward in model.py.
- Support arbitrary batch and sequence lengths up to block_size.
- Optionally tie token embedding and unembedding weights; document the choice.
- Add a shape-tracing mode that prints or records every major activation shape.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which parameter matrix dominates when vocabulary size is much larger than d_model?
- How does doubling context length affect vanilla attention score memory?
- What should happen to logits at positions 0…t if only token t+1 is changed?
- Why is the final hidden state not itself a probability distribution?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Run the causal invariance test over every prefix position.
- Compare tied and untied parameter counts.
- Record activation shapes and estimate memory for one forward pass.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Reconstruct the entire forward pass from memory.
- For one logit, trace the possible causal paths from an earlier token.
- Explain weight tying and one trade-off.
- Compute the parameter count of a specified tiny configuration by hand.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=5
```

Complete the generated files under `evidence/day-05/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day05
make check DAY=5
make complete DAY=5
```

## Bad-day floor

Wire embeddings → one block → final norm → logits and pass the output-shape test.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
