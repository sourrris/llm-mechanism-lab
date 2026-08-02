import torch

from llm_mechanism_lab.model import MiniGPT, ModelConfig


def tiny_model(tie_weights=True):
    torch.manual_seed(0)
    return MiniGPT(ModelConfig(vocab_size=31, block_size=16, n_layers=2, n_heads=2, d_model=16, hidden_dim=32, tie_weights=tie_weights))


def test_logits_shape():
    model = tiny_model()
    ids = torch.randint(0, 31, (3, 7))
    assert model(ids).shape == (3, 7, 31)


def test_prefix_logits_are_causal():
    model = tiny_model().eval()
    ids = torch.randint(0, 31, (1, 8))
    changed = ids.clone(); changed[:, 6:] = (changed[:, 6:] + 1) % 31
    with torch.no_grad():
        a, b = model(ids), model(changed)
    assert torch.allclose(a[:, :6], b[:, :6], atol=1e-6)


def test_weight_tying():
    model = tiny_model(tie_weights=True)
    assert model.unembed.weight.data_ptr() == model.token_embedding.weight.data_ptr()
