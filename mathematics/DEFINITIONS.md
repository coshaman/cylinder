# Definitions and Frozen Contract

This file freezes the mathematical object for the cylindrical total-domination
project. The target formulas below are `CONJECTURE` until the certificate,
clean-room verification, and review gates pass.

## Graph Family

We study `G_{m,n} = P_m square C_n` with:

- `width set = {5, 6, 7}`
- `m in {5, 6, 7}`
- `n >= 3`

Vertices are `(i, j)` with `0 <= i < m` and `j in Z_n`.

Two vertices are adjacent when they differ by one row in the path direction
or by one column modulo `n` in the cycle direction.

## Open Neighborhoods and Total Domination

For a vertex `v`, its open neighborhood `N(v)` is the set of adjacent
vertices. Self-membership does not dominate a vertex.

A set `D` is a total dominating set when every vertex has a neighbor in `D`.
This includes vertices already in `D`, so selected vertices still require an adjacent selected neighbor.

For a row mask `S subseteq [m]`, the vertical open neighborhood is

`N_P(S) = { i : i - 1 in S or i + 1 in S }.`

In particular, `S` is not generally contained in `N_P(S)`, because open
neighborhoods do not allow self-domination.

The total domination number is

`gamma_t(G) = min { |D| : D is a total dominating set of G }`.

## Target Families

The three target families are:

- `gamma_t(P_5 square C_n)`
- `gamma_t(P_6 square C_n)`
- `gamma_t(P_7 square C_n)`

## Target Formulas

These formulas are conjectural targets only. They are not assumptions, and
they remain conjectural until the required certificates pass.

### Width 5

For every `n >= 3`,

`gamma_t(P_5 square C_n) = ceil(3n / 2) + 1` when `n mod 4 = 2`.

`gamma_t(P_5 square C_n) = ceil(3n / 2)` otherwise.

### Width 6

Let `r = n mod 14` and define `epsilon_r` by:

- `epsilon_0 = 0`
- `epsilon_1 = 1`
- `epsilon_2 = 2`
- `epsilon_3 = 0`
- `epsilon_4 = 1`
- `epsilon_5 = 0`
- `epsilon_6 = 1`
- `epsilon_7 = 0`
- `epsilon_8 = 2`
- `epsilon_9 = 0`
- `epsilon_10 = 0`
- `epsilon_11 = 1`
- `epsilon_12 = 3`
- `epsilon_13 = 1`

The target is

`gamma_t(P_6 square C_n) = ceil(12n / 7) + epsilon_{n mod 14}`

for every `n >= 3`, except

`gamma_t(P_6 square C_12) = 22`.

### Width 7

The target is

`gamma_t(P_7 square C_n) = 2n`

for every `n >= 3`, except

- `gamma_t(P_7 square C_7) = 15`
- `gamma_t(P_7 square C_14) = 30`

## Status Vocabulary

Research-state vocabulary:

- `CONJECTURE`
- `HEURISTIC_EVIDENCE`
- `COMPUTATIONALLY_TESTED`
- `LEMMA_CONDITIONAL`
- `HUMAN_PROOF_CANDIDATE`
- `TOOL_CHECKED_LOCAL`
- `FORMALIZED_LOCAL`
- `FORMALIZED_COMPLETE`
- `REFUTED`
- `STILL_OPEN`

Primary final-status vocabulary:

- `ALL_THREE_THEOREMS_PROVED`
- `TWO_WIDTH_THEOREMS_PROVED`
- `DIFFERENT_EXACT_FORMULAS_PROVED`
- `ALREADY_RESOLVED`
- `PROTOTYPE_IDENTITY_NOT_REPRODUCED`
- `MODEL_VERIFICATION_FAILED`
- `CERTIFICATE_VERIFICATION_FAILED`
- `GITHUB_PUSH_BLOCKED`
- `REVIEW_CONVERGENCE_FAILED`
