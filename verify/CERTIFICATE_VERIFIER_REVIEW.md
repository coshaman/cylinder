# Independent re-review: Task 8 certificate verifier fix

## Verdict

**PASS WITH CAVEATS** — the package-isolation correction is effective and no
Critical or Important finding remains. The per-width verifier is independently
implemented and the requested replay checks pass.

This is an artifact-verifier review only. It does not promote the underlying
domination theorem beyond `CONJECTURE`.

## Evidence run

- `python -m pytest tests/test_mutations.py -q` → `11 passed`.
- `python verify/verify_certificates.py 5 certificates/width5` → accepted,
  `TOOL_CHECKED_LOCAL`.
- `python verify/verify_certificates.py 6 certificates/width6` → accepted,
  `TOOL_CHECKED_LOCAL`.
- `python verify/verify_certificates.py 7 certificates/width7` → accepted,
  `TOOL_CHECKED_LOCAL`.
- Each verifier report now includes `top-level certificate manifest record and
  artifact hashes verified`.
- The recorded hashes in the repository's `certificates/manifest.json` match
  the current per-width files for all three widths.
- Adversarial temporary-package check: copied the complete `certificates/`
  directory, changed the copied width-5 `N` from `16` to `999`, and ran the
  verifier against the copied `width5` directory. It was rejected with
  `top-level certificate manifest binding mismatch`.
- Removing the copied top-level manifest was rejected with
  `certificate package is missing top-level manifest`.

## Dependency and implementation classification

| Component | Classification | Basis |
|---|---|---|
| Open-neighborhood state reconstruction | Justified | `verify_certificates.py:227-228` rebuilds masks and transitions locally from the frozen equations; no producer import or execution occurs. Exact state and transition arrays, counts, and independently recomputed hashes are compared at `:231-242`. |
| Transition/weight binding | Justified | The reconstructed transition list is compared entrywise with the persisted list at `:235-236`; weights are regenerated from the next selected mask. |
| Clean-room isolation | Justified, with test-scope caveat | The verifier and mutation module contain no producer import/include or producer path use, and the implementation is self-contained. The source scan is lexical rather than a proof against every possible dynamic execution mechanism. |
| Per-width hash binding | Justified | `matrix_identity.json` binds the exact automaton manifest and both matrix byte streams at `:257-260`; the verifier recomputes the expected automaton hashes at `:239-242`. |
| `(width,N,p,c)` binding | Justified for per-width artifacts | Width is checked against the hard-coded parameter table and identity metadata is checked exactly at `:231` and `:249-252`. |
| MTX1 parsing | Justified | `_parse_matrix` checks magic, version, nonzero dimension, every tag, finite `int64` payload length, and exact end-of-file consumption at `:141-169`; dimensions are then checked against the rebuilt state count at `:263-267`. |
| Independent min-plus recomputation | Justified | `_powers_from_edges` starts each source from cost 0, propagates only rebuilt edges, minimizes integer costs, and preserves unreachable entries as `None` (`:172-200`). Both powers are compared entrywise at `:269-278`. |
| Entrywise identity and `INF` algebra | Justified in code; not fully exercised by persisted data | The final comparison explicitly maps `None` to `None` and adds `c` only to finite values at `:280-284`. No persisted matrix has an `INF` entry. |
| Top-level package binding | Justified | The manifest is resolved as `certificate_dir.parent / "manifest.json"` and is required at `:264-267`; the selected width's counts, parameters, status, and three artifact hashes are checked at `:268-291`. |
| Eight required mutations | Justified for the supplied suite | `tests/test_mutations.py:34-39` parametrizes all eight entries in `verify/mutation_tests.py:104-112`; the independent run passed all 11 tests. |

## Findings

### Resolved Important finding — package-local top-level binding

**Location:** `verify/verify_certificates.py:264-291` and
`verify/mutation_tests.py:16-20`.

The correction resolves the manifest from the supplied package's parent and
the mutation copy helper copies that manifest alongside the temporary width
directory.

The temporary-package mutations confirmed both rejection of an altered
manifest and rejection when the manifest is absent. The previous Important
finding is therefore closed.

### Minor — duplicate width records are not rejected

The verifier selects the first matching record at `:273-275` but does not
require exactly one record for each width or reject unexpected records. A
temporary package with a valid first width-5 record followed by a duplicate
width-5 record with `N=999` was accepted. This does not affect the supplied
frozen manifest or the three requested width replays, but strict package-schema
validation could reject duplicate/unexpected width records.

## Finite-to-`INF` limitation (not counted as the structural defect)

The persisted `M_N` and `M_N_plus_p` files contain no `INF` entries, as stated
in `certificates/manifest.json:50` and the Task 8 report. The mutation named
“altered infinite matrix entry” changes a finite tagged entry to the `INF` tag
(`verify/mutation_tests.py:75-80`); it does not mutate a genuinely unreachable
cell. The parser accepts that tag, and the recomputation rejects the altered
matrix, but the supplied artifacts do not exercise a valid end-to-end case in
which an `INF` entry is preserved by the identity comparison. This is the
documented finite-to-`INF` coverage limitation, not evidence that the `None`
logic is wrong.

## Suggested repair (new review required)

Optional hardening: require exactly one record for each expected width and
reject unexpected widths. The documented finite-to-`INF` coverage limitation
also remains; it is not a verifier defect.
