# Exact total domination of cylindrical grids

Author: **박성현**

Mathematical status: `GENERAL_EOD_AND_TOTAL_DOMINATION_THEOREMS_PROVED` and
`ALL_THREE_FIXED_WIDTH_THEOREMS_PROVED`.

Release status: `GENERALIZED_MANUSCRIPT_AND_PUBLIC_PACKAGE_READY`. The
authoritative clean package is `release/public` (identical to
`release/public_v2`). No journal submission or acceptance is claimed; author
metadata and licence confirmation remain pending.

This project proves the all-width efficient-open-domination characterization
and lower bounds, and determines the total domination numbers of
`P_5 □ C_n`, `P_6 □ C_n`, and `P_7 □ C_n` for every `n >= 3`. The proof uses
an open-neighborhood finite-state bijection, min-plus path semantics, exact
entrywise matrix identities, and complete finite prefixes. Recurrences are
used only at their proven thresholds; transient exceptions remain in the
finite prefix.

Reproduce the verification with:

```text
python -m pytest tests -q
python verify/verify_certificates.py 5 certificates/width5
python verify/verify_certificates.py 6 certificates/width6
python verify/verify_certificates.py 7 certificates/width7
```

The fresh baseline recorded `125 passed`, accepted width-5/6/7 certificate
replays, 11 mutation tests, and 18 prefix tests. The bounded literature audit
found no equivalent complete all-circumference classification for all three
widths. It also records exact prior subfamilies and nearby 2-domination
methodology; the manuscript states those overlaps explicitly.

The verified identities are:

```text
M_5^20 = 6 ⊗ M_5^16
M_6^35 = 24 ⊗ M_6^21
M_7^32 = 8 ⊗ M_7^28
```

The associated recurrence thresholds are 16, 21, and 28.

## Manuscript

The manuscript source and preparation materials are under `paper/`. Start
with `paper/manuscript.tex`, `paper/manuscript.pdf`, and
`paper/DAM_SUBMISSION_REQUIREMENTS_CURRENT.md` and `paper/REPRODUCIBILITY.md`.
The release baseline is recorded in
`release/BASELINE_VERIFICATION.md`.

## Repository structure

- `paper/` — manuscript, bibliography, DAM audit, and review records;
- `mathematics/` — human-readable proof records;
- `certificates/` — finite matrix certificates and manifests;
- `verify/` — clean-room verification scripts;
- `tests/` — semantic, mutation, and prefix tests;
- `results/` — theorem and referee records.

Citation metadata is in `CITATION.cff`. The author should complete the
remaining submission metadata and replace the provisional license notice
before final public release.
