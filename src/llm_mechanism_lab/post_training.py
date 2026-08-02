from __future__ import annotations

import torch
from torch import Tensor


def dpo_loss(
    policy_chosen_logp: Tensor,
    policy_rejected_logp: Tensor,
    reference_chosen_logp: Tensor,
    reference_rejected_logp: Tensor,
    beta: float = 0.1,
) -> Tensor:
    """Return mean DPO loss for paired sequence log-probabilities."""
    raise NotImplementedError("Day 12: implement DPO loss")
