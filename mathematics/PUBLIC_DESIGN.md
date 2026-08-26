# Design: Exact Total Domination of Cylindrical Grids

Status: `CONJECTURE` until the direct model, independent automaton, matrix
certificates, literature audit, and referee gates all pass.

## Scope

The project determines, or refutes, the proposed exact formulas for
\(\gamma_t(P_m\square C_n)\) for (m\in\{5,6,7\}) and every (n\ge3\).
The target families are treated independently; no result for one width is
assumed for another. The neighboring `p5_cylinder_domination` project is
reference context only and is not modified or imported.

## Trust boundary

The mathematical object is total domination with open neighborhoods: every
vertex, selected or not, must have a distinct adjacent selected vertex. Direct
graph evaluation is the semantic reference. The finite-state automaton is a
separate implementation whose states and transitions must be independently
reconstructed. Producer output, cached matrices, periodic numerical behavior,
and target formulas are evidence only until a clean-room verifier checks them.

## State model

For a cyclic column sequence (S_j\subseteq[m]), define
\[
N_P(S)=\{i: i-1\in S\text{ or }i+1\in S\},\qquad
R_j=[m]\setminus(S_{j-1}\cup N_P(S_j)).
\]
The state is (q_j=(S_j,R_j)). For the next selected mask (T=S_{j+1}), the
transition is legal exactly when (R_j\subseteq T), and its next pending mask
is
\[
R_{j+1}=[m]\setminus(S_j\cup N_P(T)).
\]
The transition weight is (|T|). The semantic issue to test explicitly is
that (N_P(S_j)) is an open vertical neighborhood: selected vertices do not
dominate themselves. The cyclic closure must account for both horizontal
neighbors, including the (n=3) case where the two cyclic neighbors are
distinct vertices despite the small circumference.

## Proof architecture

1. A direct verifier and independent MILP/SAT probe establish small exact values
   and witnesses without importing automaton code.
2. A producer and clean-room implementation independently generate legal states
   and weighted transitions.
3. A mathematical bijection proves that total dominating sets correspond
   weight-preservingly to closed walks of length (n).
4. Min-plus path semantics prove
   \(\gamma_t(P_m\square C_n)=\min_q(M_m^n)_{qq}\).
5. The decisive finite certificates are entrywise identities
   \[
   M_5^{20}=6\otimes M_5^{16},\quad
   M_6^{35}=24\otimes M_6^{21},\quad
   M_7^{32}=8\otimes M_7^{28}.
   \]
   Associativity then proves the all-(n) recurrence; no empirical periodicity
   or transient-cycle argument is substituted.

## Failure policy

Any disagreement between direct semantics, producer, clean-room generator,
matrix powers, or target values triggers systematic debugging. If an identity
does not reproduce within the specified resource limits, that width receives
`PROTOTYPE_IDENTITY_NOT_REPRODUCED`; if the clean-room verifier disagrees with
the producer, the project receives `CERTIFICATE_VERIFICATION_FAILED`. A
different exact formula may be reported only after complete independent
verification. No theorem status is promoted from finite-prefix agreement.

## Resource and reproducibility policy

All arithmetic is integer/min-plus arithmetic. Each certificate stores its
manifest, matrices, automaton hash, and SHA-256 hashes. The clean-room verifier
reconstructs the automaton and powers independently and mutation tests must
reject altered transitions, weights, states, dimensions, infinity entries, and
identity parameters. Per-width runtime is capped at 30 minutes and RAM at 8 GB.
