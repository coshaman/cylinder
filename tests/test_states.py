import json
import subprocess
import hashlib
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {
    5: (169, 2419),
    6: (441, 11025),
    7: (1156, 50303),
}
EXPECTED_STATE_HASHES = {
    5: "3dab5d356f6ef377eaf71ad224402fed0b22fdc1b9da226beb442ffd5a22030c",
    6: "2c2d8b0bddd71a33e381e25a9c50113c566e588fc9b1dcb2b1272bb87a12991f",
    7: "6076bbfc9b9bf15400939a397f8a5de842cd14db368d510723b6a13af4511b96",
}
CERTIFICATE_MANIFESTS = {
    5: PROJECT_ROOT / "certificates" / "width5" / "automaton_manifest.json",
    6: PROJECT_ROOT / "certificates" / "width6" / "automaton_manifest.json",
    7: PROJECT_ROOT / "certificates" / "width7" / "automaton_manifest.json",
}


def open_vertical(selected: int, width: int) -> int:
    all_rows = (1 << width) - 1
    return ((selected << 1) | (selected >> 1)) & all_rows


def submasks(mask: int):
    current = mask
    while True:
        yield current
        if current == 0:
            break
        current = (current - 1) & mask


def reference_states(width: int) -> list[list[int]]:
    states: list[list[int]] = []
    all_rows = (1 << width) - 1
    for selected in range(1 << width):
        allowed_pending = all_rows & ~open_vertical(selected, width)
        for pending in submasks(allowed_pending):
            states.append([selected, pending])
    return sorted(states)


def state_hash(states: list[list[int]]) -> str:
    canonical = "".join(f"{selected},{pending}\n" for selected, pending in states)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


@pytest.fixture(scope="module")
def producer_binary(tmp_path_factory: pytest.TempPathFactory) -> Path:
    binary = tmp_path_factory.mktemp("producer") / "automaton_manifest"
    if hasattr(binary, "with_suffix"):
        binary = binary.with_suffix(".exe")
    sources = [
        PROJECT_ROOT / "src" / "automaton" / "manifest.cpp",
        PROJECT_ROOT / "src" / "automaton" / "states.cpp",
        PROJECT_ROOT / "src" / "automaton" / "transitions.cpp",
    ]
    subprocess.run(
        ["g++", "-std=c++17", "-O2", *map(str, sources), "-o", str(binary)],
        cwd=PROJECT_ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return binary


def run_manifest(producer_binary: Path, width: int) -> dict:
    completed = subprocess.run(
        [str(producer_binary), str(width)],
        cwd=PROJECT_ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(completed.stdout)


@pytest.mark.parametrize("width", [5, 6, 7])
def test_state_counts_match_regression_targets(producer_binary: Path, width: int) -> None:
    manifest = run_manifest(producer_binary, width)

    assert manifest["state_count"] == EXPECTED_COUNTS[width][0]
    assert len(manifest["states"]) == EXPECTED_COUNTS[width][0]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_states_are_canonical_and_match_independent_enumeration(
    producer_binary: Path, width: int
) -> None:
    manifest = run_manifest(producer_binary, width)
    states = manifest["states"]

    assert states == sorted(states)
    assert states == reference_states(width)
    assert manifest["state_sha256"] == EXPECTED_STATE_HASHES[width]
    assert state_hash(states) == EXPECTED_STATE_HASHES[width]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_pending_masks_exclude_open_vertical_neighborhood(
    producer_binary: Path, width: int
) -> None:
    manifest = run_manifest(producer_binary, width)

    for selected, pending in manifest["states"]:
        assert pending & open_vertical(selected, width) == 0


@pytest.mark.parametrize("width", [5, 6, 7])
def test_persisted_manifest_records_state_regression_artifact(width: int) -> None:
    artifact = json.loads(CERTIFICATE_MANIFESTS[width].read_text(encoding="utf-8"))

    assert artifact["width"] == width
    assert artifact["state_count"] == EXPECTED_COUNTS[width][0]
    assert artifact["state_sha256"] == EXPECTED_STATE_HASHES[width]
    assert artifact["states"] == reference_states(width)
    assert state_hash(artifact["states"]) == EXPECTED_STATE_HASHES[width]
    assert "src/automaton/states.cpp" in artifact["producer_command"]
