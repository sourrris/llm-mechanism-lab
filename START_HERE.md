# Start here

## 1. Accept the actual contract

Your ambition is useful only when it survives boredom, confusion and failed tests. This program does not attempt to make every session pleasant. It makes the hard action small enough to start and concrete enough to finish.

Sign [CONTRACT.md](CONTRACT.md), then use [DAILY_SCHEDULE.md](DAILY_SCHEDULE.md) as the default clock before Day 1.

## 2. Set up once

Recommended: Python 3.11 or 3.12.

```bash
./scripts/bootstrap.sh
source .venv/bin/activate
make status
make start DAY=1
```

The core week runs on CPU at tiny scale. Days 9–13 benefit from a GPU, but the exercises have CPU-sized fallbacks. Do not purchase compute until the local code and experiment design work.

## 3. Use the three-level day

Every curriculum file contains:

- **Core gate:** the full required result. Aim here.
- **Bad-day floor:** the minimum hard rep when resistance is unusually high.
- **Stretch:** optional depth only after the gate passes.

The floor prevents disappearance. It is not a substitute for the core gate, and unfinished core work carries forward without restarting the program.

## 4. Protect the first hard block

The first 45 minutes follow this order:

1. Phone outside reach.
2. No social feed, new repository, package comparison or course search.
3. Read only today’s mission.
4. Write predictions before code.
5. Work for 25 minutes without AI.
6. After two real attempts, request a hint rather than a solution.

## 5. AI roles

Use the best AI aggressively, but only in roles that accelerate understanding.

### Tutor prompt

```text
Teach me [concept] as a causal computation. Start with inputs, outputs, equations and tensor shapes. Ask me to predict each step before revealing it. Do not write my exercise implementation. After I answer, identify the earliest causal gap.
```

### Hint prompt

```text
I attempted this twice. Here is my prediction, code and failing test. Give one minimal hint pointing to the earliest incorrect assumption. Do not provide replacement code.
```

### Examiner prompt

```text
Act as an adversarial LLM-mechanism examiner. Ask one question at a time. Reject vague, anthropomorphic or merely correlational explanations. Require equations, tensor shapes, a causal intervention and what remains unknown. Score only after ten questions.
```

### Research critic prompt

```text
Here are my observation, hypotheses, controls and results. Find the earliest point at which the causal claim becomes unsupported. Propose the cheapest discriminating intervention. Separate Known, Inferred, Speculative and Unknown.
```

## 6. End every day visibly

```bash
make check DAY=N
make complete DAY=N
git add -A
git commit -m "day N: <mechanism proved>"
git push
```

No beautiful retrospective. Record what predicted correctly, what failed, the earliest failure and the corrected mechanism.

## 7. When you avoid the work

Run:

```bash
make recover
```

Then perform the five-minute entry action it prints. Do not negotiate with the entire three-hour task. Start one falsifiable prediction, one tensor calculation, or one failing test.

## 8. What not to do

- Do not restart because a day was missed.
- Do not replace implementation with a tutorial clone.
- Do not count an AI explanation as your understanding.
- Do not read five papers when one experiment is blocked.
- Do not optimize the dashboard, tooling or repository structure during the sprint.
- Do not call a correlation a mechanism.

Begin Day 1 now.
