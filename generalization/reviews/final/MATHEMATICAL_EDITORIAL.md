# Mathematical editorial audit

Date: 2026-08-26

## Scope and verdict

This is an independent audit of the authorized
`cylindrical_total_domination` project only. Development-history reports and
neighboring projects were not used as evidence. The review distinguishes the
generalized symbolic branch from the finite certificate branch for widths
5--7.

## Verdict

**FAIL — editorial promotion/integrity gate.**

I found no false mathematical implication in the generalized proof chain, and
the supplied computational checks reproduced successfully. The failure is
publication-facing: the project does not have one unambiguous frozen contract
and one synchronized promoted snapshot for the generalized theorem package.
The generalized mathematics is therefore **human-proof-candidate / referee-
checked**, not certificate-backed or formally complete.

If the question is restricted to mathematical correctness of the symbolic
generalization, the appropriate sub-verdict is **PASS WITH CAVEATS**.

## Frozen claims and promotion audit

The active manuscript promotes the following claims:

1. For (m\ge2,n\ge3), (P_m\square C_n) has an EOD set iff
   (m) is odd and (4\mid n), or (m) is even and (m+1\mid n)
   (`paper/manuscript.tex:52--60`).
2. For every (m\ge2,n\ge3), the stated odd/even dual lower bounds hold
   (`paper/manuscript.tex:73--85`, proved at `:400--424`).
3. (gamma_t(P_{2k}\square C_{(2k+1)t})=k(k+1)t) for (k,t\ge1)
   (`paper/manuscript.tex:81--85`, `:418--424`).
4. The separate certificate-backed formulas are only for widths 5, 6, and 7
   (`paper/manuscript.tex:166--201`, `:606--761`).

The active `paper/manuscript.tex` and `paper/manuscript.pdf` contain the same
generalized theorem scope; `release/public_v2/paper/manuscript.tex` and its
PDF match that active manuscript. In contrast, `release/public/paper/`
contains the older fixed-width-only manuscript. The package-level
`release/public_v2/README.md:7--11` and `release/public_v2/RESULT.json:2--10`
advertise only widths 5--7, while `generalization/RESULT.json:2--14`
records the broader theorem separately. This is partial separation, but not a
single unambiguous promotion record.

The root frozen contract is also narrower than the promoted manuscript:
`mathematics/DEFINITIONS.md:12--16` freezes (m\in\{5,6,7\}), while the
generalized theorem quantifies over all (m\ge2). The `generalization/`
branch has no single corresponding definitions/frozen-contract file.

## Dependency graph and classifications

| Node | Location | Classification | Editorial/math audit |
|---|---|---|---|
| G0. Graph, EOD, and domain definitions | `generalization/mathematics/*.md`; manuscript `:40--60` | **justified, but contract unclear** | The local definitions use (m\ge2,n\ge3), open neighborhoods, path boundaries, and cycle indices correctly. The project-level frozen contract still says widths 5--7. |
| G1. EOD row equations | `EOD_LINEAR_SYSTEM.md:1--20` | **justified** | Summing over a cycle row gives (s_{i-1}+2s_i+s_{i+1}=n); (n\ge3) correctly ensures distinct horizontal neighbors. |
| G2. Uniqueness of the row system | `EOD_LINEAR_SYSTEM.md` positive-definiteness paragraph | **justified** | The quadratic-form identity with zero boundary values is positive for every nonzero vector. |
| G3. Odd-width necessity | `ODD_WIDTH_CHARACTERIZATION.md:15--43`; manuscript `:247--272` | **justified** | The unique solution forces empty even rows; the Boolean recurrence has period four and cyclic consistency forces (4\mid n). |
| G4. Odd-width sufficiency | `ODD_WIDTH_CHARACTERIZATION.md:45--67`; manuscript `:273--279` | **justified / cited** | The period-four construction is described, and the cited Kuziak--Peterin--González Yero (2014), Proposition 5.6, is genuine prior art for this family. It must not be presented as a new family. |
| G5. Even row solution and divisibility | `EVEN_WIDTH_DIVISIBILITY.md:15--44`; manuscript `:247--263` | **justified; minor unclear notation** | The vector satisfies the recurrence and integrality forces (2k+1\mid n), including (k=1). The phrase “for every integer (r) for which the index lies in ({1,\ldots,k})” should be replaced by explicit ranges. |
| G6. Even-width construction | `EVEN_WIDTH_CONSTRUCTION_PROOF.md`; manuscript `:281--391` | **justified** | The two parity cases, boundary/central rows, reflection, and (k=1,N=3) are covered by the displayed residue partitions. |
| G7. Periodic lift | `EXACT_EVEN_WIDTH_FAMILY.md:20--30`; manuscript `:393--398` | **justified** | Copy seams preserve the two cycle shifts; no invalid “disjoint union of cycles” assumption is used. |
| G8. General total-domination lower bound | `TOTAL_DOMINATION_LOWER_BOUND.md`; manuscript `:400--417` | **justified** | Row inequalities and the nonnegative dual vector give the stated ceilings. Strict positivity is used only for even width. |
| G9. Even exact family | `EXACT_EVEN_WIDTH_FAMILY.md:34--54`; manuscript `:418--424` | **justified conditional on G6--G8** | The lifted EOD set attains the lower bound. This is a symbolic all-(k) result, not a width-5--7 certificate result. |
| F1. Finite-state bijection | manuscript `:445--504` | **justified, width-limited** | The proof covers labeled closed walks and open-neighborhood semantics for (m\in\{5,6,7\}), including (n=3). It does not quantify over arbitrary (m). |
| F2. Min-plus path semantics and recurrence | manuscript `:532--604` | **justified** | The entrywise identity implication is algebraically valid, including (+\infty) semantics and threshold restrictions. |
| F3. Width-5/6/7 matrix identities | `certificates/manifest.json`; manuscript `:615--648` | **tool-checked locally** | Independent replays accepted (M_5^{20}=6\otimes M_5^{16}), (M_6^{35}=24\otimes M_6^{21}), and (M_7^{32}=8\otimes M_7^{28}). This does not support arbitrary (m). |
| F4. Finite prefixes | `results/WIDTH5_VALUES.md`, `WIDTH6_VALUES.md`, `WIDTH7_VALUES.md` | **computationally tested** | Prefix data supplies the recurrence bases; it is not a general proof and must retain that status label. |
| F5. Fixed-width formulas | manuscript `:690--720` | **justified conditional on F1--F4** | The recurrence begins only at thresholds 16, 21, and 28; the exceptional values remain in the checked prefixes. |

