# Design: Exact Total Domination of Cylindrical Grids

Status: ALL_THREE_THEOREMS_PROVED for the frozen theorem package. The finite
identities and prefix data remain explicitly labeled as tool-checked or
computational premises.

## Scope

The project determines the exact formulas for
\(\gamma_t(P_m\square C_n)\) for \(m\in\{5,6,7\}\) and every \(n\ge3\).
The target families are treated independently; no result for one width is
assumed for another.

## Trust boundary

The mathematical object is total domination with open neighborhoods: every
vertex, selected or not, must have a distinct adjacent selected vertex.
Direct graph evaluation is the semantic reference. The finite-state
automaton is independently reconstructed. Producer output, cached matrices,
periodic numerical behavior, and target formulas are evidence only until a
clean-room verifier checks them.

## State model

For a cyclic column sequence \(S_j\subseteq[m]\), define
\[
N_P(S)=\{i:i-1\in S\text{ or }i+1\in S\},\qquad
R_j=[m]\setminus(S_{j-1}\cup N_P(S_j)).
\]
The state is \(q_j=(S_j,R_j)\). For the next selected mask
\(T=S_{j+1}\), the transition is legal exactly when \(R_j\subseteq T\), and
its next pending mask is
\[
R_{j+1}=[m]\setminus(S_j\cup N_P(T)).
\]
The transition weight is \(|T|\). The open vertical neighborhood and the
cyclic closure, including \(n=3\), are part of the semantic checks.

## Proof architecture

1. A direct verifier and independent probes establish selected finite values
   and witnesses without importing the automaton implementation.
2. A clean-room implementation independently generates states and transitions.
3. A mathematical bijection proves that total dominating sets correspond
   weight-preservingly to closed walks of length \(n\).
4. Min-plus path semantics prove
   \(\gamma_t(P_m\square C_n)=\min_q(M_m^n)_{qq}\).
5. Entrywise identities
   \[
   M_5^{20}=6\otimes M_5^{16},\quad
   M_6^{35}=24\otimes M_6^{21},\quad
   M_7^{32}=8\otimes M_7^{28}
   \]
   and associativity prove the all-\(n\) tails. No empirical periodicity or
   transient-cycle argument is substituted.

## Failure and reproducibility policy

Any disagreement between direct semantics, the clean-room generator, matrix
powers, or target values triggers systematic debugging. Each certificate
stores its manifest, matrices, automaton hash, and SHA-256 hashes. The
verifier reconstructs the automaton and powers independently; mutation tests
reject altered transitions, weights, states, dimensions, infinity entries,
and identity parameters. Integer/min-plus arithmetic is used throughout.
