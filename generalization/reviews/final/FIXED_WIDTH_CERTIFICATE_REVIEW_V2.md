# Fresh fixed-width/public-package re-audit

> Historical development record retained for provenance. Superseded by the
> current certificate referee verdict; status language below is not current.

Date: 2026-08-26

## Scope and evidence rule

This is an independent re-audit of
`cylindrical_total_domination/release/public_v2` only. The old
`release/public` package and development history were not used as evidence.
Only the frozen files, submitted proof records, cited-source records, and
reproducible artifacts in `public_v2` were inspected. No source file was
modified; this report is the sole written artifact from this review.

## Verdict

**MINOR.**

The width-5, width-6, and width-7 certificate branches pass their clean-room
replays, prefix checks, mutation tests, independent automaton checks, and
per-certificate hash bindings. The generalized manuscript, generalized
mathematics, literature audit, reviews, and publication metadata are present,
and the current README/RESULT explicitly separate the generalized symbolic
contract from the fixed-width certificate contract.

The package is not an unconditional PASS because the advertised package-wide
integrity manifest is stale/incomplete, the generalized frozen-contract file
is malformed as text, and several included review/status records still carry
pre-promotion or contradictory labels. These are repairable package and
publication-contract defects. I found no certificate identity mismatch or
mathematical error in the fixed-width bridge.

## Reproduced checks

### Fixed-width certificates

`python verify/verify_certificates.py {5,6,7} certificates/width{5,6,7}`
accepted all three certificates with status `TOOL_CHECKED_LOCAL` and no
errors. Each run independently rebuilt the state and transition semantics,
checked the manifest contents, counts, canonical hashes, strong connectivity,
metadata bindings, MTX1 dimensions/tags, both matrix powers, and the
entrywise shift including tagged-`INF` semantics.

| width | states | transitions | identity | `(N,p,c)` | replay |
|---:|---:|---:|---|---|---|
| 5 | 169 | 2,419 | `M_5^20 = 6 ⊗ M_5^16` | `(16,4,6)` | accepted |
| 6 | 441 | 11,025 | `M_6^35 = 24 ⊗ M_6^21` | `(21,14,24)` | accepted |
| 7 | 1,156 | 50,303 | `M_7^32 = 8 ⊗ M_7^28` | `(28,4,8)` | accepted |

The persisted matrices contain no `INF` entries. The verifier's `None`/`INF`
logic is present, and the mutation suite exercises the finite-to-tagged-`INF`
rejection boundary; this is a coverage limitation, not an identity failure.

### Prefixes, mutations, and independent reconstruction

- `python -m pytest tests/test_prefix_values.py -q --import-mode=importlib -p no:cacheprovider`
  -> **18 passed**. The unrestricted clean-room diagonal traces cover
  `3..19`, `3..34`, and `3..31` for widths 5, 6, and 7, including the stated
  exceptions at width 6, `n=12`, and width 7, `n=7,14`.
- `python -m pytest tests/test_mutations.py -q --import-mode=importlib -p no:cacheprovider`
  -> **11 passed**. Deleted/inserted/reweighted transitions, a corrupted
  state, finite and tagged-infinite matrix changes, a dimension change, and
  changed `(N,p,c)` parameters were rejected.
- `python -m pytest tests/test_independent_automaton.py -q --import-mode=importlib -p no:cacheprovider`
  -> **12 passed**. The independent Python/C++ reconstruction matched all
  three persisted state/transition sets, counts, hashes, weights, and strong
  connectivity.
- `python -m pytest tests -q --import-mode=importlib -p no:cacheprovider`
  -> **125 passed**. The post-update contract smoke test also passed (`5
  passed`); the latest textual package changes did not alter executable
  certificate code.

These are finite computational premises. They do not replace the written
automaton bijection, min-plus path lemma, or thresholded recurrence argument.

## Dependency graph and classifications

1. **Generalized scope contract -> manuscript scope — justified, with a
   contract-format defect.** `README.md` and `RESULT.json` now name
   `generalization/mathematics/DEFINITIONS_GENERALIZED.md` and separately
   identify `mathematics/DEFINITIONS.md` as the width-5/6/7 certificate
   contract. The manuscript and rendered PDF state the generalized
   (m\ge2,n\ge3) EOD theorem, the two lower bounds, and the exact even-width
   family. This repairs the former scope omission.

2. **Generalized symbolic branch — cited/justified by the submitted records.**
   The included proof ledger and reviews classify the row-system necessity,
   odd-width characterization, even-width divisibility/construction,
   lower-bound argument, periodic lift, and exact even family as proved or
   cited. The odd EOD family is explicitly attributed as prior art. The
   generalized branch is not silently supported by the fixed-width matrices.

3. **Fixed-width semantic bridge — justified.** The state/pending-row
   definitions, open-neighborhood convention, selected-vertex requirement,
   cyclic closure including (n=3), and head-column weight are explicitly
   proved in `mathematics/STATE_SEMANTICS.md` and
   `mathematics/AUTOMATON_BIJECTION_FINAL.md`.

4. **State/transition manifests -> matrix certificates — tool-checked
   locally.** `verify/verify_certificates.py` is a clean-room implementation:
   it does not import or execute producer code. The replay results above bind
   each persisted manifest and matrix byte stream to reconstructed semantics.

5. **Matrix identities + prefixes -> infinite fixed-width formulas —
   justified conditionally.** `MINPLUS_PATH_SEMANTICS_FINAL.md`,
   `MINPLUS_IDENTITY_LEMMA_FINAL.md`, and `COMPLETE_PROOF_FINAL.md` correctly
   use entrywise identities only from thresholds (16,21,28), respectively;
   the complete prefix ranges supply the bases through (N+p-1). The
   exceptions below the thresholds are not propagated by the recurrence.

