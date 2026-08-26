# Odd-width EOD characterization

Let (m=2k+1\ge3) and (n\ge3). Let (x_{i,j}\in\{0,1\}) indicate
whether ((i,j)) belongs to an EOD set in (P_m\square C_n), with
(j\in\mathbb Z_n) and (x_{0,j}=x_{m+1,j}=0). The open-neighborhood
condition is

\[
x_{i-1,j}+x_{i+1,j}+x_{i,j-1}+x_{i,j+1}=1. \tag{1}
\]

The row-sum system obtained by summing (1) is proved in
`EOD_LINEAR_SYSTEM.md`.

Set (u_i=s_i/n). The unique solution of

\[
2u_i+u_{i-1}+u_{i+1}=1,qquad u_0=u_{2k+2}=0,
\]

is

\[
u_i=\begin{cases}1/2,&i\text{ odd},\\0,&i\text{ even}.
\end{cases} \tag{2}
\]

Substitution verifies the equation at odd and even rows, including both
boundaries, and uniqueness proves (s_i=nu_i). Thus every even row is empty.

For an odd row (i), (1) becomes

\[
x_{i,j-1}+x_{i,j+1}=1. \tag{3}
\]

Replacing (j) by (j+1) gives (x_{i,j}+x_{i,j+2}=1), hence
(x_{i,j+2}=1-x_{i,j}) and (x_{i,j+4}=x_{i,j}). If
(n\equiv1,2,3\pmod4), cyclic consistency respectively identifies the
two terms in (3), identifies the two terms after a two-step shift, or
identifies the two terms after a reverse one-step shift. In each case it
would give (2x_{i,j}=1), impossible for a Boolean variable. Therefore
(4\mid n).

Conversely, let (n=4t). On every even row select nothing. On consecutive
odd rows use alternating period-four column pairs

\[
\{0,1\},\{4,5\},\ldots,\{4t-4,4t-3\}
\]

and

\[
\{2,3\},\{6,7\},\ldots,\{4t-2,4t-1\},
\]

choosing the first or second pattern according to the parity of the odd-row
index so that adjacent odd rows use complementary patterns. On an odd row,
the two horizontal selected-neighbor indicators sum to one by the period-four
pattern. On an even row, both horizontal terms are zero and the two adjacent
odd rows have complementary selected columns, so their vertical indicators
sum to one. The two path-boundary rows are odd rows, so they are handled by
the horizontal period-four check and have no missing vertical contribution.
This is precisely the explicit family in Proposition 5.6 of
Kuziak--Peterin--González Yero (2014), which supplies the complete boundary
check. Hence (P_{2k+1}\square C_{4t}) has an EOD set.
