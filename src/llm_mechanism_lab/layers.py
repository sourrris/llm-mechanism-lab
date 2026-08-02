from __future__ import annotations

import torch
from torch import Tensor, nn


class RMSNorm(nn.Module):
    def __init__(self, d_model: int, eps: float = 1e-5) -> None:
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError("Day 04: implement RMSNorm")


class SwiGLU(nn.Module):
    def __init__(self, d_model: int, hidden_dim: int, bias: bool = False) -> None:
        super().__init__()
        self.gate = nn.Linear(d_model, hidden_dim, bias=bias)
        self.value = nn.Linear(d_model, hidden_dim, bias=bias)
        self.out = nn.Linear(hidden_dim, d_model, bias=bias)

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError("Day 04: implement SwiGLU")


def apply_rope(x: Tensor, positions: Tensor, base: float = 10_000.0) -> Tensor:
    """Apply rotary position embedding to the last dimension.

    x: [batch, heads, time, d_head], d_head must be even.
    positions: [time] integer or floating positions.
    """
    raise NotImplementedError("Day 04: implement RoPE")
