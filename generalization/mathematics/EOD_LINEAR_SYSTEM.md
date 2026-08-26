# The EOD row-sum system

Let (D) be an efficient open dominating set in
(P_m\square C_n). Write (x_{i,j}=1) when ((i,j)\in D), and (0)
otherwise, with (j\in\mathbb Z_n) and (x_{0,j}=x_{m+1,j}=0). Every vertex
has exactly one selected open neighbor, so

\[
x_{i-1,j}+x_{i+1,j}+x_{i,j-1}+x_{i,j+1}=1. \tag{1}
\]

Define (s_i=\sum_{j\in\mathbb Z_n}x_{i,j}), and set (s_0=s_{m+1}=0).
Summing (1) over (j) gives

\[
s_{i-1}+s_{i+1}+2s_i=n,
\qquad 1\le i\le m, 
\tag{2}
\]

because the two cycle neighbors are distinct for (n\ge3). In matrix form,
(B_ms=n\mathbf 1), where (B_m) has diagonal (2), adjacent entries
(1), and zero elsewhere.

The matrix is positive definite: for (z_0=z_{m+1}=0),

\[
z^TB_mz
=\sum_{i=0}^{m}(z_i+z_{i+1})^2>0
\]

for every nonzero (z). Hence (2) has a unique solution.

This proves the row-sum necessity without using any construction or finite
search.
