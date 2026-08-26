VALID_WIDTHS = {5, 6, 7}


def validate_instance(m: int, n: int, selected: set[tuple[int, int]] | None = None) -> None:
    if m not in VALID_WIDTHS:
        raise ValueError("m must be one of 5, 6, or 7")
    if n < 3:
        raise ValueError("n must be at least 3")
    if selected is None:
        return
    for i, j in selected:
        if not (0 <= i < m and 0 <= j < n):
            raise ValueError(f"invalid vertex {(i, j)} for P_{m} square C_{n}")


def neighbors(m: int, n: int, vertex: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    i, j = vertex
    out = []
    if i > 0:
        out.append((i - 1, j))
    if i + 1 < m:
        out.append((i + 1, j))
    out.append((i, (j - 1) % n))
    out.append((i, (j + 1) % n))
    return tuple(out)


def is_total_dominating(m: int, n: int, selected: set[tuple[int, int]]) -> bool:
    validate_instance(m, n, selected)
    return all(
        any(adjacent in selected for adjacent in neighbors(m, n, (i, j)))
        for i in range(m)
        for j in range(n)
    )
