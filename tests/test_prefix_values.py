from __future__ import annotations

import json
import importlib.util
import inspect
import sys
from pathlib import Path

import numpy as np
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.direct.graph import is_total_dominating
from src.direct.milp_probe import minimum_total_domination

PREFIXES = {
    5: range(3, 20),
    6: range(3, 35),
    7: range(3, 32),
}

PARAMETERS = {5: (16, 4, 6), 6: (21, 14, 24), 7: (28, 4, 8)}
EPSILON_14 = (0, 1, 2, 0, 1, 0, 1, 0, 2, 0, 0, 1, 3, 1)


def clean_room_verifier():
    source = PROJECT_ROOT / "verify" / "verify_certificates.py"
    spec = importlib.util.spec_from_file_location("task9_clean_room", source)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def formula_value(width: int, n: int) -> int:
    if width == 5:
        return (3 * n + 1) // 2 + (1 if n % 4 == 2 else 0)
    if width == 6:
        if n == 12:
            return 22
        return (12 * n + 6) // 7 + EPSILON_14[n % 14]
    if width == 7:
        return {7: 15, 14: 30}.get(n, 2 * n)
    raise ValueError(f"unsupported width {width}")


def trace_diagonal_values(width: int, n_limit: int) -> list[int]:
    """Compute closed-walk diagonal minima from the clean-room edge graph.

    The source set is the full reconstructed state set. This computes the
    unrestricted diagonal minimum directly, rather than relying on a
    low-column-weight rotation argument.
    """
    verifier = clean_room_verifier()
    states = verifier._rebuild_states(width)
    transitions = verifier._rebuild_transitions(width, states)
    sources = list(range(len(states)))
    incoming: list[list[tuple[int, int]]] = [[] for _ in states]
    for tail, head, weight in transitions:
        incoming[head].append((tail, weight))

    infinity = np.int64(10**9)
    costs = np.full((len(sources), len(states)), infinity, dtype=np.int64)
    costs[np.arange(len(sources)), sources] = 0
    values: list[int] = []
    for step in range(1, n_limit + 1):
        following = np.full_like(costs, infinity)
        for head, edges in enumerate(incoming):
            tails = np.fromiter((tail for tail, _weight in edges), dtype=np.intp)
            weights = np.fromiter((weight for _tail, weight in edges), dtype=np.int64)
            following[:, head] = np.min(costs[:, tails] + weights, axis=1)
        costs = following
        if step >= 3:
            values.append(int(np.min(costs[np.arange(len(sources)), sources])))

    certificate = PROJECT_ROOT / "certificates" / f"width{width}"
    _dimension, matrix = verifier._parse_matrix(certificate / "M_N.bin")
    n, _period, _increment = PARAMETERS[width]
    persisted_diagonal = [
        matrix[index * _dimension + index]
        for index in range(_dimension)
        if matrix[index * _dimension + index] is not None
    ]
    assert values[n - 3] == min(persisted_diagonal)
    return values


def read_value_table(width: int) -> dict[int, int]:
    path = PROJECT_ROOT / "results" / f"WIDTH{width}_VALUES.md"
    text = path.read_text(encoding="utf-8")
    payload = text.split("```json\n", 1)[1].split("\n```", 1)[0]
    return {int(n): int(value) for n, value in json.loads(payload).items()}


@pytest.mark.parametrize("width", [5, 6, 7])
def test_frozen_prefix_value_tables_exist_and_cover_every_required_n(width: int) -> None:
    values = read_value_table(width)
    assert list(values) == list(PREFIXES[width])


def test_frozen_exception_values_are_present() -> None:
    assert read_value_table(6)[12] == 22
    assert read_value_table(7)[7] == 15
    assert read_value_table(7)[14] == 30


@pytest.mark.parametrize("width", [5, 6, 7])
def test_clean_room_diagonal_minima_match_every_persisted_prefix_row(width: int) -> None:
    actual = trace_diagonal_values(width, max(PREFIXES[width]))
    table = read_value_table(width)
    assert actual == [table[n] for n in PREFIXES[width]]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_formula_matches_every_clean_room_prefix_value(width: int) -> None:
    values = trace_diagonal_values(width, max(PREFIXES[width]))
    assert values == [formula_value(width, n) for n in PREFIXES[width]]


@pytest.mark.parametrize(
    ("width", "n", "expected"),
    [(5, 3, 5), (5, 10, 16), (6, 12, 22), (6, 21, 36), (7, 7, 15), (7, 14, 30), (7, 20, 40)],
)
def test_selected_rows_cross_check_independent_direct_witnesses(
    width: int, n: int, expected: int
) -> None:
    value, selected = minimum_total_domination(width, n)
    assert value == expected
    assert len(selected) == expected
    assert is_total_dominating(width, n, selected)
    assert read_value_table(width)[n] == expected


def test_clean_room_trace_does_not_use_direct_per_n_optimization() -> None:
    source = inspect.getsource(trace_diagonal_values)
    assert "minimum_total_domination" not in source
    assert "src.direct" not in source
    assert "src.automaton" not in source
