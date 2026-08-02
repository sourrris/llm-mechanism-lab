# Included training data

`tiny_corpus.txt` is an original, synthetic micro-corpus included only to make the Day 06–07 plumbing experiments reproducible without a download.

It is deliberately small. Use it to:

- test tokenization and batching;
- overfit a tiny model;
- compare decoding settings;
- verify checkpoints and generation.

Do not use it to infer scaling behaviour or general language capability. A model memorizing this corpus proves that the training path works, not that the model generalizes.
