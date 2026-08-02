# Roadmap

- **Day 01 · 2026-08-03 · [Text → logits → probabilities](curriculum/day-01-text-to-probabilities.md):** Build the numerical atoms of an autoregressive language model and trace one next-token prediction end to end.
- **Day 02 · 2026-08-04 · [Build a byte-level BPE tokenizer](curriculum/day-02-byte-pair-tokenization.md):** Understand how raw text becomes the discrete sequence the transformer actually sees.
- **Day 03 · 2026-08-05 · [Attention by hand](curriculum/day-03-attention-by-hand.md):** Implement single-head causal self-attention and explain information routing precisely.
- **Day 04 · 2026-08-06 · [Build the transformer block](curriculum/day-04-transformer-block.md):** Assemble multi-head attention, residual pathways, RMSNorm, RoPE and SwiGLU into one decoder block.
- **Day 05 · 2026-08-07 · [Assemble a mini-GPT](curriculum/day-05-mini-gpt-forward.md):** Build the complete decoder-only forward pass from token IDs to next-token logits.
- **Day 06 · 2026-08-08 · [Make the model learn](curriculum/day-06-learning-and-optimization.md):** Understand how prediction error becomes weight change and prove the full training path by overfitting one batch.
- **Day 07 · 2026-08-09 · [Train, sample and explain generation](curriculum/day-07-training-and-generation.md):** Train the mini-GPT on a small corpus and separate learned logits from decoding behaviour.
- **Day 08 · 2026-08-10 · [Diagnose behaviour without storytelling](curriculum/day-08-behavior-diagnostic-stack.md):** Learn the seven-layer diagnostic stack and apply it to controlled failure cases.
- **Day 09 · 2026-08-11 · [See inside: activations and the logit lens](curriculum/day-09-activations-and-logit-lens.md):** Use hooks and cached activations to locate where output-relevant information becomes decodable.
- **Day 10 · 2026-08-12 · [Causal tracing with activation patching](curriculum/day-10-activation-patching.md):** Replace internal activations between clean and corrupted runs to identify causally important locations.
- **Day 11 · 2026-08-13 · [From locations to circuits](curriculum/day-11-circuits-and-ablation.md):** Narrow a behaviour from layer/position localization to attention-head and MLP components using ablation and path hypotheses.
- **Day 12 · 2026-08-14 · [How post-training reshapes behaviour](curriculum/day-12-post-training.md):** Separate pretraining capability from assistant behaviour by understanding SFT and preference optimization.
- **Day 13 · 2026-08-15 · [Run an original mini-study](curriculum/day-13-original-mini-study.md):** Convert one observed LLM behaviour into a falsifiable, controlled and causally probed research question.
- **Day 14 · 2026-08-16 · [Final defense and mechanism atlas](curriculum/day-14-final-defense.md):** Demonstrate closed-book command of the complete stack and convert the sprint into a durable research system.

## Phase boundary

- **Days 1–7:** build the machine.
- **Days 8–12:** diagnose and intervene on the machine.
- **Day 13:** conduct an original mini-study.
- **Day 14:** defend the mechanism atlas and choose one 30-day research direction.

Do not unlock later work because it looks more exciting. The later tools are interpretable only when the forward and training computations are already concrete in your mind.
