import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.direct.graph import is_total_dominating
from src.direct.milp_probe import minimum_total_domination


@pytest.mark.parametrize(
    ("m", "n", "expected"),
    [
        (5, 3, 5),
        (5, 6, 10),
        (5, 10, 16),
        (5, 14, 22),
        (5, 20, 30),
        (6, 3, 6),
        (6, 4, 8),
        (6, 8, 16),
        (6, 12, 22),
        (6, 14, 24),
        (6, 21, 36),
        (6, 26, 48),
        (7, 3, 6),
        (7, 7, 15),
        (7, 14, 30),
        (7, 15, 30),
        (7, 20, 40),
    ],
)
def test_required_small_exact_values_return_rechecked_witnesses(m, n, expected):
    value, selected = minimum_total_domination(m, n)

    assert value == expected
    assert len(selected) == expected
    assert is_total_dominating(m, n, selected)
