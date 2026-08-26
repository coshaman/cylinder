# Final Task C — entrywise identity recurrence

Status: `PASS`.

Assume entrywise (M^{N+p}=c\otimes M^N), with finite integer (c). Min-plus
multiplication is associative because both parenthesizations minimize the
same finite set of triple products; (+\infty) is absorbing. For every
matrix (A,B),

\[
((c\otimes A)\otimes B)_{uv}=c\otimes(A\otimes B)_{uv},
\]

because finite candidates all receive the same additive shift and every
(+\infty) candidate remains (+\infty). Thus, for every (k\ge0),

\[
M^{N+p+k}=M^{N+p}\otimes M^k
=c\otimes(M^N\otimes M^k)=c\otimes M^{N+k}.
\]

Taking diagonal minima yields the infinity-safe recurrence

\[
g(N+p+k)=c\otimes g(N+k).
\]

The complete finite-prefix reconstruction gives a finite value (g(r)) for
every (r\in[3,N+p-1]). Repeatedly reducing any later index by (p) reaches
one of these base indices; applying the displayed recurrence then propagates
finiteness to every later (g)-value. Consequently
the scalar operation is ordinary addition on the relevant values, and

\[
g(n+p)=g(n)+c,
\qquad n\ge N.
\]

This recurrence is not asserted for bases below \(N\); transient exceptions
remain governed by the finite prefix.

The verified triples are

\[
(N,p,c)=(16,4,6),\quad(21,14,24),\quad(28,4,8),
\]

for widths (5,6,7), respectively.
