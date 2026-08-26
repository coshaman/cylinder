# Round 02 Graph-Theoretic Referee Review

Date: 2026-08-26  
Scope: `cylindrical_total_domination` only; current manuscript, current tests,
current certificates, and the reproducible verification scripts.

## Verdict

**STRONG_ACCEPT**

I found no blocking graph-theoretic error or unresolved semantic gap. The
total-domination/automaton correspondence is correct for the stated domains
(m\in\{5,6,7\}) and (n\ge 3); the cyclic seam is handled in both
directions; the (n=3) case uses the two distinct horizontal neighbors of
the simple cycle (C_3); and the repaired prefix computation minimizes over
every reconstructed state as a possible source.

The finite-prefix part is computer-assisted evidence, not a human derivation,
but that is the manuscript's declared proof model. The current implementation
does perform the claimed unrestricted diagonal minimization, and the clean-room
certificate and mutation checks pass.

## Scores

Scores are on a 1--5 scale.

| criterion | score | assessment |
|---|---:|---|
| total-domination semantics | 5/5 | Open neighborhoods and selected-vertex obligations are explicit and correctly used. |
| automaton state/transition model | 5/5 | State realizability, pending-mask update, legality, and weights agree with independent reconstructions. |
| bijection and inverse map | 5/5 | Both soundness and completeness are proved, including wraparound. |
| seam and (n=3) handling | 5/5 | The excluded (n=2) degeneracy is respected; (C_3) is checked with distinct left/right neighbors. |
| unrestricted prefix minima | 5/5 | The repaired trace initializes one source row for every state and takes the full diagonal minimum. |
| reproducibility | 5/5 | 125 tests and all three clean-room certificate verifiers pass. |
| exposition | 4/5 | The graph-theoretic argument is clear; one extra explicit sentence tying “unrestricted” to the source loop would improve auditability. |

## Dependency graph and classifications

| dependency | location | classification | referee check |
|---|---|---|---|
| Graph family, open-neighborhood total domination, and domains | `paper/manuscript.tex:42--47`, `:137--152` | **JUSTIFIED** | The definition requires a selected open neighbor even for selected vertices; (P_m\square C_n) and (n\ge3) are stated consistently. |
| Pending-mask meaning (R_j=[m]\setminus(S_{j-1}\cup N_P(S_j))) | `paper/manuscript.tex:156--161` | **JUSTIFIED** | A row is pending exactly when left and vertical open-neighbor alternatives are absent. Self-domination is never inserted. |
| Fixed state set (Q_m) | `paper/manuscript.tex:162--166`; `src/automaton/states.cpp`; `verify/independent_states.py` | **JUSTIFIED** | The existential predecessor condition is equivalent to (R\cap N_P(S)=\varnothing); independent enumeration matches all states and hashes for widths 5, 6, and 7. |
| Transition legality (R\subseteq T) and forced head mask | `paper/manuscript.tex:168--179`; `src/automaton/transitions.cpp` | **JUSTIFIED** | Every pending row receives its right selected neighbor, and the head mask is exactly the next left/vertical residual. Independent truth-table reconstruction matches all persisted transitions. |
| Walk → total dominating set | `paper/manuscript.tex:188--196` | **JUSTIFIED** | If a row is not pending it has a selected left or vertical neighbor; if pending, transition legality supplies a selected right neighbor. This covers selected vertices as well. |
| Total dominating set → closed walk | `paper/manuscript.tex:198--203` | **JUSTIFIED** | Total domination forces the right neighbor precisely when both left and vertical alternatives are absent; the same argument applies across the wraparound edge. |
| Inverse property and weight preservation | `paper/manuscript.tex:205--209` | **JUSTIFIED** | Pending masks are forced by selected masks, and ∑(|S_{j+1}|\)=∑(|S_j|\)=\(|D|\). |
| (n=3) seam | `paper/manuscript.tex:210--212`; `tests/test_transfer_semantics.py:107--123` | **JUSTIFIED** | (j-1\equiv j+1\pmod n) would imply (n\mid2), impossible for (n=3). The positive and negative seam tests distinguish the two horizontal obligations. Exhaustive independent checks also agree for widths 5, 6, and 7 at (n=3). |
| Matrix-power closed-walk semantics | `paper/manuscript.tex:217--249`; `mathematics/MINPLUS_PATH_SEMANTICS_FINAL.md` | **JUSTIFIED** | The induction over the penultimate state is valid, with empty minima represented by (+\infty). |
| Finite prefix values | `paper/manuscript.tex:283--296`; `tests/test_prefix_values.py:50--120` | **JUSTIFIED** as a finite computer-assisted premise | The clean-room trace reconstructs states/transitions, initializes every source state, propagates costs, minimizes over all source diagonal entries, and compares every required row with both the persisted table and the stated formula. |
| Entrywise recurrence certificates | `verify/verify_certificates.py`; `certificates/manifest.json` | **JUSTIFIED** as tool-checked finite evidence | Widths 5, 6, and 7 independently rebuild the graph and verify both powers entrywise, including (+\infty) parsing and mutation rejection. |
| Literature context | `paper/manuscript.tex:49--64`, `paper/references.bib` | **CITED** and nonessential to the proof | The cited prior work is context/novelty scope; no graph-theoretic implication in the submitted proof depends on it. |
| Hidden assumption, missing case, or incorrect inequality | throughout the checked graph-theory chain | **NO GAP / NO ERROR / NO UNCLEAR STEP FOUND** | All stated quantifiers, domains, seams, and degeneracies tested below are covered. |

