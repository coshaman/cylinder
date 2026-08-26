# Final Referee Adjudication — Threshold Audit

## Scope

This adjudication reopened only the prior tropical-review finding. No new
search, automaton, proof architecture, or feasibility gate was used.

## Existing premises rechecked

The persisted identities remain accepted with zero mismatches:

\[
M_5^{20}=6\otimes M_5^{16},\qquad
M_6^{35}=24\otimes M_6^{21},\qquad
M_7^{32}=8\otimes M_7^{28}.
\]

The finite-prefix ranges remain:

\[
3\!:\!19,\qquad 3\!:\!34,\qquad 3\!:\!31
\]

for widths 5, 6, and 7.

## Fresh tropical/min-plus referee

**PASS.** From

\[
M^{N+p}=c\otimes M^N
\]

associativity and scalar-shift compatibility give, for every \(k\ge0\),

\[
M^{N+p+k}=c\otimes M^{N+k}.
\]

Taking diagonal minima gives \(g(n+p)=g(n)+c\) only for \(n=N+k\ge N\).
The prior examples with bases 12 and 7 are below their respective thresholds
and are therefore not counterexamples.

## Fresh theorem-coverage referee

**PASS.** The thresholded recurrences cover all remaining indices:

- width 5: \(n\ge16\), prefix through 19; every \(n\ge20\) reduces to 16--19;
- width 6: \(n\ge21\), prefix through 34; every \(n\ge35\) reduces to 21--34;
- width 7: \(n\ge28\), prefix through 31; every \(n\ge32\) reduces to 28--31.

The transient exceptions \(n=12\) for width 6 and \(n=7,14\) for width 7
are below the thresholds and are covered directly by the finite prefixes.

## Decision

The prior tropical objection was invalid because it applied the recurrence below
its proven threshold. The mathematical status is promoted to:

`ALL_THREE_THEOREMS_PROVED`
