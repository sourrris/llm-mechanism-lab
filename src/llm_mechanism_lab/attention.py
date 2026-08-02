from __future__ import annotations

import math

import torch
from torch import Tensor, nn

from .tensor_ops import causal_attention_mask, stable_softmax


def scaled_dot_product_attention(
    q: Tensor,
    k: Tensor,
    v: Tensor,
    mask: Tensor | None = None,
) -> tuple[Tensor, Tensor]:
    """Return (output, attention_probabilities).

    q, k, v: [batch, heads, time, d_head]
    mask: broadcastable boolean mask where True means visible.
    """
    raise NotImplementedError("Day 03: implement scaled dot-product attention")


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int, bias: bool = False) -> None:
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=bias)
        self.out = nn.Linear(d_model, d_model, bias=bias)

    def forward(self, x: Tensor) -> tuple[Tensor, Tensor]:
        """Causal self-attention over x shaped [batch, time, d_model]."""
        raise NotImplementedError("Day 04: implement multi-head attention")
