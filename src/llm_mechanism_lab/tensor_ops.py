from __future__ import annotations

import torch
from torch import Tensor


def stable_softmax(x: Tensor, dim: int = -1) -> Tensor:
    """Compute numerically stable softmax without calling torch.softmax.

    Preserve input shape and normalize along ``dim``.
    """
    raise NotImplementedError("Day 01: implement stable_softmax")


def causal_attention_mask(sequence_length: int, device: torch.device | str | None = None) -> Tensor:
    """Return a boolean mask of shape [T, T].

    ``True`` means the key position is visible to the query position.
    Query row i may see key columns 0..i and no future columns.
    """
    raise NotImplementedError("Day 01: implement causal_attention_mask")


def cross_entropy_from_logits(logits: Tensor, targets: Tensor) -> Tensor:
    """Mean next-token cross-entropy without F.cross_entropy.

    ``logits`` has shape [..., vocab]. ``targets`` has shape [...].
    """
    raise NotImplementedError("Day 01: implement cross_entropy_from_logits")
