from __future__ import annotations


VALID_WIDTHS = {5, 6, 7}


def _row_mask(width: int) -> int:
    if width not in VALID_WIDTHS:
        raise ValueError("width must be 5, 6, or 7")
    return (1 << width) - 1


def vertical_neighbors(chosen: int, width: int) -> int:
    rows = _row_mask(width)
    return ((chosen << 1) | (chosen >> 1)) & rows


def canonical_states(width: int) -> list[list[int]]:
    rows = _row_mask(width)
    records: list[list[int]] = []
    for chosen in range(rows + 1):
        blocked = vertical_neighbors(chosen, width)
        for waiting in range(rows + 1):
            if waiting & blocked:
                continue
            records.append([chosen, waiting])
    return records


def state_lines(states: list[list[int]]) -> str:
    return "".join(f"{chosen},{waiting}\n" for chosen, waiting in states)
