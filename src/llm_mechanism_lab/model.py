from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import Tensor, nn

from .attention import MultiHeadAttention
from .layers import RMSNorm, SwiGLU


@dataclass(frozen=True)
class ModelConfig:
    vocab_size: int
    block_size: int = 128
    n_layers: int = 4
    n_heads: int = 4
    d_model: int = 128
    hidden_dim: int = 384
    bias: bool = False
    tie_weights: bool = True


class TransformerBlock(nn.Module):
    def __init__(self, config: ModelConfig) -> None:
        super().__init__()
        self.norm1 = RMSNorm(config.d_model)
        self.attn = MultiHeadAttention(config.d_model, config.n_heads, config.bias)
        self.norm2 = RMSNorm(config.d_model)
        self.mlp = SwiGLU(config.d_model, config.hidden_dim, config.bias)

    def forward(self, x: Tensor) -> Tensor:
        raise NotImplementedError("Day 05: implement a pre-norm transformer block")


class MiniGPT(nn.Module):
    def __init__(self, config: ModelConfig) -> None:
        super().__init__()
        self.config = config
        self.token_embedding = nn.Embedding(config.vocab_size, config.d_model)
        self.blocks = nn.ModuleList([TransformerBlock(config) for _ in range(config.n_layers)])
        self.final_norm = RMSNorm(config.d_model)
        self.unembed = nn.Linear(config.d_model, config.vocab_size, bias=False)
        if config.tie_weights:
            self.unembed.weight = self.token_embedding.weight

    def forward(self, token_ids: Tensor) -> Tensor:
        """Return logits shaped [batch, time, vocab]."""
        raise NotImplementedError("Day 05: implement MiniGPT.forward")
