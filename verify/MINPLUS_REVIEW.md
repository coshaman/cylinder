# Task 6 Independent Review: Min-Plus Engine

## Verdict

**PASS WITH CAVEATS**

The two requested code repairs are verified. The focused test suite passes,
both C++ translation units compile, negative signed construction now preserves
the value, and oversized matrix dimensions are rejected before allocation.
The producer and clean-room verifier still implement the same min-plus
semantics on the tested domain. The mathematical artifact remains sufficient
for the stated application (a finite, nonempty state set): the path-walk
induction, scalar shift, associativity, and entrywise-identity recurrence are
correct, including the `INF` cases. No Critical finding and no blocking proof
gap were found.

This verdict does not certify any particular matrix identity or total-
domination formula; the lemma explicitly leaves those conditional.

## Evidence and reproducibility

- Command: `pytest tests/test_minplus.py -q`
- Result: `6 passed in 9.73s` on this re-review.
- Both `src/automaton/minplus.cpp` and
  `verify/independent_minplus.cpp` compiled with `g++ -std=c++17 -O2`.
- Independent spot checks agreed between the two executables for negative
  arbitrary-length decimal values, `INF`, and matrix multiplication.
- A maximal `size_t` dimension was rejected by both executables with
  `matrix dimensions overflow` and exit status 1.
- The repaired signed constructors delegate to decimal-string parsing:
  `Integer(long long)` at `minplus.cpp:17-18` and `BigInt(long long)` at
  `independent_minplus.cpp:18-19`.
- The submitted clean-room test passed: the verifier contains neither
  `minplus.cpp` nor an include of `../src`.
- `task-6-report.md` was not present anywhere under
  `cylindrical_total_domination`, so that requested artifact could not be
  read or audited.

## Dependency and proof classification

1. **Definitions in `MINPLUS_IDENTITY_LEMMA.md:9-41` — Justified.**
   The extended-integer operations use `INF` as an absorbing multiplicative
   element, and the matrix product is the finite-state min-plus product. The
   identity matrix has diagonal `0` and off-diagonal `INF`, matching the
   stated semantics.

2. **Lemma 1 base case, `:54-59` — Justified.**
   The length-zero diagonal cost is `0`; off-diagonal reachability is `INF`.
   This relies on the stated convention that no finite walk has value `INF`.

3. **Lemma 1 induction, `:61-76` — Justified.**
   Partitioning a length-​`r+1` walk by its unique penultimate state gives the
   matrix product. Absorption correctly handles an absent prefix or edge, and
   finiteness of `Q` makes the minimum attained. No quantifier or inequality
   direction error was found.

4. **Lemma 2 scalar shift, `:88-99` — Justified.**
   For finite `c`, shifting finite candidates preserves order and leaves all
   `INF` candidates at `INF`. The proof covers the all-`INF` case.

5. **Lemma 2 associativity, `:101-114` — Justified.**
   Both parenthesizations minimize the same finite set of triple candidates;
   integer addition is associative on finite values and `INF` absorbs in any
   position. The finite-state/nonempty assumption needed for matrix minima is
   stated in the setup for the automaton application.

6. **Lemma 3 propagation, `:137-148` — Justified.**
   From the literal entrywise identity, associativity and the standard
   semigroup power law give
   `M^(N+p+k) = c ⊗ M^(N+k)`. The power law is invoked rather than separately
   proved, but it follows immediately by induction from the displayed power
   definition and associativity; this is not a substantive gap.

7. **Lemma 3 diagonal minimum, `:150-165` — Justified.**
   Taking diagonal entries and then the finite minimum commutes with a finite
   scalar shift. The proof explicitly handles at least one finite diagonal
   and all diagonal entries equal to `INF`. The conclusion is conditional on
   an exact entrywise identity, not on a trace or finite-prefix experiment.

## Implementation audit

### Producer: `src/automaton/minplus.cpp`

- **`INF` semantics — Justified.** `std::optional<Integer>` represents
  reachability; `nullopt` is absorbing in `minplus_add` (`:159-164`), and
  minima ignore unreachable candidates (`:174-181`). This is exact, not a
  large finite sentinel.
- **Decimal arithmetic — Justified for parsed CLI values.** The string
  parser validates an optional sign and decimal digits (`:19-38`), and the
  digit-wise addition/subtraction (`:84-120`) avoids fixed-width overflow.
  Leading zeroes and negative zero normalize correctly.
- **Power semantics — Justified.** `minplus_power` starts from the exact
  identity, supports exponent zero, and repeated squaring (`:195-211`) uses
  `uint64_t` shifts without cost arithmetic overflow.
- **Diagonal minimum — Justified for square CLI matrices.** It ignores
  unreachable diagonal entries and returns `INF` iff no diagonal entry is
  finite (`:214-223`).
- **Input-size guard — Justified.** `checked_size` verifies the row/column
  product against `std::numeric_limits<std::size_t>::max()` before vector
  allocation (`:148-155`), and throws `std::length_error` on overflow.

### Clean-room verifier: `verify/independent_minplus.cpp`

- **Structural separation — Justified.** It has no producer include,
  declaration, or link-time dependency; it defines separate `BigInt`,
  `Cost`, `Grid`, multiplication, power, and diagonal routines in an
  unnamed namespace (`:11-13`, `:15-225`). The implementation uses different
  names and data representation (`reachable` plus `BigInt`) rather than
  importing producer state.
- **Semantics — Justified.** `Cost{reachable=false}` is exact `INF`, identity
  is diagonal zero/off-diagonal unreachable (`:186-192`), and multiplication,
  power, and diagonal minimum cover the same edge cases independently.
- **Verifier input-size guard — Justified.** `checked_size` verifies the
  square product before allocation (`:149-155`) and throws
  `std::length_error` on overflow.

## Remaining findings

1. **Important, non-code: missing requested report artifact.**
   `cylindrical_total_domination/task-6-report.md` is absent. Consequently,
   this review cannot verify any claims that were supposed to be documented
   there. The implementation and proof review above is based only on the
   available requested files.

## Resolved findings from the prior review

- The signed integral constructor defect is resolved: both constructors now
  delegate to `std::to_string(value)` and the decimal parser; negative values
  are preserved.
- The matrix storage overflow defect is resolved: both allocation paths check
  the product against `std::numeric_limits<std::size_t>::max()` and throw
  `std::length_error` before multiplication/allocation when it would overflow.

## Critical findings

None.

## Suggested repairs (separate from verdict)

- Restore or provide `task-6-report.md` if it is part of the frozen Task 6
  submission. The code repairs reviewed here are complete; a substantive
  change to the proof or producer/verifier relationship requires a new
  independent review.
