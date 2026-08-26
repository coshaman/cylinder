# Independent Automaton Report

Status: `TOOL_CHECKED_LOCAL` for Task 5 clean-room automaton reconstruction.

Command:

`pytest tests/test_independent_automaton.py -q`

Scope:

- Reconstructed widths: 5, 6, 7.
- Producer boundary: `src/automaton` was not imported, not included, and not executed by the clean-room implementation.
- Python state reconstruction: `verify/independent_states.py`.
- C++ transition reconstruction: `verify/independent_transitions.cpp`.
- Test source scan rejects references to producer imports and producer source files.

Mathematical reconstruction:

- State records are all pairs `(S,R)` with `R` disjoint from the open vertical neighborhood of `S`.
- Edge records use `R subseteq T`, next pending `[m] \ (S union N_P(T))`, and weight `|T|`.
- Strong connectivity is recomputed from the independently reconstructed edge set.

Persisted manifest comparison:

| width | states | transitions | state SHA-256 | transition SHA-256 | strongly connected |
| --- | ---: | ---: | --- | --- | --- |
| 5 | 169 | 2419 | 3dab5d356f6ef377eaf71ad224402fed0b22fdc1b9da226beb442ffd5a22030c | b6501f275b981d5cd2387837b499c3b110baf6241ebd9cdc485b41db68062ec1 | true |
| 6 | 441 | 11025 | 2c2d8b0bddd71a33e381e25a9c50113c566e588fc9b1dcb2b1272bb87a12991f | ced3c9e4227b7f9b885e01959206b467874397bc4f309a264b0b1c0074946d51 | true |
| 7 | 1156 | 50303 | 6076bbfc9b9bf15400939a397f8a5de842cd14db368d510723b6a13af4511b96 | a645d24f6f3bd7c2c86cc967a71459466c20cafa5a8de21292db02d6e49460cc | true |

Mutation coverage:

- Deleted state changes the canonical state set and state hash.
- Reweighted edge changes the canonical transition set and transition hash.
- Deleting all outgoing edges from state 0 is rejected by strong-connectivity recomputation.

Conclusion:

The independent reconstruction matches Task 4 state sets, edge sets, weights, counts, persisted manifest hashes, and strong connectivity for widths 5, 6, and 7. This report does not promote any theorem claim beyond the Task 5 automaton-check state.
