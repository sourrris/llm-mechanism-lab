# Day 02: Build a byte-level BPE tokenizer

**Date:** 2026-08-04  
**Mission:** Understand how raw text becomes the discrete sequence the transformer actually sees.  
**Source:** Primary backbone: Stanford CS336 tokenization material.

## Definition of done

All Day 02 tokenizer tests pass; encode/decode round-trip Unicode; tokenizer-report.md includes at least four controlled comparisons.

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

- The model never receives characters or words directly; it receives token IDs produced by a tokenizer.
- Byte-level tokenization guarantees coverage while learned merges provide compression.
- Merge order matters because BPE applies learned pair merges iteratively, not all at once.
- Token boundaries alter sequence length, positions, attention patterns and the difficulty of prediction.
- A tokenizer can create behavioural differences even when two strings look semantically equivalent to a person.

## You must do yourself

- Implement BytePairTokenizer.train, encode and decode in tokenizer.py.
- Use deterministic tie-breaking so repeated training produces identical merges.
- Preserve round-trip correctness for Unicode text by operating on UTF-8 bytes.
- Create tokenizer-report.md comparing tokenization of code, English, Bengali and misspelled text.

The first implementation and first explanation are yours. AI may provide a minimal hint after two archived attempts.

## Predictions required before execution

- Which pairs will merge first in “banana banana banana” and why?
- Will a leading space usually affect tokenization? State the mechanism, not merely yes/no.
- Why can rare names and malformed code consume more context than common phrases?
- What failure would occur if decode treated token IDs as Unicode code points rather than byte sequences?

For every prediction, record: expected direction, mechanism, confidence from 0–100%, and what result would falsify it.

## Required experiments

- Train at three vocabulary sizes and compare compression ratio.
- Measure token count after changing only capitalization, whitespace and punctuation.
- Find one visually small edit that causes a large token-sequence change.

Change one variable at a time unless the experiment explicitly studies an interaction.

## Oral defense

Answer without notes, then let an AI examiner challenge the answer:

- Walk through one complete BPE merge manually.
- Explain the difference between the tokenizer vocabulary and the model embedding matrix.
- Explain why tokenization is part of the causal mechanism behind model behaviour.
- State what byte fallback guarantees and what it does not guarantee.

A fluent answer fails if it omits equations, tensor shapes, a causal path, an intervention or remaining uncertainty where those are relevant.

## Evidence files

Run:

```bash
make start DAY=2
```

Complete the generated files under `evidence/day-02/`. Keep failed predictions and both pre-hint implementation attempts.

## Gate command

```bash
python -m pytest -q tests/day02
make check DAY=2
make complete DAY=2
```

## Bad-day floor

Implement UTF-8 byte encode/decode round-trip and manually perform three BPE merges on one short string.

After doing the floor, record it. Do not pretend the core gate passed. Resume here instead of restarting the program.

## Stretch only after passing

- Rebuild the central function in a blank file without autocomplete.
- Create one adversarial case that breaks a naive implementation.
- Explain the mechanism to an imagined skeptical researcher in under three minutes.
