import torch

from llm_mechanism_lab.optim import AdamW


def test_first_step_matches_torch_adamw():
    p1 = torch.tensor([1.0, -2.0], requires_grad=True)
    p2 = p1.detach().clone().requires_grad_(True)
    p1.grad = torch.tensor([0.3, -0.4])
    p2.grad = p1.grad.clone()
    ours = AdamW([p1], lr=1e-2, betas=(0.9, 0.99), eps=1e-8, weight_decay=0.1)
    reference = torch.optim.AdamW([p2], lr=1e-2, betas=(0.9, 0.99), eps=1e-8, weight_decay=0.1)
    ours.step(); reference.step()
    assert torch.allclose(p1, p2, atol=1e-7, rtol=1e-7)


def test_optimizer_reduces_quadratic():
    p = torch.tensor([5.0], requires_grad=True)
    optimizer = AdamW([p], lr=0.1, weight_decay=0.0)
    start = p.square().item()
    for _ in range(100):
        optimizer.zero_grad()
        loss = p.square().sum()
        loss.backward()
        optimizer.step()
    assert p.square().item() < start * 0.01
