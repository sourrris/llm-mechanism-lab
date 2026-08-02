import torch

from llm_mechanism_lab.attention import MultiHeadAttention
from llm_mechanism_lab.layers import RMSNorm, SwiGLU, apply_rope


def test_rmsnorm_unit_rms_with_unit_weights():
    torch.manual_seed(0)
    layer = RMSNorm(8, eps=1e-8)
    x = torch.randn(3, 5, 8) * 7
    y = layer(x)
    rms = y.pow(2).mean(-1).sqrt()
    assert torch.allclose(rms, torch.ones_like(rms), atol=1e-5)


def test_swiglu_shape_and_gradients():
    layer = SwiGLU(8, 24)
    x = torch.randn(2, 4, 8, requires_grad=True)
    y = layer(x)
    assert y.shape == x.shape
    y.sum().backward()
    assert x.grad is not None and torch.isfinite(x.grad).all()


def test_rope_preserves_norm_and_position_zero():
    torch.manual_seed(1)
    x = torch.randn(2, 3, 5, 8)
    positions = torch.arange(5)
    y = apply_rope(x, positions)
    assert y.shape == x.shape
    assert torch.allclose(y.norm(dim=-1), x.norm(dim=-1), atol=1e-5)
    assert torch.allclose(y[:, :, 0], x[:, :, 0], atol=1e-6)


def test_multihead_shape_and_causality():
    torch.manual_seed(2)
    layer = MultiHeadAttention(12, 3)
    x = torch.randn(2, 6, 12)
    y, p = layer(x)
    assert y.shape == x.shape
    assert p.shape == (2, 3, 6, 6)
    assert torch.equal(p.triu(diagonal=1), torch.zeros_like(p).triu(diagonal=1))
