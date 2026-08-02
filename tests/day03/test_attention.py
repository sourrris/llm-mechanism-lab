import math

import torch

from llm_mechanism_lab.attention import scaled_dot_product_attention
from llm_mechanism_lab.tensor_ops import causal_attention_mask


def test_attention_matches_reference():
    torch.manual_seed(0)
    q = torch.randn(2, 3, 4, 5, dtype=torch.float64)
    k = torch.randn(2, 3, 4, 5, dtype=torch.float64)
    v = torch.randn(2, 3, 4, 5, dtype=torch.float64)
    mask = causal_attention_mask(4)
    output, probabilities = scaled_dot_product_attention(q, k, v, mask)
    scores = q @ k.transpose(-2, -1) / math.sqrt(5)
    scores = scores.masked_fill(~mask, float("-inf"))
    expected_p = torch.softmax(scores, dim=-1)
    expected_o = expected_p @ v
    assert torch.allclose(probabilities, expected_p, atol=1e-10, rtol=1e-10)
    assert torch.allclose(output, expected_o, atol=1e-10, rtol=1e-10)


def test_future_values_cannot_change_earlier_output():
    torch.manual_seed(1)
    q = torch.randn(1, 1, 5, 4)
    k = torch.randn(1, 1, 5, 4)
    v = torch.randn(1, 1, 5, 4)
    mask = causal_attention_mask(5)
    original, _ = scaled_dot_product_attention(q, k, v, mask)
    changed_v = v.clone(); changed_v[:, :, 4] += 10_000
    changed, _ = scaled_dot_product_attention(q, k, changed_v, mask)
    assert torch.allclose(original[:, :, :4], changed[:, :, :4])


def test_probabilities_normalize():
    q = torch.zeros(1, 2, 3, 4)
    k = torch.zeros_like(q)
    v = torch.randn_like(q)
    _, p = scaled_dot_product_attention(q, k, v, causal_attention_mask(3))
    assert torch.allclose(p.sum(-1), torch.ones_like(p.sum(-1)))
