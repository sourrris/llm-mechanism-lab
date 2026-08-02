import torch
import torch.nn.functional as F

from llm_mechanism_lab.post_training import dpo_loss


def test_dpo_matches_definition():
    pc = torch.tensor([-1.0, -2.0])
    pr = torch.tensor([-2.0, -1.5])
    rc = torch.tensor([-1.4, -2.2])
    rr = torch.tensor([-1.8, -1.6])
    beta = 0.3
    logit = beta * ((pc - pr) - (rc - rr))
    expected = -F.logsigmoid(logit).mean()
    assert torch.allclose(dpo_loss(pc, pr, rc, rr, beta), expected)


def test_better_chosen_margin_reduces_loss():
    base = dpo_loss(torch.tensor([0.0]), torch.tensor([0.0]), torch.tensor([0.0]), torch.tensor([0.0]))
    improved = dpo_loss(torch.tensor([2.0]), torch.tensor([-2.0]), torch.tensor([0.0]), torch.tensor([0.0]))
    assert improved < base
