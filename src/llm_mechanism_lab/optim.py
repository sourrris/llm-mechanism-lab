from __future__ import annotations

import math
from collections.abc import Iterable

import torch
from torch import Tensor


class AdamW:
    """Small educational AdamW implementation.

    Implement parameter groups only if needed. The required path accepts an
    iterable of tensors and supports lr, betas, eps and weight_decay.
    """

    def __init__(
        self,
        params: Iterable[Tensor],
        lr: float = 3e-4,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-8,
        weight_decay: float = 0.01,
    ) -> None:
        self.params = list(params)
        self.lr = lr
        self.betas = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.step_number = 0
        self.m = [torch.zeros_like(p) for p in self.params]
        self.v = [torch.zeros_like(p) for p in self.params]

    @torch.no_grad()
    def step(self) -> None:
        raise NotImplementedError("Day 06: implement AdamW.step")

    def zero_grad(self) -> None:
        for parameter in self.params:
            parameter.grad = None
