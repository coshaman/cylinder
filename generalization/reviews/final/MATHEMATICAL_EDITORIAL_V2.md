# Mathematical editorial audit — superseding review

Date: 2026-08-26

## Scope and verdict

This review supersedes `MATHEMATICAL_EDITORIAL.md`. It audits only the current
authorized `cylindrical_total_domination` project. Development-history reports
and neighboring projects were not used as evidence.

## Verdict

**FAIL — current frozen-package integrity gate.**

The mathematical proof chain has no located false implication. The generalized
branch is a coherent human-proof candidate, and the width-5--7 certificate
branch reproduced successfully. However, the current frozen contract is not
readable as mathematics and the claimed root integrity manifest is not
current. These are blocking editorial defects for promotion of the package,
not a mathematical counterexample.

Sub-verdicts:

- Generalized symbolic mathematics: **PASS WITH CAVEATS**.
- Width-5--7 certificate-backed mathematics: **PASS**, with status limited to
  `TOOL_CHECKED_LOCAL` plus the stated semantic and prefix assembly.
- Manuscript branch separation: **PASS** after the latest metadata repair.
- Frozen snapshot/integrity: **FAIL** until the two blockers below are fixed.

## Repairs verified

The following claimed repairs are present and correct in scope:

1. `generalization/mathematics/DEFINITIONS_GENERALIZED.md` exists and states
   that it is separate from the width-5--7 contract.
2. `release/public_v2/README.md` now names both the all-width structural branch
   and the width-5--7 finite branch.
3. `release/public_v2/RESULT.json` now records
   `generalized_theorem_status` and the generalized contract path, while also
   retaining `publication_status: NOT_SUBMITTED`.
4. The active manuscript and `release/public_v2/paper/manuscript.tex` have the
   generalized theorem and the separate finite certificate layer.
5. `paper/references.bib` now contains a Kuziak--Peterin--González Yero (2014)
   entry.

The public_v2 manuscript and PDF match the active manuscript by SHA-256.

## Frozen-contract finding

**Blocking for editorial freeze; minor relative to the proof itself.**

`generalization/mathematics/DEFINITIONS_GENERALIZED.md:7--18` is corrupted as
rendered text: it contains `mge2`, `nge3`, `4mid n`, `gelceil`, and `tge1`,
with literal carriage-return damage inside the ceiling expressions. The
intended claim is recoverable from the manuscript and the other proof files,
but this file cannot serve as a character-stable frozen mathematical contract.

The intended domain and claims are:

\[
m\ge2,\quad n\ge3,
\]

\[
P_m\square C_n\text{ has an EOD set}
\iff (m\text{ odd and }4\mid n)\text{ or }
(m\text{ even and }m+1\mid n),
\]

the odd/even lower bounds stated in `TOTAL_DOMINATION_LOWER_BOUND.md`, and
\[
\gamma_t(P_{2k}\square C_{(2k+1)t})=k(k+1)t
\quad(k,t\ge1).
\]

Because the active manuscript states these claims clearly and the proof files
repeat their domains, this is not a proof gap. It is nevertheless blocking for
a frozen-contract/promotion gate until the contract is repaired and hashed.

## Dependency graph and classifications

