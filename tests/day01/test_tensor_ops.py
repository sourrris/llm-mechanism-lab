import torch
import torch.nn.functional as F

from llm_mechanism_lab.tensor_ops import (
    causal_attention_mask,
    cross_entropy_from_logits,
    stable_softmax,
)


def test_softmax_matches_torch_and_rows_sum_to_one():
    torch.manual_seed(0)
    x = torch.randn(4, 7, dtype=torch.float64)
    actual = stable_softmax(x, dim=-1)
    assert torch.allclose(actual, torch.softmax(x, dim=-1), atol=1e-10, rtol=1e-10)
    assert torch.allclose(actual.sum(dim=-1), torch.ones(4, dtype=x.dtype))


def test_softmax_is_finite_for_extreme_logits():
    x = torch.tensor([[10_000.0, 9_999.0, -10_000.0]])
    result = stable_softmax(x)
    assert torch.isfinite(result).all()
    assert torch.allclose(result.sum(-1), torch.ones(1))


def test_causal_mask_visibility():
    mask = causal_attention_mask(4)
    expected = torch.tensor(
        [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]],
        dtype=torch.bool,
    )
    assert mask.dtype == torch.bool
    assert mask.shape == (4, 4)
    assert torch.equal(mask.cpu(), expected)


def test_cross_entropy_matches_pytorch():
    torch.manual_seed(1)
    logits = torch.randn(2, 3, 11, dtype=torch.float64)
    targets = torch.randint(0, 11, (2, 3))
    actual = cross_entropy_from_logits(logits, targets)
    expected = F.cross_entropy(logits.reshape(-1, 11), targets.reshape(-1))
    assert torch.allclose(actual, expected, atol=1e-10, rtol=1e-10)
