# DAM final revision report

Date: 2026-08-27

## Manuscript

- Title: Efficient Open Domination and Exact Total Domination in Cylindrical
  Grids
- Author display: 박성현
- Current PDF: 13 pages
- Submission state: not submitted

## Scientific status

- General EOD theorem: GENERAL_EOD_AND_TOTAL_DOMINATION_THEOREMS_PROVED
- General lower bound: PROVED
- Exact even-width family: PROVED
- Width 5 theorem: PROVED
- Width 6 theorem: PROVED
- Width 7 theorem: PROVED

## Priority and literature

The current priority audit is PARTIALLY_OVERLAPPING. The odd-width EOD
family is PRIOR; the all-width EOD characterization is
NOT_FOUND_IN_AUDIT; the even exact family has PARTIAL_OVERLAP; and the
general lower bound is UNCERTAIN_PRIORITY. The audit now includes the 2023
Haynes--Hedetniemi--Henning monograph, Klavzar--Zerovnik and
Bouznif--Moncel--Preissmann methodology, and Wehrmann--Koster's 2026 torus
paper, which concerns C_m square C_n rather than P_m square C_n.

## Revision loop

Fresh independent panel verdicts: mathematical referee ACCEPT; certificate
referee ACCEPT; literature referee MINOR_REVISION (priority wording only, with
no equivalent theorem found); and DAM editorial referee MINOR_REVISION
(administrative metadata and bibliography polish only). The certificate
referee explicitly confirmed the threshold bases 16--19, 21--34, and 28--31,
and rejected no claim. No artificial unanimous-acceptance criterion is used;
correctness and prior-art objections are the decisive gates.

## Reproducibility

- EOD pilot: 495 cases, 0 mismatches
- Construction regression: PASS for k=1..30
- Public clean-room tests: 125 passed
- Width-5, width-6, width-7 certificate replays: accepted, zero errors
- Mutation tests: PASS
- Prefix tests: PASS
- PDF build: successful, 13 pages, zero LaTeX errors and zero undefined
  citations/references
- Public snapshots: 105 files, 104 manifest entries, synchronized hashes

## Submission materials

The DAM staging bundle contains manuscript source/PDF, bibliography,
highlights, cover letter, data/code statement, declarations, author metadata,
and submission checklist. Remaining author actions are the verified
Latin-script identity if required, affiliation/contact details, declarations,
AI-assistance disclosure, and licence choice.

## Publication commit

The local nested publication repository is based on the verified remote main
base 426ace86f9c6c7cd9869fc2bf3fbedef57ec04d1. Codex does not perform the final
push. The exact author-side command file is
release/PUSH_PUBLIC_REPOSITORY.ps1; it checks cleanliness, ancestry, pushes
without force, and verifies remote equality.

## Final scientific readiness

DAM_CONTENT_READY_AUTHOR_METADATA_PENDING
