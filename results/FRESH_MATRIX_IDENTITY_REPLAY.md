# Fresh matrix-identity replay

Status: `TOOL_CHECKED_LOCAL`; this is certificate evidence, not by itself a
human proof.

Fresh command:

```text
python verify/verify_certificates.py 5 certificates/width5
python verify/verify_certificates.py 6 certificates/width6
python verify/verify_certificates.py 7 certificates/width7
```

| width | dimension | entries checked | finite entries | infinite entries | mismatches |
|---:|---:|---:|---:|---:|---:|
| 5 | 169 | 28,561 | 28,561 | 0 | 0 |
| 6 | 441 | 194,481 | 194,481 | 0 | 0 |
| 7 | 1,156 | 1,336,336 | 1,336,336 | 0 | 0 |

The clean-room verifier independently rebuilt states, transitions, costs,
both powers, the top-level manifest binding, and the entrywise infinity-safe
identity. All three commands accepted with status `TOOL_CHECKED_LOCAL`.
Persisted artifact hashes were reproduced by the fresh replay.
