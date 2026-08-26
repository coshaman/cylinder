# Fresh Release Baseline Verification

Date: 2026-08-26

Project: `cylindrical_total_domination`

## Results

- `python -m pytest tests -q` — **125 passed**.
- `python verify/verify_certificates.py 5 certificates/width5` — accepted;
  zero identity mismatches; `TOOL_CHECKED_LOCAL`.
- `python verify/verify_certificates.py 6 certificates/width6` — accepted;
  zero identity mismatches; `TOOL_CHECKED_LOCAL`.
- `python verify/verify_certificates.py 7 certificates/width7` — accepted;
  zero identity mismatches; `TOOL_CHECKED_LOCAL`.
- `python -m pytest tests/test_mutations.py -q` — **11 passed**.
- `python -m pytest tests/test_prefix_values.py -q` — **18 passed**.
- SHA-256 manifest comparison — **PASS**.

The three verifier runs independently rebuilt state and transition semantics,
checked dimensions and manifest bindings, recomputed both persisted matrix
powers, and verified the entrywise min-plus identities including infinity
semantics.

## Frozen certificate parameters

\[
M_5^{20}=6\otimes M_5^{16},\qquad
M_6^{35}=24\otimes M_6^{21},\qquad
M_7^{32}=8\otimes M_7^{28}.
\]

The associated recurrence thresholds remain (16,21,28), respectively.
