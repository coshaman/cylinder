"""Deterministic certificate mutations used by the Task 8 rejection suite."""

from __future__ import annotations

import json
import hashlib
import shutil
import struct
from pathlib import Path
from typing import Callable


Mutation = Callable[[Path], None]


def copy_certificate(source: Path, destination_parent: Path) -> Path:
    destination = destination_parent / source.name
    shutil.copytree(source, destination)
    shutil.copy2(source.parent / "manifest.json", destination_parent / "manifest.json")
    return destination


def _update_manifest(certificate: Path, edit: Callable[[dict], None]) -> None:
    path = certificate / "automaton_manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    edit(data)
    path.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")


def _edit_matrix_entry(path: Path, entry: int, value: int | None) -> None:
    raw = bytearray(path.read_bytes())
    offset = 16
    for _ in range(entry):
        tag = raw[offset]
        offset += 1 + (8 if tag == 1 else 0)
    old_tag = raw[offset]
    old_size = 1 + (8 if old_tag == 1 else 0)
    if value is None:
        raw[offset : offset + old_size] = b"\x00"
    elif old_tag == 1:
        raw[offset] = 1
        raw[offset + 1 : offset + 9] = struct.pack("<q", value)
    else:
        raw[offset : offset + old_size] = b"\x01" + struct.pack("<q", value)
    path.write_bytes(raw)


def delete_transition(certificate: Path) -> None:
    _update_manifest(certificate, lambda data: data["transitions"].pop())


def insert_transition(certificate: Path) -> None:
    _update_manifest(certificate, lambda data: data["transitions"].append(data["transitions"][0]))


def reweight_transition(certificate: Path) -> None:
    def edit(data: dict) -> None:
        data["transitions"][0][2] += 1

    _update_manifest(certificate, edit)


def corrupt_state_mask(certificate: Path) -> None:
    def edit(data: dict) -> None:
        data["states"][0][1] = 1

    _update_manifest(certificate, edit)


def alter_finite_matrix_entry(certificate: Path) -> None:
    path = certificate / "M_N.bin"
    _edit_matrix_entry(path, 0, 1)
    _bind_mutated_matrix_hash(certificate, path)


def alter_infinite_matrix_entry(certificate: Path) -> None:
    # The persisted width-5/6/7 matrices have no INF entries.  This mutation
    # exercises the same tagged-entry boundary by changing a finite entry to INF.
    path = certificate / "M_N.bin"
    _edit_matrix_entry(path, 0, None)
    _bind_mutated_matrix_hash(certificate, path)


def _bind_mutated_matrix_hash(certificate: Path, matrix: Path) -> None:
    identity = certificate / "matrix_identity.json"
    data = json.loads(identity.read_text(encoding="utf-8"))
    data["M_N_sha256"] = hashlib.sha256(matrix.read_bytes()).hexdigest()
    identity.write_text(json.dumps(data), encoding="utf-8")


def alter_matrix_dimension(certificate: Path) -> None:
    path = certificate / "M_N.bin"
    raw = bytearray(path.read_bytes())
    raw[8:16] = struct.pack("<Q", 168)
    path.write_bytes(raw)


def alter_identity_parameters(certificate: Path) -> None:
    path = certificate / "matrix_identity.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["N"] = 17
    path.write_text(json.dumps(data), encoding="utf-8")


MUTATIONS: dict[str, Mutation] = {
    "deleted transition": delete_transition,
    "inserted transition": insert_transition,
    "reweighted transition": reweight_transition,
    "corrupted state mask": corrupt_state_mask,
    "altered finite matrix entry": alter_finite_matrix_entry,
    "altered infinite matrix entry": alter_infinite_matrix_entry,
    "altered matrix dimension": alter_matrix_dimension,
    "altered (N,p,c)": alter_identity_parameters,
}


__all__ = ["MUTATIONS", "copy_certificate"]
