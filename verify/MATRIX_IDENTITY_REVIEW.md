# Task 7 Independent Review: Matrix Identities

## Verdict

**PASS WITH CAVEATS**

The frozen width-5, width-6, and width-7 artifacts are internally consistent.
The focused test passes, an independent parser found no entrywise mismatch, and
a fresh replay of `power_identity.cpp` reproduced all six binary matrix hashes.
The report correctly keeps `TOOL_CHECKED_LOCAL` at artifact level and does not
promote a total-domination theorem.

No Critical finding and no identity mismatch were found. The caveats below are
verification-coverage limitations, not evidence that the persisted identities
are false. The later clean-room/mutation task is outside this Task 7 review.

## Frozen scope reviewed

- `AGENTS.md`
- `cylindrical_total_domination/docs/DESIGN.md`
- `cylindrical_total_domination/mathematics/MINPLUS_IDENTITY_LEMMA.md`
- `src/automaton/power_identity.cpp`
- `tests/test_matrix_identity.py`
- all width-5/6/7 `automaton_manifest.json`, `matrix_identity.json`, `M_N.bin`,
  and `M_N_plus_p.bin`
- `.superpowers/sdd/2026-08-25-cylindrical-total-domination/task-7-report.md`

## Reproduction and artifact checks

- `python -m pytest tests/test_matrix_identity.py -q` → **8 passed**.
- Recompiled and ran the producer in an isolated temporary directory for all
  three widths. Each run reported `TOOL_CHECKED_LOCAL` and zero mismatches.
- Independent MTX1 parsing verified magic, version `1`, dimensions, tags,
  exact file lengths, and all entries. The six persisted matrices contain
  1,559,378 compared entries in total; every comparison satisfies
  `right = left + c`.
- The persisted manifest SHA-256 fields in the metadata equal the actual
  manifest hashes. The manifest state/transition canonical hashes, matrix
  hashes, and report sizes/hashes also match.
- Replay hashes equal the frozen hashes:

  | width | `M_N.bin` | `M_N_plus_p.bin` | computed mismatches |
  |---:|---|---|---:|
  | 5 | equal | equal | 0 |
  | 6 | equal | equal | 0 |
  | 7 | equal | equal | 0 |

- Fresh replay resource observations were approximately 0.11/0.67/7.13 s and
  13/23/83 MB peak RSS for widths 5/6/7, respectively, below the 1,800 s and
  8 GB caps. These are independent observations; the report's recorded values
  are also below the caps.

## Dependency graph and classification

1. **Frozen statement and status — Justified.** `DESIGN.md:3,52-58,64-77`
   requires exact entrywise identities as finite certificates, while retaining
   project status `CONJECTURE` and prohibiting theorem promotion from finite
   evidence. The Task 7 report states the same artifact-only boundary at
   `.superpowers/.../task-7-report.md:3-4,101-102`.

2. **Frozen parameters — Justified.** `power_identity.cpp:418-424` hard-codes
   `(N,p,c)=(16,4,6),(21,14,24),(28,4,8)` for widths 5, 6, and 7. The JSON
   manifests have the expected state/transition counts, and
   `test_matrix_identity.py:46-55,66-68` checks the persisted parameters.

3. **Manifest input — Justified for the frozen manifests; limited parser
   validation.** `power_identity.cpp:189-212` checks requested width, declared
   counts, edge bounds, and nonnegative weights, then hashes the whole file.
   It consumes only the transition list; it does not validate the manifest's
   state list or its embedded `state_sha256`/`transition_sha256` fields. The
   independent audit verified those fields and the complete persisted
   manifests, so no current artifact inconsistency was found.

4. **Min-plus power computation — Justified on this bounded input.**
   `power_identity.cpp:276-307` starts from the exact diagonal-zero matrix and
   propagates every row through every outgoing edge for exactly the requested
   exponent. The matrix orientation and edge weights agree with the stated
   row-to-column recurrence. Observed finite values are 22–30/28–36 (width 5),
   36–44/60–68 (width 6), and 54–64/62–72 (width 7), so the finite `int64_t`
   additions cannot overflow for these artifacts.

5. **INF representation and shift comparison — Justified in code, not
   exercised by these persisted powers.** `kInfinity` is an internal sentinel,
   but serialization uses a separate tag (`0 = INF`, `1 = finite int64`) at
   `power_identity.cpp:318-332`; `compare_shifted` preserves INF and adds only
   to finite entries at `:346-363`. The mathematical lemma's absorbing-INF
   convention is compatible with this. However, all six matrices have zero INF
   entries, so the persisted identity certificates do not empirically exercise
   either INF serialization or the INF comparison branch.

6. **Binary parser and entrywise test — Justified for current bytes; test gap.**
   `test_matrix_identity.py:22-39,70-90` checks magic, tagged values, exact
   length, dimensions, matrix hashes, and the complete entrywise shift. The
   test does not check the MTX1 version field, cross-check metadata's
   `manifest_sha256`, or recompute `mismatch_count`/`first_mismatch`; those
   fields were independently checked here for the frozen artifacts. The C++
   writer emits native-endian integer fields while the format claims
   little-endian (`power_identity.cpp:310-330`); this is correct on the review
   host but is a portability assumption.

7. **Resource evidence — Justified as bounded execution evidence.** The
   producer checks runtime/RSS during power generation and records measurements
   in metadata. Fresh replay was below both caps. This establishes neither a
   mathematical theorem nor a universal performance guarantee.

8. **Mathematical implication — Cited/conditional, not proved by Task 7.**
   `MINPLUS_IDENTITY_LEMMA.md:116-168` correctly makes the all-`n` recurrence
   conditional on a literal entrywise identity and explicitly says it does not
   establish any particular automaton identity or domination formula. Task 7
   supplies artifact evidence for the three bounded identities only.

## Important findings

1. **Important — INF coverage is vacuous in the frozen certificates.** Every
   entry of every persisted matrix is finite. The source-level handling is
   correct for the reviewed bounded values, but the artifacts do not test the
   format's INF tag or the INF branch of the comparison. This is an evidence
   limitation, not an identity failure.

2. **Important — The Task 7 test is not a standalone certificate verifier.** It
   does not validate the MTX1 version, manifest hash binding, or mutation
   rejection, and it does not regenerate powers. The independent replay and
   hash audit above close the gap for the frozen files. The DESIGN.md mutation
   requirement and clean-room rebuild belong to Task 8 and remain a separate
   gate.

3. **Minor — MTX1 endianness is assumed rather than explicitly encoded by the
   writer.** The current Windows artifacts match the declared little-endian
   format; a portable producer should write bytes explicitly or assert the host
   byte order.

## Critical findings

None.

## Suggested repairs (separate from verdict)

- Add a clean-room certificate verifier/mutation suite that checks manifest
  binding, MTX1 version, dimensions, finite/INF mutations, and `(N,p,c)`.
- Add a small MTX1 fixture containing both INF and finite entries, and assert
  the version and metadata hash fields in the focused test.
- Make the binary writer explicitly little-endian if cross-host reproducibility
  is required.

No producer files were modified. A substantive change to the producer,
artifacts, or Task 7 claims requires a new independent review.
