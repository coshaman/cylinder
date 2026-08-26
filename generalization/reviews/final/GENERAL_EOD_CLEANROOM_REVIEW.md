# Generalized EOD Clean-room Review — Role A

Date: 2026-08-26

## Verdict

**PASS** for the generalized mathematical claims assigned to Role A.

I found no fatal or substantive mathematical error in the row-system
necessity argument, the odd-width converse, the all-
`k` even-width construction, the total-domination lower bound, the exact
even-width family, or the periodic lift. The finite computations were used
only as falsification/supporting checks, not as proof.

## Scope and evidence discipline

Reviewed current generalized artifacts in `generalization/mathematics/`, the
even-construction experiment, the primary 2014 citation, and the current
certificate manifests/verifier relevant to the stated evidence boundary.
Development-history reviews, manuscript files, release files, and neighboring
projects were not used as evidence. No source, manuscript, or release file was
edited; this report is the only written artifact from this review.

There are no Lean artifacts in the assigned generalized proof, so no Lean
build or `sorry` audit applies.

## Dependency graph and classifications

| Node | Location | Classification | Check |
|---|---|---|---|
| D0. Graph/EOD encoding | `EOD_LINEAR_SYSTEM.md`, definition paragraphs | **justified** | With `m>=2`, `n>=3`, the four indicators are exactly the open neighbors; path-boundary variables are correctly zero and cycle indices are modulo `n`. |
| D1. Row-sum system | `EOD_LINEAR_SYSTEM.md`, equations (1)–(2) | **justified** | Summing over a cycle row gives `s_(i-1)+2s_i+s_(i+1)=n`; the two horizontal neighbors are distinct for `n>=3`. |
| D2. Uniqueness | `EOD_LINEAR_SYSTEM.md`, positive-definiteness paragraph | **justified** | The displayed identity `z^T B_m z = sum (z_i+z_(i+1))^2`, with both boundary values zero, is positive for every nonzero vector. |
| D3. Odd necessity | `ODD_WIDTH_CHARACTERIZATION.md`, equations (2)–(3) and the residue paragraph | **justified** | The alternating row solution satisfies all boundary equations and uniqueness forces even rows empty. The recurrence has period four; cyclic consistency for residues 1, 2, and 3 modulo 4 yields `2x=1`, impossible for a Boolean variable. |
| D4. Odd sufficiency | `ODD_WIDTH_CHARACTERIZATION.md`, converse construction | **cited** | Proposition 5.6 of Kuziak–Peterin–González Yero (2014) gives the required `P_(2r+1) square C_(4t)` EOD set and explicitly states it is efficiently open dominating. The source construction matches the two period-four column patterns and the path-row parity cases. |
| D5. Even row solution/divisibility | `EVEN_WIDTH_DIVISIBILITY.md`, equations (1)–(3) | **justified** | The vector `a` satisfies the tridiagonal equations, including boundaries and the symmetry center. Since `a_2=1` for `k>=2`, and `a_1=a_2=1` for `k=1`, integrality of `s_i=n a_i/(2k+1)` forces `2k+1` to divide `n`. |
| D6. Even all-`k` construction | `EVEN_WIDTH_CONSTRUCTION_PROOF.md`, definitions through identities (I0)–(II2) | **justified** | The `E_r`, `C_r`, and `D_r` sets have the stated disjointness and sizes. The integer intervals and the one explicitly identified wrap residue prove each displayed disjoint partition modulo `4h+1` or `4h+3`. The ranges cover every row on one half, including the boundary and central rows. |
| D7. Reflection and boundaries | `EVEN_WIDTH_CONSTRUCTION_PROOF.md`, final reflection paragraph | **justified** | Reflection exchanges the two vertical-neighbor sets and leaves horizontal shifts unchanged. `A_0=A_(2k+1)=empty` handles both path boundaries. The cases `k=1` (`N=3`) and `k=2` (`N=5`) are included by the stated ranges; direct inspection gives the expected row partitions. |
| D8. Periodic lift | `EXACT_EVEN_WIDTH_FAMILY.md`, explicit lift paragraph | **justified** | For `N=2k+1`, lifting residues to `Z_(Nt)` preserves both horizontal neighbors, including copy seams, and preserves the disjoint partition row by row. No assumption that the larger cycle is a disjoint union of smaller cycles is made. |
| D9. Total-domination lower bound | `TOTAL_DOMINATION_LOWER_BOUND.md`, equations (1)–(2) and cases | **justified** | Row-wise at-least-one domination gives `B_m d >= n 1`. Multiplication by the explicitly nonnegative solution of `B_m y=1` is direction-preserving, and symmetry of `B_m` gives `|D| >= n 1^T y`. Integer rounding gives the displayed ceilings. |
| D10. Equality and exact family | `TOTAL_DOMINATION_LOWER_BOUND.md` final paragraph and `EXACT_EVEN_WIDTH_FAMILY.md` | **justified** | For even width every dual coordinate is positive, so equality in the unrounded bound forces zero slack in every row and hence exactly one selected neighbor at every vertex. The lifted EOD set has size `k(k+1)t`, exactly meeting the lower bound. |

## Independent checks

I independently reconstructed the even-width row vector and obtained the
claimed equation for every `k=1,...,100`. I independently implemented the
displayed residue-set construction and checked all row partitions for
`k=1,...,100`; no failure occurred. Direct Boolean enumeration for small
`(m,n)` also agreed with the stated EOD criterion, including `k=1` and `k=2`.
These checks are consistency/falsification evidence only.

The cited primary source is:

Kuziak, Peterin, and González Yero, “Efficient open domination in graph
products,” DMTCS 16 (2014), Proposition 5.6,
<https://dmtcs.episciences.org/1267/pdf>.

## Non-blocking caveats

1. `EVEN_WIDTH_DIVISIBILITY.md` says “for every integer `r` for which the
   index lies in `(1,...,k)`.” This should be written explicitly as
   `r=1,...,k`; the formulas and subsequent verification make the intended
   range clear, so this is a notation issue, not a proof gap.

2. The older base `mathematics/DEFINITIONS.md` still freezes the original
   width set `{5,6,7}`, whereas the assigned generalized artifacts state
   `m>=2`. If both are presented as one frozen public contract, the scope
   extension must be made explicit. This does not invalidate the generalized
   proof reviewed here because its own statement and definitions are
   explicit.

3. The width-5/6/7 certificate manifests and verifier support the phrase
   “certificate-backed” as a tool-checked computational premise. The current
   finite-prefix result files themselves do not turn those certificates into
   a general proof without the separate threshold/prefix argument. I have not
   used those computations to justify any all-`m` claim, and this Role A review
   is not an acceptance review of those separate fixed-width formulas.

## Suggested repairs (not required for the PASS verdict)

- Replace the ambiguous `r`-range sentence by an explicit quantifier.
- Reconcile the base frozen-contract file with the generalized theorem if the
  generalization is to be included in the same final package.
- Keep certificate status and theorem status visibly separate in any final
  presentation.

No substantive repair to the generalized EOD or lower-bound proof is required
on the evidence reviewed here. A new review is required after any substantive
mathematical change.
