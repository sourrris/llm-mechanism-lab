from __future__ import annotations

import torch
from torch import Tensor


def filtered_probabilities(
    logits: Tensor,
    temperature: float = 1.0,
    top_k: int | None = None,
    top_p: float | None = None,
) -> Tensor:
    """Convert one or more logit rows to a filtered probability distribution."""
    raise NotImplementedError("Day 07: implement temperature/top-k/top-p filtering")


@torch.no_grad()
def generate(
    model: torch.nn.Module,
    token_ids: Tensor,
    max_new_tokens: int,
    temperature: float = 1.0,
    top_k: int | None = None,
    top_p: float | None = None,
    generator: torch.Generator | None = None,
) -> Tensor:
    """Autoregressively append sampled tokens."""
    raise NotImplementedError("Day 07: implement generation")
