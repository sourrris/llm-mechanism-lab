# Behaviour diagnostic stack

## Reproduction record

- Model and checkpoint:
- Base or instruction-tuned:
- System/user/chat template:
- Complete visible context:
- Tools/retrieval/runtime:
- Temperature, top-k, top-p, seed:
- Exact observed behaviour and metric:

## Diagnose in order

1. **Input construction:** hidden instructions, chat template, retrieval, truncation, tools.
2. **Tokenization:** boundaries, whitespace, rare fragments, context length.
3. **Forward computation:** embeddings, attention routing, MLP transformations, residual state, logits.
4. **Training origin:** data, objective, architecture, optimization trajectory.
5. **Post-training origin:** SFT, preferences, reward, refusal/safety, distillation.
6. **Decoding:** temperature, truncation, randomness, repetition handling.
7. **External runtime:** agent loop, memory, retrieval, tool errors, application filters.

## Twelve cases

For each, create at least two hypotheses and one discriminating intervention.

1. A model spells a common word correctly but repeatedly misspells a rare surname.
2. An answer changes after a single leading space is added to a short prompt.
3. The same prompt alternates between two answers at temperature 1 but stabilizes at temperature 0.
4. A base checkpoint continues a dangerous request while its instruction-tuned sibling refuses.
5. A coding agent repeats the same wrong repair after receiving a failing test log.
6. A long conversation causes the model to ignore an early constraint.
7. A retrieval-augmented answer cites a false statement present in the retrieved document.
8. Tool output is correct but the final natural-language summary reverses a sign.
9. A model gives the right multiple-choice answer but an unfaithful verbal explanation.
10. A prompt paraphrase preserves meaning but changes the chosen answer.
11. Greedy decoding loops on a repeated phrase while nucleus sampling escapes it.
12. An apparent “knowledge edit” disappears when the prompt format changes.

## Required conclusion format

- Known:
- Inferred:
- Speculative:
- Unknown:
- Cheapest next intervention:
