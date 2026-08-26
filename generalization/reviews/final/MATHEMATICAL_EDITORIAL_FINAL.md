# Mathematical/editorial final re-audit

Date: 2026-08-26

## Scope

This review uses only the current authorized project
`cylindrical_total_domination`. The current generalized contract,
`paper/manuscript.tex`, `release/public_v2`, the root and `public_v2`
manifests, and the current review/replay records were inspected. The excluded
`release/public` snapshot and neighboring projects were not used as authority.
This review supersedes the earlier mathematical-editorial records; their
malformed-contract and stale-hash objections are not carried forward.

## Verdict

**MINOR for package readiness.**

**Mathematical correctness: PASS.** No false implication was found in the
generalized EOD characterization, the total-domination lower bound, the exact
even-width family, or the separate width-5/6/7 certificate-backed formulas.
The remaining qualification is that the generalized all-width branch is a
human proof checked by symbolic reasoning and independent finite falsification,
not a Lean/formally complete proof. The fixed-width branch is
`TOOL_CHECKED_LOCAL` plus the written semantic bridge and finite-prefix
argument, exactly as stated by the manuscript.

**Editorial/package readiness: MINOR.** The frozen mathematical files and
integrity manifests are repaired and internally consistent. Submission-facing
author metadata and licence confirmation remain explicitly incomplete, and a
small number of non-mathematical synchronization items remain (listed below).
These do not invalidate the theorems or the reproducibility claim.

## Frozen statement and dependency graph

| Node | Location | Classification | Audit result |
|---|---|---|---|
| G0. Generalized contract | `generalization/mathematics/DEFINITIONS_GENERALIZED.md` | **justified** | The contract now renders validly and fixes (m\ge2), (n\ge3), open neighborhoods, EOD semantics, the odd/even divisibility criterion, both lower bounds, and the exact family for (k,t\ge1). The root copy and `release/public_v2` copy are byte-identical. |
| G1. EOD row system | `generalization/mathematics/EOD_LINEAR_SYSTEM.md`; manuscript `:228--245` | **justified** | Summing exact open-neighbor equations over a cycle row gives (s_{i-1}+2s_i+s_{i+1}=n); (n\ge3) makes the two horizontal neighbors distinct. |
| G2. Uniqueness | same files | **justified** | The displayed quadratic form (sum (z_i+z_{i+1})^2), with zero boundary values, is positive for every nonzero vector. |
| G3. Odd-width necessity | `ODD_WIDTH_CHARACTERIZATION.md`; manuscript `:265--272` | **justified** | The unique row solution empties even rows; the Boolean recurrence has period four and cyclic consistency forces (4\mid n). |
| G4. Odd-width sufficiency | same file; cited Proposition 5.6 | **cited / justified** | The (1100/0011) construction checks the horizontal, vertical, and path-boundary conditions. The odd family is correctly identified as prior art, not as a new contribution. |
| G5. Even-width divisibility | `EVEN_WIDTH_DIVISIBILITY.md`; manuscript `:247--263` | **justified** | The explicit row solution satisfies the boundary equations; an entry equal to (1) and integrality force (2k+1\mid n), including (k=1). |
| G6. Even-width construction | `EVEN_WIDTH_CONSTRUCTION_PROOF.md`; manuscript `:281--391` | **justified** | The two parity cases, modular interval identities, boundary rows, reflection, central rows, and (k=1,N=3) are covered. The independent construction replay passes (k=1,\ldots,30); this is supporting evidence, not a substitute for the all-(k) proof. |
| G7. Periodic lift | `EXACT_EVEN_WIDTH_FAMILY.md`; manuscript `:393--398` | **justified** | The base partition identity lifts copy-by-copy across the cycle seam, preserving both horizontal shifts. |
| G8. General lower bound | `TOTAL_DOMINATION_LOWER_BOUND.md`; manuscript `:400--417` | **justified** | Row domination inequalities and the nonnegative vector (B_m^{-1}{\bf1}) give the stated ceilings. Strict positivity is used only for the equality characterization in even width. |
| G9. Exact even family | `EXACT_EVEN_WIDTH_FAMILY.md`; manuscript `:418--424` | **justified conditional on G6--G8** | The lifted EOD set has size (k(k+1)t), exactly matching the lower bound. |
| F1. Finite-state semantics | manuscript `:445--504` and `public_v2/verify` records | **justified, width-limited** | The pending-mask definition, legal transition, wraparound, selected-vertex semantics, and (n=3) case establish the weight-preserving closed-walk bijection for (m\in\{5,6,7\}). |
| F2. Min-plus path and recurrence lemmas | manuscript `:532--604` | **justified** | The induction, (+\infty) convention, scalar shift, associativity, and entrywise identity propagation are correct. The recurrence is explicitly restricted to bases (n\ge N). |
| F3. Matrix identities | `certificates/`, clean-room verifier, manuscript `:615--648` | **tool-checked local** | Fresh width-5/6 replay results accept with zero errors; the current project record and user-confirmed repeated width-7 replays report `accepted: true` with zero errors. |
| F4. Finite prefixes | `results/WIDTH5_VALUES.md`, `WIDTH6_VALUES.md`, `WIDTH7_VALUES.md` | **computationally tested** | The finite ranges (3{:}19), (3{:}34), and (3{:}31) supply the recurrence bases and exceptions. Computation is not being promoted to an all-width proof. |
| F5. Fixed-width formulas | manuscript `:690--720` | **justified conditional on F1--F4** | Thresholds and prefix intervals line up, and the width-6 (n=12) and width-7 (n=7,14) exceptions are not propagated below threshold. |

The dependency order is sound:

`G1--G5 -> G6--G7 -> G8--G9`, independently of the finite branch;
`F1--F4 -> F5`, with the manuscript supplying the semantic and algebraic
bridges. No finite certificate is used as evidence for an arbitrary-width
claim.

## Reproducibility and integrity checks

- The no-cache full test run completed with **125 passed**.
- `generalization/experiments/check_even_construction.py` returned
  **PASS k=1..30**.
- `paper/check_consistency.py` returned **manuscript consistency: PASS**.
- Width 5 and width 6 clean-room certificate replays accepted with zero
  errors; the current fresh records and repeated width-7 runs report the same
  result for width 7.
- The root `SHA256SUMS` validates all **509/509** listed files.
- `release/public_v2/SHA256SUMS` validates all **106/106** listed files.
- The active manuscript and `release/public_v2/paper/manuscript.tex` are
  byte-identical, as are the generalized contract, generalized proof ledger,
  generalized result record, manuscript PDF, and the reviewed V2 audit copy.
- No Lean artifact is present, so no Lean build or live `sorry`/`admit` audit
  applies. No such escape hatch occurs in the reviewed mathematical or public
  proof artifacts.

These checks establish the claimed finite premises and snapshot integrity; they
do not replace the written all-(k) symbolic argument.

## Remaining minor findings

1. **Author/submission metadata remains incomplete.**
   `paper/AUTHOR_METADATA_TO_CONFIRM.md` and
   `submission/dam/SUBMISSION_STATUS.md` correctly leave the verified
   romanization, affiliation/address, corresponding-author e-mail, ORCID,
   funding/competing-interest statements, author contributions, and
   author-approved licence pending. `release/public_v2/RESULT.json` correctly
   says `NOT_SUBMITTED` and records the metadata/ licence limitation. This is
   the principal reason package readiness is MINOR rather than PASS; it is not a
   mathematical defect.

2. **Fixed-width contract prose has a stale status sentence.**
   `release/public_v2/mathematics/DEFINITIONS.md` says the target formulas
   remain conjectural until certificates pass, although the same package’s
   `README.md`/`RESULT.json`, the manuscript, and the successful replays record
   them as proved. This is a self-description contradiction in an auxiliary
   contract document, not a contradiction in the theorem statement or proof.

3. **Auxiliary bibliography key synchronization is incomplete.**
   The manuscript’s embedded bibliography uses `KuziakPeterinYero2014`, while
   `paper/references.bib` currently names the corresponding entry
   `KuziakPeterinGonzalezYero2014`; the verified-reference note also does not
   list that source as one of its numbered entries. The cited source and its
   Proposition 5.6 are nevertheless identified in the manuscript and the
   bounded literature review. This is a reproducibility/editorial issue, not a
   proof gap.

4. **Internal review status must remain clearly non-journal status.**
   The generalized result record contains an internal venue-panel decision, but
   the public package correctly states `NOT_SUBMITTED` and no journal
   acceptance is claimed. The present wording is acceptable provided that
   distinction is preserved.

## Suggested repairs, separate from the verdict

- Complete author, declaration, and licence fields before journal submission.
- Replace the stale conjectural sentence in the fixed-width contract with the
  current proved-status wording, while preserving historical status labels in
  a clearly marked audit section if desired.
- Reconcile the BibTeX key and the verified-reference inventory before a
  submission build.

These are editorial/metadata repairs. A substantive change to the generalized
proof, automaton semantics, cited theorem scope, or certificate premises would
require a new independent review.
