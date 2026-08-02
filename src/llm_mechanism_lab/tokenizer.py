from __future__ import annotations

from dataclasses import dataclass, field


Token = tuple[int, ...]


@dataclass
class BytePairTokenizer:
    """Minimal deterministic byte-level BPE tokenizer.

    Base token IDs 0..255 represent individual bytes. New token IDs are
    allocated in merge order. Store merge pairs and enough token-byte mapping
    to support deterministic encode/decode.
    """

    merges: list[tuple[int, int]] = field(default_factory=list)
    token_bytes: dict[int, bytes] = field(
        default_factory=lambda: {i: bytes([i]) for i in range(256)}
    )

    def train(self, text: str, vocab_size: int) -> None:
        """Learn pair merges from UTF-8 bytes until vocab_size is reached."""
        raise NotImplementedError("Day 02: implement BPE training")

    def encode(self, text: str) -> list[int]:
        """Encode text by applying learned merges in rank order."""
        raise NotImplementedError("Day 02: implement BPE encoding")

    def decode(self, token_ids: list[int]) -> str:
        """Concatenate token bytes and decode UTF-8."""
        raise NotImplementedError("Day 02: implement BPE decoding")
