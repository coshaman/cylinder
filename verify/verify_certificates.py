"""Clean-room verification of the persisted cylindrical-grid certificates.

This module deliberately contains its own mask, state, transition, and
min-plus implementations.  It does not import or execute producer code.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


WIDTH_PARAMETERS = {5: (16, 4, 6), 6: (21, 14, 24), 7: (28, 4, 8)}
MATRIX_MAGIC = b"MTX1"
MATRIX_FORMAT = "MTX1 little-endian uint64 dimension, tagged int64 entries"
ACCEPTED_STATUS = "TOOL_CHECKED_LOCAL"
PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class VerificationReport:
    width: int
    accepted: bool
    status: str
    checks: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _fail(width: int, errors: Iterable[str], checks: Iterable[str] = ()) -> VerificationReport:
    return VerificationReport(width, False, "CERTIFICATE_VERIFICATION_FAILED", tuple(checks), tuple(errors))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json(path: Path) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key!r} in {path.name}")
            result[key] = value
        return result

    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return value


def _rows_mask(width: int) -> int:
    if width not in WIDTH_PARAMETERS:
        raise ValueError("width must be 5, 6, or 7")
    return (1 << width) - 1


def _vertical_neighbors(mask: int, width: int) -> int:
    rows = _rows_mask(width)
    return ((mask << 1) | (mask >> 1)) & rows


def _bit_count(mask: int) -> int:
    count = 0
    while mask:
        count += mask & 1
        mask >>= 1
    return count


def _rebuild_states(width: int) -> list[list[int]]:
    rows = _rows_mask(width)
    states: list[list[int]] = []
    for selected in range(rows + 1):
        blocked = _vertical_neighbors(selected, width)
        for pending in range(rows + 1):
            if pending & blocked == 0:
                states.append([selected, pending])
    return states


def _rebuild_transitions(width: int, states: list[list[int]]) -> list[list[int]]:
    rows = _rows_mask(width)
    indexes = {(selected, pending): index for index, (selected, pending) in enumerate(states)}
    transitions: list[list[int]] = []
    for tail, (selected, pending) in enumerate(states):
        for next_selected in range(rows + 1):
            if pending & ~next_selected:
                continue
            next_pending = rows & ~(selected | _vertical_neighbors(next_selected, width))
            try:
                head = indexes[(next_selected, next_pending)]
            except KeyError as error:
                raise ValueError("rebuilt transition points to a missing state") from error
            transitions.append([tail, head, _bit_count(next_selected)])
    return transitions


def _state_lines(states: Iterable[list[int]]) -> str:
    return "".join(f"{selected},{pending}\n" for selected, pending in states)


def _transition_lines(transitions: Iterable[list[int]]) -> str:
    return "".join(f"{tail},{head},{weight}\n" for tail, head, weight in transitions)


def _reachable(start: int, graph: list[list[int]]) -> set[int]:
    seen = {start}
    queue: deque[int] = deque([start])
    while queue:
        node = queue.popleft()
        for head in graph[node]:
            if head not in seen:
                seen.add(head)
                queue.append(head)
    return seen


def _strongly_connected(state_count: int, transitions: list[list[int]]) -> bool:
    forward = [[] for _ in range(state_count)]
    reverse = [[] for _ in range(state_count)]
    for tail, head, _weight in transitions:
        forward[tail].append(head)
        reverse[head].append(tail)
    return len(_reachable(0, forward)) == state_count and len(_reachable(0, reverse)) == state_count


def _parse_matrix(path: Path) -> tuple[int, list[int | None]]:
    raw = path.read_bytes()
    if len(raw) < 16 or raw[:4] != MATRIX_MAGIC:
        raise ValueError(f"{path.name}: invalid MTX1 header")
    version, dimension = struct.unpack_from("<IQ", raw, 4)
    if version != 1:
        raise ValueError(f"{path.name}: unsupported matrix version {version}")
    if dimension == 0:
        raise ValueError(f"{path.name}: zero matrix dimension")
    values: list[int | None] = []
    offset = 16
    for _ in range(dimension * dimension):
        if offset >= len(raw):
            raise ValueError(f"{path.name}: truncated matrix tag")
        tag = raw[offset]
        offset += 1
        if tag == 0:
            values.append(None)
        elif tag == 1:
            if offset + 8 > len(raw):
                raise ValueError(f"{path.name}: truncated finite matrix entry")
            (value,) = struct.unpack_from("<q", raw, offset)
            offset += 8
            values.append(value)
        else:
            raise ValueError(f"{path.name}: invalid entry tag {tag}")
    if offset != len(raw):
        raise ValueError(f"{path.name}: trailing bytes after matrix")
    return dimension, values


def _powers_from_edges(
    state_count: int, transitions: list[list[int]], prefix: int, exponent: int
) -> tuple[list[int | None], list[int | None]]:
    outgoing: list[list[tuple[int, int]]] = [[] for _ in range(state_count)]
    for tail, head, weight in transitions:
        outgoing[tail].append((head, weight))

    prefix_result: list[int | None] = []
    result: list[int | None] = []
    for source in range(state_count):
        current: list[int | None] = [None] * state_count
        current[source] = 0
        for step in range(1, exponent + 1):
            following: list[int | None] = [None] * state_count
            for tail, prefix_cost in enumerate(current):
                if prefix_cost is None:
                    continue
                for head, weight in outgoing[tail]:
                    candidate = prefix_cost + weight
                    old = following[head]
                    if old is None or candidate < old:
                        following[head] = candidate
            current = following
            if step == prefix:
                prefix_result.extend(current)
        result.extend(current)
    return prefix_result, result


def _compare(left: list[int | None], right: list[int | None], label: str) -> str | None:
    if len(left) != len(right):
        return f"{label}: entry count mismatch"
    for index, (actual, expected) in enumerate(zip(left, right)):
        if actual != expected:
            return f"{label}: mismatch at flat entry {index}: got {actual!r}, expected {expected!r}"
    return None


def verify_width_certificate(width: int, certificate_dir: Path) -> VerificationReport:
    checks: list[str] = []
    try:
        if width not in WIDTH_PARAMETERS:
            return _fail(width, ["unsupported width"])
        certificate_dir = Path(certificate_dir)
        manifest_path = certificate_dir / "automaton_manifest.json"
        identity_path = certificate_dir / "matrix_identity.json"
        matrix_n_path = certificate_dir / "M_N.bin"
        matrix_np_path = certificate_dir / "M_N_plus_p.bin"
        for path in (manifest_path, identity_path, matrix_n_path, matrix_np_path):
            if not path.is_file():
                return _fail(width, [f"missing certificate artifact: {path.name}"], checks)

        manifest = _json(manifest_path)
        identity = _json(identity_path)
        expected_n, expected_p, expected_c = WIDTH_PARAMETERS[width]
        states = _rebuild_states(width)
        transitions = _rebuild_transitions(width, states)
        checks.append("state and transition semantics rebuilt independently")

        if manifest.get("width") != width:
            return _fail(width, ["manifest width mismatch"], checks)
        if manifest.get("states") != states:
            return _fail(width, ["manifest states differ from clean-room reconstruction"], checks)
        if manifest.get("transitions") != transitions:
            return _fail(width, ["manifest transitions differ from clean-room reconstruction"], checks)
        if manifest.get("state_count") != len(states) or manifest.get("transition_count") != len(transitions):
            return _fail(width, ["manifest count mismatch"], checks)
        if manifest.get("state_sha256") != hashlib.sha256(_state_lines(states).encode()).hexdigest():
            return _fail(width, ["state hash mismatch"], checks)
        if manifest.get("transition_sha256") != hashlib.sha256(_transition_lines(transitions).encode()).hexdigest():
            return _fail(width, ["transition hash mismatch"], checks)
        if not _strongly_connected(len(states), transitions) or manifest.get("strongly_connected") is not True:
            return _fail(width, ["strong-connectivity check failed"], checks)
        if manifest.get("producer_command") is None:
            return _fail(width, ["manifest is missing provenance command"], checks)
        checks.append("manifest records, hashes, counts, and connectivity verified")

        if identity.get("width") != width or identity.get("state_count") != len(states) or identity.get("transition_count") != len(transitions):
            return _fail(width, ["identity metadata dimensions mismatch"], checks)
        if (identity.get("N"), identity.get("p"), identity.get("c")) != (expected_n, expected_p, expected_c):
            return _fail(width, ["identity parameters differ from frozen (N,p,c)"], checks)
        if identity.get("matrix_format") != MATRIX_FORMAT:
            return _fail(width, ["unsupported matrix format"], checks)
        if identity.get("status") != ACCEPTED_STATUS or identity.get("identity_holds") is not True or identity.get("mismatch_count") != 0:
            return _fail(width, ["identity metadata is not an accepted local certificate"], checks)
        if identity.get("manifest_sha256") != _sha256(manifest_path):
            return _fail(width, ["manifest artifact hash mismatch"], checks)
        if identity.get("M_N_sha256") != _sha256(matrix_n_path) or identity.get("M_N_plus_p_sha256") != _sha256(matrix_np_path):
            return _fail(width, ["matrix artifact hash mismatch"], checks)
        checks.append("identity metadata, parameters, and SHA-256 bindings verified")

        top_level_path = certificate_dir.parent / "manifest.json"
        if not top_level_path.is_file():
            return _fail(width, ["certificate package is missing top-level manifest"], checks)
        top_level = _json(top_level_path)
        if top_level.get("status") != ACCEPTED_STATUS or top_level.get("theorem_status") != "ALL_THREE_THEOREMS_PROVED":
            return _fail(width, ["top-level certificate manifest status is invalid"], checks)
        entries = top_level.get("widths")
        if not isinstance(entries, list):
            return _fail(width, ["top-level certificate manifest has no width records"], checks)
        top_entry = next((entry for entry in entries if entry.get("width") == width), None)
        if top_entry is None:
            return _fail(width, ["top-level certificate manifest is missing width record"], checks)
        expected_top = {
            "width": width,
            "state_count": len(states),
            "transition_count": len(transitions),
            "N": expected_n,
            "p": expected_p,
            "c": expected_c,
            "automaton_manifest_sha256": _sha256(manifest_path),
            "M_N_sha256": _sha256(matrix_n_path),
            "M_N_plus_p_sha256": _sha256(matrix_np_path),
            "identity_status": ACCEPTED_STATUS,
            "identity_holds": True,
        }
        if any(top_entry.get(key) != value for key, value in expected_top.items()):
            return _fail(width, ["top-level certificate manifest binding mismatch"], checks)
        checks.append("top-level certificate manifest record and artifact hashes verified")

        dimension_n, matrix_n = _parse_matrix(matrix_n_path)
        dimension_np, matrix_np = _parse_matrix(matrix_np_path)
        if dimension_n != len(states) or dimension_np != len(states):
            return _fail(width, ["matrix dimension does not match reconstructed state count"], checks)
        checks.append("MTX1 matrices parsed with strict dimensions and tags")

        recomputed_n, recomputed_n_plus_p = _powers_from_edges(
            len(states), transitions, expected_n, expected_n + expected_p
        )
        mismatch = _compare(matrix_n, recomputed_n, "M_N")
        if mismatch:
            return _fail(width, [mismatch], checks)
        mismatch = _compare(matrix_np, recomputed_n_plus_p, "M_N_plus_p")
        if mismatch:
            return _fail(width, [mismatch], checks)
        checks.append("both persisted powers recomputed from clean-room transitions")

        for index, (base, shifted) in enumerate(zip(matrix_n, matrix_np)):
            expected = None if base is None else base + expected_c
            if shifted != expected:
                return _fail(width, [f"entrywise identity mismatch at flat entry {index}"], checks)
        checks.append("entrywise min-plus identity verified, including INF semantics")
        return VerificationReport(width, True, ACCEPTED_STATUS, tuple(checks), ())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError, struct.error) as error:
        return _fail(width, [str(error)], checks)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="verify one cylindrical total-domination certificate")
    parser.add_argument("width", type=int)
    parser.add_argument("certificate_dir", type=Path)
    arguments = parser.parse_args(argv)
    report = verify_width_certificate(arguments.width, arguments.certificate_dir)
    print(json.dumps(report.as_dict(), sort_keys=True))
    return 0 if report.accepted else 1


if __name__ == "__main__":
    sys.exit(main())