The dependency order is mathematically sound: G1--G5 establish necessity,
G6--G7 establish even sufficiency, G8--G9 establish the even exact family,
and F1--F5 form a separate fixed-width branch. No F-node is needed to prove a
G-node, and no G-node is silently used as a certificate for F3.

## Reproducible checks

The following checks were rerun from the authorized project:

- `python generalization/experiments/check_even_construction.py` — `PASS k=1..30`.
- `python -m pytest tests -q` — `125 passed`.
- `python verify/verify_certificates.py 5 certificates/width5` — accepted,
  zero errors.
- `python verify/verify_certificates.py 6 certificates/width6` — accepted,
  zero errors.
- `python verify/verify_certificates.py 7 certificates/width7` — accepted,
  zero errors.
- `python paper/check_consistency.py` — `manuscript consistency: PASS`.

These results support the stated finite artifacts and falsify no generalized
claim. They do not promote computation to an all-width proof. No Lean
artifacts were present, so no Lean build or `sorry` audit applies.

## Findings and severity

1. **Blocking — no single frozen contract for the promoted scope.**
   `mathematics/DEFINITIONS.md:12--16` freezes only widths 5--7, while the
   manuscript and `generalization/RESULT.json` promote (m\ge2). A reader
   cannot determine from the project contract whether the generalized theorem
   is part of the frozen target or a separate research extension.

2. **Blocking — snapshot/integrity metadata is stale at the project root.**
   Recomputing root `SHA256SUMS` found seven mismatches:
   `generalization/mathematics/COMPLETE_GENERALIZED_PROOF.md`,
   `generalization/mathematics/EXACT_EVEN_WIDTH_FAMILY.md`,
   `generalization/RESULT.json`, `mathematics/DEFINITIONS.md`,
   `paper/manuscript.log`, `paper/manuscript.pdf`, and
   `paper/manuscript.tex`. The `release/public_v2/SHA256SUMS` file is internally
   consistent, but the project root is not frozen by its claimed manifest.

3. **Major — release identity is ambiguous.** `release/public` is a
   fixed-width-only snapshot, whereas `release/public_v2` matches the active
   generalized manuscript. The generalized theorem is present in the latter,
   but its top-level README/RESULT do not state the generalized theorem. A
   submission or archive must name exactly which snapshot is authoritative.

4. **Minor — citation artifacts are not synchronized.** The manuscript’s
   inline bibliography contains Kuziak--Peterin--González Yero (2014), but
   `paper/references.bib` and `paper/REFERENCES_VERIFIED.md` do not list that
   source. This does not invalidate the proof, but it weakens reproducibility
   and makes the prior-art boundary harder to audit.

5. **Minor — internal acceptance is not external publication.**
   `generalization/RESULT.json` records an internal venue-panel `ACCEPT`, while
   the root and `release/public_v2` metadata say publication is not complete or
   not submitted. The manuscript may state an internal review status, but must
   not imply journal acceptance.

## Generalization/novelty boundary

The source-bounded literature record supports the following wording:

- The odd family (P_{2r+1}\square C_{4t}) is prior art and is attributed to
  Kuziak--Peterin--González Yero (2014, Proposition 5.6).
- The all-width EOD iff theorem and arbitrary-even-width exact family are
  apparently new within the reviewed sources, with small-width overlap.
- The width-5/6/7 formulas are separate finite-state/min-plus results and are
  not evidence for arbitrary width.

No global novelty or worldwide nonexistence claim is justified by the bounded
literature audit.

## Suggested repairs (separate from the verdict)

1. Add a generalized frozen-contract file, or explicitly make the two theorem
   branches separate contracts with an interface stating which files prove
   which claims.
2. Select one final package, synchronize its README/RESULT/manuscript scope,
   and label `release/public` as superseded if it is not authoritative.
3. Regenerate the root integrity manifest after freezing the final snapshot.
4. Synchronize `references.bib` and `REFERENCES_VERIFIED.md`, and cite the
   prior EOD source at the point where the odd family is used.
5. Keep internal venue reviews separate from any external acceptance claim.

Each substantive repair requires a new independent review before promotion.
