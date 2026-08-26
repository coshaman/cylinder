# State Semantics for the Transfer Automaton

Status: `HUMAN_PROOF_CANDIDATE`.

Provenance:

- Frozen graph and total-domination definitions: `mathematics/DEFINITIONS.md`.
- Design equation for the state model: `docs/DESIGN.md`.
- Independent semantic audit used as evidence, not as a substitute for the proof: `workstreams/SEMANTICS_AUDIT.md`.

Open obligations for this file: none internal to the state-semantics definitions below. Later producer code must still be checked against these definitions.

## 1. Graph And Mask Conventions

Fix \(m\in\{5,6,7\}\). Let
\[
[m]\triangleq\{0,1,\ldots,m-1\}.
\]
A row set \(S\subseteq[m]\) is encoded by an integer mask
\[
\operatorname{mask}(S)\triangleq \sum_{i\in S}2^i.
\]
For a mask \(A\), write
\[
\operatorname{rows}_m(A)\triangleq\{i\in[m]:\text{ the }2^i\text{ bit of }A\text{ is }1\}.
\]
Only the low \(m\) bits are semantic. Define
\[
\mathbf 1_m\triangleq 2^m-1.
\]
For a mask \(A\), its row-complement mask is
\[
\operatorname{comp}_m(A)\triangleq \mathbf 1_m\mathbin{\&}\sim A,
\]
where \(\&\) denotes bitwise conjunction and \(\sim\) denotes bitwise negation in the host integer representation. The conjunction with \(\mathbf 1_m\) restricts the result to rows in \([m]\).

## 2. Open Vertical Neighborhood

For \(S\subseteq[m]\), define the open vertical neighborhood in the path \(P_m\) by
\[
N_P(S)\triangleq \{i\in[m]:(i>0\text{ and }i-1\in S)\text{ or }(i+1<m\text{ and }i+1\in S)\}.
\]
In mask form, if \(s=\operatorname{mask}(S)\), define
\[
N_m(s)\triangleq ((s\ll 1)\mathbin{|}(s\gg 1))\mathbin{\&}\mathbf 1_m,
\]
where \(\ll,\gg\) are bit shifts and \(|\) is bitwise disjunction.

Step 2.1 proves that \(N_m\) encodes \(N_P\). Fix \(i\in[m]\). The \(2^i\) bit of \(s\ll1\) is \(1\) exactly when \(i>0\) and the \(2^{i-1}\) bit of \(s\) is \(1\). The \(2^i\) bit of \(s\gg1\) is \(1\) exactly when \(i+1<m\) and the \(2^{i+1}\) bit of \(s\) is \(1\). Bitwise disjunction takes the union of these two alternatives, and bitwise conjunction with \(\mathbf 1_m\) removes no bit indexed by \(i\in[m]\). Therefore
\[
\operatorname{rows}_m(N_m(s))=N_P(S).
\]

Step 2.2 records the open-neighborhood consequence. A selected row \(i\in S\) contributes to \(N_P(S)\) only through a selected row \(i-1\) or \(i+1\), when that row exists. Membership \(i\in S\) is not a sufficient condition for \(i\in N_P(S)\). Hence a selected vertex still requires an adjacent selected vertex; self-membership does not satisfy total domination.

## 3. Pending Rows

Let \(S_{j-1},S_j\subseteq[m]\) be the selected row sets in two consecutive columns of \(P_m\square C_n\). Define
\[
R_j\triangleq [m]\setminus\bigl(S_{j-1}\cup N_P(S_j)\bigr).
\]
In mask form, with \(p=\operatorname{mask}(S_{j-1})\) and \(s=\operatorname{mask}(S_j)\), define
\[
\operatorname{next\_pending}_m(p,s)
\triangleq
\operatorname{comp}_m\bigl(p\mathbin{|}N_m(s)\bigr).
\]

Step 3.1 proves the mask equation. For \(i\in[m]\), the \(2^i\) bit of \(p\mathbin{|}N_m(s)\) is \(1\) exactly when \(i\in S_{j-1}\cup N_P(S_j)\), by the definition of \(p\), by Step 2.1, and by the set meaning of bitwise disjunction. The complement mask \(\operatorname{comp}_m\) has bit \(i\) equal to \(1\) exactly when that disjunction bit is \(0\). Therefore
\[
\operatorname{rows}_m(\operatorname{next\_pending}_m(p,s))
=
[m]\setminus\bigl(S_{j-1}\cup N_P(S_j)\bigr)
=R_j.
\]

