# Computer-Assisted Proof Referee

## Verdict

**MINOR_REVISION**

The finite computational premises are reproducible in the present environment,
and the clean-room verifier accepts all three persisted certificates. The
package is not ready for an unconditional computational-editorial acceptance
because the integrity snapshot is not self-consistent and the mutation report
overstates the exercised negative-control coverage.

This review uses only the authorized `cylindrical_total_domination` project.
No neighboring project or development-history report was used as evidence.
The referee did not edit source files.

## Reproduced evidence

From the project root, the following completed successfully:

- `python -m pytest tests -q`: **125 passed** in 161.02 seconds.
- `python verify/verify_certificates.py 5 certificates/width5`: accepted,
  status `TOOL_CHECKED_LOCAL`.
- The corresponding width-6 and width-7 commands: accepted, status
  `TOOL_CHECKED_LOCAL`.
- `python -m pytest tests/test_mutations.py -q`: **11 passed**.
- `python -m pytest tests/test_prefix_values.py -q`: **18 passed**.

The three `release/public_v2` certificate commands also accepted. The
certificate checks reconstruct the state and transition arrays, verify their
counts and canonical hashes, parse both tagged matrices, recompute both
powers, and check the entrywise shift identity. The root and `public_v2`
verifiers differ only in the package-level theorem-status value expected in
their respective manifests.

No Lean artifacts were present, so no Lean build or `sorry` audit applies.

## Dependency graph and classification

| Dependency | Classification | Assessment |
|---|---|---|
| Frozen graph/domain contract | justified | `mathematics/DEFINITIONS.md:10-40` fixes (m\in\{5,6,7\}), (n\ge3), open neighborhoods, and total domination. |
| State and transition reconstruction | justified | `verify/verify_certificates.py:85-110` independently rebuilds the finite graph and `:232-248` compares the complete arrays, counts, hashes, and strong connectivity. |
| Matrix parsing and power replay | justified | `verify/verify_certificates.py:142-199,293-308` strictly parses MTX1 data and recomputes both persisted powers from reconstructed edges. |
| Entrywise certificate identity | justified | `verify/verify_certificates.py:310-314` checks every entry, including the `None`/INF branch. All three live replays passed. |
| Total-domination/closed-walk bridge | cited | `mathematics/AUTOMATON_BIJECTION_FINAL.md:5-42` supplies the human semantic argument. The computational package does not independently prove this bridge. |
| Min-plus path semantics | cited | `mathematics/MINPLUS_PATH_SEMANTICS_FINAL.md:5-29` supplies the walk interpretation used by the prefix trace. |
| All-(n) propagation | cited/conditional | `mathematics/MINPLUS_IDENTITY_LEMMA_FINAL.md:5-48` correctly states the dependence on an entrywise identity plus a finite prefix. The computation alone is not an all-(n) proof. |
| Prefix coverage | justified as a finite premise | `tests/test_prefix_values.py:18-25,50-88,98-120` covers exactly (3\le n\le19,34,31), uses every reconstructed state as a source, and matches the frozen formulas. |
| (C_3) degeneracy | justified | `AUTOMATON_BIJECTION_FINAL.md:34-36` and `tests/test_direct.py` address distinct horizontal neighbors for (n=3). |
| Clean-room separation | justified with a scope caveat | The verifier has no producer import/execution; the test is lexical and cannot prove exclusion of every possible dynamic execution mechanism. |

## Blocking editorial findings

1. **Minor but acceptance-blocking integrity defect: the hash manifests are stale at the
   review snapshot.** A fresh audit of every listed path found five mismatches
   in the root `SHA256SUMS`: `paper/references.bib`,
   `release/public_v2/generalization/reviews/final/FIXED_WIDTH_CERTIFICATE_REVIEW.md`,
   `release/public_v2/paper/references.bib`, `release/public_v2/README.md`,
   and `release/public_v2/RESULT.json`. The separate
   `release/public_v2/SHA256SUMS` likewise has four mismatches for the latter
   four paths. The certificate-internal hashes and clean-room replays still
   pass, so this does not falsify the finite identities; it does prevent the
   published integrity manifest from serving its stated purpose. Regenerate
   the manifest only after freezing one package snapshot, then verify every
   listed path.

2. **Minor evidence error: the mutation count is overstated.**
   `verify/mutation_tests.py:100-113` defines eight mutations. The 11 passing
   test cases in `tests/test_mutations.py:29-54` consist of one baseline,
   eight mutation cases, one report-format case, and one lexical-isolation
   case. Thus `REPRODUCIBILITY.md:14-15`,
   `release/public_v2/paper/REPRODUCIBILITY.md:22-27`, and
   `results/NEGATIVE_CONTROLS_FINAL.md:8-17` should not call all 11 cases
   negative controls.

3. **Coverage gap in the matrix mutations.** The finite and finite-to-INF
   mutation helpers rebind the inner `matrix_identity.json` hash but do not
   update the copied package-level `certificates/manifest.json` hash. The
   verifier checks that package-level binding at
   `verify/verify_certificates.py:264-291`, before parsing or recomputing the
   matrix at `:293-308`. Consequently the documented mutation suite rejects
   these mutations early; it does not exercise the claimed tagged-INF or
   recomputation path. Independent temporary tests with both inner and
   package-level hashes rebound reached the deeper checks and were rejected as
   expected, so this is an evidence-coverage defect rather than a demonstrated
   verifier failure. Add rebound-hash mutations (and assert the failure stage)
   or narrow the coverage claim.

4. **Reproducibility documentation is incomplete.** The executable checks
   require `pytest`, NumPy, and a CBC executable for the selected direct
   witness checks. `src/direct/milp_probe.py:14-31` uses a host-specific CBC
   fallback under `Path.home()`, while the package has no requirements or
   environment lock file. Add supported versions, solver installation/path
   instructions, and a deterministic environment description. This is a
   portability caveat, not a failure in the current run.

The root hash file also includes volatile cache/support paths (including
`.pytest_cache` and `.superpowers` entries) while excluding itself. Those
choices make it unsuitable as a stable public-package manifest unless the
scope is reduced to frozen release artifacts. During this review the root
manifest was rewritten from 303 to 494 entries by an external concurrent
process; the final stable audit above is the one reported here. Freeze the
workspace before the next review.

## Conclusion and required resubmission

The clean-room finite certificates, exact prefix ranges, direct semantic
cross-checks, and verifier logic are acceptable as computational premises.
The required revision is limited to freezing and rehashing the release
snapshot, correcting the mutation-count/coverage statements, and documenting
the execution environment. After those changes, a new independent review is
required; this verdict should not be promoted to `ACCEPT` by editing this
report alone.
