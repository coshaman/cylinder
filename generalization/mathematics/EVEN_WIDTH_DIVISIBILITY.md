# Even-width EOD divisibility

Let (n\ge3), let (x_{i,j}\in\{0,1\}) indicate an efficient open
dominating set in (P_{2k}\square C_n), with (j\in\mathbb Z_n), and put
(x_{0,j}=x_{2k+1,j}=0). Summing the exact open-neighbor equations over a
cycle row gives the unique row system

\[
2s_i+s_{i-1}+s_{i+1}=n,
\qquad s_0=s_{2k+1}=0,
\]

as proved directly in `EOD_LINEAR_SYSTEM.md`.

Let (m=2k). Define (a_0=a_{2k+1}=0). For every integer (r) for which
the index lies in (1,\ldots,k), set

\[
a_{2r-1}=k-r+1,qquad a_{2r}=r,
\]

and then set (a_{2k+1-i}=a_i). Direct substitution gives

\[
2a_i+a_{i-1}+a_{i+1}=2k+1. \tag{1}
\]

For an odd index (i=2r-1) away from the symmetry point, the three values
are (k-r+1,r-1,r), whose weighted sum is (2k+1). For an even index
(i=2r), they are (r,k-r+1,k-r), with the same sum. The boundary and
central indices satisfy the same equation by the stated symmetry and boundary
values.

Therefore the unique solution of the row system is

\[
s_i=\frac{n a_i}{2k+1}. \tag{2}
\]

For (k\ge2), (a_2=1); for (k=1), (a_1=a_2=1). Thus some (a_i)
equals (1), and integrality of (s_i) implies

\[
2k+1\mid n. \tag{3}
\]