## Unrestricted-prefix audit

This was the key repair-specific check. In
`tests/test_prefix_values.py:60--77`, the current code has

```python
sources = list(range(len(states)))
costs[np.arange(len(sources)), sources] = 0
...
np.min(costs[np.arange(len(sources)), sources])
```

Thus there is one initial zero-cost source for every reconstructed state, not
only states with a low-weight selected mask. The calculation is exactly

\[
\min_{q\in Q_m}(M_m^n)_{qq}=g_m(n).
\]

The test also asserts that the trace does not call the direct optimizer
(`test_clean_room_trace_does_not_use_direct_per_n_optimization`). The direct
MILP is used only for selected witness cross-checks, so it is not silently
substituting for the finite-state minimum.

## Reproducible checks performed

- `python -m pytest tests -q` → **125 passed**.
- `python -m pytest tests/test_prefix_values.py -q` → **18 passed**.
- `python -m pytest tests/test_mutations.py -q` → **11 passed**.
- State/transition/transfer-focused tests → **40 passed**.
- `python paper/check_consistency.py` → **manuscript consistency: PASS**.
- `python verify/verify_certificates.py 5 certificates/width5` → accepted.
- `python verify/verify_certificates.py 6 certificates/width6` → accepted.
- `python verify/verify_certificates.py 7 certificates/width7` → accepted.

The three certificate outputs report zero identity mismatches and
`TOOL_CHECKED_LOCAL`.

As an independent seam spot-check, I enumerated all column-mask sequences for
(P_5\square C_3) and (P_5\square C_4), comparing literal open-neighborhood
domination against the closed-walk predicate. The counts and minima agreed:

| instance | dominating sequences | minimum |
|---|---:|---:|
| (P_5\square C_3) | 12,767 | 5 |
| (P_5\square C_4) | 299,209 | 6 |

An additional all-mask (n=3) check gave exact agreement for widths 5, 6,
and 7, with minima 5, 6, and 6 respectively.

## Concrete blockers

**None for this graph-theoretic review.** In particular, the former type of
blocker—minimizing only over a restricted source subset—is not present in the
current prefix test or its documented replay.

The certificate manifest retains `theorem_status: "CONJECTURE"`, but its own
scope says it records certificate-verification status only; this is metadata
scope, not a defect in the graph-theoretic argument. Likewise, the finite
prefix remains correctly labeled computationally tested rather than being
misrepresented as a purely human lemma.

## Non-blocking suggestions

1. Keep the explicit all-state source assertion in the prefix test and add the
   same sentence to the manuscript immediately after Proposition
   `prop:finite`, so a reader need not inspect the code to interpret
   “unrestricted.”
2. Add an all-width exhaustive (n=3) seam regression, rather than the current
   illustrative width-five seam cases, as a small future strengthening.

Neither suggestion changes the verdict. A new review is required if the
state semantics, source set, prefix computation, or theorem statement is
substantively changed.

