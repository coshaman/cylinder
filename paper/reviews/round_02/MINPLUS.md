# Round 02 — Tropical / Min-Plus Referee

## Verdict

**STRONG_ACCEPT**, scoped to the cylindrical_total_domination min-plus layer:
path semantics, the thresholded recurrence implication, exact base coverage,
and the submitted width-5/6/7 identity artifacts are correct. I found no
actual algebraic counterexample.

This is a fresh review of the frozen project files and reproducible artifacts;
it does not certify claims outside the requested tropical/min-plus scope.

## Frozen data

| width | certified identity | threshold \(N\) | period \(p\) | shift \(c\) | checked prefix |
|---:|---|---:|---:|---:|---|
| 5 | \(M_5^{20}=6\otimes M_5^{16}\) | 16 | 4 | 6 | \(3\le n\le19\) |
| 6 | \(M_6^{35}=24\otimes M_6^{21}\) | 21 | 14 | 24 | \(3\le n\le34\) |
| 7 | \(M_7^{32}=8\otimes M_7^{28}\) | 28 | 4 | 8 | \(3\le n\le31\) |

The identity parameters agree between `paper/manuscript.tex:314--324`,
`verify/verify_certificates.py:20`, the per-width metadata, and the top-level
certificate manifest.

## Dependency audit

1. **State-to-matrix path semantics — Justified, conditional only on the
   submitted automaton bijection.**

   `paper/manuscript.tex:217--249` and
   `mathematics/MINPLUS_PATH_SEMANTICS_FINAL.md:5--29` use the zero-diagonal,
   \(+\infty\)-off-diagonal identity. The \(k=0\) case is exact. For the
   induction step, partitioning a length-\((k+1)\) walk by its unique
   penultimate state gives the min-plus product. The state set is finite, so
   the displayed minimum is over a finite index set; absent prefixes and
   edges contribute \(+\infty\) and cannot create a walk. Taking the minimum
   diagonal entry therefore gives the minimum closed-walk weight.

2. **Associativity and scalar shift — Justified.**

   `paper/manuscript.tex:252--280` and
   `mathematics/MINPLUS_IDENTITY_LEMMA_FINAL.md:5--20` correctly use
   \((a+b)+d=a+(b+d)\) on finite costs and absorption of \(+\infty\). For any
   finite \(c\), every finite candidate in a subsequent product is shifted by
   exactly \(c\), while unreachable candidates remain \(+\infty\). Thus
   \[
   (c\otimes A)\otimes B=c\otimes(A\otimes B)
   \]
   entrywise, including the all-unreachable case.

3. **Power-law propagation — Justified.**

   From the literal entrywise identity \(M^{N+p}=c\otimes M^N\), associativity
   and the standard power law give, for every \(k\ge0\),
   \[
   M^{N+p+k}=M^{N+p}\otimes M^k
   =c\otimes(M^N\otimes M^k)
   =c\otimes M^{N+k}.
   \]
   No commutativity of arbitrary matrices is assumed; only powers of the same
   matrix and associativity are used.

4. **Diagonal-minimum recurrence — Justified.**

   Taking the finite minimum over diagonal entries commutes with a common
   finite additive shift. The ordinary-integer form
   \(g(n+p)=g(n)+c\) is stated only when the relevant diagonal minimum is
   finite. The finite prefix supplies that finiteness for every base used in
   the tail argument.

5. **Exact certificate premises — Cited/tool-checked, not promoted to a
   purely human proof.**

   `verify/verify_certificates.py:211--315` independently reconstructs states,
   transitions, weights, matrix powers, dimensions, hashes, and the entrywise
   identity. It checks the tagged-(INF) rule explicitly:
   `expected = None if base is None else base + expected_c`.
   The resulting finite certificate premises are exactly the three identities
   in the frozen table above.

6. **Exact finite-prefix coverage — Cited/tool-checked.**

   `results/FINITE_PREFIX_FINAL.md:13--22`,
   `tests/test_prefix_values.py:18--24,50--120`, and the three width value
   tables cover every integer in the stated prefix ranges, not merely the
   displayed exceptional and tail rows. The trace uses every reconstructed
   state as a possible source, so the diagonal minima are unrestricted within
   the reconstructed graph.

## Threshold audit: no below-threshold propagation

The tail reductions are exact:

- Width 5: every \(n\ge20\) repeatedly subtracts \(4\) until it reaches one
  of \(16,17,18,19\). The recurrence is invoked only with current base
  \(n\ge16\); values \(3\le n\le15\) come directly from the prefix.
- Width 6: every \(n\ge35\) repeatedly subtracts \(14\) until it reaches one
  of \(21,\ldots,34\). The recurrence is never invoked at a base below 21.
- Width 7: every \(n\ge32\) repeatedly subtracts \(4\) until it reaches one
  of \(28,29,30,31\). The recurrence is never invoked at a base below 28.

In particular, the exceptional finite-prefix values \(g_6(12)=22\),
\(g_7(7)=15\), and \(g_7(14)=30\) are not used as recurrence bases. The
manuscript explicitly records this at `paper/manuscript.tex:378--395`.
There is no illicit inference of \(g_6(26)\) from \(g_6(12)\), nor of any
width-7 tail value from \(n=7\) or \(n=14\); \(g_6(26)\) and all required
tail bases are independently included in the finite coverage.

## Reproduction performed

Fresh commands from the project directory:

- `python -m pytest tests/test_minplus.py tests/test_matrix_identity.py tests/test_prefix_values.py tests/test_project_contract.py -q`
  — **37 passed**.
- `python verify/verify_certificates.py 5 certificates/width5` — accepted;
  zero identity mismatches.
- `python verify/verify_certificates.py 6 certificates/width6` — accepted;
  zero identity mismatches.
- `python verify/verify_certificates.py 7 certificates/width7` — accepted on
  clean rerun; zero identity mismatches.
- `python paper/check_consistency.py` — `manuscript consistency: PASS`.

The verifier reports independent reconstruction of all three automata,
recomputation of both powers, and explicit infinity-safe entrywise identity
checks. The persisted matrices happen to have zero \(+\infty\) entries, so
the live identity instances do not exercise an unreachable matrix entry;
the abstract proof and tagged parser still handle that case, and the min-plus
fixtures/mutation checks exercise the boundary.

## Counterexample search

No sign error, inequality reversal, associativity failure, invalid scalar
shift, threshold violation, or below-threshold propagation was found. No
actual algebraic counterexample is reported because none was produced by the
independent checks.

## Suggested repairs (nonblocking)

None required for this scoped verdict. For maximal audit transparency, a
future certificate fixture could include a genuinely unreachable matrix entry,
but its absence from the three accepted identities is a coverage limitation,
not a defect in the recurrence argument.
