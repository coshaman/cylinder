# Task 9 prefix-values review

Date: 2026-08-25  
Scope: Task 9 only: finite prefix tables, clean-room min-plus tracing,
certificate diagonal cross-checks, formula exceptions, and selected direct
witnesses.

## Verdict

**PASS**

The requested finite computational artifact is reproduced:
the local Task 9 suite passes (`18 passed`), all three certificate replays are
accepted, the required ranges and formula exceptions are present, and the
selected direct witnesses pass value, cardinality, and literal open-neighborhood
checks. The artifacts consistently retain `COMPUTATIONALLY_TESTED`/
`CONJECTURE` status and do not promote the prefix computation to an all-
`n` theorem.

## Evidence run

- `python -m pytest tests/test_prefix_values.py -q` -> `18 passed`.
- `python verify/verify_certificates.py 5 certificates/width5` -> accepted,
  `TOOL_CHECKED_LOCAL`.
- `python verify/verify_certificates.py 6 certificates/width6` -> accepted,
  `TOOL_CHECKED_LOCAL`.
- `python verify/verify_certificates.py 7 certificates/width7` -> accepted,
  `TOOL_CHECKED_LOCAL`.

## Re-review of the source-state correction

The prior Important finding is resolved. For a length-`n` closed walk, let
the integer nonnegative column weights be `w_0,...,w_(n-1)`. If its total
weight is below the frozen target `T(n)`, then

\[
\min_j w_j \le \left\lfloor\frac{T(n)-1}{n}\right\rfloor.
\]

The amended docstring and Task 9 report apply this row-by-row. Independent
evaluation over the required rows gives maximum bound 1 for widths 5 and 6,
and maximum bound 2 for width 7, attained only at `n=7,14`. Thus every
hypothetical lower closed walk has a selected mask of weight at most two;
rotation places that state in the restricted source set. This covers the
previous width-7, `n=14`, weight-29 concern.

## Dependency classification

| Component | Classification | Review basis |
|---|---|---|
| Frozen graph/formula definitions | Justified | `mathematics/DEFINITIONS.md` fixes (P_m\square C_n), open neighborhoods, domains, formulas, and exceptions. |
| Required prefix ranges | Justified | `tests/test_prefix_values.py:18-22,107-110` checks exactly (3\le n\le19,34,31) for widths 5, 6, 7. |
| Formula arithmetic and exceptions | Justified | `tests/test_prefix_values.py:38-47,113-116,126-129`; all persisted rows match, including width 6 (n=12=22) and width 7 (n=7,14=(15,30)). |
| Clean-room edge reconstruction | Justified | `trace_diagonal_values` calls only `_rebuild_states` and `_rebuild_transitions` from `verify/verify_certificates.py`; no producer automaton import or execution occurs. |
| Min-plus relaxation | Justified for the reconstructed finite graph | `tests/test_prefix_values.py:70-86` performs integer relaxation over every reconstructed incoming edge; the certificate verifier independently recomputes persisted powers entrywise. |
| Avoidance of direct per-(n) optimization | Justified, with lexical-test scope caveat | The trace body has no direct optimizer or producer import; the explicit source guard is at `tests/test_prefix_values.py:146-150`. Direct MILP is used only in the seven selected-row checks. |
| Certificate diagonal cross-check | Justified | At each width, `tests/test_prefix_values.py:88-96` compares the traced value at frozen (N) to the minimum persisted (M_N) diagonal; the three verifier replays also recompute both matrices and the entrywise identity. |
| Selected direct witnesses | Justified as computational cross-checks | `tests/test_prefix_values.py:132-143` checks ((5,3),(5,10),(6,12),(6,21),(7,7),(7,14),(7,20)), including solver value, witness size, and `is_total_dominating`. |
| Status boundary | Justified | The three value files and `task-9-report.md:4-5,60-63` explicitly state finite computational evidence only and preserve theorem status as conjectural. |

## Findings

No Critical or Important finding remains. The lexical source guard for direct
optimizer exclusion remains only a scope-limited test of source text, but the
trace implementation itself visibly performs clean-room reconstruction and
min-plus relaxation, with direct MILP calls confined to the selected-row test.

## Scope boundary

This review accepts only the finite computational evidence described above. It
does not accept the automaton-to-graph bijection, the all-(n) recurrence, or
any target formula as a proved theorem; those remain outside Task 9's evidence
boundary and retain their repository statuses.
