#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-private}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$TARGET/dashboard" "$TARGET/resumes" "$TARGET/cover_letters/templates" "$TARGET/cover_letters/generated"

cp "$ROOT_DIR/templates/candidate_profile.template.json" "$TARGET/candidate_profile.json"
cp "$ROOT_DIR/templates/application_rules.template.md" "$TARGET/application_rules.md"
cp "$ROOT_DIR/templates/resume_routing.template.md" "$TARGET/resume_routing.md"
cp "$ROOT_DIR/templates/answer_bank.template.md" "$TARGET/answer_bank.md"
cp "$ROOT_DIR"/dashboard/*.csv "$TARGET/dashboard/"

echo "Private workflow workspace initialized at: $TARGET"
echo "Fill this workspace with real candidate data. Do not commit it."

