# Exact total domination in cylindrical grids

Author: **박성현**

Mathematical status: `ALL_THREE_THEOREMS_PROVED`.

The primary theorem package characterizes efficient open domination for every
\(P_m\square C_n\) with \(m\ge2,n\ge3\), proves the general lower bounds,
and gives the exact even-width family. It also determines
\(\gamma_t(P_5\square C_n)\),
\(\gamma_t(P_6\square C_n)\), and \(\gamma_t(P_7\square C_n)\) for every
\(n\ge3\). It includes the total-domination/automaton bijection, min-plus
path semantics, exact matrix identities, complete finite prefixes, mutation
tests, and clean-room certificate verification.

The verified identities are:

```text
M_5^20 = 6 ⊗ M_5^16
M_6^35 = 24 ⊗ M_6^21
M_7^32 = 8 ⊗ M_7^28
```

The recurrence thresholds are respectively 16, 21, and 28; values below a
threshold are covered only by the finite prefix and are not propagated.

Run from this directory:

```text
python -m pytest tests -q --import-mode=importlib
python verify/verify_certificates.py 5 certificates/width5
python verify/verify_certificates.py 6 certificates/width6
python verify/verify_certificates.py 7 certificates/width7
python -m pytest tests/test_mutations.py -q
python -m pytest tests/test_prefix_values.py -q
```

The generalized contract is frozen in
`generalization/mathematics/DEFINITIONS_GENERALIZED.md`; the width-5--7
certificate contract is in `mathematics/DEFINITIONS.md`. The mathematical proof records and fresh review reports are in
`mathematics/`, `generalization/`, and `results/`. This is a research artifact
package, not a journal acceptance or submission. Author contact/declaration
fields and the final licence choice remain explicitly marked for author
confirmation; no facts have been inferred.
