# Reproducibility

Run these commands from the repository root:

```text
python -m pytest tests -q
python verify/verify_certificates.py 5 certificates/width5
python verify/verify_certificates.py 6 certificates/width6
python verify/verify_certificates.py 7 certificates/width7
python -m pytest tests/test_mutations.py -q
python -m pytest tests/test_prefix_values.py -q
```

Expected results are 125 passing tests, 11 passing mutation tests, 18 passing
prefix tests, and accepted certificate verifiers with zero identity
mismatches. The finite graph counts are:

| width | states | transitions | identity |
|---:|---:|---:|---|
| 5 | 169 | 2,419 | `M_5^20 = 6 ⊗ M_5^16` |
| 6 | 441 | 11,025 | `M_6^35 = 24 ⊗ M_6^21` |
| 7 | 1,156 | 50,303 | `M_7^32 = 8 ⊗ M_7^28` |

The clean-room verifier reconstructs the finite state graphs and recomputes
the persisted matrix powers. `SHA256SUMS` is an integrity manifest for the
listed project artifacts; it does not replace the verifier.
