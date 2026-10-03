from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINAL = "--final" in sys.argv
errors: list[str] = []

contracts = [ROOT / "contracts/termlock.py", ROOT / "contracts/commitment_gate.py"]
required_files = [
    ROOT / "README.md",
    ROOT / "SUBMISSION.md",
    ROOT / "DEPLOYMENT.md",
    ROOT / "BUILD_STATUS.md",
    ROOT / "docs/ARCHITECTURE.md",
    ROOT / "docs/INVARIANTS.md",
    ROOT / "docs/SECURITY.md",
    ROOT / "tests/test_termlock.py",
    ROOT / "tests/test_source_invariants.py",
    ROOT / "tests/test_live_studionet.py",
    ROOT / "fixtures/party_a_terms.txt",
    ROOT / "fixtures/party_b_terms.txt",
]

for p in required_files:
    if not p.exists():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

for p in contracts:
    if not p.exists():
        errors.append(f"missing {p.relative_to(ROOT)}")
        continue
    src = p.read_text(encoding="utf-8")
    try:
        ast.parse(src)
    except SyntaxError as exc:
        errors.append(f"syntax error in {p.name}: {exc}")
    if "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" not in src:
        errors.append(f"unexpected dependency pin in {p.name}")

core = (ROOT / "contracts/termlock.py").read_text(encoding="utf-8")
core_markers = [
    "run_nondet_unsafe",
    "response_format=\"json\"",
    "submit_terms",
    "assess_current_round",
    "approve_current_assessment",
    "lock_agreement",
    "assessed_a_hash",
    "a_approved_assessment",
    "b_approved_assessment",
    "TERMLOCK_SCHEMA_V1",
    "TERMLOCK_ASSESSMENT_V1",
    "TERMLOCK_LOCK_V1",
    "model returned duplicate dimension",
    "current submissions already assessed",
    "identical Party A terms already current",
]
for marker in core_markers:
    if marker not in core:
        errors.append(f"missing core marker: {marker}")

consumer = (ROOT / "contracts/commitment_gate.py").read_text(encoding="utf-8")
for marker in [
    "@gl.contract_interface",
    ".view().is_locked",
    "expected_lock_hash must be 64 hex",
    "action already consumed",
    "CommitmentGate",
]:
    if marker not in consumer:
        errors.append(f"missing consumer marker: {marker}")

if (ROOT / "frontend").exists():
    errors.append("frontend directory present")

for p in ROOT.rglob("*"):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if p.name in {".env", "id_rsa", "id_ed25519"}:
        errors.append(f"sensitive file present: {rel}")
    if any(part in {".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"} for part in rel.parts):
        errors.append(f"generated/cache directory present: {rel}")
    if p.suffix in {".pyc", ".pyo"}:
        errors.append(f"compiled artifact present: {rel}")

# Network references must not drift to Studio preview.
network_text = "\n".join(
    p.read_text(encoding="utf-8", errors="ignore")
    for p in ROOT.rglob("*")
    if p.is_file() and p.resolve() != Path(__file__).resolve() and p.name != "pin_fixture_commit.py" and p.suffix in {".md", ".py", ".yaml", ".yml", ".txt"}
)
if "studio-dev.genlayer.com/api" in network_text or re.search(r"\b61997\b", network_text):
    errors.append("preview Studio network reference found; stable Studionet 61999 is required")
if "https://studio.genlayer.com/api" not in network_text:
    errors.append("stable Studionet RPC reference missing")
if "61999" not in network_text:
    errors.append("stable Studionet chain ID reference missing")

if FINAL:
    # This marker is intentionally named in verification guidance and in the
    # pinning helper. Check the published fixture references themselves so the
    # checklist can state what the final gate rejects without tripping it.
    fixture_reference_files = [
        ROOT / "tests/test_live_studionet.py",
        ROOT / "fixtures/README.md",
    ]
    if any(
        "FIXTURE_COMMIT_PLACEHOLDER" in p.read_text(encoding="utf-8")
        for p in fixture_reference_files
        if p.exists()
    ):
        errors.append("fixture commit placeholder remains")
    dep = (ROOT / "DEPLOYMENT.md").read_text(encoding="utf-8")
    if "PENDING" in dep:
        errors.append("DEPLOYMENT.md still contains PENDING proof")
    if "NOT RUN" in dep or "UNVERIFIED" in dep:
        errors.append("DEPLOYMENT.md still contains unverified proof markers")

if errors:
    print("PREFLIGHT FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("PREFLIGHT PASS")
print(" - required repository files present")
print(" - contract Python parses")
print(" - stable dependency pin present")
print(" - consensus/revision/approval/consumer markers present")
print(" - no frontend directory")
print(" - no obvious sensitive/generated artifacts")
print(" - stable Studionet / chain 61999 references present")
if not FINAL:
    print(" - handoff mode: deployment placeholders permitted")
