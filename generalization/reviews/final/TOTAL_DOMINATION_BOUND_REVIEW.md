# Role C review: total-domination lower bound

## Verdict

**PASS.** The claimed lower bound is proved for \(m\ge 2,\ n\ge 3\). The
even-width equality implication used by the exact-family argument is also
valid. I found no blocking or substantive minor mathematical defect in the
assigned material.

This is a clean-room review of the current mathematical artifacts and the
current manuscript only. Development-history reports and status summaries
were not used as evidence.

## Frozen claims reviewed

For every total dominating set \(D\subseteq P_m\mathbin{\square} C_n\), with
\(d_i=|D\cap(\{i\}\mathbin{\times} C_n)|\), \(d_0=d_{m+1}=0\),

\[
\gamma_t(P_m\mathbin{\square} C_n)\ge
\begin{cases}
\left\lceil (m+1)n/4\right\rceil,&m\text{ odd},\\
\left\lceil m(m+2)n/[4(m+1)]\right\rceil,&m\text{ even}.
\end{cases}
\]

The assigned exact-family claim is

\[
\gamma_t(P_{2k}\mathbin{\square} C_{(2k+1)t})=k(k+1)t,
\qquad k,t\ge1.
\]

## Dependency graph and classification

1. **Row domination inequalities — justified.** In
   generalization/mathematics/TOTAL_DOMINATION_LOWER_BOUND.md:3-8, every
   vertex in row \(i\) has at least one selected open neighbor. Summing over
   the row gives
   \(2d_i+d_{i-1}+d_{i+1}\ge n\): each selected vertex in row \(i\)
   contributes to two distinct horizontal neighbors because \(n\ge3\), and
   selected vertices in adjacent path rows contribute vertically.

2. **Tridiagonal operator and dual identity — justified.** The matrix
   \(B_m\) has diagonal \(2\), adjacent entries \(1\), and is symmetric.
   Thus \(B_md\) is exactly the vector of row left sides, while
   \(\mathbf1^{\mathsf T}d=y^{\mathsf T}B_md\) whenever
   \(B_my=\mathbf1\). The uniqueness/positive-definiteness argument in
   generalization/mathematics/EOD_LINEAR_SYSTEM.md:21-32 is valid since
   \[
   z^{\mathsf T}B_mz=\sum_{i=0}^m(z_i+z_{i+1})^2>0
   \]
   for a nonzero vector with \(z_0=z_{m+1}=0\).

3. **Odd-width dual vector — justified.** The vector with value \(1/2\) on
   odd rows and \(0\) on even rows satisfies \(B_my=\mathbf1\), including
   the two boundary rows. Its sum is
   \((k+1)/2=(m+1)/4\) for \(m=2k+1\), as recorded at
   generalization/mathematics/TOTAL_DOMINATION_LOWER_BOUND.md:20-28.

4. **Even-width dual vector — justified.** For \(m=2k\), the displayed
   integers \(a_i\) satisfy \(B_ma=(2k+1)\mathbf1\), including the boundary
   and central equations, as checked in
   generalization/mathematics/EVEN_WIDTH_DIVISIBILITY.md:15-37.
   Therefore \(y_i=a_i/(2k+1)\). Every \(a_i>0\): for \(k=1\), both entries
   equal \(1\); for \(k\ge2\), \(a_2=1\), and all displayed values and their
   reflections are positive.

5. **Nonnegative multiplication — justified.** Since \(B_md\ge n\mathbf1\)
   componentwise and \(y\ge0\), multiplication and summation preserve the
   inequality:
   \[
   |D|=y^{\mathsf T}B_md\ge n\,\mathbf1^{\mathsf T}y.
   \]
   No strict positivity is needed for the lower bound.

6. **Even sum evaluation — justified.** Reflection pairs the first \(k\)
   entries with the last \(k\). The first-half sum is
   \(k(k+1)/2\), hence
   \[
   \sum_i y_i=\frac{k(k+1)}{2k+1}
   =\frac{m(m+2)}{4(m+1)}.
   \]
   This is the calculation at
   generalization/mathematics/TOTAL_DOMINATION_LOWER_BOUND.md:30-35.

7. **Ceiling step — justified.** Since \(|D|\) is an integer and is at
   least the displayed rational quantity, \(|D|\ge\lceil\cdot\rceil\).
   Minimizing over all total dominating sets gives the stated bound. The
   inequality direction is unchanged; no integrality assumption on the
   rational lower-bound expression is made.

8. **Equality implication for even width — justified.** When \(m=2k\), all
   \(y_i>0\). Equality in the unrounded dual inequality makes every
   nonnegative row slack zero. Each row slack is the sum, over that row, of
   the nonnegative integer quantities \(|N(v)\cap D|-1\). Therefore every
   vertex has exactly one selected open neighbor, so \(D\) is an EOD set.
   This is valid at both path boundaries because \(d_0=d_{m+1}=0\).

## Independent checks

- Exact rational arithmetic independently verified \(B_my=\mathbf1\),
  \(y\ge0\), and the two stated sums for every \(2\le m\le100\).
- Exhaustive enumeration independently checked the lower-bound inequality
  for \((m,n)=(2,3\ldots8),(3,3\ldots6),(4,3\ldots5)\). These checks are
  corroboration only and are not used as the proof.

## Findings

No error, gap, or unclear dependency remains in the assigned lower-bound
argument. The review does not certify the separate odd-width literature
citation or the fixed-width certificate-backed formulas.

## Optional editorial clarification

The standalone lower-bound artifact could state \(m\ge2\) explicitly in its
first sentence, rather than leaving that restriction to the frozen theorem
statement. This is not a mathematical defect in the reviewed theorem.
