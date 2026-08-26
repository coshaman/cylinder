from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

# Make the repository root importable under both `pytest` and `python -m pytest`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify.mutation_tests import MUTATIONS, copy_certificate


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VERIFIER = PROJECT_ROOT / "verify" / "verify_certificates.py"
CERTIFICATE = PROJECT_ROOT / "certificates" / "width5"


def run_verifier(certificate_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER), "5", str(certificate_dir)],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
    )


def test_baseline_certificate_is_accepted() -> None:
    result = run_verifier(CERTIFICATE)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("mutation_name", MUTATIONS)
def test_each_required_mutation_is_rejected(tmp_path: Path, mutation_name: str) -> None:
    certificate = copy_certificate(CERTIFICATE, tmp_path)
    MUTATIONS[mutation_name](certificate)
    result = run_verifier(certificate)
    assert result.returncode != 0, f"{mutation_name} was accepted: {result.stdout}{result.stderr}"


def test_report_is_machine_readable_and_keeps_local_status() -> None:
    result = run_verifier(CERTIFICATE)
    report = json.loads(result.stdout)
    assert report["accepted"] is True
    assert report["status"] == "TOOL_CHECKED_LOCAL"
    assert "entrywise min-plus identity verified, including INF semantics" in report["checks"]


def test_verifier_and_mutation_suite_do_not_use_producer_source() -> None:
    for path in [VERIFIER, PROJECT_ROOT / "verify" / "mutation_tests.py"]:
        text = path.read_text(encoding="utf-8")
        for forbidden in ["src/automaton", "power_identity.cpp", "manifest.cpp", "transitions.cpp"]:
            assert forbidden not in text
