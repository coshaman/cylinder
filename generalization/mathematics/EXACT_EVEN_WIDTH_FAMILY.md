# Exact even-width family

If the all-(k) construction in `EVEN_WIDTH_CONSTRUCTION.md` is proved,
then for (k,t\ge1) it gives an EOD set in

\[
P_{2k}\square C_{(2k+1)t}.
\]

The construction proof gives (|A_i|=a_i): in Case I,
(|E_r|=r) and (|C_r|=2(h-r)), while in Case II,
(|E_r|=r) and (|D_r|=2(h-r+1)); the reflected rows have equal sizes.
Pairing the reflected entries therefore gives

\[
\sum_{i=1}^{2k}a_i=k(k+1).
\]

For an explicit lift, put (N=2k+1) and define

\[
\widetilde A_i=\{a+qN\pmod{Nt}:a\in A_i, 0\le q<t\}.
\]

At a column (qN+a), with (0\le a<N), the two horizontal neighbors
correspond to (a-1,a+1) modulo (N); when (a=0) or (a=N-1), the
neighbor lies in the adjacent copy. Thus the four pieces in the base
partition identity lift copy-by-copy to a disjoint partition of
(\mathbb Z_{Nt}). Repeating the (C_{2k+1}) pattern therefore preserves
the local seam identity, so the EOD set has cardinality

\[
t\sum_{i=1}^{2k}a_i=k(k+1)t.
\]

The lower bound gives

\[
\gamma_t(P_{2k}\square C_{(2k+1)t})
\ge
\frac{(2k)(2k+2)}{4(2k+1)}(2k+1)t
=k(k+1)t.
\]

The proved EOD construction attains this bound, so the conclusion is

\[
\boxed{\gamma_t(P_{2k}\square C_{(2k+1)t})=k(k+1)t.}
\]

For odd width, the known (P_{2k+1}\square C_{4t}) EOD family of
Proposition 5.6 in Kuziak--Peterin--González Yero (2014) similarly
has cardinality (2(k+1)t), and the odd-width lower bound is equal to that
number. This recovers a known sharp family rather than claiming it as new.
