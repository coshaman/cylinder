# GitHub Release Audit

Date: 2026-08-26

The public package was assembled in `release/public`, committed locally on
branch `main`, and verified locally. The final local commit is available from
`git log`; the attempted push to
`https://github.com/coshaman/cylinder.git` failed because the execution
environment could not connect to GitHub. The escalated push request was also
rejected by the safety reviewer because it would publish the staged research
package to an external destination.

Therefore the remote branch and public URL were not verified. This is a
release blocker; no claim of successful public publication is made.

Local package evidence:

- `python -m pytest tests -q`: 125 passed in `release/public`.
- Width 5, 6, and 7 certificate verifiers: accepted, zero identity
  mismatches.
- Mutation suite: 11 passed.
- Unrestricted prefix suite: 18 passed.
- Public `SHA256SUMS`: 76 entries, zero local mismatches after cache cleanup.
