#!/usr/bin/env bash
# ============================================================
# 001-zuss-validate.sh — ZUSS Compliance Validator
# ============================================================
# Validates all .md files in zs-docs for:
#   1. File naming (nnn-descriptive-name.md)
#   2. Sequential numbering within folders (no gaps)
#   3. YAML front matter presence and required fields
#   4. License footer presence and correctness
#   5. Banned words
#   6. Sentence case on headings
#   7. No latest tag references
#
# Usage: bash scripts/001-zuss-validate.sh
# Returns: 0 if all checks pass, 1 if any fail
# ============================================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
EXIT_CODE=0
PASS=0
FAIL=0
WARN=0

# --------------- Colors ---------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# --------------- Helpers ---------------
pass() { PASS=$((PASS + 1)); echo -e "  ${GREEN}✓${NC} $1"; }
fail() { FAIL=$((FAIL + 1)); echo -e "  ${RED}✗${NC} $1"; EXIT_CODE=1; }
warn() { WARN=$((WARN + 1)); echo -e "  ${YELLOW}⚠${NC} $1"; }
section() { echo -e "\n${CYAN}═══ $1 ═══${NC}"; }

# --------------- 1. File naming ---------------
section "1. File naming (nnn-descriptive-name.md)"

# Exclude INDEX.md files, scripts/, and AGENTS/README/TODO/llms.txt
INVALID_NAMES=0
while IFS= read -r f; do
    basename=$(basename "$f")
    [[ "$basename" == "INDEX.md" ]] && continue
    [[ "$basename" == "AGENTS.md" ]] && continue
    [[ "$basename" == "README.md" ]] && continue
    [[ "$basename" == "TODO.md" ]] && continue
    [[ "$basename" == "llms.txt" ]] && continue
    if ! echo "$basename" | grep -qE '^[0-9]{3}-[a-z0-9]+(-[a-z0-9]+)*\.md$'; then
        fail "Naming violation: $f"
        INVALID_NAMES=$((INVALID_NAMES + 1))
    fi
done < <(find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort)

[[ $INVALID_NAMES -eq 0 ]] && pass "All non-index files match nnn-descriptive-name.md pattern"

# --------------- 2. Sequential numbering ---------------
section "2. Sequential numbering (no gaps)"

