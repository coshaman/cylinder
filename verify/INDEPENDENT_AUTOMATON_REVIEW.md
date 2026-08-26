# Independent Automaton Review

## Verdict

`PASS`

This gate covers Task 5 only: the clean-room reconstruction of the width-5,
width-6, and width-7 state and weighted-transition automata. It does not review
matrix powers, matrix identities, or any theorem claim.

Critical findings: none.

Important findings: none.

## Frozen scope reviewed

- `AGENTS.md`
- `docs/DESIGN.md`
- `mathematics/STATE_SEMANTICS.md`
- `certificates/width5/automaton_manifest.json`
- `certificates/width6/automaton_manifest.json`
- `certificates/width7/automaton_manifest.json`
- `verify/independent_states.py`
- `verify/independent_transitions.cpp`
- `tests/test_independent_automaton.py`
- `verify/INDEPENDENT_AUTOMATON_REPORT.md`
- `.superpowers/sdd/2026-08-25-cylindrical-total-domination/task-5-report.md`

## Dependency graph and classification

1. `STATE_SEMANTICS.md` and `DESIGN.md` define the low-bit mask convention,
   open vertical neighborhood, pending rows, legal successor condition, next
   pending update, and head-column weight. **Justified.**
2. `verify/independent_states.py:13-28` reconstructs
   `N_m(S)` and enumerates every `(S,R)` with `R & N_m(S) = 0`, in ascending
   canonical order. This is exactly the stated legitimate-state condition.
   **Justified.**
3. `verify/independent_transitions.cpp:24-84` independently reconstructs the
   same node universe, retains exactly successors with `R subseteq T`, computes
   `R' = rows & ~(S | N_m(T))`, resolves the persisted head index, and assigns
   `popcount(T)` as weight. **Justified.**
4. `tests/test_independent_automaton.py:121-155` compares the complete state and
   transition arrays, canonical SHA-256 values, expected counts, and SCC flags
   against each persisted manifest. **Justified.**
5. SCC is computed both by the C++ reconstruction (`:111-119`) and by the
   Python test (`tests/test_independent_automaton.py:109-118`), using forward and
   reverse reachability from state 0. **Justified.**
6. `tests/test_independent_automaton.py:158-175` checks deletion of a state,
   reweighting of an edge, and deletion of all outgoing edges of state 0. Each
   mutation is rejected by the relevant equality/hash/SCC check. **Justified,
   with limited mutation scope.**
7. `tests/test_independent_automaton.py:178-185` scans the two clean-room source
   files, while direct inspection confirms that the Python file imports only
   `__future__` and the C++ file includes only standard-library headers. The
   test compiles and executes only `verify/independent_transitions.cpp`; no
   producer source or producer executable is imported, included, or executed.
   **Justified for the frozen implementation.**

The producer command stored in each manifest is metadata identifying the source
of the persisted reference artifact. It is not invoked by the clean-room test.

## Independent checks performed

Focused command, run from the project root:

```text
pytest tests/test_independent_automaton.py -q
```

Result: `12 passed in 5.78s`.

I also ran a separate reconstruction probe that did not import either
clean-room module. For each width it independently regenerated the canonical
states and edges from the equations, checked the state/edge order, verified the
closed-form state and edge counts, recomputed both canonical SHA-256 hashes,
checked every edge's legal-subset condition, next-state formula, and weight,
and recomputed forward/reverse reachability. Results:

| width | states | transitions | result |
| ---: | ---: | ---: | --- |
| 5 | 169 | 2419 | formulas, hashes, counts, SCC: OK |
| 6 | 441 | 11025 | formulas, hashes, counts, SCC: OK |
| 7 | 1156 | 50303 | formulas, hashes, counts, SCC: OK |

## Mutation and isolation assessment

The mutations are meaningful for this task: removing a state changes the exact
state set and state hash; changing an edge weight changes the exact transition
set and transition hash; removing state 0's outgoing edges makes the graph fail
the independently recomputed strong-connectivity test. Matrix-specific mutation
categories such as infinity entries and identity parameters are outside Task 5
and were not treated as evidence here.

The source scan is a defense-in-depth check rather than a complete static
language analysis: its forbidden strings do not cover every possible spelling
of a producer path or every possible dynamic execution mechanism. That is a
minor robustness caveat, not a current clean-room violation, because the
submitted Python and C++ sources were directly inspected and contain no such
dependency or execution path.

The Task 5 report's historical claim about a prior red TDD run is not
independently recoverable from the frozen artifacts; it is not needed for this
verdict. The current focused run and reconstruction checks are reproducible.

## Suggested optional strengthening

If the project wants the isolation test itself to carry more of the burden,
normalize path separators and scan for producer executable/source basenames,
compiler invocations, and process-launch calls. This is an optional hardening
change; it is not a requested repair to the reviewed implementation.

No substantive repair is required by this review. Any later substantive change
to the reconstruction or its tests requires a new independent review.
