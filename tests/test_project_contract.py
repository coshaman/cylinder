from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFINITIONS = PROJECT_ROOT / "mathematics" / "DEFINITIONS.md"
DESIGN = PROJECT_ROOT / "mathematics" / "PUBLIC_DESIGN.md"
PLAN = PROJECT_ROOT / "paper" / "REPRODUCIBILITY.md"
BRIEF = PROJECT_ROOT / "paper" / "manuscript.tex"


REQUIRED_DIRECTORIES = [
    PROJECT_ROOT / "paper",
    PROJECT_ROOT / "mathematics",
    PROJECT_ROOT / "results",
    PROJECT_ROOT / "certificates",
    PROJECT_ROOT / "verify",
    PROJECT_ROOT / "tests",
]

TARGET_FAMILIES = [
    "gamma_t(P_5 square C_n)",
    "gamma_t(P_6 square C_n)",
    "gamma_t(P_7 square C_n)",
]

STATUS_VOCABULARY = [
    "CONJECTURE",
    "HEURISTIC_EVIDENCE",
    "COMPUTATIONALLY_TESTED",
    "LEMMA_CONDITIONAL",
    "HUMAN_PROOF_CANDIDATE",
    "TOOL_CHECKED_LOCAL",
    "FORMALIZED_LOCAL",
    "FORMALIZED_COMPLETE",
    "REFUTED",
    "STILL_OPEN",
    "ALL_THREE_THEOREMS_PROVED",
    "TWO_WIDTH_THEOREMS_PROVED",
    "DIFFERENT_EXACT_FORMULAS_PROVED",
    "ALREADY_RESOLVED",
    "PROTOTYPE_IDENTITY_NOT_REPRODUCED",
    "MODEL_VERIFICATION_FAILED",
    "CERTIFICATE_VERIFICATION_FAILED",
    "GITHUB_PUSH_BLOCKED",
    "REVIEW_CONVERGENCE_FAILED",
]


def definitions_text() -> str:
    return DEFINITIONS.read_text(encoding="utf-8")


def status_vocabulary() -> set[str]:
    text = definitions_text()
    _, status_section = text.split("## Status Vocabulary", maxsplit=1)
    return set(re.findall(r"`([A-Z_]+)`", status_section))


def test_required_project_paths_exist() -> None:
    for directory in REQUIRED_DIRECTORIES:
        assert directory.is_dir(), f"Missing required directory: {directory}"

    for file_path in [BRIEF, DESIGN, PLAN, DEFINITIONS]:
        assert file_path.is_file(), f"Missing required file: {file_path}"


def test_definitions_freeze_widths_and_lower_bound() -> None:
    text = definitions_text()

    assert "m in {5, 6, 7}" in text
    assert "n >= 3" in text
    assert "width set = {5, 6, 7}" in text
    assert "G_{m,n} = P_m square C_n" in text
    assert "m >= 2" not in text
    assert "width set = {5, 6, 7, 8}" not in text
    assert "P_8 square C_n" not in text


def test_definitions_describe_open_neighborhood_total_domination() -> None:
    text = definitions_text()

    assert "open neighborhood" in text
    assert "Self-membership does not dominate a vertex." in text
    assert "selected vertices still require an adjacent selected neighbor" in text
    assert "N_P(S) = { i : i - 1 in S or i + 1 in S }." in text
    assert "selected vertices dominate themselves" not in text
    assert "self-domination is allowed" not in text

    for family in TARGET_FAMILIES:
        assert family in text


def test_definitions_freeze_exact_target_formulas() -> None:
    text = definitions_text()

    assert "`gamma_t(P_5 square C_n) = ceil(3n / 2) + 1` when `n mod 4 = 2`." in text
    assert "`gamma_t(P_5 square C_n) = ceil(3n / 2)` otherwise." in text

    for epsilon_line in [
        "- `epsilon_0 = 0`",
        "- `epsilon_1 = 1`",
        "- `epsilon_2 = 2`",
        "- `epsilon_3 = 0`",
        "- `epsilon_4 = 1`",
        "- `epsilon_5 = 0`",
        "- `epsilon_6 = 1`",
        "- `epsilon_7 = 0`",
        "- `epsilon_8 = 2`",
        "- `epsilon_9 = 0`",
        "- `epsilon_10 = 0`",
        "- `epsilon_11 = 1`",
        "- `epsilon_12 = 3`",
        "- `epsilon_13 = 1`",
    ]:
        assert epsilon_line in text

    assert "`gamma_t(P_6 square C_n) = ceil(12n / 7) + epsilon_{n mod 14}`" in text
    assert "`gamma_t(P_6 square C_12) = 22`." in text

    assert "`gamma_t(P_7 square C_n) = 2n`" in text
    assert "- `gamma_t(P_7 square C_7) = 15`" in text
    assert "- `gamma_t(P_7 square C_14) = 30`" in text


def test_definitions_list_exact_status_vocabulary() -> None:
    assert status_vocabulary() == set(STATUS_VOCABULARY)
