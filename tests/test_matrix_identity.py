from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT_ROOT / "src" / "automaton" / "power_identity.cpp"
WIDTHS = {
    5: (16, 4, 6),
    6: (21, 14, 24),
    7: (28, 4, 8),
}


def read_matrix(path: Path) -> tuple[int, list[int | None]]:
    raw = path.read_bytes()
    assert raw[:4] == b"MTX1"
    (size,) = struct.unpack_from("<Q", raw, 8)
    offset = 16
    values: list[int | None] = []
    for _ in range(size * size):
        tag = raw[offset]
        offset += 1
        if tag == 0:
            values.append(None)
        else:
            assert tag == 1
            (value,) = struct.unpack_from("<q", raw, offset)
            offset += 8
            values.append(value)
    assert offset == len(raw)
    return size, values


def test_power_identity_producer_source_exists() -> None:
    assert SOURCE.is_file(), f"missing producer: {SOURCE}"


@pytest.mark.parametrize("width,parameters", sorted(WIDTHS.items()))
def test_persisted_manifest_parameters_are_frozen(
    width: int, parameters: tuple[int, int, int]
) -> None:
    manifest = PROJECT_ROOT / "certificates" / f"width{width}" / "automaton_manifest.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["width"] == width
    assert data["state_count"] == {5: 169, 6: 441, 7: 1156}[width]
    assert data["transition_count"] == {5: 2419, 6: 11025, 7: 50303}[width]
    assert parameters[0] > 0 and parameters[1] > 0 and parameters[2] > 0


@pytest.mark.parametrize("width,parameters", sorted(WIDTHS.items()))
def test_matrix_artifacts_have_exact_dimensions_and_record_identity(
    width: int, parameters: tuple[int, int, int]
) -> None:
    certificate = PROJECT_ROOT / "certificates" / f"width{width}"
    metadata = json.loads(
        (certificate / "matrix_identity.json").read_text(encoding="utf-8")
    )
    n, p, c = parameters
    assert (metadata["N"], metadata["p"], metadata["c"]) == (n, p, c)
    assert metadata["width"] == width

    first_size, first = read_matrix(certificate / "M_N.bin")
    second_size, second = read_matrix(certificate / "M_N_plus_p.bin")
    assert first_size == second_size == metadata["state_count"]
    assert len(first) == len(second) == first_size * first_size
    assert metadata["M_N_sha256"] == hashlib.sha256(
        (certificate / "M_N.bin").read_bytes()
    ).hexdigest()
    assert metadata["M_N_plus_p_sha256"] == hashlib.sha256(
        (certificate / "M_N_plus_p.bin").read_bytes()
    ).hexdigest()

    if metadata["status"] == "TOOL_CHECKED_LOCAL":
        assert metadata["identity_holds"] is True
        assert all(
            right == (None if left is None else left + c)
            for left, right in zip(first, second)
        )
    else:
        assert metadata["status"] == "PROTOTYPE_IDENTITY_NOT_REPRODUCED"
        assert metadata["identity_holds"] is False
        assert metadata["mismatch_count"] > 0


def test_producer_compiles_as_a_standalone_cxx17_program(tmp_path: Path) -> None:
    compiler = shutil.which("g++")
    if compiler is None:
        pytest.fail("g++ is required for the matrix identity producer")
    output = tmp_path / "power_identity"
    subprocess.run(
        [compiler, "-std=c++17", "-O2", str(SOURCE), "-o", str(output)],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
