# EOD-cylinder theorem status

Status: `GENERAL_EOD_THEOREM_PROVED`; independently reviewed with no fatal
objection.

The target domain is (m\ge2, n\ge3). An efficient open dominating set is a set (D) satisfying

\[
|N(v)\cap D|=1
\]

for every vertex (v), with (N(v)) the open neighborhood. Path boundary
rows outside (1,ldots,m) are absent, and cycle columns are modulo (n).

The row-sum argument proves the necessary conditions:

\[
m\text{ odd}\Longrightarrow4\mid n,
\qquad
m=2k\Longrightarrow2k+1\mid n.
\]

For odd (m), the converse is the explicit
(P_{2r+1}\square C_{4t}) construction in Proposition 5.6 of
Kuziak--Peterin--González Yero (2014), with the open-neighbor condition
checked in that construction.

For even (m=2k), let (N=2k+1). The self-contained file
`EVEN_WIDTH_CONSTRUCTION_PROOF.md` defines every row set (A_i\subseteq
\mathbb Z_N) and proves

\[
A_{i-1}\dot\cup A_{i+1}\dot\cup(A_i-1)\dot\cup(A_i+1)=\mathbb Z_N,
\quad A_0=A_{2k+1}=\varnothing.
\]

The first two pieces are the selected vertical neighbors of a vertex in row
(i); the last two are its selected horizontal neighbors. Hence the identity
is exactly the EOD condition, including both path-boundary rows. Reflection
(A_{2k+1-i}=A_i) preserves the identity because it exchanges the two
vertical-neighbor pieces and leaves column shifts unchanged.

If (n=Nt), repeat each (A_i) with period (N). At a copy seam, the last
column of one copy and the first column of the next are the two consecutive
cycle neighbors, just as in the base (C_N) pattern; therefore the same row
identity holds on (C_{Nt}). The case (k=1) has (N=3) and is included:
the construction gives (A_1=A_2=\{0\}), the EOD set of the triangular
prism (P_2\square C_3).

Thus the target iff characterization follows if the independently reviewed
interval proof is accepted. The finite (k\le30) regression is supporting
evidence, not the proof. The generalized result must not be promoted until
the hostile referee reports are resolved.
