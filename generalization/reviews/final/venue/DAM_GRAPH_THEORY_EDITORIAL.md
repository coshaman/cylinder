# DAM graph-theory editorial review

## Review scope and method

This review is limited to the current manuscript and the frozen `release/public_v2`
package in this project. The manuscript source
`submission/dam/manuscript.tex` and `release/public_v2/paper/manuscript.tex` are
byte-identical (SHA-256
`D84BE8FDF3EC6236F3D58B4E77D4B1D414494853BA508253B0CAB624A49B057C`). I did not
use neighboring projects or development-history reports as evidence.

The audit was adversarial: definitions and quantifiers were read literally;
the dependency graph was reconstructed; the EOD construction was independently
implemented for \(k=1,\ldots,30\); the public_v2 test suite and certificate
verifiers were rerun; and the manuscript PDF was rendered and inspected.

## Verdict

**MINOR_REVISION.**

I found no blocking graph-theoretic error in the stated results or in the
finite-state semantics. The EOD row equations, the total-domination lower
bound, the open-neighborhood automaton bijection, the min-plus bridge, and the
thresholded recurrence are mathematically coherent. The public_v2 artifacts
also reproduce the stated finite premises.

The paper should nevertheless receive a new editorial pass before acceptance:
the proof of the all-width residue construction is too compressed at several
set-disjointness and boundary points, index conventions change mid-paper, and
the public artifact contains a contradictory status label. These are repairable
presentation and reproducibility-contract issues. A substantive repair to a
proof would require a fresh review.

## Dependency graph and step classifications

| Node | Location | Classification | Assessment |
|---|---|---|---|
| Graph and total-domination definitions | Manuscript lines 40--45, 428--443; `public_v2/mathematics/DEFINITIONS.md` | **justified** | The Cartesian product, open-neighborhood convention, path boundary, cycle indexing, and the requirement that selected vertices also be dominated are stated consistently. |
| EOD equations and row summation | Manuscript lines 228--245 | **justified** | Equation (1) correctly counts open horizontal and vertical neighbors, including path boundaries; summing over a cycle row gives (2). The positive-definiteness identity is correct. |
| Row solution and divisibility | Manuscript lines 247--263 | **justified** | The displayed odd/even solutions satisfy the boundary equations, and uniqueness makes substitution sufficient. In the even case \(a_i=1\) does force \(2k+1\mid n\). |
| Odd-width EOD necessity and construction | Manuscript lines 265--279 | **justified** | The Boolean recurrence gives period four and the \(4\mid n\) condition. The alternating \(1100/0011\) construction handles the vertical and boundary rows. |
| Even-width residue construction | Manuscript lines 281--391; `public_v2/mathematics/COMPLETE_PROOF_FINAL.md` | **justified, with exposition gap** | The formulas and independently checked identities are consistent, including \(k=1\). However, several claimed disjoint-union and wrap-around facts are asserted rather than fully demonstrated; see Finding 1. |
| General total-domination lower bound | Manuscript lines 400--424 | **justified** | The row inequalities are correct. Multiplication by the nonnegative vector \(B_m^{-1}{\bf1}\) gives the stated bounds, and the even EOD lift attains equality. |
| Finite-state definition | Manuscript lines 447--470; `public_v2/mathematics/AUTOMATON_BIJECTION_FINAL.md` | **justified** | The pending mask excludes exactly the left and vertical alternatives; the head update correctly excludes the current-column horizontal-left alternative \(S\) and vertical coverage by \(T\). The quantified predecessor condition is equivalent to \(R\subseteq[m]\\setminus N_P(S)\). |
| Closed-walk bijection | Manuscript lines 472--504 | **justified** | Both soundness and completeness are present, including the wraparound transition and the fact that self-membership is not domination. The \(n=3\) distinct-neighbor point is correctly addressed. |
| Min-plus path semantics | Manuscript lines 532--558 | **justified** | The induction over the penultimate state is valid with \(+\infty\) for missing walks. |
| Thresholded recurrence | Manuscript lines 576--604; `public_v2/mathematics/MINPLUS_IDENTITY_LEMMA_FINAL.md` | **justified** | Entrywise equality, associativity, scalar shifting, diagonal minimization, and the restriction to bases \(n\ge N\) are handled correctly. |
| Finite certificate proposition | Manuscript lines 606--648; public_v2 certificates and verifier | **cited/artifact-supported** | This is a computer-assisted premise, not a human derivation. The frozen verifier independently rebuilds the graph and recomputes both powers, so the stated certificate premise is reproducible. |
| Promotion to the three infinite formulas | Manuscript lines 690--720 | **justified conditional on the finite proposition** | The thresholds and prefix intervals line up: \(3\!:\!19\), \(3\!:\!34\), and \(3\!:\!31\), with bases \(16\!:\!19\), \(21\!:\!34\), and \(28\!:\!31\). The arithmetic reduction and exceptional-value handling are correct. |
| Literature boundary and novelty wording | Manuscript lines 87--162, 209--223 | **cited, with citation-precision caveat** | The cited records support the broad distinction between total domination, ordinary domination, EOD, cylinders, toroidal products, and 2-domination. The exact theorem numbers/original source for the \(P_p\\square C_3,C_4\) prior formulas should be made more explicit; see Finding 3. |

No step was classified as an error. No unproved computational observation was
used as a substitute for the recurrence argument; the computation supplies
only the finite proposition claimed in the manuscript.

## Findings

### 1. Minor: the even-width construction proof suppresses essential set bookkeeping

**Location:** manuscript lines 319--391, especially equations (4)--(10).

