from llm_mechanism_lab.tokenizer import BytePairTokenizer


def test_round_trip_unicode():
    text = "LLMs समझते? বাংলা + code_123 🚀"
    tokenizer = BytePairTokenizer()
    tokenizer.train(text * 5, vocab_size=280)
    assert tokenizer.decode(tokenizer.encode(text)) == text


def test_training_is_deterministic():
    text = "banana bandana banana bandana"
    a = BytePairTokenizer(); a.train(text, vocab_size=270)
    b = BytePairTokenizer(); b.train(text, vocab_size=270)
    assert a.merges == b.merges


def test_larger_vocabulary_compresses_repetitive_text():
    text = "transformer transformer transformer " * 10
    small = BytePairTokenizer(); small.train(text, vocab_size=256)
    large = BytePairTokenizer(); large.train(text, vocab_size=300)
    assert len(large.encode(text)) < len(small.encode(text))


def test_unseen_bytes_still_round_trip():
    tokenizer = BytePairTokenizer()
    tokenizer.train("ordinary training text", vocab_size=265)
    text = "unseen: Ω🙂"
    assert tokenizer.decode(tokenizer.encode(text)) == text
