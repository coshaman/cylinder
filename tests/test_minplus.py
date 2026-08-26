from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PRODUCER = PROJECT_ROOT / "src" / "automaton" / "minplus.cpp"
VERIFIER = PROJECT_ROOT / "verify" / "independent_minplus.cpp"


def compile_engine(source: Path, output: Path) -> None:
    assert source.is_file(), f"missing engine source: {source}"
    compiler = shutil.which("g++")
    if compiler is None:
        pytest.fail("g++ is required for the min-plus engine tests")
    subprocess.run(
        [compiler, "-std=c++17", "-O2", str(source.relative_to(PROJECT_ROOT)), "-o", str(output)],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


@pytest.fixture(scope="session")
def engines(tmp_path_factory: pytest.TempPathFactory) -> tuple[Path, Path]:
    build = tmp_path_factory.mktemp("minplus-build")
    producer = build / "producer"
    verifier = build / "verifier"
    compile_engine(PRODUCER, producer)
    compile_engine(VERIFIER, verifier)
    return producer, verifier


def run_engine(executable: Path, operation: str, payload: str) -> list[str]:
    result = subprocess.run(
        [str(executable), operation],
        input=payload,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.split()


def matrix_payload(matrix: list[list[str]]) -> str:
    size = len(matrix)
    return f"{size}\n" + "\n".join(" ".join(row) for row in matrix) + "\n"


def multiply_payload(left: list[list[str]], right: list[list[str]]) -> str:
    return matrix_payload(left) + "\n".join(" ".join(row) for row in right) + "\n"


def reference_add(left: str, right: str) -> str:
    if left == "INF" or right == "INF":
        return "INF"
    return str(int(left) + int(right))


def reference_multiply(left: list[list[str]], right: list[list[str]]) -> list[list[str]]:
    return [
        [
            min((reference_add(left[i][k], right[k][j]) for k in range(len(right))), key=lambda value: (value == "INF", int(value) if value != "INF" else 0))
            for j in range(len(right))
        ]
        for i in range(len(left))
    ]


def test_identity_and_infinity_absorption(engines: tuple[Path, Path]) -> None:
    matrix = [["0", "7", "INF"], ["INF", "0", "-2"], ["11", "INF", "0"]]
    identity = [["0", "INF", "INF"], ["INF", "0", "INF"], ["INF", "INF", "0"]]

    for executable in engines:
        assert run_engine(executable, "multiply", multiply_payload(matrix, identity)) == [
            "3",
            "3",
            "0",
            "7",
            "INF",
            "INF",
            "0",
            "-2",
            "11",
            "INF",
            "0",
        ]
        assert run_engine(executable, "multiply", multiply_payload(
            [["INF", "INF"], ["INF", "INF"]],
            [["0", "-9"], ["12", "0"]],
        )) == ["2", "2", "INF", "INF", "INF", "INF"]


@pytest.mark.parametrize(
    "left,right,third",
    [
        (
            [["0", "2", "INF"], ["INF", "0", "3"], ["4", "INF", "0"]],
            [["1", "INF", "5"], ["2", "0", "INF"], ["INF", "4", "1"]],
            [["0", "3", "INF"], ["INF", "0", "2"], ["1", "INF", "0"]],
        ),
        (
            [["INF", "8"], ["-3", "0"]],
            [["2", "INF"], ["INF", "5"]],
            [["0", "-4"], ["7", "INF"]],
        ),
    ],
)
def test_associativity_examples(
    engines: tuple[Path, Path],
    left: list[list[str]],
    right: list[list[str]],
    third: list[list[str]],
) -> None:
    expected = reference_multiply(reference_multiply(left, right), third)
    assert expected == reference_multiply(left, reference_multiply(right, third))
    for executable in engines:
        first = run_engine(executable, "multiply", multiply_payload(left, right))
        first_matrix = [first[2 + i * len(left) : 2 + (i + 1) * len(left)] for i in range(len(left))]
        second = run_engine(executable, "multiply", multiply_payload(first_matrix, third))
        assert second[2:] == [entry for row in expected for entry in row]


def test_diagonal_minimum_handles_unreachable_diagonal(engines: tuple[Path, Path]) -> None:
    matrix = [["9", "INF", "3"], ["4", "-8", "INF"], ["INF", "5", "12"]]
    for executable in engines:
        assert run_engine(executable, "diagonal", matrix_payload(matrix)) == ["-8"]
        assert run_engine(executable, "diagonal", matrix_payload([["INF", "1"], ["2", "INF"]])) == ["INF"]


def test_exact_power_semantics_including_zero_and_large_integer(engines: tuple[Path, Path]) -> None:
    matrix = [["0", "5", "INF"], ["INF", "0", "2"], ["3", "INF", "0"]]
    expected_power_two = ["0", "5", "7", "5", "0", "2", "3", "8", "0"]
    for executable in engines:
        assert run_engine(executable, "power", "2 0\n1 INF\nINF 1\n") == [
            "2", "2", "0", "INF", "INF", "0"
        ]
        assert run_engine(executable, "power", "3 2\n" + "\n".join(" ".join(row) for row in matrix) + "\n") == [
            "3", "3", *expected_power_two
        ]
        huge = "10" * 40
        assert run_engine(executable, "multiply", multiply_payload(
            [[huge, "INF"], ["INF", "0"]],
            [["0", "INF"], ["INF", "0"]],
        )) == [
            "2", "2", huge, "INF", "INF", "0"
        ]


def test_verifier_is_clean_room_translation_unit() -> None:
    text = VERIFIER.read_text(encoding="utf-8")
    assert "minplus.cpp" not in text
    assert "#include \"../src" not in text
