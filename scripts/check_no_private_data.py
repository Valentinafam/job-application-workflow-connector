#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "private"}
SKIP_SUFFIXES = {".pdf", ".docx", ".png", ".jpg", ".jpeg", ".zip", ".pyc"}

PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone_like": re.compile(r"(\+?\d[\d\s().-]{7,}\d)"),
    "mac_user_path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "linkedin_job_url": re.compile(r"https?://(www\.)?linkedin\.com/jobs/view/\d+", re.I),
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() not in SKIP_SUFFIXES:
            yield path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings: list[str] = []
    custom_terms_path = root / "private_patterns.txt"
    custom_terms: list[str] = []
    if custom_terms_path.exists():
        custom_terms = [
            line.strip()
            for line in custom_terms_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]

    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(root)
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(f"{rel}: {label}: {match.group(0)[:120]}")
        for term in custom_terms:
            if term.lower() in text.lower():
                findings.append(f"{rel}: custom_private_term: {term[:120]}")

    if findings:
        print("Potential private data found:")
        for item in findings:
            print(f"- {item}")
        return 1

    print("No obvious private data patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
