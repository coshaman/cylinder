# Final finite-prefix reconstruction

Status: `COMPUTATIONALLY_TESTED`.

Fresh command:

```text
python -m pytest tests/test_prefix_values.py -q
```

Result: `18 passed`.

The clean-room diagonal traces cover every row in (3\le n\le19) for width
5, (3\le n\le34) for width 6, and (3\le n\le31) for width 7. Every row
matches the target formula, including (P_6\square C_{12}=22),
(P_7\square C_7=15), and (P_7\square C_{14}=30). Selected direct witnesses
were replayed with literal open-neighborhood semantics at widths/lengths
((5,3),(5,10),(6,12),(6,21),(7,7),(7,14),(7,20)).

The prefix computation uses reconstructed automaton edges and min-plus
relaxation with every reconstructed state as a possible source, so the
reported diagonal minima are unrestricted. Direct optimization is used only
for selected cross-checks.