Step 3.2 identifies the semantic content of \(R_j\). Fix \(i\in[m]\). The vertex \((i,j)\) can be dominated from column \(j-1\) exactly when \(i\in S_{j-1}\). It can be dominated vertically inside column \(j\) exactly when \(i\in N_P(S_j)\). If \(i\in R_j\), both alternatives are absent. The only remaining neighbor of \((i,j)\) that can still be selected is \((i,j+1)\), represented by \(i\in S_{j+1}\). This applies whether or not \(i\in S_j\), because total domination uses open neighborhoods.

## 4. States And Legitimate State Pairs

A state is a pair
\[
q_j\triangleq(S_j,R_j).
\]
In mask form it is a pair \((s,r)\), where \(s=\operatorname{mask}(S_j)\) and \(r=\operatorname{mask}(R_j)\).

Every state produced by the pending-row formula satisfies
\[
R_j\subseteq [m]\setminus N_P(S_j),
\]
because \(R_j=[m]\setminus(S_{j-1}\cup N_P(S_j))\).

Conversely, if \(S\subseteq[m]\) and \(R\subseteq[m]\setminus N_P(S)\), then the pair \((S,R)\) can occur for a suitable previous mask. Define
\[
P\triangleq [m]\setminus(R\cup N_P(S)).
\]
Since \(R\cap N_P(S)=\varnothing\), for each \(i\in[m]\) there are three cases:

1. If \(i\in R\), then \(i\notin P\) and \(i\notin N_P(S)\), so \(i\in[m]\setminus(P\cup N_P(S))\).
2. If \(i\notin R\) and \(i\in N_P(S)\), then \(i\in P\cup N_P(S)\), so \(i\notin[m]\setminus(P\cup N_P(S))\).
3. If \(i\notin R\) and \(i\notin N_P(S)\), then \(i\in P\), so \(i\notin[m]\setminus(P\cup N_P(S))\).

The membership decision in the complement equals membership in \(R\) for every row \(i\). Therefore
\[
[m]\setminus(P\cup N_P(S))=R.
\]

## 5. Legal Transitions And Deterministic Update

Let \(q_j=(S_j,R_j)\), and let the next selected row set be \(T=S_{j+1}\). The transition from \(q_j\) to a state with selected mask \(T\) is legal exactly when
\[
R_j\subseteq T.
\]
In mask form, with \(r=\operatorname{mask}(R_j)\) and \(t=\operatorname{mask}(T)\), this condition is
\[
r\mathbin{\&}\sim t=0.
\]
The equality is evaluated on the low \(m\) bits; since \(r\) has no bits outside \([m]\), no additional mask is needed.

Step 5.1 proves necessity. If \(i\in R_j\), Step 3.2 says that \((i,j)\) has no selected neighbor in column \(j-1\) and no selected vertical neighbor in column \(j\). Total domination can still hold for \((i,j)\) only if the right horizontal neighbor \((i,j+1)\) is selected, which is the condition \(i\in S_{j+1}=T\). Thus \(R_j\subseteq T\).

Step 5.2 proves sufficiency for the current column. If \(R_j\subseteq T\), then every \(i\in R_j\) is dominated by the selected right horizontal neighbor \((i,j+1)\). If \(i\notin R_j\), then \(i\in S_{j-1}\cup N_P(S_j)\), so \((i,j)\) is dominated from the left or vertically. Hence all vertices in column \(j\) are dominated.

Step 5.3 gives the deterministic next pending mask. Once \(S_j\) and \(T=S_{j+1}\) are fixed, the pending rows for column \(j+1\) are
\[
R_{j+1}\triangleq [m]\setminus\bigl(S_j\cup N_P(T)\bigr).
\]
In mask form, with \(s=\operatorname{mask}(S_j)\) and \(t=\operatorname{mask}(T)\),
\[
r'=\operatorname{next\_pending}_m(s,t).
\]
This value depends on \(s\) and \(t\), not on any additional choice.

## 6. Head-Column Weight

The weight of a transition whose head selected mask is \(T\) is
\[
w(q_j,q_{j+1})\triangleq |T|.
\]
In mask form this is the population count of \(t=\operatorname{mask}(T)\). On a length-\(n\) closed walk, each column \(j\) is the head of exactly one transition, namely \(q_{j-1}\to q_j\) with indices modulo \(n\). Therefore the total transition weight is
\[
\sum_{j=0}^{n-1}|S_j|,
\]
which is the number of selected vertices represented by the column masks.
