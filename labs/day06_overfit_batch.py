"""Day 06 scaffold: prove the complete training path by overfitting one batch.

Required output:
    evidence/day-06/training-curve.csv
    evidence/day-06/bug-autopsy.md

Do not begin with a full corpus. Freeze one batch, make the loss collapse, then
introduce exactly one bug and trace the earliest violated invariant.
"""


def main() -> None:
    # TODO 1: create/load a tokenizer and one fixed token batch.
    # TODO 2: instantiate a tiny MiniGPT and your AdamW.
    # TODO 3: log step, loss, gradient norm and learning rate.
    # TODO 4: stop only after a preregistered overfit threshold is reached.
    # TODO 5: repeat with one deliberate bug and document the diagnosis.
    raise NotImplementedError("Complete during Day 06")


if __name__ == "__main__":
    main()
