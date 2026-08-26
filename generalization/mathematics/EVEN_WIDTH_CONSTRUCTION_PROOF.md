# Symbolic residue proof for the even-width construction

This file supplies the detailed set calculation for the construction in
`EVEN_WIDTH_CONSTRUCTION.md` and repeats all definitions needed for the
proof. Let (N=2k+1), let rows be (1,ldots,2k), and let columns be
(\mathbb Z_N). For a row set (A_i\subseteq\mathbb Z_N), define
(D_k=\{(i,j):j\in A_i\}). The required open-neighborhood condition is
equivalent to

\[
A_{i-1}\dot\cup A_{i+1}\dot\cup(A_i-1)\dot\cup(A_i+1)=\mathbb Z_N,
\quad A_0=A_{2k+1}=\varnothing. \tag{EOD}
\]

Indeed, for a vertex in row (i), the four pieces are respectively its
vertical neighbors in rows (i-1,i+1) and the selected columns at its two
horizontal neighbors. Disjoint union therefore means exactly one selected
open neighbor.

The row sets used below are as follows. Put

\[
E_r=\{2(r-1)-4t\pmod N:0\le t<r\},\qquad E_0=\varnothing.
\]

If (k=2h), put

\[
C_r=\bigcup_{t=0}^{h-r-1}\{2r+2+4t,2r+3+4t\},
\]

and set (A_{2r}=E_r) for (1\le r\le h),
(A_{2r+1}=E_r\cup C_r) for (0\le r<h). If (k=2h+1), put

\[
D_r=\bigcup_{t=0}^{h-r}\{2r+1+4t,2r+2+4t\},
\]

and set (A_{2r}=E_r) for (1\le r\le h),
(A_{2r-1}=E_r\cup D_r) for (1\le r\le h+1). In both cases, complete
the row sets by (A_{2k+1-i}=A_i). Empty unions are understood as empty.

The pieces in each displayed row union are disjoint modulo (N). In Case I,
the nonwrapped elements of (E_r) are at most (2r-2), below the first
element (2r+2) of (C_r); after wrapping by (N=4h+1), the wrapped
elements of (E_r) are at least (4h-2r+3), above the last element
(4h-2r-1) of (C_r). In Case II the same comparison is
(2r-2<2r+1) before wrapping and (4h-2r+5>4h-2r+2) after wrapping.
Consequently

\[
|A_{2r}|=r,quad |A_{2r+1}|=2h-r (k=2h),
\]

and

\[
|A_{2r}|=r,quad |A_{2r-1}|=2h-r+2 (k=2h+1),
\]

on the displayed halves; reflection gives the remaining row sizes.

For (q\ge0), write

\[
J(a,q)=\{a+4t,a+1+4t:0\le t<q\}.
\]

Then (C_r=J(2r+2,h-r)), (D_r=J(2r+1,h-r+1)), and
(E_r=\{2r-2-4t:0\le t<r\}). Define

\[
U_r=E_{r-1}\cup E_r\cup(E_r-1)\cup(E_r+1),
\]

\[
V_r=E_r\cup E_{r+1}\cup(E_r-1)\cup(E_r+1).
\]

Grouping the four terms indexed by (t), for (0\le t<r-1), gives

\[
2r-4-4t,\ 2r-3-4t,\ 2r-2-4t,\ 2r-1-4t.
\]

The final element of (E_r) and its shifts supply
(1-2r,2-2r,3-2r). The blocks concatenate, so

\[
U_r=\{1-2r,\ldots,2r-1\}. \tag{1}
\]

For (V_r), the same blocks are followed by the extra final element
(-2r\) of (E_{r+1}), hence

\[
V_r=\{1-2r,\ldots,2r\}\cup\{-2r\}. \tag{2}
\]

The interval arguments below have length at most the relevant modulus. Their
endpoints identify the one possible wrap-around residue explicitly, so no
unjustified injectivity claim about reduction modulo an arbitrary odd number
is being used.

The labels used below mean the following row identities:

\[
\begin{aligned}
(I0)&:\ E_1\dot\cup(C_0-1)\dot\cup(C_0+1)=\mathbb Z_{4h+1},\\
(I1)&:\ (E_{r-1}\cup C_{r-1})\dot\cup(E_r\cup C_r)
\dot\cup(E_r-1)\dot\cup(E_r+1)=\mathbb Z_{4h+1},\\
(I2)&:\ E_r\dot\cup E_{r+1}\dot\cup((E_r\cup C_r)-1)
\dot\cup((E_r\cup C_r)+1)=\mathbb Z_{4h+1},\\
(II1)&:\ E_{r-1}\dot\cup E_r\dot\cup((E_r\cup D_r)-1)
\dot\cup((E_r\cup D_r)+1)=\mathbb Z_{4h+3},\\
(II2)&:\ (E_r\cup D_r)\dot\cup(E_{r+1}\cup D_{r+1})
\dot\cup(E_r-1)\dot\cup(E_r+1)=\mathbb Z_{4h+3}.
\end{aligned}
\]

The ranges are (1\le r\le h) in (I1), (1\le r<h) in (I2),
(1\le r\le h+1) in (II1), and (1\le r\le h) in (II2).

## Case (k=2h)

Here (N=4h+1). The sets (C_0-1) and (C_0+1) are the disjoint blocks

\[
[1,4],[5,8],\ldots,[4h-3,4h],
\]

and (E_1=\{0\}). This proves the boundary identity (I0).

For (1\le r\le h), the unshifted sets (C_{r-1}) and (C_r) concatenate
to the interval

\[
[2r,4h-2r+1].
\]

Joining this with (1) gives an interval of (4h+1) integers, proving (I1).

For (1\le r<h), the shifted sets (C_r-1) and (C_r+1) concatenate
to

\[
[2r+1,4h-2r].
\]

The interval part of (2) joins it to ([1-2r,4h-2r]), which has (4h)
integers. Its next residue modulo (4h+1) is (-2r), the singleton in
(2), proving (I2). The omitted (r=0) instance is exactly the already
proved boundary identity (I0). The central row uses (I1) with (r=h).

## Case (k=2h+1)

Here (N=4h+3). For (1\le r\le h), the shifted sets (D_r-1) and
(D_r+1) concatenate to

\[
[2r,4h-2r+3].
\]

Together with (1), this is an interval of (4h+3) integers. For
(r=h+1), (D_r=\varnothing) and (1) itself has (4h+3) integers. This
proves (II1).

For (1\le r\le h), the unshifted sets (D_r,D_{r+1}) concatenate to

\[
[2r+1,4h-2r+2].
\]

Together with the interval part of (2), this gives (4h+2) consecutive
integers; the next residue is (-2r), the singleton in (2). This proves
(II2).

Reflection (i\mapsto2k+1-i) exchanges the two neighboring row sets and
does not change columns. Thus the identities on the displayed half imply
the identities on the reflected half. Therefore every row satisfies

\[
A_{i-1}\dot\cup A_{i+1}\dot\cup(A_i-1)\dot\cup(A_i+1)=\mathbb Z_{2k+1},
\]

which proves the EOD property for the constructed set, including the two
path-boundary rows through (A_0=A_{2k+1}=\varnothing).
