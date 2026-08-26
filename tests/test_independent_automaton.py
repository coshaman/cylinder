import hashlib
import importlib.util
import json
import subprocess
from collections import deque
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PY_VERIFIER = PROJECT_ROOT / "verify" / "independent_states.py"
CPP_VERIFIER = PROJECT_ROOT / "verify" / "independent_transitions.cpp"
REPORT = PROJECT_ROOT / "verify" / "INDEPENDENT_AUTOMATON_REPORT.md"
TASK_REPORT = PROJECT_ROOT / "verify" / "INDEPENDENT_AUTOMATON_REPORT.md"
MANIFESTS = {
    width: PROJECT_ROOT / "certificates" / f"width{width}" / "automaton_manifest.json"
    for width in [5, 6, 7]
}
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
EXPECTED_TRANSITION_HASHES = {
    5: "b6501f275b981d5cd2387837b499c3b110baf6241ebd9cdc485b41db68062ec1",
    6: "ced3c9e4227b7f9b885e01959206b467874397bc4f309a264b0b1c0074946d51",
    7: "a645d24f6f3bd7c2c86cc967a71459466c20cafa5a8de21292db02d6e49460cc",
}


def load_independent_states_module():
    spec = importlib.util.spec_from_file_location("independent_states", PY_VERIFIER)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def independent_states():
    return load_independent_states_module()


@pytest.fixture(scope="module")
def independent_binary(tmp_path_factory: pytest.TempPathFactory) -> Path:
    binary = tmp_path_factory.mktemp("independent") / "independent_transitions"
    if hasattr(binary, "with_suffix"):
        binary = binary.with_suffix(".exe")
    subprocess.run(
        ["g++", "-std=c++17", "-O2", str(CPP_VERIFIER), "-o", str(binary)],
        cwd=PROJECT_ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return binary


def manifest(width: int) -> dict:
    return json.loads(MANIFESTS[width].read_text(encoding="utf-8"))


def run_independent_transitions(binary: Path, width: int) -> dict:
    completed = subprocess.run(
        [str(binary), str(width)],
        cwd=PROJECT_ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(completed.stdout)


def canonical_state_hash(states: list[list[int]]) -> str:
    payload = "".join(f"{selected},{pending}\n" for selected, pending in states)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def canonical_transition_hash(transitions: list[list[int]]) -> str:
    payload = "".join(f"{tail},{head},{weight}\n" for tail, head, weight in transitions)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def reachable(start: int, graph: list[list[int]]) -> set[int]:
    seen = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for head in graph[node]:
            if head not in seen:
                seen.add(head)
                queue.append(head)
    return seen


def strongly_connected(state_count: int, transitions: list[list[int]]) -> bool:
    forward = [[] for _ in range(state_count)]
    reverse = [[] for _ in range(state_count)]
    for tail, head, _weight in transitions:
        forward[tail].append(head)
        reverse[head].append(tail)
    return (
        len(reachable(0, forward)) == state_count
        and len(reachable(0, reverse)) == state_count
    )


@pytest.mark.parametrize("width", [5, 6, 7])
def test_clean_room_state_sets_match_task_4_manifests(independent_states, width: int) -> None:
    artifact = manifest(width)
    states = independent_states.canonical_states(width)

    assert states == artifact["states"]
    assert len(states) == EXPECTED_COUNTS[width][0]
    assert canonical_state_hash(states) == EXPECTED_STATE_HASHES[width]
    assert canonical_state_hash(states) == artifact["state_sha256"]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_clean_room_transition_sets_and_weights_match_task_4_manifests(
    independent_binary: Path, width: int
) -> None:
    artifact = manifest(width)
    rebuilt = run_independent_transitions(independent_binary, width)

    assert rebuilt["states"] == artifact["states"]
    assert rebuilt["transitions"] == artifact["transitions"]
    assert len(rebuilt["transitions"]) == EXPECTED_COUNTS[width][1]
    assert canonical_transition_hash(rebuilt["transitions"]) == EXPECTED_TRANSITION_HASHES[width]
    assert canonical_transition_hash(rebuilt["transitions"]) == artifact["transition_sha256"]


@pytest.mark.parametrize("width", [5, 6, 7])
def test_clean_room_strong_connectivity_matches_manifests(
    independent_binary: Path, width: int
) -> None:
    rebuilt = run_independent_transitions(independent_binary, width)
    artifact = manifest(width)

    assert rebuilt["strongly_connected"] is True
    assert strongly_connected(len(rebuilt["states"]), rebuilt["transitions"]) is True
    assert rebuilt["strongly_connected"] is artifact["strongly_connected"]


def test_mutations_are_rejected_by_manifest_comparison(
    independent_states, independent_binary: Path
) -> None:
    width = 5
    artifact = manifest(width)
    states = independent_states.canonical_states(width)
    transitions = run_independent_transitions(independent_binary, width)["transitions"]

    missing_state = states[:-1]
    reweighted_edges = [edge[:] for edge in transitions]
    reweighted_edges[0][2] += 1
    disconnected_edges = [edge for edge in transitions if edge[0] != 0]

    assert missing_state != artifact["states"]
    assert canonical_state_hash(missing_state) != artifact["state_sha256"]
    assert reweighted_edges != artifact["transitions"]
    assert canonical_transition_hash(reweighted_edges) != artifact["transition_sha256"]
    assert strongly_connected(len(states), disconnected_edges) is False


def test_clean_room_sources_do_not_reference_producer_code() -> None:
    forbidden = ["src/automaton", "automaton/", "states.cpp", "transitions.cpp", "manifest.cpp"]
    for path in [PY_VERIFIER, CPP_VERIFIER]:
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            assert token not in text
    assert "src.automaton" not in PY_VERIFIER.read_text(encoding="utf-8")


def test_required_reports_record_command_hashes_and_scope() -> None:
    for report in [REPORT, TASK_REPORT]:
        text = report.read_text(encoding="utf-8")
        assert "pytest tests/test_independent_automaton.py -q" in text
        assert "src/automaton" in text
        assert "not imported" in text
        for expected_hash in [*EXPECTED_STATE_HASHES.values(), *EXPECTED_TRANSITION_HASHES.values()]:
            assert expected_hash in text
