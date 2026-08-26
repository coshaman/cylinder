from __future__ import annotations

from functools import cache
from pathlib import Path
import shutil
import subprocess
import tempfile

from src.direct.graph import is_total_dominating, neighbors, validate_instance


def _variable(vertex: tuple[int, int]) -> str:
    return f"x_{vertex[0]}_{vertex[1]}"


def _cbc_path() -> str:
    found = shutil.which("cbc")
    if found:
        return found
    bundled = (
        Path.home()
        / "AppData"
        / "Roaming"
        / "Python"
        / "Python310"
        / "site-packages"
        / "pulp"
        / "solverdir"
        / "cbc"
        / "win"
        / "i64"
        / "cbc.exe"
    )
    if bundled.exists():
        return str(bundled)
    raise RuntimeError("CBC executable not found")


def _write_lp(path: Path, m: int, n: int) -> None:
    vertices = [(i, j) for i in range(m) for j in range(n)]
    lines = [
        "Minimize",
        " obj: " + " + ".join(_variable(vertex) for vertex in vertices),
        "Subject To",
    ]
    for vertex in vertices:
        lines.append(
            f" dom_{vertex[0]}_{vertex[1]}: "
            + " + ".join(_variable(adjacent) for adjacent in neighbors(m, n, vertex))
            + " >= 1"
        )
    lines.append("Binary")
    lines.extend(f" {_variable(vertex)}" for vertex in vertices)
    lines.append("End")
    path.write_text("\n".join(lines) + "\n", encoding="ascii")


def _read_solution(path: Path) -> set[tuple[int, int]]:
    selected = set()
    for line in path.read_text(encoding="ascii").splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[1].startswith("x_") and float(parts[2]) > 0.5:
            _, row, column = parts[1].split("_")
            selected.add((int(row), int(column)))
    return selected


@cache
def minimum_total_domination(m: int, n: int) -> tuple[int, set[tuple[int, int]]]:
    validate_instance(m, n)
    with tempfile.TemporaryDirectory(prefix="ctd_milp_") as tmp:
        tmp_path = Path(tmp)
        model_path = tmp_path / "model.lp"
        solution_path = tmp_path / "solution.txt"
        _write_lp(model_path, m, n)
        result = subprocess.run(
            [_cbc_path(), str(model_path), "-solve", "-solution", str(solution_path), "-quit"],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 or "Optimal solution found" not in result.stdout:
            raise RuntimeError(
                f"CBC did not prove optimality for P_{m} square C_{n}:\n{result.stdout}\n{result.stderr}"
            )
        selected = _read_solution(solution_path)

    value = len(selected)
    if not is_total_dominating(m, n, selected):
        raise RuntimeError(f"internal witness check failed for P_{m} square C_{n}")
    return value, selected
