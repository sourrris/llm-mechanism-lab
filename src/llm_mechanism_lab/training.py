from __future__ import annotations

from collections.abc import Iterable

import torch
from torch import Tensor, nn

from .optim import AdamW


def next_token_batch(token_ids: Tensor) -> tuple[Tensor, Tensor]:
    """Split [batch, time] token IDs into shifted inputs and targets.

    For ``[t0, t1, t2, t3]`` the model input is ``[t0, t1, t2]`` and the
    corresponding targets are ``[t1, t2, t3]``.
    """
    raise NotImplementedError("Day 06: implement the autoregressive shift")


def next_token_loss(model: nn.Module, token_ids: Tensor) -> Tensor:
    """Run the shifted batch and return mean next-token cross-entropy."""
    raise NotImplementedError("Day 06: connect model logits to shifted targets")


def global_grad_norm(parameters: Iterable[Tensor]) -> Tensor:
    """Return the L2 norm over all existing parameter gradients."""
    raise NotImplementedError("Day 06: implement global gradient norm")


def clip_grad_norm(parameters: Iterable[Tensor], max_norm: float) -> Tensor:
    """Clip gradients in place and return their norm before clipping."""
    raise NotImplementedError("Day 06: implement global gradient clipping")


def train_step(
    model: nn.Module,
    token_ids: Tensor,
    optimizer: AdamW,
    max_grad_norm: float | None = 1.0,
) -> tuple[float, float]:
    """Perform one optimization step and return ``(loss, grad_norm)``.

    Required order: zero gradients, forward loss, backward, optional clipping,
    optimizer step. Explain what changes if any adjacent pair is swapped.
    """
    raise NotImplementedError("Day 06: implement one complete training step")
