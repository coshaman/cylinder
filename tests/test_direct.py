import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.direct.graph import is_total_dominating


def test_selected_vertex_does_not_dominate_itself_without_open_neighbor():
    selected = {(2, 1)}

    assert not is_total_dominating(5, 3, selected)


def test_vertical_open_neighbor_can_dominate_selected_vertex():
    selected = {
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (3, 0), (3, 1), (3, 2),
    }

    assert is_total_dominating(5, 3, selected)


def test_c3_uses_distinct_left_and_right_horizontal_neighbors():
    selected = {
        (0, 1), (0, 2),
        (1, 0), (1, 1),
        (2, 0), (2, 2),
        (3, 1), (3, 2),
        (4, 0), (4, 1),
    }

    assert is_total_dominating(5, 3, selected)


@pytest.mark.parametrize(
    ("m", "n", "selected"),
    [
        (4, 3, set()),
        (5, 2, set()),
        (5, 3, {(-1, 0)}),
        (5, 3, {(5, 0)}),
        (5, 3, {(0, 3)}),
    ],
)
def test_rejects_invalid_width_circumference_and_vertices(m, n, selected):
    with pytest.raises(ValueError):
        is_total_dominating(m, n, selected)