6. **Publication metadata — transparent but not submission-complete.**
   `RESULT.json` says `NOT_SUBMITTED`; author fields and the final license are
   explicitly pending. `CITATION.cff`, the manuscript, literature audit, and
   venue records are present. No external journal acceptance is established
   by these files.

## Findings

### 1. Minor — `SHA256SUMS` is stale and incomplete

The current `SHA256SUMS` contains 96 syntactically valid entries. Every listed
path exists, but four listed hashes no longer match the current files:

- `README.md`;
- `RESULT.json`;
- `paper/references.bib`;
- `generalization/reviews/final/FIXED_WIDTH_CERTIFICATE_REVIEW.md`.

After excluding generated `__pycache__` and `.pytest_cache` files, four
current substantive files are unlisted:

- `generalization/mathematics/DEFINITIONS_GENERALIZED.md`;
- `generalization/reviews/final/BMMSS_NOVELTY_EDITORIAL.md`;
- `generalization/reviews/final/MATHEMATICAL_EDITORIAL.md`;
- `generalization/reviews/final/venue/DAM_GRAPH_THEORY_EDITORIAL.md`.

This V2 report is a post-audit deliverable and is likewise not counted as
part of the pre-existing frozen hash snapshot.

The six per-width certificate hashes and their internal metadata bindings do
match. Thus this is a package-snapshot/integrity defect, not evidence against
the three matrix identities.

### 2. Minor — generalized frozen contract is malformed

`generalization/mathematics/DEFINITIONS_GENERALIZED.md:7,13-15` contains
rendered text such as `mge2`, `nge3`, `4mid n`, and `gelceil` instead of the
intended inequality, divisibility, and ceiling notation. It also contains an
embedded carriage-return character inside the ceiling expression. The
manuscript and proof files state the intended formulas correctly, so the
mathematical intent is recoverable, but the file advertised by `RESULT.json`
as the frozen generalized contract is not an exact, clean contract.

### 3. Minor — included status records are not synchronized

The current promoted records say `ALL_THREE_THEOREMS_PROVED` and
`GENERAL_EOD_AND_TOTAL_DOMINATION_THEOREMS_PROVED` (`README.md`,
`RESULT.json`, `generalization/RESULT.json`, and
`generalization/mathematics/COMPLETE_GENERALIZED_PROOF.md`). However:

- `generalization/mathematics/EOD_COMPLETE_THEOREM.md:52-53` still says the
  generalized result must not be promoted until hostile reports are resolved;
- `verify/PAPER_REVIEW.md:13-15,33,48` still says the project is
  `STILL_OPEN` and the formulas are `CONJECTURE`;
- `verify/MATRIX_IDENTITY_REVIEW.md:57` describes the project status as
  `CONJECTURE`; and
- `generalization/reviews/final/MATHEMATICAL_EDITORIAL.md:12` gives an
  editorial-promotion `FAIL`, while `generalization/RESULT.json:14,21`
  records manuscript promotion completed and an internal venue-panel
  `ACCEPT`.

These can be reconciled as historical/scope-limited reports, but the files do
not consistently mark them as superseded. The contradiction is publication-
facing and does not invalidate the proof chain or certificate replay.

### 4. Minor — some claimed reproducibility entry points are absent

The current included review records refer to
`generalization/experiments/check_even_construction.py` and
`paper/check_consistency.py`, but neither path exists in `public_v2`. The
package does contain the symbolic construction proofs and the fixed-width
test/verifier artifacts, so this is a reproducibility-record omission rather
than a mathematical gap. `paper/DAM_SUBMISSION_REQUIREMENTS_CURRENT.md` also
mentions a draft `paper/SUBMISSION_CHECKLIST.md` that is absent.

### 5. Minor — BibTeX key mismatch remains

`paper/manuscript.tex:139` cites `KuziakPeterinYero2014`, whereas
`paper/references.bib:97` defines `KuziakPeterinGonzalezYero2014`. The PDF is
usable because it contains an embedded bibliography, but the advertised
editable `.bib` source does not resolve that citation key. This is an
editorial/reproducibility issue only.

## Non-findings

- No live Lean artifact or `sorry`/`admit` escape hatch was found; no Lean
  build gate applies.
- The width-specific verifier is not being used to claim arbitrary-width
  certificate coverage.
- The fixed-width recurrence thresholds and prefix intervals are aligned.
- The current README/RESULT now expose both theorem branches and no longer
  omit the generalized package from the public snapshot.
- The publication metadata honestly records `NOT_SUBMITTED` and pending
  author/license decisions; the internal venue-panel label is not treated as
  a journal acceptance.

## Suggested repairs (separate from the verdict)

1. Freeze the final `public_v2` file set and regenerate `SHA256SUMS`, or
   narrow its documented scope explicitly.
2. Rewrite `DEFINITIONS_GENERALIZED.md` with literal, valid mathematical
   notation and bind that file in the integrity manifest.
3. Mark pre-promotion reviews as superseded/scope-limited, reconcile the EOD
   promotion sentence, and distinguish internal editorial decisions from
   `NOT_SUBMITTED` publication status.
4. Either include the referenced construction/consistency scripts and
   submission checklist or remove those reproducibility references.
5. Make the BibTeX citation key identical to the manuscript key, then rerun
   the publication-document check.

A substantive repair to the theorem statements, generalized proof, semantic
bridge, or certificate premises requires a new independent review. Under the
current snapshot, the required verdict is **MINOR**.
