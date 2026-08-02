# AI usage contract

## Allowed

- Explain a concept after you state your current model.
- Generate adversarial questions and test cases.
- Review your code and identify the earliest incorrect assumption.
- Offer progressively stronger hints.
- Attack causal claims and propose controls.
- Grade a closed-book explanation.
- Help read primary-source material after you formulate a question.

## Not allowed for the first implementation

- Writing stable softmax, BPE, attention, transformer blocks, AdamW, generation or DPO loss for you.
- Replacing your broken function with a complete solution.
- Producing the prediction log after an experiment has run.
- Writing the final oral-defense answers.
- Inventing results, plots or evidence.

## Hint ladder

1. Ask a question about the violated invariant.
2. Point to the wrong tensor or equation.
3. Point to the wrong line or operation.
4. Show a smaller analogous example.
5. Provide pseudocode only after the first four levels fail.
6. Full code is permitted only after you archive both attempts and explain the correction yourself.

AI accelerates feedback. It does not replace the cognitive operation being trained.
