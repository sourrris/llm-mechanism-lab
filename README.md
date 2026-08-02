# LLM Mechanism Forge

> **Fourteen days to build the machine, open it, intervene on it, and defend what you think it is doing.**

Built for **Sourish Chakraborty**: high ambition, high technical ceiling, low tolerance for passive coursework, and a tendency to switch projects when the work becomes slow or uncomfortable.

This repository is designed around one rule:

> **You do not get credit for consuming an explanation. You get credit for predicting, implementing, testing, intervening and explaining without notes.**

## The honest target

Fourteen days cannot manufacture top-0.1% research standing. It can create the compressed foundation and research loop needed to pursue it intelligently:

- Build a small decoder-only transformer without framework shortcuts.
- Trace every important tensor from text to next-token probability.
- Train it, break it, diagnose it and explain why it failed.
- Separate weights, context, post-training, decoding and runtime effects.
- Cache and patch internal activations in a real open model.
- Replicate one circuit result and conduct one original mini-study.
- Defend claims using causal evidence instead of a persuasive story.

## Start in three commands

```bash
./scripts/bootstrap.sh
source .venv/bin/activate
make today
```

Then:

```bash
make start DAY=1
# Do the mission.
make check DAY=1
make complete DAY=1
```

Open the interactive local command centre:

```bash
make dashboard
# Visit http://localhost:8000/docs/
```

## The daily loop

```text
PREDICT → BUILD → BREAK → MEASURE → EXPLAIN → DEFEND → COMMIT
```

1. **Predict first.** Write what should happen before running code.
2. **Build it yourself.** The first implementation of core mechanisms is yours.
3. **Break it deliberately.** Introduce controlled failures and identify their earliest cause.
4. **Measure.** Shapes, logits, losses, gradients and interventions beat impressions.
5. **Explain closed-book.** Reconstruct the mechanism without borrowing language.
6. **Defend.** Let AI attack the causal gaps after your own explanation exists.
7. **Commit evidence.** Every completed day ends with a visible commit.

## Your first action

Read [START_HERE.md](START_HERE.md), then run:

```bash
make start DAY=1
```

Do not redesign the curriculum. Do not collect more resources. Do not start another AI project for fourteen days. Put tempting ideas in [PARKING_LOT.md](PARKING_LOT.md) and return to the current gate.

## Structure

```text
curriculum/          The 14 daily missions
src/                 Your from-scratch implementation
labs/                Interpretability and post-training investigations
tests/               Day-specific executable gates
evidence/            Predictions, explanations, results and oral defenses
mechanism-atlas/      Your compressed causal map of LLMs
research/             Diagnostic and original-study protocols
scripts/forge.py      Progress, grading and recovery CLI
docs/                 Interactive dashboard
```

## Completion is binary

A day is complete only when `make complete DAY=N` passes. Reading, watching, thinking about starting, or receiving an AI-generated solution does not count.

A bad day still has a floor. The floor prevents a zero; it does **not** falsely mark the full day complete. Never restart. Resume from the earliest failed gate.

## Source backbone

The sequence is compressed from implementation-first and interpretability-first primary materials: Stanford CS336, ARENA Transformer Interpretability, TransformerLens, NNsight, the original Transformer paper and causal circuit work. See [resources/OFFICIAL_SOURCES.md](resources/OFFICIAL_SOURCES.md).

## License

MIT. The learning evidence is yours; the standard is non-negotiable.
