# Daily execution schedule

This schedule is built around a **09:00–18:00 workday** and the protected **19:30–21:00 walk / decompression block**. The clock removes daily negotiation; the gate defines what counts.

## Weekdays · Aug 3–7 and Aug 10–14

| Time | Operation | Non-negotiable output |
|---|---|---|
| 06:45–06:55 | Wake, water, phone outside reach | Today’s curriculum file open |
| 06:55–07:20 | Closed-book retrieval + predictions | `predictions.md` started before code or AI |
| 07:20–07:55 | Targeted learning | Only equations / concepts blocking the next function |
| 07:55–08:25 | First implementation attempt | One real attempt or one failing test |
| 12:50–13:10 | Lunch retrieval | Explain the morning mechanism without notes |
| 21:15–22:15 | Build | Working code or intervention, not reading |
| 22:15–22:25 | Break | Leave the screen |
| 22:25–23:10 | Break + measure | Controlled failure, metric, trace or ablation |
| 23:10–23:35 | Explain + oral defense | Closed-book explanation and examiner objections |
| 23:35–23:45 | Gate + commit | `make check`, evidence log, focused commit |

**Hard stop: 23:45.** An all-nighter creates the appearance of intensity while damaging the next gate.

## Weekends · Aug 8–9 and Aug 15–16

| Time | Operation | Output |
|---|---|---|
| 08:30–09:45 | Retrieve, predict, learn | Preregistered predictions and equations |
| 10:15–11:45 | Build | Core implementation |
| 15:00–16:15 | Experiment | Break, measure and compare |
| 21:15–22:15 | Defend and close | Oral defense, evidence gate and commit |

The weekend block begins with any unfinished current gate. Never skip ahead because the later topic looks more exciting.

## The start trigger

At the first block, do not ask whether you feel ready. Execute:

```bash
make today
make start DAY=N
```

Then write one prediction. Motivation is not an input to this decision.

## Bad-day mode

A bad day is allowed. A zero is not.

1. Run `make recover`.
2. Perform the printed five-minute entry action.
3. Complete the day’s published floor.
4. Record it with `make floor DAY=N`.
5. Leave the core gate open and resume from its earliest failed step.

The floor preserves contact with difficulty. It is not fake completion.

## Catch-up without restarting

The final deadline remains **August 16, 2026**.

- **One gate behind:** the next weekend’s first block closes it. Remove stretch work and optional reading.
- **Two gates behind:** use two full weekend blocks on the oldest gate, then continue sequentially. Reduce dataset/model size, not prediction, measurement or explanation.
- **Three or more gates behind:** stop all non-Yardi side projects and all optional curriculum work. Complete only core gates in order. Do not rewrite the plan.

No missed day returns you to Day 1.

## Reward rule

Entertainment begins only after one tangible artifact exists: a passing test, completed derivation, plot, intervention result or recorded oral defense. Reward evidence, not hours spent near the repository.

## End-of-day sentence

Before closing the laptop, write:

> The earliest thing I did not understand was ___; the evidence that corrected it was ___; tomorrow’s first executable action is ___.
