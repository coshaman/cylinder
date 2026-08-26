# Generalized finalization report

Date: 2026-08-26

## Scope

The authorized project is `cylindrical_total_domination`. The clean
publication snapshot is `release/public_v2`.

## Mathematical disposition

The generalized symbolic theorem branch received independent PASS reviews for
the EOD row-system theorem, even-width construction, total-domination lower
bound, and exact even-width family. The fixed-width certificate branch
received accepted clean-room replays for widths 5, 6, and 7, including the
matrix identities and thresholded finite-prefix reductions. The literature
audit is `PARTIALLY_OVERLAPPING`: the odd EOD family is prior art and is
credited; the all-width characterization and arbitrary-even-width family
were not found in the audited sources, subject to the stated search limits.

## Reproducibility evidence

- public_v2 test suite: 125 passed;
- mutation suite: 11 negative controls passed;
- prefix suite: 18 rows passed;
- clean-room certificate verifier: widths 5, 6, and 7 accepted with zero
  errors;
- public_v2 payload: 104 regular files; SHA256SUMS has 103 manifest entries,
  with zero missing files and zero mismatches;
- root SHA256SUMS: regenerated after the final source snapshot.

## Publication preparation

The manuscript, generalized contract, proof records, certificates, verifier,
review reports, DAM requirements audit, cover letter, highlights, declarations,
and data/code statement are staged. No journal submission or acceptance is
claimed. The supplied author name is `박성현`; affiliation, postal address,
corresponding-author e-mail, ORCID, declarations, and author-approved licence
remain isolated as author-completion items.

## Final status

`GENERALIZED_MANUSCRIPT_AND_PUBLIC_PACKAGE_READY`

The DAM staging is not marked `DAM_SUBMISSION_READY` until the author supplies
the unresolved metadata and licence choice. The isolated publication snapshot
is committed locally in the nested `release/public` repository at the
verified descendant commit recorded in `DAM_FINAL_REVISION_REPORT.md`. The
target is `https://github.com/coshaman/cylinder` on `main`; Codex does not
perform the final push, and the author-side script must fetch and verify
remote equality immediately before pushing. See `FINAL_REMOTE_AUDIT.md`.
