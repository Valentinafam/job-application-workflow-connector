#!/usr/bin/env bash
set -euo pipefail

CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
SKILLS_DIR="$CODEX_HOME/skills"

mkdir -p "$SKILLS_DIR"

echo "Install these upstream skills with Codex's skill installer when available:"
echo
echo "1. ApplyPilot"
echo "   Upstream: https://github.com/yvonnehe772/applypilot"
echo "   License: MIT"
echo
echo "2. LinkedIn Keyword Resume Coach"
echo "   Upstream: https://github.com/Shuboya1030/linkedin-keyword-resume-coach"
echo "   License: no explicit license was visible when this connector was prepared."
echo "   This script does not copy or redistribute its source."
echo
echo "Suggested Codex prompt:"
echo "Install yvonnehe772/applypilot and Shuboya1030/linkedin-keyword-resume-coach as local skills, then use this connector's workflow docs to link lead finding to application tracking."

