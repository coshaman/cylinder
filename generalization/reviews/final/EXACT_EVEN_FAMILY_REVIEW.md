# Role C review: exact even-width family

## Verdict

**PASS.** The construction, its residue proof, the periodic lift, the
cardinality calculation, and the lower-bound matching are sufficient to prove
\[
\gamma_t(P_{2k}\mathbin{\square} C_{(2k+1)t})=k(k+1)t
\]
for all \(k,t\ge1\). No blocking or substantive minor mathematical defect was
found in the assigned exact-family argument.

This is a clean-room review of current statements, definitions, proof
artifacts, and reproducible checks in the authorized project. Development-
history reports and status summaries were not used as evidence.

## Dependency graph and classification

1. **EOD identity — justified.** In
   generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md:3-18,
   \[
   A_{i-1}\dot\cup A_{i+1}\dot\cup(A_i-1)\dot\cup(A_i+1)=\mathbb Z_N
   \]
   is exactly the one-open-selected-neighbor condition for row \(i\): the
   first two pieces are vertical selected neighbors and the last two are
   horizontal selected neighbors. The empty boundary rows correctly handle
   both path ends.

2. **Residue construction — justified.** The definitions at
   generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md:20-41 cover
   both \(k=2h\) and \(k=2h+1\), with \(k=1\) included in the latter case.
   The row reflection \(A_{2k+1-i}=A_i\) is well-defined and preserves the
   row identity by exchanging the two vertical pieces.

3. **\(U_r,V_r\) interval identities — justified.** The four-term grouping
   in generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md:63-103
   gives
   \[
   U_r=[1-2r,2r-1]_{\mathbb Z},\qquad
   V_r=[1-2r,2r]_{\mathbb Z}\cup\{-2r\}.
   \]
   The endpoint calculations account for the final element of \(E_r\) and
   the extra element of \(E_{r+1}\). The subsequent ranges never require an
   interval longer than the modulus, so reduction modulo \(N\) introduces
   exactly the stated seam residue and no unintended collision.

4. **Case \(k=2h\) row identities — justified.** The boundary identity
   (I0) is the partition into \(0\) and the consecutive blocks
   \([1,4],[5,8],\ldots,[4h-3,4h]\). For \(1\le r\le h\), the concatenation
   of \(C_{r-1},C_r\) with \(U_r\) has \(4h+1=N\) consecutive integer
   representatives, proving (I1). For \(1\le r<h\), the shifted \(C_r\)
   sets plus the interval part of \(V_r\) have \(N-1\) consecutive residues,
   and the singleton \(-2r\) fills the unique missing residue, proving (I2).
   The central row is the \(r=h\) instance of (I1). This is the calculation
   at generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md:124-153.

5. **Case \(k=2h+1\) row identities — justified.** For \(1\le r\le h\),
   the shifted \(D_r\) sets plus \(U_r\) form \(4h+3=N\) consecutive
   representatives. At \(r=h+1\), \(D_r=\varnothing\) and \(U_r\) itself
   has \(N\) entries. The \(D_r,D_{r+1}\) concatenation plus \(V_r\) fills
   \(N-1\) consecutive residues and then \(-2r\), proving the second row
   identity. The stated ranges cover the displayed half, and reflection
   covers the rest. Thus every base row satisfies the EOD identity. See
   generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md:155-187.

6. **Base-set cardinalities — justified.** The construction proof separates
   the nonwrapped \(E_r\) representatives from the \(C_r\) or \(D_r\)
   representatives, with strict endpoint separation. Hence
   \[
   |A_{2r}|=r,\quad
   |A_{2r+1}|=2h-r\ (k=2h),\quad
   |A_{2r-1}|=2h-r+2\ (k=2h+1).
   \]
   Direct summation on the displayed half gives \(k(k+1)/2\); reflection
   doubles it, so
   \[
   \sum_{i=1}^{2k}|A_i|=k(k+1).
   \]
   This agrees with
   generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md:43-61 and
   generalization/mathematics/EXACT_EVEN_WIDTH_FAMILY.md:10-17.

7. **Periodic lift — justified.** For \(N=2k+1\), define
   \[
   \widetilde A_i=\{a+qN\pmod{Nt}:a\in A_i,\ 0\le q<t\}.
   \]
   The map from a base representative \(a\in\{0,\ldots,N-1\}\) and copy
   \(q\) to \(a+qN\pmod{Nt}\) is injective on the stated ranges. Vertical
   pieces lift within the same copy. A horizontal shift across \(a=0\) or
   \(a=N-1\) lands in the preceding or following copy, respectively, with
   the wrap from copy \(0\) to copy \(t-1\) handled by modulo \(Nt\). Thus
   every base disjoint partition lifts to a disjoint partition on
   \(\mathbb Z_{Nt}\), including the global seam. The argument in
   generalization/mathematics/EXACT_EVEN_WIDTH_FAMILY.md:19-34 is correct.

8. **Matching lower bound — justified.** Substituting \(m=2k\) and
   \(n=(2k+1)t\) into the reviewed lower bound gives
   \[
   \frac{(2k)(2k+2)}{4(2k+1)}(2k+1)t=k(k+1)t.
   \]
   This is an integer, so the ceiling does not alter it. The lifted EOD set
   is a total dominating set of exactly this size; the lower bound applies to
   every total dominating set. Therefore the minimum equals this size.

## Independent checks

- The supplied current construction checker passes for \(k=1,\ldots,30\).
- An independently implemented verifier checked every lifted row partition and
  the cardinality for \(k=1,\ldots,40\) and \(t=1,\ldots,8\), including the
  \(k=1,N=3\) case. These checks are corroboration only; the all-\(k\) result
  rests on the symbolic residue proof.
- Small exhaustive total-domination computations were consistent with the
  lower bound, including the boundary cases \(m=2,3,4\) and \(n=3\).

## Findings

No error, gap, or unclear dependency remains in the assigned exact-family
proof. The odd-width family and its external prior citation are outside this
role's certification; this report therefore does not use them to establish
the even family.

## Suggested repair

No substantive repair is required. For maximum self-containment, the final
artifact may replace the phrase “conditional on the EOD construction” with an
explicit reference to the immediately preceding symbolic residue lemma, since
that lemma is present and proved in the current artifact set.
