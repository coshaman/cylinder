# Final Manuscript Audit

Date: 2026-08-26

## Project guard

The working directory is exactly
`C:\Users\owner\Documents\ChatGPT\쌀먹\cylindrical_total_domination`, with
basename `cylindrical_total_domination`. `RESULT.json`, `README.md`,
`SHA256SUMS`, `mathematics/`, `results/`, `verify/`, and `certificates/` are
present. `RESULT.json` and the final referee adjudication record
`ALL_THREE_THEOREMS_PROVED`.

Reports referring to P4Q, paired domination, `p5_cylinder_domination`, or
`shuffle_m6` were excluded as wrong-project evidence.

## Correctness

- The manuscript formulas agree with `RESULT.json` for widths 5, 6, and 7.
- The recurrence thresholds are stated correctly: 16, 21, and 28.
- The identities are stated correctly:
  \(M_5^{20}=6\otimes M_5^{16}\),
  \(M_6^{35}=24\otimes M_6^{21}\), and
  \(M_7^{32}=8\otimes M_7^{28}\).
- The exceptions \(g_6(12)=22\), \(g_7(7)=15\), and \(g_7(14)=30\)
  remain in the finite prefix and are not propagated below threshold.
- Fresh graph-theory review: PASS.
- Fresh tropical/min-plus review: PASS; no algebraic flaw or threshold-valid
  counterexample was found.
- Fresh certificate replays for widths 5, 6, and 7: accepted, with zero
  identity mismatches and `TOOL_CHECKED_LOCAL` status.

## Novelty and references

The literature audit is current through 2026-08-26 and uses a deliberately
narrow claim: the cited exact-cylinder result covers smaller fixed widths,
while this work determines widths 5--7. No equivalent target-width
classification was found in the documented audit. Bibliographic entries used
by the manuscript are recorded in `REFERENCES_VERIFIED.md` and
`references.bib`.

## Exposition

The manuscript gives the total-domination/closed-walk bijection, min-plus path
semantics, scalar-shift and (+\infty) conventions, the threshold lemma, and
explicit theorem-to-prefix arguments. It compiles to `manuscript.pdf`; the
LaTeX log has no undefined-reference, citation, warning, or error diagnostics.

## Reproducibility

- Full project test suite: 125 passed.
- Width-5, width-6, and width-7 certificate verifiers: accepted.
- Mutation and prefix suites: passed.
- `paper/check_consistency.py`: PASS.
- `SHA256SUMS`: PASS.

The finite artifacts, commands, dimensions, expected outputs, and hash
purpose are documented in `REPRODUCIBILITY.md`.

## Journal audit

The current DAM scope and author-guide requirements are recorded in
`DAM_SUBMISSION_REQUIREMENTS.md`; highlights, cover letter, declaration notes,
and data/code notes are prepared. However, the manuscript still contains an
editable author placeholder, and no persistent public artifact identifier or
archive URL exists in the workspace.

## Final status

`JOURNAL_REQUIREMENT_BLOCKER`

The remaining blocker is author-specific and cannot be invented: exact author
names/order, affiliations and postal addresses, corresponding-author email,
and applicable declarations are listed in `AUTHOR_METADATA_TO_CONFIRM.md`.
The public repository/DOI or journal-compliant explanation for non-deposit
must likewise be supplied before external submission.
