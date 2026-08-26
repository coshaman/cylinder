# Complete proof assembly

The proof is the conjunction of the three final bridge lemmas:

1. [AUTOMATON_BIJECTION_FINAL.md](AUTOMATON_BIJECTION_FINAL.md) proves the
   open-neighborhood, weight-preserving bijection for every (n\ge3).
2. [MINPLUS_PATH_SEMANTICS_FINAL.md](MINPLUS_PATH_SEMANTICS_FINAL.md) proves
   the closed-walk interpretation of matrix powers.
3. [MINPLUS_IDENTITY_LEMMA_FINAL.md](MINPLUS_IDENTITY_LEMMA_FINAL.md) proves
   the infinity-safe recurrence and its finite-value specialization. The
   complete finite prefix supplies a finite diagonal value at every base
   index (r\in[3,N+p-1]), so the specialization never invokes undefined
   (+\infty+c).

The fresh certificate replay verifies the three entrywise identities and the
finite-prefix reconstruction verifies every required prefix row. The
recurrence is used only from its proven thresholds: \(n\ge16\), \(n\ge21\),
and \(n\ge28\), respectively. Every \(n\ge N+p\) reduces to a base in
\([N,N+p-1]\), while all smaller values are already in the finite prefix.
Together with the three PASS referee reports and the bounded literature audit,
these are the exact premises of the all-(n) proof, so the formulas follow for
every (n\ge3) by repeated recurrence reduction.

The computational artifacts remain labeled `TOOL_CHECKED_LOCAL` and
`COMPUTATIONALLY_TESTED` as evidence classifications, while the independent
referee PASS reports accept the exact certificate premises used here. The
resulting theorem status is `ALL_THREE_THEOREMS_PROVED`.
