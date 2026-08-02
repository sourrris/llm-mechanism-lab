# Mathematical crash sheet

## Shapes

For batch `B`, sequence `T`, model width `D`, heads `H`, head width `Dh = D/H`, vocabulary `V`:

```text
IDs               [B, T]
Embeddings X      [B, T, D]
W_Q, W_K, W_V     [D, H*Dh]
Q, K, V           [B, H, T, Dh]
Scores            [B, H, T, T]
Attention probs   [B, H, T, T]
Head outputs      [B, H, T, Dh]
Concatenated      [B, T, D]
Logits            [B, T, V]
```

## Stable softmax

\[
\operatorname{softmax}(z)_i = \frac{e^{z_i-m}}{\sum_j e^{z_j-m}},\quad m=\max_j z_j
\]

Adding the same constant to all logits leaves probabilities unchanged.

## Attention

\[
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
\]

\[
A=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_h}}+M\right),\quad O=AV
\]

## Cross-entropy

For target token `y`:

\[
L=-\log p_y=-z_y+\log\sum_j e^{z_j}
\]

## RMSNorm

\[
\operatorname{RMSNorm}(x)=g\odot\frac{x}{\sqrt{\frac{1}{D}\sum_i x_i^2+\epsilon}}
\]

## DPO

For policy `π`, reference `π_ref`, chosen `y_w`, rejected `y_l`:

\[
r=\beta\left[(\log\pi(y_w|x)-\log\pi(y_l|x))-(\log\pi_{ref}(y_w|x)-\log\pi_{ref}(y_l|x))\right]
\]

\[
L_{DPO}=-\log\sigma(r)
\]

Derive these rather than memorizing symbols without their computational role.
