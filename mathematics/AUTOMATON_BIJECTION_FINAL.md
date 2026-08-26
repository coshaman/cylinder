# Final Task A — total domination / automaton bijection

Status: `PASS`.

Fix (m\in\{5,6,7\}) and (n\ge3). For column sets (S_j\subseteq[m]),
let

\[
R_j=[m]\setminus\bigl(S_{j-1}\cup N_P(S_j)\bigr),
\]

with indices modulo (n). A state is (q_j=(S_j,R_j)). The transition to
the next column (T=S_{j+1}) is legal exactly when (R_j\subseteq T), and
its head pending set is forced to be

\[
R_{j+1}=[m]\setminus\bigl(S_j\cup N_P(T)\bigr).
\]

Soundness: take a cyclic legal walk and define
\(D=\{(i,j):i\in S_j\}\). If (i\notin R_j), then (i\in S_{j-1}) or
(i\in N_P(S_j)), so ((i,j)) has a selected left or vertical open
neighbor. If (i\in R_j), legality gives (i\in S_{j+1}), so its right
horizontal neighbor is selected. These are all open-neighborhood cases; the
fact that (i\in S_j) never supplies domination of ((i,j)).

Completeness: given a total dominating set (D), define
\(S_j=\{i:(i,j)\in D\}\) and (R_j) by the displayed formula. If
(i\in R_j), the left and vertical selected-neighbor alternatives are absent;
total domination therefore forces ((i,j+1)\in D). Hence (R_j\subseteq
S_{j+1}), and the next pending formula holds by definition. This applies to
the wraparound transition (n-1\to0).

For (n=3), the two horizontal neighbors are distinct because
(j-1\equiv j+1\pmod n) would imply (n\mid2). Thus the cyclic encoding
matches the simple graph (C_3) without duplicate-neighbor multiplicity.

The constructions are inverse because the pending masks are forced by the
selected masks and the defining formula. Finally, the transition weight is
(|S_{j+1}|), so a closed walk has weight
\(\sum_j|S_{j+1}|=\sum_j|S_j|=|D|\). Therefore labeled total dominating sets
and labeled legal length-(n) closed walks are weight-preserving bijective.
