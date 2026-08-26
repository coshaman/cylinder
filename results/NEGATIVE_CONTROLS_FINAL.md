# Final negative controls

Status: `TOOL_CHECKED_LOCAL`.

Fresh command:

```text
python -m pytest tests/test_mutations.py -q
```

Result: `11 passed`.

The suite rejects deleted, inserted, and reweighted transitions; corrupted
state masks; altered finite and tagged-infinite matrix entries; altered
dimensions; and altered ((N,p,c)) parameters. It also rejects missing or
incorrect package-level manifest bindings. The persisted matrices contain no
infinite cells, so the infinity mutation is a finite-to-infinity tagged-entry
control; the parser and identity logic still handle genuine infinity entries.
