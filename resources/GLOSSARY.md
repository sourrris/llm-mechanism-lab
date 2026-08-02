# Mechanism glossary

- **Activation:** an intermediate tensor value produced during a forward pass.
- **Ablation:** an intervention that removes or replaces a component/activation to test causal relevance.
- **Attention pattern:** normalized query-key routing weights across source positions.
- **Circuit:** a causally relevant component subgraph for a defined behaviour and input distribution.
- **Clean/corrupted pair:** matched inputs where the target behaviour succeeds/fails, used for causal patching.
- **Decodability:** information can be recovered by a readout; this alone does not prove causal use.
- **Direct logit attribution:** a decomposition of residual/component contributions to token logits under specified linear operations.
- **Hook:** a programmatic point used to observe or modify an intermediate activation.
- **Logit:** an unnormalized score for an output token.
- **Mechanistic faithfulness:** whether an interpretability approximation uses the same relevant computation as the original model.
- **Residual stream:** the shared vector state updated by attention and MLP sublayers across depth.
- **RoPE:** rotary position embedding applied to query/key coordinates.
- **SAE:** sparse autoencoder used to decompose activations into learned sparse features.
- **SFT:** supervised fine-tuning on demonstrated input-response pairs.
- **Tokenization:** deterministic mapping between text/bytes and token IDs.
- **Unembedding:** projection from final hidden state to vocabulary logits.
