# A general lower bound for total domination

Let (n\ge3). Let (D) be any total dominating set of (P_m\square C_n),
and let (d_i=|D\cap(\{i\}\times C_n)|), with (d_0=d_{m+1}=0). Summing
the at-least-one domination condition over row (i) gives

\[
2d_i+d_{i-1}+d_{i+1}\ge n. \tag{1}
\]

Let (y=B_m^{-1}\mathbf1). By `EOD_LINEAR_SYSTEM.md` and
`EVEN_WIDTH_DIVISIBILITY.md`, the explicit solutions below have (y_i\ge0),
so multiplying (1) by (y_i) and summing preserves the inequality:

\[
|D|=\mathbf1^Td=y^TB_md
\ge n\,\mathbf1^Ty. \tag{2}
\]

If (m=2k+1), define (z_i=1/2) for odd (i) and (z_i=0) for even
(i). With (z_0=z_{m+1}=0), direct substitution gives
(2z_i+z_{i-1}+z_{i+1}=1) at every row, including the boundaries.
Uniqueness of the row system therefore gives (y=z), so the odd-width
solution gives

\[
\mathbf1^Ty=\frac{k+1}{2}=\frac{m+1}{4}.
\]

If (m=2k), the even-width solution gives

\[
\mathbf1^Ty=\frac{\sum_i a_i}{2k+1}
=\frac{k(k+1)}{2k+1}
=\frac{m(m+2)}{4(m+1)}.
\]

Since (|D|) is an integer,

\[
\boxed{\gamma_t(P_m\square C_n)\ge
\begin{cases}
\left\lceil\dfrac{m+1}{4}n\right\rceil,&m\text{ odd},\\[2mm]
\left\lceil\dfrac{m(m+2)}{4(m+1)}n\right\rceil,&m\text{ even}.
\end{cases}}
\]

For even (m), every coordinate of (y) is positive because every
(a_i>0). Thus equality in the unrounded bound forces equality in every
row inequality (1). Each row inequality is a sum of nonnegative integer
slacks over the vertices of that row, so every individual vertex has exactly
one selected neighbor. Consequently equality at the unrounded bound implies
that (D) is an EOD set.
