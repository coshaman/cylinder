import pytest


def all_mask_pairs(width: int):
    limit = 1 << width
    for previous in range(limit):
        for current in range(limit):
            yield previous, current


def rows(mask: int, width: int) -> set[int]:
    return {i for i in range(width) if mask & (1 << i)}


def mask(row_set: set[int]) -> int:
    out = 0
    for i in row_set:
        out |= 1 << i
    return out


def reference_open_vertical_rows(selected_rows: set[int], width: int) -> set[int]:
    dominated = set()
    for i in selected_rows:
        if i > 0:
            dominated.add(i - 1)
        if i + 1 < width:
            dominated.add(i + 1)
    return dominated


def reference_next_pending(previous: int, current: int, width: int) -> int:
    already_dominated = rows(previous, width) | reference_open_vertical_rows(rows(current, width), width)
    return mask(set(range(width)) - already_dominated)


def vertical_open_neighbor_mask(selected: int, width: int) -> int:
    all_rows = (1 << width) - 1
    return ((selected << 1) | (selected >> 1)) & all_rows


def next_pending(previous: int, current: int, width: int) -> int:
    all_rows = (1 << width) - 1
    return all_rows & ~(previous | vertical_open_neighbor_mask(current, width))


def transition_legal(pending: int, next_selected: int) -> bool:
    return pending & ~next_selected == 0


def transition_next_pending(current: int, next_selected: int, width: int) -> int:
    return next_pending(current, next_selected, width)


def closed_walk_is_legal(column_masks: list[int], width: int) -> bool:
    pending = [
        next_pending(column_masks[j - 1], column_masks[j], width)
        for j in range(len(column_masks))
    ]
    return all(
        transition_legal(pending[j], column_masks[(j + 1) % len(column_masks)])
        for j in range(len(column_masks))
    )


@pytest.mark.parametrize("width", [5, 6, 7])
def test_next_pending_matches_direct_truth_table_for_all_mask_pairs(width: int) -> None:
    for previous, current in all_mask_pairs(width):
        assert next_pending(previous, current, width) == reference_next_pending(previous, current, width)


@pytest.mark.parametrize("width", [5, 6, 7])
def test_transition_legality_is_subset_truth_table(width: int) -> None:
    for pending, next_selected in all_mask_pairs(width):
        expected = rows(pending, width) <= rows(next_selected, width)
        assert transition_legal(pending, next_selected) is expected


@pytest.mark.parametrize("width", [5, 6, 7])
def test_deterministic_transition_update_ignores_old_pending_after_legality(width: int) -> None:
    for current, next_selected in all_mask_pairs(width):
        expected = reference_next_pending(current, next_selected, width)
        assert transition_next_pending(current, next_selected, width) == expected


def test_selected_vertex_requires_open_selected_neighbor() -> None:
    width = 5
    previous_edges = (1 << 0) | (1 << 4)
    selected_middle_only = 1 << 2

    pending = next_pending(previous_edges, selected_middle_only, width)

    assert pending & selected_middle_only
    assert not transition_legal(pending, 0)
    assert transition_legal(pending, selected_middle_only)


def test_vertical_neighbor_can_satisfy_selected_vertex_without_self_domination() -> None:
    width = 5
    adjacent_pair = (1 << 1) | (1 << 2)

    pending = next_pending(0, adjacent_pair, width)

    assert not (pending & adjacent_pair)


def test_c3_closed_walk_uses_distinct_left_and_right_horizontal_neighbors() -> None:
    width = 5
    columns = [0b10110, 0b11001, 0b01101]

    assert closed_walk_is_legal(columns, width)

    for j in range(3):
        left = (j - 1) % 3
        right = (j + 1) % 3
        assert left != right


def test_c3_closure_rejects_missing_right_neighbor_obligation() -> None:
    width = 5
    columns = [0b10110, 0b11000, 0b01101]

    assert not closed_walk_is_legal(columns, width)