find "$ROOT_DIR" -maxdepth 2 -type d -name '[0-9][0-9][0-9]-*' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort | while IFS= read -r dir; do
    dirname=$(basename "$dir")
    # Get all numbered files in this directory (exclude INDEX.md)
    numbers=$(find "$dir" -maxdepth 1 -name '*.md' -not -name 'INDEX.md' | sort | sed -n 's/.*\/\([0-9]\{3\}\)-.*/\1/p')
    
    expected=1
    gap_found=0
    for num in $numbers; do
        # Strip leading zeros for comparison
        num_int=$((10#$num))
        if [[ $num_int -ne $expected ]]; then
            fail "Gap in $dirname: expected $expected, found $num"
            gap_found=1
        fi
        expected=$((expected + 1))
    done
    if [[ $gap_found -eq 0 ]]; then
        highest=$(echo "$numbers" | tail -1)
        pass "$dirname: sequential (001-$highest)"
    fi
done

# --------------- 3. YAML front matter ---------------
section "3. YAML front matter"

while IFS= read -r f; do
    basename=$(basename "$f")
    # Skip informational root files that don't need YAML front matter
    case "$basename" in
        AGENTS.md|README.md|TODO.md) continue ;;
    esac
    
    # Check file directly (avoid pipefail + grep -q SIGPIPE issue)
    first=$(head -1 "$f")
    if [[ "$first" != "---" ]]; then
        fail "$basename: missing YAML front matter (no opening ---)"
        continue
    fi
    
    # Check for closing --- using here-string (pipe-safe)
    if ! grep -q '^---' <<< "$(tail -n +2 "$f")"; then
        fail "$basename: missing YAML front matter (no closing ---)"
        continue
    fi
    
    # Extract YAML block
    yaml=$(sed -n '1,/^---/p' "$f" | sed '1d;$d')
    
    # Check required fields (INDEX.md has different requirements)
    if [[ "$basename" == INDEX.md ]]; then
        for field in "id:" "title:" "domain:" "doc-type:" "summary:" "entity-type:"; do
            if ! grep -q "$field" <<< "$yaml"; then
                fail "$basename: missing required YAML field: $field"
            fi
        done
    else
        for field in "id:" "title:" "domain:" "doc-type:" "entity-type:" "summary:" "version:" "status:" "last_updated:" "isolation_tier:" "capabilities:" "audience:"; do
            if ! grep -q "$field" <<< "$yaml"; then
                fail "$basename: missing required YAML field: $field"
            fi
        done
    fi
done < <(find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort)

# --------------- 4. License footer ---------------
section "4. License footer"

while IFS= read -r f; do
    basename=$(basename "$f")
    
    if ! grep -q "ZarishSphere Foundation" "$f"; then
        fail "$basename: missing license footer (no 'ZarishSphere Foundation')"
    fi
    if ! grep -q "Apache 2.0 (code) · CC BY 4.0 (documentation)" "$f"; then
        fail "$basename: license footer incorrect (wrong license text)"
    fi
    if ! grep -q "github.com/zarishsphere" "$f"; then
        fail "$basename: license footer missing GitHub link"
    fi
done < <(find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort)

# --------------- 5. Banned words ---------------
section "5. Banned words"

while IFS= read -r f; do
    basename=$(basename "$f")
    if grep -q -i -w 'genuinely\|honestly\|straightforward' "$f"; then
        fail "$basename: contains banned word(s): genuinely, honestly, or straightforward"
    fi
done < <(find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort)

# --------------- 6. Sentence case on headings ---------------
section "6. Heading case (sentence case)"

while IFS= read -r f; do
    basename=$(basename "$f")
    while IFS= read -r line; do
        # Skip numbered headings like "## 1. Title" - those are allowed
        if grep -qE '^[0-9]+\.' <<< "$line"; then
            continue
        fi
        # Check if subsequent words start with uppercase (heuristic for non-sentence-case)
        if echo "$line" | grep -qE '\b[A-Z][a-z]{2,}\b'; then
            warn "$basename: possible non-sentence-case heading: '$line'"
        fi
    done < <(grep -E '^##[^#]' "$f" 2>/dev/null || true)
done < <(find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort)

# --------------- 7. No latest tag ---------------
section "7. No 'latest' tag references"

while IFS= read -r f; do
    basename=$(basename "$f")
    # Check for 'latest' outside backtick context (inline code) and outside fenced code blocks
    # Extract lines containing 'latest', filter out lines where it's inside backticks
    if python3 -c "
import sys, re
with open('$f', 'r') as fh:
    content = fh.read()
# Remove fenced code blocks
content = re.sub(r'\x60\x60\x60.*?\x60\x60\x60', '', content, flags=re.DOTALL)
content = re.sub(r'\x60\x60.*?\x60\x60', '', content, flags=re.DOTALL)
# Remove inline backtick code
content = re.sub(r'\x60[^\x60]*?\x60', '', content)
# Now check for remaining 'latest'
if re.search(r'\blatest\b', content, re.IGNORECASE):
    sys.exit(1)
" 2>/dev/null; then
        :
    else
        fail "$basename: contains 'latest' tag reference (forbidden by ZUSS)"
    fi
done < <(find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/_raw/*' -not -path '*/.opencode/*' -not -name 'PRD_zs-ui-*.md' | sort)

# Wait for background processes
wait

# --------------- Summary ---------------
echo ""
echo -e "${CYAN}════════════════════════════════════════${NC}"
echo -e "${CYAN}  Validation summary${NC}"
echo -e "${CYAN}════════════════════════════════════════${NC}"
echo -e "  ${GREEN}Passed:${NC} $PASS"
echo -e "  ${RED}Failed:${NC} $FAIL"
echo -e "  ${YELLOW}Warnings:${NC} $WARN"
echo ""

if [[ $EXIT_CODE -eq 0 ]]; then
    echo -e "${GREEN}✓ All ZUSS compliance checks passed.${NC}"
else
    echo -e "${RED}✗ $FAIL checks failed. Review issues above.${NC}"
fi

exit $EXIT_CODE
