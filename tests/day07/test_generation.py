import torch
from torch import nn

from llm_mechanism_lab.generation import filtered_probabilities, generate


def test_temperature_and_normalization():
    logits = torch.tensor([[1.0, 2.0, 3.0]])
    cold = filtered_probabilities(logits, temperature=0.2)
    hot = filtered_probabilities(logits, temperature=2.0)
    assert torch.allclose(cold.sum(-1), torch.ones(1))
    assert torch.allclose(hot.sum(-1), torch.ones(1))
    assert cold.max() > hot.max()


def test_top_k_keeps_only_k_tokens():
    logits = torch.tensor([[1.0, 2.0, 3.0, 4.0]])
    p = filtered_probabilities(logits, top_k=2)
    assert (p > 0).sum().item() == 2


def test_top_p_keeps_minimal_nucleus():
    logits = torch.log(torch.tensor([[0.5, 0.3, 0.15, 0.05]]))
    p = filtered_probabilities(logits, top_p=0.75)
    assert (p > 0).sum().item() == 2
    assert torch.allclose(p.sum(-1), torch.ones(1))


class DeterministicNext(nn.Module):
    def forward(self, ids):
        b, t = ids.shape
        logits = torch.full((b, t, 5), -1000.0)
        next_id = (ids[:, -1] + 1) % 5
        logits[torch.arange(b), -1, next_id] = 1000.0
        return logits


def test_generate_appends_tokens():
    ids = torch.tensor([[0, 1]])
    result = generate(DeterministicNext(), ids, max_new_tokens=3, temperature=1.0)
    assert result.tolist() == [[0, 1, 2, 3, 4]]
