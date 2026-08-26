# Independent proof-referee report: even-width construction

## Scope and verdict

**Mode:** \`FULL_SYMBOLIC_PROOF\`  
**Verdict:** \`PASS\`  
**Severity:** no minor or fatal finding.

I reviewed only the frozen definitions and proof in
\`generalization/mathematics/EVEN_WIDTH_CONSTRUCTION.md\` and
\`generalization/mathematics/EVEN_WIDTH_CONSTRUCTION_PROOF.md\`. No
development-history material or neighboring project was used.

The asserted identity is correct for every \(k\geq 1\), including the
endpoint cases and \(k=1\). The proof's interval arguments do establish
disjointness modulo \(N\), not merely coverage.

## Dependency and step classification

1. **Definitions \(\to\) EOD identity — justified.** For a vertex in row
   \(i\), the four possible selected open neighbors are exactly the
   columns in \(A_{i-1}\), \(A_{i+1}\), \(A_i-1\), and \(A_i+1\), with
   \(A_0=A_{2k+1}=\varnothing\). Thus the displayed disjoint-union
   identity is equivalent to efficient open domination.
2. **Set descriptions \(E_r,C_r,D_r\) — justified.** The claimed internal
   disjointness follows from the stated before/after-wrap comparisons;
   the bounds are valid in both moduli.
3. **The auxiliary identities \(U_r,V_r\) — justified independently
   below.** Their relevant interval lengths are at most \(N\), so the
   displayed representatives cannot create an unexamined modular
   collision.
4. **Parity-specific concatenations and row ranges — justified.** The
   ranges cover exactly the displayed half, including the central row and
   the boundary row.
5. **Reflection — justified.** Reflection swaps the two vertical-neighbor
   sets and preserves the horizontal shifts, so it transfers the identities
   to the remaining rows, including the opposite path boundary.

No step is merely \`cited\`, \`gap\`, \`error\`, or \`unclear\`; there is no
external citation on which this construction proof depends.

## Independent symbolic derivation

All intervals below are integer intervals whose elements are then reduced
modulo the relevant odd modulus. Write

\[
 E_r=\{2r-2-4t:0\le t<r\}.
\]
For \(r\ge1\), form

\[
 U_r=E_{r-1}\cup E_r\cup(E_r-1)\cup(E_r+1),
\]
\[
 V_r=E_r\cup E_{r+1}\cup(E_r-1)\cup(E_r+1).
\]

For \(0\le t<r-1\), the four terms with that \(t\), in increasing order,
are

\[
 2r-4-4t,\quad 2r-3-4t,\quad 2r-2-4t,\quad 2r-1-4t.
\]

They form consecutive blocks. The remaining three terms from \(E_r\) and
its shifts are

\[
 1-2r,\quad 2-2r,\quad 3-2r,
\]

which attach to the last block. Therefore

\[
 U_r=[1-2r,\,2r-1]. \tag{U}
\]

The additional set \(E_{r+1}\) contributes, relative to \(U_r\), exactly
the two new endpoints \(-2r\) and \(2r\). Hence

\[
 V_r=[1-2r,\,2r]\cup\{-2r\}. \tag{V}
\]

For Case I, \(N=4h+1\), \(r\le h\) in (U), so the interval in (U) has
length \(4r-1\le4h-1<N\). For (V), \(r<h\), and the interval has length
\(4r<N\); moreover \(-2r\) differs from every integer in
\([1-2r,2r]\) by a positive integer between \(1\) and \(4r<N\), so it is a
new residue. For Case II, \(N=4h+3\), \(r\le h+1\) in (U), and the only
length-\(N\) instance is \(r=h+1\); in (V), \(r\le h\), so the interval
length is \(4r<N\) and the singleton is distinct. Thus (U) and (V) are
valid residue-set identities in every use below.

### Case I: \(k=2h\), \(N=4h+1\)

Here \(C_r=J(2r+2,h-r)\), where

\[
 J(a,q)=\{a+4t,a+1+4t:0\le t<q\}.
\]

**Boundary row.** \(C_0-1\) and \(C_0+1\) interlace to give

\[
 [1,4]\cup[5,8]\cup\cdots\cup[4h-3,4h]=[1,4h],
\]

and \(E_1=\{0\}\). These are all \(4h+1\) residues, proving (I0).

**Even displayed rows.** For \(1\le r\le h\),

\[
 C_{r-1}=J(2r,h-r+1),\qquad C_r=J(2r+2,h-r).
\]

Their pairs interlace and concatenate to

\[
 C_{r-1}\cup C_r=[2r,\,4h-2r+1].
\]

Combining this with (U) gives the consecutive integer interval

\[
 [1-2r,\,4h-2r+1],
\]

whose length is \(4h+1=N\). This proves (I1), including the central
instance \(r=h\) (where \(C_h=\varnothing\)).

**Odd displayed rows after the boundary.** For \(1\le r<h\), shifting the
two interlacing blocks gives

\[
 (C_r-1)\cup(C_r+1)=[2r+1,\,4h-2r].
\]

The interval part of (V) joins it to

\[
 [1-2r,\,4h-2r],
\]

which has \(4h=N-1\) consecutive integers. Its next integer is
\(4h-2r+1\equiv-2r\pmod{4h+1}\), exactly the singleton in (V). This
proves (I2). The omitted \(r=0\) case is precisely the already checked
boundary identity (I0). When \(h=1\), this range is empty, as required.

Thus (I0), (I1), and (I2) cover rows \(1,\ldots,2h\).

### Case II: \(k=2h+1\), \(N=4h+3\)

Here \(D_r=J(2r+1,h-r+1)\).

**Odd displayed rows.** For \(1\le r\le h\),

\[
 (D_r-1)\cup(D_r+1)=[2r,\,4h-2r+3].
\]

Combining with (U) yields

\[
 [1-2r,\,4h-2r+3],
\]

of length \(4h+3=N\), proving (II1). At the endpoint \(r=h+1\),
\(D_{h+1}=\varnothing\) and (U) is

\[
 U_{h+1}=[-2h-1,\,2h+1],
\]

again of length \(4h+3=N\). This is the central odd row. In particular,
when \(h=0\) (that is, \(k=1,N=3\)), it is exactly
\([-1,1]\pmod 3=\mathbb Z_3\).

**Even displayed rows.** For \(1\le r\le h\), the two unshifted blocks
interlace as

\[
 D_r\cup D_{r+1}=[2r+1,\,4h-2r+2].
\]

The interval part of (V) joins this to

\[
 [1-2r,\,4h-2r+2],
\]

which has \(4h+2=N-1\) consecutive integers. The next residue is

\[
 4h-2r+3\equiv-2r\pmod{4h+3},
\]

the singleton in (V). This proves (II2). For \(h=0\), the range is empty,
which is correct.

Thus (II1) and (II2) cover rows \(1,\ldots,2h+1\).

## Reflection and final EOD conclusion

Let \(R(i)=2k+1-i\). From \(A_{R(i)}=A_i\), the row identity at \(R(i)\)
has the same four residue sets as the identity at \(i\), with the two
vertical sets exchanged:

\[
 A_{R(i)-1}=A_{i+1},\qquad A_{R(i)+1}=A_{i-1},\qquad
 A_{R(i)}\pm1=A_i\pm1.
\]

For \(i=1\), this also uses \(A_0=\varnothing\) and transfers the checked
boundary row to row \(2k\), where the other boundary set is
\(A_{2k+1}=\varnothing\). The central pair is covered by the endpoint
instances above. Therefore every row \(1\le i\le2k\) satisfies

\[
 A_{i-1}\dot\cup A_{i+1}\dot\cup(A_i-1)\dot\cup(A_i+1)
 =\mathbb Z_{2k+1},
\]

so \(D_k\) is EOD.

## Regression evidence

An independently written, in-memory verifier reconstructed the row sets
from the definitions and checked both coverage and pairwise disjointness
of the four pieces for every \(1\le k\le100\). It reported no failure,
including \(k=1\), \(k=2\), and both central-row types. This is supporting
evidence only; the verdict rests on the symbolic derivation above.

## Suggested repairs

No substantive repair is required. For maximal expository precision, the
proof could explicitly say at the first use of (U) and (V) that the
integer intervals denote their reductions in \(\mathbb Z_N\), and could
state explicitly that the displayed row ranges partition the first half
in each parity case. These are clarity improvements, not mathematical
gaps.
