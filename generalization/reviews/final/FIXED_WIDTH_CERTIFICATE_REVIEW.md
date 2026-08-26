# Role E — fixed-width certificate and public-package review

Date: 2026-08-26

## Scope and evidence rule

This is a clean-room review of the current artifacts in
`cylindrical_total_domination` only. Development-history reports and
neighboring projects were not used as evidence. The review covers the fixed
width certificate branch (`m=5,6,7`) and the public package. It does not
re-approve the separate generalization proofs.

The frozen finalization claims include the all-width EOD characterization,
the all-width total-domination lower bound, the even-width exact family, the
known odd family, and the fixed-width formulas. The certificate branch is
relevant only to the last of these.

## Verdict

**FATAL** for finalization/publication of the stated final theorem package.

The fixed-width certificates themselves pass the requested replay checks, but
the public package is not the current final theorem package: it contains only
the fixed-width manuscript and artifacts, while the current manuscript claims
the all-width EOD theorem, the general lower bound, and the even-width exact
family. The public manuscript and source manuscript are materially different,
and the root integrity manifest is stale for current manuscript artifacts.
This is a publication-facing scope/integrity failure, not a detected error in
the three fixed-width matrix identities.

## Dependency graph and classifications

1. **Finite state/transition reconstruction — justified.**
   `verify/verify_certificates.py` independently rebuilds states and
   transitions from the width-specific definitions, checks manifest contents,
   counts, hashes, and strong connectivity, and then recomputes the persisted
   powers. The verifier hard-codes only
   `WIDTH_PARAMETERS = {5: ..., 6: ..., 7: ...}`; this is appropriate for the
   fixed-width branch and is not an all-width verifier.

2. **Width-5/6/7 certificate identities — justified, tool-checked locally.**
   Fresh root replays accepted all three identities:

   - `M_5^20 = 6 ⊗ M_5^16`;
   - `M_6^35 = 24 ⊗ M_6^21`;
   - `M_7^32 = 8 ⊗ M_7^28`.

   Each replay returned `accepted: true`, zero errors, and status
   `TOOL_CHECKED_LOCAL`, including strict matrix parsing, recomputed powers,
   and entrywise identity checks. The public-package replays for widths 5, 6,
   and 7 likewise returned `accepted: true`; the width-7 process completed
   with exit code 0 immediately as it was stopped. The persisted matrices
   contain no `INF` entries, as explicitly disclosed in
   `certificates/manifest.json`; the tagged `INF` path is exercised by the
   mutation suite rather than by a persisted witness.

3. **Negative controls and source-tree reproducibility — justified.**
   The root full suite completed with `125 passed`; the mutation suite
   completed with `11 passed`; and the root width-5/6/7 certificate replays
   passed. The public package full suite completed with `125 passed`, with
   cache/bytecode writes disabled for this check. These results support the
   fixed-width artifact branch only; computation is not by itself a proof of
   an all-width statement.

4. **Finite identity plus prefix data implies each fixed-width tail —
   justified conditional on the written semantic lemmas.**
   The current `mathematics/COMPLETE_PROOF_FINAL.md`,
   `mathematics/MINPLUS_PATH_SEMANTICS_FINAL.md`, and
   `mathematics/MINPLUS_IDENTITY_LEMMA_FINAL.md` provide the stated bridge:
   total domination is represented by weighted closed walks, matrix powers
   encode walk minima, and the entrywise shift propagates from the recorded
   thresholds. The current prefix records cover the stated base ranges. This
   review accepts the certificate premise and its fixed-width scope; it does
   not convert the certificate into evidence for arbitrary `m`.

5. **Certificate support for the all-width claims — gap/blocking scope error.**
   The verifier, certificate manifest, certificate directories, and public
   package are restricted to widths 5, 6, and 7. Nothing in this branch
   verifies the quantifier `m >= 2` in the EOD characterization or lower
   bound, nor the all-`k` construction in the even-width family. Those claims
   require the separate human proof/citation branch and must not be presented
   as certificate-backed conclusions.

6. **Current manuscript versus public manuscript — fatal publication
   mismatch.**
   `paper/manuscript.tex` currently has the title *Efficient Open Domination
   and Exact Total Domination in Cylindrical Grids* and states the all-width
   EOD theorem, the general lower bound, and
   `gamma_t(P_(2k) square C_((2k+1)t)) = k(k+1)t` in its abstract and
   introduction. In contrast, `release/public/paper/manuscript.tex` has the
   title *Exact Total Domination Numbers of Cylindrical Grids of Widths Five,
   Six, and Seven* and its abstract/introduction are restricted to widths
   5--7. The public package also contains no `generalization/` directory.
   Therefore the public release does not carry the frozen final theorem
   scope.

7. **Root integrity manifest — fatal stale metadata.**
   Recomputing the current root `SHA256SUMS` found three mismatches:
   `paper/manuscript.tex`, `paper/manuscript.pdf`, and `paper/manuscript.log`.
   The public package's own `release/public/SHA256SUMS` had 76 entries and
   zero mismatches, so it is internally self-consistent, but that does not
   repair its mismatch with the current source/final manuscript. The current
   source and public artifacts consequently represent different snapshots.

8. **Release status metadata — justified as a blocker, not an acceptance.**
   `RESULT.json`, `release/FINAL_RELEASE_REPORT.md`, and
   `release/GITHUB_RELEASE_AUDIT.md` explicitly retain
   `REVIEW_CONVERGENCE_FAILED`, `GITHUB_PUSH_BLOCKED`, and publication/metadata
   blockers. The public package's own final release report records a different
   local commit identifier from the source-side report. These records do not
   establish successful publication and are consistent with withholding a
   release claim.

## Checked identities and package facts

- Width 5: 169 states, 2,419 transitions, `(N,p,c)=(16,4,6)`.
- Width 6: 441 states, 11,025 transitions, `(N,p,c)=(21,14,24)`.
- Width 7: 1,156 states, 50,303 transitions, `(N,p,c)=(28,4,8)`.
- Root and public certificate manifests bind the state manifests and both
  matrix files by SHA-256; all replayed bindings matched.
- The finite-prefix and mutation evidence is labeled computational/tool
  evidence in the current artifacts and was not promoted here beyond its
  logical role.

## Suggested repairs (not part of the verdict)

1. Decide whether the release is for the full frozen theorem package or only
   the fixed-width paper. If full scope is intended, rebuild `release/public`
   from the current manuscript and include the required generalization proof
   artifacts with an explicit scope manifest.
2. If fixed-width-only scope is intended, remove or separately label the
   broader theorem claims from the finalization package rather than implying
   certificate support for them.
3. Rebuild the current manuscript PDF/log and regenerate the root integrity
   manifest after the final snapshot is frozen.
4. Re-run this review after the substantive package/scope repair; the present
   verdict is not an approval of a repaired package.
