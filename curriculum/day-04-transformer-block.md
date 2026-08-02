# Day 04: Build the transformer block

**Date:** 2026-08-06  
**Mission:** Assemble multi-head attention, residual pathways, RMSNorm, RoPE and SwiGLU into one decoder block.  
**Source:** Primary backbone: Stanford CS336 architectures and ARENA Transformers from Scratch.

## Definition of done

Day 04 tests pass; block-diagram.md is drawn from memory; ablation predictions are written before execution and compared with results.

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

- Multiple heads create separate learned routing/content subspaces before their outputs are recombined.
- The residual stream is the shared communication channel to which attention and MLP components write.
- Pre-normalization changes the input scale seen by each sublayer while preserving a direct residual path.
- RoPE rotates query/key coordinates as a function of position, making relative displacement available to attention.
- A gated MLP can conditionally transform information at each position without moving information across positions.

## You must do yourself

- Implement MultiHeadAttention without nn.MultiheadAttention.
- Implement RMSNorm from its equation.
- Implement SwiGLU and rotary position application.
- Implement one pre-norm TransformerBlock with explicit residual additions.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- What breaks if q and k are rotated with inconsistent position angles?
- Why does RoPE preserve vector norm?
- What is the behavioural difference between removing an MLP update and removing the residual path?
- Why can an MLP be important for a behaviour even though it never attends to another token?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Measure output scale with and without RMSNorm across inputs multiplied by 0.1, 1 and 10.
- Verify numerically that RoPE preserves pairwise vector norms.
- Ablate attention, MLP and each residual update separately in a randomly initialized block.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Draw the complete pre-norm block from memory.
- Explain what each head can do that one large head cannot trivially reproduce.
- Explain the residual stream as a computational object, not a metaphor.
- State exactly where positional information enters a RoPE-based model.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=4
```

Complete the generated files under `evidence/day-04/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day04
make check DAY=4
make complete DAY=4
```

## Bad-day floor

Implement RMSNorm and one residual sublayer, then explain why the residual path protects information flow.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
