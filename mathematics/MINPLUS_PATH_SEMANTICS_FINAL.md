# Final Task B — min-plus path semantics

Status: `PASS`.

Let (Q) be the finite state set and let (M_{uv}) be the edge weight, or
(+\infty) when no edge exists. Define (M^0) with zero diagonal and
(+\infty) off diagonal, and (M^{k+1}=M^k\otimes M).

For every (k\ge0),

\[
(M^k)_{uv}=\min\{\text{weight of a length-}k\text{ walk from }u\text{ to }v\}.
\]

For (k=0), this is exactly the identity convention. For the induction step,
partition every length-(k+1) walk by its unique penultimate state (x).
The minimum prefix cost is ((M^k)_{ux}), the final edge contributes
(M_{xv}), and taking the finite minimum over (x\in Q) gives

\[
\min_x\bigl((M^k)_{ux}\otimes M_{xv}\bigr)=(M^{k+1})_{uv}.
\]

The (+\infty) value is absorbing, so missing prefixes and missing edges are
handled exactly. Combining this lemma with the Task A bijection gives

\[
\gamma_t(P_m\square C_n)=\min_q(M_m^n)_{qq},
\qquad n\ge3.
\]
