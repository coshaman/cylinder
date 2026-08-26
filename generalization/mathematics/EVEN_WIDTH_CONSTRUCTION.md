# Even-width EOD construction

Let (k\ge1), (N=2k+1), and identify the cycle columns with
(\mathbb Z_N). Define

\[
E_0=\varnothing,qquad
E_r=\{2(r-1)-4t\pmod N:0\le t<r\}.
\]

If (k=2h), define (A_{2r}=E_r) for (1\le r\le h), and

\[
A_{2r+1}=E_r\cup
\bigcup_{t=0}^{h-r-1}\{2r+2+4t,2r+3+4t\},
\qquad0\le r<h.
\]

If (k=2h+1), define (A_{2r}=E_r) for (1\le r\le h), and

\[
A_{2r-1}=E_r\cup
\bigcup_{t=0}^{h-r}\{2r+1+4t,2r+2+4t\},
\qquad1\le r\le h+1.
\]

In both cases set (A_{2k+1-i}=A_i), and let

\[
D_k=\{(i,j):1\le i\le2k, j\in A_i\}.
\]

The complete all-(k) proof that (D_k) is EOD is in
`EVEN_WIDTH_CONSTRUCTION_PROOF.md`. It proves the row identity

\[
A_{i-1}\dot\cup A_{i+1}\dot\cup(A_i-1)\dot\cup(A_i+1)
=\mathbb Z_N,
\]

including (k=1,N=3), both path boundaries, and the reflected rows.
