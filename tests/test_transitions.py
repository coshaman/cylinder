import json
import subprocess
import hashlib
from collections import deque
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {
    5: (169, 2419),
    6: (441, 11025),
    7: (1156, 50303),
}
EXPECTED_STRONGLY_CONNECTED = {
    5: True,
    6: True,
    7: True,
}
EXPECTED_TRANSITION_HASHES = {
    5: "b6501f275b981d5cd2387837b499c3b110baf6241ebd9cdc485b41db68062ec1",
    6: "ced3c9e4227b7f9b885e01959206b467874397bc4f309a264b0b1c0074946d51",
    7: "a645d24f6f3bd7c2c86cc967a71459466c20cafa5a8de21292db02d6e49460cc",
}
CERTIFICATE_MANIFESTS = {
    5: PROJECT_ROOT / "certificates" / "width5" / "automaton_manifest.json",
    6: PROJECT_ROOT / "certificates" / "width6" / "automaton_manifest.json",
    7: PROJECT_ROOT / "certificates" / "width7" / "automaton_manifest.json",
}


def open_vertical(selected: int, width: int) -> int:
    all_rows = (1 << width) - 1
    return ((selected << 1) | (selected >> 1)) & all_rows


def next_pending(previous: int, current: int, width: int) -> int:
    all_rows = (1 << width) - 1
    return all_rows & ~(previous | open_vertical(current, width))


def popcount(mask: int) -> int:
    return bin(mask).count("1")


def expected_edges(states: list[list[int]], width: int) -> list[list[int]]:
    state_to_index = {tuple(state): index for index, state in enumerate(states)}
    edges: list[list[int]] = []
    for tail, (current_selected, current_pending) in enumerate(states):
        for next_selected in range(1 << width):
            if current_pending & ~next_selected:
                continue
            head_state = (next_selected, next_pending(current_selected, next_selected, width))
            edges.append([tail, state_to_index[head_state], popcount(next_selected)])
    return sorted(edges)


def transition_hash(transitions: list[list[int]]) -> str:
    canonical = "".join(f"{tail},{head},{weight}\n" for tail, head, weight in transitions)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def reachable_from(start: int, graph: list[list[int]]) -> set[int]:
    seen = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for head in graph[node]:
            if head not in seen:
                seen.add(head)
                queue.append(head)
    return seen


def is_strongly_connected(state_count: int, edges: list[list[int]]) -> bool:
    forward = [[] for _ in range(state_count)]
    reverse = [[] for _ in range(state_count)]
    for tail, head, _weight in edges:
        forward[tail].append(head)
        reverse[head].append(tail)
    return (
        len(reachable_from(0, forward)) == state_count
        and len(reachable_from(0, reverse)) == state_count
    )


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
def test_transition_counts_match_regression_targets(
    producer_binary: Path, width: int
) -> None:
    manifest = run_manifest(producer_binary, width)

    assert manifest["transition_count"] == EXPECTED_COUNTS[width][1]
    assert len(manifest["transitions"]) == EXPECTED_COUNTS[width][1]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_every_transition_matches_independent_reference_predicate(
    producer_binary: Path, width: int
) -> None:
    manifest = run_manifest(producer_binary, width)
    states = [tuple(state) for state in manifest["states"]]
    state_to_index = {state: index for index, state in enumerate(states)}
    seen_edges = set()

    for edge in manifest["transitions"]:
        tail, head, weight = edge
        current_selected, current_pending = states[tail]
        next_selected, next_pending_mask = states[head]

        assert edge == [tail, head, weight]
        assert 0 <= tail < len(states)
        assert 0 <= head < len(states)
        assert current_pending & ~next_selected == 0
        assert next_pending_mask == next_pending(current_selected, next_selected, width)
        assert state_to_index[(next_selected, next_pending_mask)] == head
        assert weight == popcount(next_selected)
        assert isinstance(weight, int)
        assert weight >= 0
        seen_edges.add(tuple(edge))

    assert len(seen_edges) == len(manifest["transitions"])
    assert manifest["transitions"] == expected_edges(manifest["states"], width)
    assert manifest["transition_sha256"] == EXPECTED_TRANSITION_HASHES[width]
    assert transition_hash(manifest["transitions"]) == EXPECTED_TRANSITION_HASHES[width]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_transition_list_is_canonical_and_strongly_connected(
    producer_binary: Path, width: int
) -> None:
    manifest = run_manifest(producer_binary, width)
    transitions = manifest["transitions"]

    assert transitions == sorted(transitions)
    assert is_strongly_connected(len(manifest["states"]), transitions) is EXPECTED_STRONGLY_CONNECTED[width]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_persisted_manifest_records_transition_regression_artifact(width: int) -> None:
    artifact = json.loads(CERTIFICATE_MANIFESTS[width].read_text(encoding="utf-8"))

    assert artifact["width"] == width
    assert artifact["transition_count"] == EXPECTED_COUNTS[width][1]
    assert artifact["strongly_connected"] is EXPECTED_STRONGLY_CONNECTED[width]
    assert artifact["transition_sha256"] == EXPECTED_TRANSITION_HASHES[width]
    assert artifact["transitions"] == expected_edges(artifact["states"], width)
    assert transition_hash(artifact["transitions"]) == EXPECTED_TRANSITION_HASHES[width]
    assert "src/automaton/transitions.cpp" in artifact["producer_command"]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_producer_output_exactly_matches_persisted_manifest(
    producer_binary: Path, width: int
) -> None:
    artifact = json.loads(CERTIFICATE_MANIFESTS[width].read_text(encoding="utf-8"))

    assert run_manifest(producer_binary, width) == artifact
