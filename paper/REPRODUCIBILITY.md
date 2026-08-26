# Reproducibility

All commands below are run from the project root:

```text
python -m pytest tests -q --import-mode=importlib
python verify/verify_certificates.py 5 certificates/width5
python verify/verify_certificates.py 6 certificates/width6
python verify/verify_certificates.py 7 certificates/width7
python -m pytest tests/test_mutations.py -q
python -m pytest tests/test_prefix_values.py -q
```

Expected finite graphs and certificate parameters are:

| width | states | transitions | identity | prefix |
|---:|---:|---:|---|---|
| 5 | 169 | 2,419 | (M_5^{20}=6\otimes M_5^{16}) | (3\le n\le19) |
| 6 | 441 | 11,025 | (M_6^{35}=24\otimes M_6^{21}) | (3\le n\le34) |
| 7 | 1,156 | 50,303 | (M_7^{32}=8\otimes M_7^{28}) | (3\le n\le31) |

Each certificate verifier must report `accepted: true`, zero identity
mismatches, and status `TOOL_CHECKED_LOCAL`. The prefix test covers 18 rows
using every reconstructed state as a possible source, hence unrestricted
diagonal minima;
the mutation test covers 11 negative controls. The complete test suite is
expected to pass with 125 tests in the current repository state.

`SHA256SUMS` binds the finite artifacts and manuscript-support files. It is a
file-integrity manifest, not a substitute for the clean-room verifier. Raw
matrices and manifests remain in `certificates/`; the verifier entry point is
`verify/verify_certificates.py`.

The logical proof is: human total-domination/closed-walk and min-plus lemmas,
then exact finite identities and prefixes, then independent replay of those
finite artifacts. The code does not replace the semantic argument.
