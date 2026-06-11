#!/usr/bin/env bash
# ============================================================
# 003-resolve-cross-refs.sh — Cross-Reference Validator
# ============================================================
# Delegates to fast Python implementation.
#
# Usage: bash scripts/003-resolve-cross-refs.sh
# Returns: 0 if all refs resolve, 1 if any broken refs found
# ============================================================

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Prefer Python3 implementation (much faster)
PY_SCRIPT="$ROOT_DIR/scripts/003-resolve-cross-refs.py"
if command -v python3 &>/dev/null && [[ -f "$PY_SCRIPT" ]]; then
    exec python3 "$PY_SCRIPT"
fi

# ============================================================
# Fallback: original bash implementation (slower)
# Only used if Python is not available
# ============================================================

set -euo pipefail
EXIT_CODE=0
PASS=0
FAIL=0
SKIP=0

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'
pass() { PASS=$((PASS + 1)); echo -e "  ${GREEN}✓${NC} $1"; }
fail() { FAIL=$((FAIL + 1)); echo -e "  ${RED}✗${NC} $1"; EXIT_CODE=1; }
skip() { SKIP=$((SKIP + 1)); echo -e "  ${YELLOW}⊘${NC} $1"; }
section() { echo -e "\n${CYAN}═══ $1 ═══${NC}"; }

resolve_target() {
    local source_file="$1" target="$2" dirpath
    dirpath=$(dirname "$source_file")
    local file_target="${target%%#*}"; file_target="${file_target%%§*}"
    file_target="${file_target#"${file_target%%[![:space:]]*}"}"
    file_target="${file_target%"${file_target##*[![:space:]]}"}"
    [[ -z "$file_target" ]] && return 0
    if echo "$file_target" | grep -qE '^https?://'; then skip "External in $(basename "$source_file"): $file_target"; return 0; fi
    if echo "$file_target" | grep -qE '^/'; then skip "Absolute in $(basename "$source_file"): $file_target"; return 0; fi
    if echo "$file_target" | grep -qE '^zs-'; then skip "Cross-repo in $(basename "$source_file"): $file_target"; return 0; fi
    if echo "$(basename "$file_target")" | grep -qiE 'filename|example|template|your-|old-name|new-name'; then skip "Template in $(basename "$source_file"): $file_target"; return 0; fi

    local resolved="$dirpath/$file_target"
    if [[ -f "$resolved" ]]; then pass "$(basename "$source_file") → $file_target"; return 0; fi
    local root_resolved="$ROOT_DIR/$file_target"
    if [[ -f "$root_resolved" ]]; then pass "$(basename "$source_file") → $file_target (root-relative)"; return 0; fi
    fail "$(basename "$source_file") → $file_target (not found)"; return 1
}

DOC_FOLDERS=$(find "$ROOT_DIR"/00[0-9]-*/ -maxdepth 0 -type d 2>/dev/null | sort)

section "1. Markdown link references"
while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    filepath="${line%%:*}"; rest="${line#*:}"; rest="${rest#*:}"
    echo "$rest" | grep -oP '(?<=\]\().+?\.md[^)]*' 2>/dev/null | while IFS= read -r target; do
        [[ -z "$target" ]] && continue
        resolve_target "$filepath" "$target"
    done
done < <(grep -rnP '\]\([^)]*\.md' $DOC_FOLDERS --include='*.md' 2>/dev/null)

section "2. ZUSS cross-reference notation"
while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    filepath="${line%%:*}"; content="${line#*:}"; content="${content#*:}"
    between=$(echo "$content" | grep -oP '→\s+\*\*\K[^*]*(?=\*\*)' 2>/dev/null || true)
    [[ -z "$between" ]] && continue
    echo "$between" | grep -q '(' 2>/dev/null && continue
    echo "$between" | grep -oP '[^\s]+\.md[^*]*' 2>/dev/null | while IFS= read -r target; do
        [[ -z "$target" ]] && continue
        echo "$target" | grep -q '^\[' && continue
        resolve_target "$filepath" "$target"
    done
done < <(grep -rnP '→\s+\*\*[^*]*\.md' $DOC_FOLDERS --include='*.md' 2>/dev/null)

section "3. Wikilink-style cross-references"
while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    filepath="${line%%:*}"; content="${line#*:}"; content="${content#*:}"
    echo "$content" | grep -oP '(?<=\[\[)[^\]]+\.md[^\]]*(?=\]\])' 2>/dev/null | while IFS= read -r target; do
        [[ -z "$target" ]] && continue
        resolve_target "$filepath" "$target"
    done
done < <(grep -rnP '\[\[[^\]]*\.md' $DOC_FOLDERS --include='*.md' 2>/dev/null)

echo ""
echo -e "${CYAN}════════════════════════════════════════${NC}"
echo -e "${CYAN}  Cross-reference summary${NC}"
echo -e "${CYAN}════════════════════════════════════════${NC}"
echo -e "  ${GREEN}Resolved:${NC} $PASS"
echo -e "  ${RED}Broken:${NC} $FAIL"
echo -e "  ${YELLOW}Skipped:${NC} $SKIP"
echo ""
[[ $EXIT_CODE -eq 0 ]] && echo -e "${GREEN}✓ All cross-references resolve.${NC}" || echo -e "${RED}✗ $FAIL broken cross-references found.${NC}"
exit $EXIT_CODE