The proof says that the \(U_r\) and \(V_r\) identities follow by “grouping”
representatives, then invokes concatenation and “explicit” wrap-around to obtain
the disjoint unions. The exact ranges in which the interval representatives
are distinct modulo \(N\), and the reason that the \(E_r\), \(C_r\), and \(D_r\)
pieces do not overlap, are not written out. The central and boundary cases are
then summarized as “omitted empty-union cases.” This is enough for a patient
reader to reconstruct, and independent checks found no counterexample, but the
lemma is the only all-width even sufficiency argument and should not depend on
unstated interval bookkeeping.

**Why it matters:** the EOD characterization and the general equality family
depend on this lemma. A small indexing or modular-overlap error would invalidate
both claims.

**Suggested repair:** state the exact ranges for \(r\) in each use of (4) and
(5), show the cardinality and disjointness of each displayed block, and write
the \(k=1\), boundary, and central cases explicitly (or give a short separate
case table). Keep the independent construction check as evidence, not as the
proof of the all-\(k\) statement.

### 2. Minor: row-index conventions change without an explicit reindexing sentence

**Location:** manuscript lines 228--255 versus lines 428--443 and onward.

The EOD section uses rows \(1,\ldots,m\) with \(s_0=s_{m+1}=0\), while the
finite-state section switches to \([m]=\{0,\ldots,m-1\}\). Both conventions are
valid and the formulas are internally consistent, but the paper never plainly
says that the second convention is a reindexing of the first.

**Why it matters:** the all-width construction and the width-five-to-seven
automaton are adjacent major components. A reader can reasonably wonder
whether \(A_i\), \(S_j\), and \(N_P\) refer to the same row labels at the seam.

**Suggested repair:** add one sentence at the start of the preliminaries, e.g.
“The preceding EOD section uses one-based row labels; from this point on we
relabel the same path vertices by \([m]=\{0,\ldots,m-1\}\).”

### 3. Minor: prior-result citation scope should be made bibliographically precise

**Location:** manuscript lines 87--115 and 135--150.

The manuscript attributes the exact \(P_p\\square C_3\) and
\(P_p\\square C_4\) formulas to Hu--Sohn--Chen (2016), while the cited paper’s
title and abstract emphasize \(C_m\)-bundles over a cycle and the toroidal
case; the dissertation records the cylinder formulas and identifies the same
reference. The claim is plausible and consistent with the public record, but
the manuscript should identify the precise theorem in the original article,
or cite the original source directly if the formulas are inherited from an
earlier paper.

**Why it matters:** DAM readers need to distinguish a cylinder
\(P_p\\square C_q\) from a toroidal product or a graph bundle. The manuscript is
trying to make exactly that distinction, so the citation should be auditable
without consulting a dissertation.

**Suggested repair:** add theorem/section numbers and state explicitly whether
the cited result is in Hu--Sohn--Chen itself or is being cited through the
dissertation’s provenance account. The same precision would improve the EOD
reference to Proposition 5.6 and Theorem 5.7.

### 4. Minor: public_v2 contains a stale mathematical-status sentence

**Location:** `release/public_v2/mathematics/DEFINITIONS.md`, “Target Formulas.”

That file first records the primary status as `ALL_THREE_THEOREMS_PROVED`, but
then says that the target formulas are “conjectural targets only” and remain
conjectural until certificates pass. The certificates do pass in the frozen
package, and the manuscript presents the formulas as theorems.

**Why it matters:** this is a contract-level exposition contradiction in the
public artifact, even though it does not alter the theorem proved by the
manuscript.

**Suggested repair:** change the paragraph to describe the targets as the
initial frozen targets and state that the final package promotes them after the
semantic proof and certificate checks, or preserve the historical label in a
clearly marked non-final section.

### 5. Minor: finite-prefix evidence is not reader-visible enough in the paper

**Location:** manuscript lines 615--648 and Tables 2--4.

The proof of the all-\(n\) claims depends on every prefix row, but the paper
prints only the width-five full prefix and selected width-six/width-seven
rows. The missing rows are referred to as “machine-readable” project data.
That is acceptable for a computer-assisted supplement, but the manuscript does
not give a permanent artifact identifier, release URL, or exact version binding
in the text itself.

**Why it matters:** the theorem proof is conditional on a finite proposition
whose input is external to the typeset article. The public_v2 package does
contain the data and a clean-room verifier, but a DAM reader needs a stable way
to identify exactly which artifact is part of the proof.

**Suggested repair:** cite a permanent repository/release archive in the
manuscript and state that the omitted prefix rows are included in a named
supplement. Optionally print the compact complete prefix tables in an appendix.

## Verification performed

- `python -m pytest tests -q --import-mode=importlib` in `release/public_v2`:
  **125 passed**.
- `python verify/verify_certificates.py 5 certificates/width5`:
  **accepted: true**, zero identity mismatches.
- The corresponding width-six and width-seven commands:
  **accepted: true**, zero identity mismatches.
- The certificate checks rebuilt states, transitions, dimensions, hashes,
  finite/\(+\infty\) matrix tags, both persisted powers, and entrywise
  min-plus identities.
- An independent implementation of the manuscript’s even-width residue
  formulas verified the defining partition identities and row cardinalities
  for \(k=1,\ldots,30\). This is a falsification check, not a replacement for
  the all-\(k\) proof.
- The rendered 12-page manuscript PDF was visually inspected. No clipped
  equations, overlapping text, broken tables, or unreadable reference block
  was found. The prior-results table is dense but legible.
- No Lean artifact is present in the reviewed proof package, and no live
  `sorry`/`admit` escape hatch occurs in the reviewed manuscript or public_v2
  proof artifacts.

## Required disposition

The mathematical claims may proceed after the five presentation/artifact
repairs above, provided the residue-lemma expansion does not change its
content. Any change to the construction, state semantics, cited theorem scope,
or finite certificate premises should trigger a new graph-theory review.