| Node | Location | Classification | Scope check |
|---|---|---|---|
| G0. Generalized definitions | generalized contract; manuscript `:52--60` | **unclear as frozen text, justified in manuscript** | (m\ge2,n\ge3), open neighborhoods, path boundaries, and selected-vertex domination are correctly intended. |
| G1. EOD row system | `EOD_LINEAR_SYSTEM.md` | **justified** | Summing exact open-neighbor equations gives (s_{i-1}+2s_i+s_{i+1}=n); (n\ge3) handles distinct cycle neighbors. |
| G2. Row-system uniqueness | `EOD_LINEAR_SYSTEM.md` | **justified** | The displayed quadratic form is positive with zero boundary values. |
| G3. Odd necessity | `ODD_WIDTH_CHARACTERIZATION.md`; manuscript `:265--272` | **justified** | Empty even rows and the Boolean period-four recurrence force (4\mid n). |
| G4. Odd sufficiency | `ODD_WIDTH_CHARACTERIZATION.md`; manuscript `:273--279` | **justified / cited** | The construction is valid and Proposition 5.6 of Kuziak--Peterin--González Yero (2014) is prior art. It is not a new family. |
| G5. Even divisibility | `EVEN_WIDTH_DIVISIBILITY.md`; manuscript `:247--263` | **justified** | The explicit row vector and integrality force (2k+1\mid n), including (k=1). The remaining range wording is only a minor clarity issue. |
| G6. Even construction | `EVEN_WIDTH_CONSTRUCTION_PROOF.md`; manuscript `:281--391` | **justified** | Both parity cases, boundaries, reflection, central rows, and (k=1,N=3) are covered. |
| G7. Periodic lift | `EXACT_EVEN_WIDTH_FAMILY.md`; manuscript `:393--398` | **justified** | Copy seams preserve the two horizontal shifts. |
| G8. General lower bound | `TOTAL_DOMINATION_LOWER_BOUND.md`; manuscript `:400--417` | **justified** | Row inequalities plus the nonnegative dual vector yield the ceilings; strict positivity is needed only in the even case. |
| G9. Even exact family | `EXACT_EVEN_WIDTH_FAMILY.md`; manuscript `:418--424` | **justified conditional on G6--G8** | The lifted EOD construction attains the lower bound for all (k,t\ge1). |
| F1. Finite-state bijection | manuscript `:445--504` | **justified, width-limited** | It covers (m\in\{5,6,7\}), not arbitrary (m). |
| F2. Min-plus semantics/recurrence | manuscript `:532--604` | **justified** | Entrywise identities propagate with correct (+infty) and threshold handling. |
| F3. Matrix identities | `certificates/manifest.json`; manuscript `:615--648` | **tool-checked locally** | The three exact identities are independently replayable only for widths 5, 6, and 7. |
| F4. Prefix values | `results/WIDTH{5,6,7}_VALUES.md` | **computationally tested** | Prefixes are finite premises, not an all-width argument. |
| F5. Fixed-width formulas | manuscript `:690--720` | **justified conditional on F1--F4** | Thresholds and exceptional prefixes are handled without propagating below threshold. |

The dependency order is sound: G1--G5 → G6--G7 → G8--G9 is the generalized
branch; F1--F5 is a separate fixed-width branch. No certificate is used to
prove an arbitrary-width claim, and no generalized claim is represented as a
width-5--7 matrix certificate.

## Reproducible checks rerun

- `python generalization/experiments/check_even_construction.py` — `PASS k=1..30`.
- `python -m pytest tests -q` — `125 passed`.
- Width-5 certificate verifier — accepted, zero errors.
- Width-6 certificate verifier — accepted, zero errors.
- Width-7 certificate verifier — accepted, zero errors.
- `python paper/check_consistency.py` — `manuscript consistency: PASS`.

These checks support the finite artifact layer and provide falsification
coverage only; they do not certify arbitrary (m). No Lean artifacts are
present, so no Lean build or `sorry` audit applies.

## Remaining findings and severity

1. **Blocking — malformed generalized frozen contract.** The new file exists,
   but its displayed formulas are not parseable mathematical notation. Repair
   the text, then treat that repaired file as a new frozen statement requiring
   review.

2. **Blocking — root integrity manifest is still not regenerated correctly.**
   The current root `SHA256SUMS` does not list
   `generalization/mathematics/DEFINITIONS_GENERALIZED.md` and has five stale
   listed hashes: `paper/references.bib`,
   `release/public_v2/generalization/reviews/final/FIXED_WIDTH_CERTIFICATE_REVIEW.md`,
   `release/public_v2/paper/references.bib`, `release/public_v2/README.md`, and
   `release/public_v2/RESULT.json`. The manifest therefore cannot bind the
   claimed repaired snapshot.

3. **Minor — verification bibliography remains incomplete.** The new BibTeX
   entry is present under the key
   `KuziakPeterinGonzalezYero2014`, while the manuscript’s inline bibliography
   uses `KuziakPeterinYero2014`, and `paper/REFERENCES_VERIFIED.md` still omits
   the source. The theorem citation is present in the manuscript, so this is
   an ancillary synchronization issue, not a mathematical gap.

4. **Minor — internal venue status is not journal acceptance.** The package
   correctly says `NOT_SUBMITTED`; the internal `venue_panel`/`final_decision`
   fields must remain clearly labeled as internal review metadata.

## Generalization and novelty boundary

The odd family (P_{2r+1}\square C_{4t}) is prior art and is attributed to
Kuziak--Peterin--González Yero (2014, Proposition 5.6). The all-width EOD
characterization and arbitrary-even-width exact family are apparently new only
within the source-bounded literature audit, with small-width overlap. The
width-5--7 formulas are separate certificate-backed fixed-width results and
are not evidence for arbitrary width.

## Suggested repairs, separate from the verdict

1. Rewrite `DEFINITIONS_GENERALIZED.md` with valid, stable notation and
   explicit quantifiers.
2. Regenerate the root `SHA256SUMS` after the final repair and verify every
   listed path, including the new contract.
3. Synchronize the BibTeX key and `REFERENCES_VERIFIED.md`.
4. After those substantive repairs, obtain a new independent review; do not
   treat this report as approval of the repaired snapshot.
