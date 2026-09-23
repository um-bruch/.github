"""Parity, inventory, and health contract tests for um-bruch organization profile."""

import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

PARITY_FILES = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "profile" / "README.md",
    REPO_ROOT / "profile" / "README_de.md",
    REPO_ROOT / "llms.txt",
    REPO_ROOT / "CHANGELOG.md",
]

PUBLIC_REPOS = [
    "verordnungsampel",
    "locuterra",
    "system-medicine",
    "multiaxial-diagnostic-system",
    "regressangst",
    ".github",
]


@pytest.fixture(scope="module")
def file_contents():
    contents = {}
    for path in PARITY_FILES:
        assert path.is_file(), f"Required file missing: {path}"
        data = path.read_bytes()
        text = data.decode("utf-8")
        assert "\ufffd" not in text, f"Invalid UTF-8 character in {path}"
        rel_key = path.relative_to(REPO_ROOT).as_posix()
        contents[rel_key] = text
    return contents


def test_files_exist_and_non_empty(file_contents):
    """Verify all core documentation files exist and have substantial content."""
    for rel_path, text in file_contents.items():
        assert len(text) > 300, f"File {rel_path} unexpectedly small ({len(text)} chars)"

    logo = REPO_ROOT / "profile" / "assets" / "um-bruch-logo.png"
    assert logo.is_file(), "Missing um-bruch logo PNG"
    assert logo.stat().st_size > 1000, "um-bruch logo PNG unexpectedly small"


def test_markdown_fence_balance(file_contents):
    """Verify that all markdown files have balanced triple backticks."""
    for filename, text in file_contents.items():
        matches = re.findall(r"^```", text, flags=re.MULTILINE)
        assert len(matches) % 2 == 0, f"Unbalanced code fences in {filename}: {len(matches)} count"


def test_public_repo_inventory(file_contents):
    """Verify that all 6 public repositories are documented across primary profile files."""
    for filename in ["README.md", "profile/README.md", "profile/README_de.md", "llms.txt"]:
        text = file_contents[filename]
        for repo in PUBLIC_REPOS:
            assert repo in text, f"Missing public repo '{repo}' in {filename}"


def test_check_timestamp_parity(file_contents):
    """Verify that verification timestamps are synchronized to 2026-09-23."""
    assert "2026-09-23" in file_contents["README.md"]
    assert "<!-- last-checked: 2026-09-23 -->" in file_contents["profile/README.md"]
    assert "<!-- last-checked: 2026-09-23 -->" in file_contents["profile/README_de.md"]
    assert "## Last-checked: 2026-09-23" in file_contents["llms.txt"]
    assert "2026-09-23" in file_contents["CHANGELOG.md"]


def test_push_timestamp_parity(file_contents):
    """Verify that latest push timestamps match repository live metadata."""
    for filename in ["README.md", "profile/README.md", "profile/README_de.md", "llms.txt", "CHANGELOG.md"]:
        text = file_contents[filename]
        assert "2026-08-25" in text or "25.08.2026" in text, f"Missing locuterra push date in {filename}"
        assert "2026-08-21" in text or "21.08.2026" in text, f"Missing system-medicine push date in {filename}"
        assert "2026-09-20" in text or "20.09.2026" in text, f"Missing verordnungsampel push date in {filename}"
        assert "2026-08-05" in text or "05.08.2026" in text, f"Missing multiaxial push date in {filename}"
        assert "2026-07-27" in text or "27.07.2026" in text, f"Missing regressangst push date in {filename}"
        assert "2026-09-20" in text or "20.09.2026" in text, f"Missing .github push date in {filename}"


def test_ecosystem_cross_linking(file_contents):
    """Verify that sister organizations are properly linked."""
    ecosystem_orgs = [
        "open-bricks",
        "research-line",
        "ellmos-ai",
        "doc-bricks",
        "dev-bricks",
        "file-bricks",
        "entertain-and-more",
        "assistassets-ai",
        "um-bruch",
        "lukisch",
    ]
    for org in ecosystem_orgs:
        assert org in file_contents["profile/README.md"], f"Missing ecosystem org '{org}' in English profile"
        assert org in file_contents["profile/README_de.md"], f"Missing ecosystem org '{org}' in German profile"
        assert org in file_contents["llms.txt"], f"Missing ecosystem org '{org}' in llms.txt"


def test_research_use_boundary_disclaimer(file_contents):
    """Verify that Research Use Only boundary is stated."""
    assert "Research-Use Boundary" in file_contents["profile/README.md"]
    assert "Forschungsvorbehalt" in file_contents["profile/README_de.md"]
    assert "not medical advice or certified medical devices under EU MDR" in file_contents["llms.txt"]


def test_no_forbidden_local_paths(file_contents):
    """Ensure no local developer filesystem paths leak into public profile files."""
    forbidden = [
        r"C:\Users",
        "C:/Users",
        r"C:\_Local_DEV",
        "C:/_Local_DEV",
        "OneDrive",
    ]
    for filename, text in file_contents.items():
        for pattern in forbidden:
            assert pattern not in text, f"Forbidden local path '{pattern}' leaked into {filename}"
