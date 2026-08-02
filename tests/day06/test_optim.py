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

from torch import nn

from llm_mechanism_lab.training import (
    clip_grad_norm,
    global_grad_norm,
    next_token_batch,
    next_token_loss,
    train_step,
)


def test_next_token_batch_shifts_by_one():
    ids = torch.tensor([[4, 7, 2, 9], [1, 3, 5, 8]])
    inputs, targets = next_token_batch(ids)
    assert torch.equal(inputs, ids[:, :-1])
    assert torch.equal(targets, ids[:, 1:])


class NextTokenOracle(nn.Module):
    def __init__(self, vocab_size: int = 11) -> None:
        super().__init__()
        self.vocab_size = vocab_size

    def forward(self, ids):
        b, t = ids.shape
        logits = torch.full((b, t, self.vocab_size), -20.0)
        predicted = (ids + 1) % self.vocab_size
        return logits.scatter(-1, predicted.unsqueeze(-1), 20.0)


def test_next_token_loss_uses_shifted_targets():
    ids = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
    loss = next_token_loss(NextTokenOracle(), ids)
    assert loss.item() < 1e-6


def test_global_norm_and_clipping_are_joint_across_parameters():
    a = torch.tensor([0.0, 0.0], requires_grad=True)
    b = torch.tensor([0.0], requires_grad=True)
    a.grad = torch.tensor([3.0, 4.0])
    b.grad = torch.tensor([12.0])
    norm = global_grad_norm([a, b])
    assert torch.allclose(norm, torch.tensor(13.0))
    before = clip_grad_norm([a, b], max_norm=6.5)
    assert torch.allclose(before, torch.tensor(13.0))
    assert torch.allclose(global_grad_norm([a, b]), torch.tensor(6.5), atol=1e-5)


class TinyNextModel(nn.Module):
    def __init__(self, vocab_size: int = 6, d_model: int = 12) -> None:
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.output = nn.Linear(d_model, vocab_size)

    def forward(self, ids):
        return self.output(self.embedding(ids))


def test_train_step_reduces_fixed_batch_loss():
    torch.manual_seed(3)
    model = TinyNextModel()
    batch = torch.tensor([[0, 1, 2, 3, 4, 5]]).repeat(8, 1)
    optimizer = AdamW(model.parameters(), lr=0.05, weight_decay=0.0)
    start = next_token_loss(model, batch).item()
    last = start
    for _ in range(80):
        last, grad_norm = train_step(model, batch, optimizer, max_grad_norm=1.0)
        assert grad_norm >= 0 and torch.isfinite(torch.tensor(grad_norm))
    assert last < start * 0.15
