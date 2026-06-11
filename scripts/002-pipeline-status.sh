#!/usr/bin/env bash
# ============================================================
# 002-pipeline-status.sh — Document Pipeline Status
# ============================================================
# Shows completion status of all documents across all folders.
# Reads actual front matter status fields + skeleton heuristic.
# Reports counts of stable, draft, and skeleton documents.
#
# Usage: bash scripts/002-pipeline-status.sh
# Returns: 0 always (informational)
# ============================================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}════════════════════════════════════════${NC}"
echo -e "${CYAN}  zs-docs pipeline status${NC}"
echo -e "${CYAN}════════════════════════════════════════${NC}"
echo ""

TOTAL_DOCS=0
TOTAL_STABLE=0
TOTAL_DRAFT=0
TOTAL_SKELETON=0

for dir in "$ROOT_DIR"/[0-9][0-9][0-9]-*/; do
    dirname=$(basename "$dir")

    docs=()
    while IFS= read -r f; do
        basename=$(basename "$f")
        [[ "$basename" == "INDEX.md" ]] && continue
        docs+=("$f")
    done < <(find "$dir" -maxdepth 1 -name '*.md' | sort)

    total=${#docs[@]}
    stable=0
    draft=0
    skeleton=0

    for doc in "${docs[@]}"; do
        status=$(python3 -c "
import re, os
with open('$doc', 'r', encoding='utf-8', errors='replace') as fh:
    content = fh.read()
m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
if not m:
    print('skeleton'); exit()
data = {}
for line in m.group(1).split('\n'):
    kv = re.match(r'^(\w[\w-]*):\s*(.*)', line)
    if kv and kv.group(1) == 'status':
        val = kv.group(2).strip().strip('\"').strip(\"'\")
        print(val.lower() if val else 'draft')
        exit()
print('draft')
        " 2>/dev/null)

        if [ "$status" = "stable" ] || [ "$status" = "active" ]; then
            stable=$((stable + 1))
        elif [ "$status" = "skeleton" ]; then
            skeleton=$((skeleton + 1))
        else
            draft=$((draft + 1))
        fi
    done

    TOTAL_DOCS=$((TOTAL_DOCS + total))
    TOTAL_STABLE=$((TOTAL_STABLE + stable))
    TOTAL_DRAFT=$((TOTAL_DRAFT + draft))
    TOTAL_SKELETON=$((TOTAL_SKELETON + skeleton))

    if [[ $total -gt 0 ]]; then
        bar_width=20
        if [[ $stable -gt 0 ]]; then
            stable_pct=$((stable * 100 / total))
            filled=$((stable_pct * bar_width / 100))
        else
            filled=0
        fi
        bar=""
        for ((i=0; i<bar_width; i++)); do
            if [[ $i -lt $filled ]]; then
                bar="${bar}█"
            else
                bar="${bar}░"
            fi
        done

        if [[ $stable -eq $total ]]; then
            color=$GREEN
            status_label="all stable"
        elif [[ $skeleton -eq $total ]]; then
            color=$YELLOW
            status_label="all skeleton"
        elif [[ $stable -gt 0 ]]; then
            color=$CYAN
            status_label="${stable} stable, ${draft} draft"
        else
            color=$YELLOW
            status_label="${draft} draft"
        fi

        printf "  ${color}%s${NC}  %s  (%d/%d)  %s\n" \
            "$bar" "$dirname" "$((stable + draft))" "$total" "$status_label"
    fi
done

echo ""
echo -e "${CYAN}────────────────────────────────────────${NC}"
printf "  Total: %d documents  |  ${GREEN}%d stable${NC}  |  ${YELLOW}%d draft${NC}  |  ${RED}%d skeleton${NC}\n" \
    "$TOTAL_DOCS" "$TOTAL_STABLE" "$TOTAL_DRAFT" "$TOTAL_SKELETON"

if [[ $TOTAL_SKELETON -eq 0 && $TOTAL_STABLE -eq 0 ]]; then
    echo -e "  ${YELLOW}⚠ All documents are in draft — none marked stable/active${NC}"
elif [[ $TOTAL_SKELETON -eq 0 ]]; then
    echo -e "  ${GREEN}✓ No skeleton documents${NC}"
else
    echo -e "  ${YELLOW}⚠ $TOTAL_SKELETON skeleton documents remain${NC}"
fi
echo ""
