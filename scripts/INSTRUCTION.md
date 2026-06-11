# INSTRUCTION.md — Scripts reference for zs-docs

This document describes every script in `scripts/`, when to run each one, how to
interpret its output, what to do next based on the results, and the exact scope
of files each script touches.

---

## Important: scope of all scripts

All scripts in this folder are **documentation-only**. They scan only:

- The 10 documentation folders: `001-meta/` through `010-ecosystem/`
- Root documentation files: `INDEX.md`, `AGENTS.md`, `README.md`, `TODO.md`, `llms.txt`

They **never** scan or modify:

- `.opencode/` — agent definitions, skill files, MCP server, configuration
- `node_modules/` — dependency directories
- `.git/` — Git metadata (when initialised)
- `scripts/` — the scripts themselves
- Any hidden files or folders starting with `.`

This isolation ensures the validation pipeline can be run safely at any time
without impacting the agent ecosystem, opencode configuration, or MCP setup.

---

## Quick reference

| Script | What it does | When to run |
|---|---|---|
| `010-refresh-files.py` | Normalise labels, regenerate INDEX.md + llms.txt, fix footers | After adding/changing any .md file |
| `001-zuss-validate.sh` | ZUSS compliance: naming, numbering, YAML, footers, banned words, headings, `latest` tags | After `refresh`, before any push |
| `002-pipeline-status.sh` | Document completion status by folder | Any time (informational) |
| `003-resolve-cross-refs.sh` | Validate all `→` cross-references resolve to existing files | Any time, especially after renames |
| `004-zarishsphere-init.sh` | Create and push all ZarishSphere GitHub repositories | Before first GitHub push |

---

## Run order before every push

1. `python3 scripts/010-refresh-files.py`
2. `bash scripts/001-zuss-validate.sh`
3. `bash scripts/002-pipeline-status.sh`
4. `bash scripts/003-resolve-cross-refs.sh`

If all pass without `✗` failures, the repo is ready for commit.

---

## 1. `010-refresh-files.py` — Refresh all generated files

**Path:** `scripts/010-refresh-files.py`
**Run:** `python3 scripts/010-refresh-files.py`
**Takes:** ~1–3 seconds
**Idempotent:** Yes — second run changes nothing if nothing has changed.
**Exit code:** 0 always (warnings printed to stdout)

### What it does (4 steps)

#### Step 1 — Normalize front matter labels
- **Scan scope:** 36 known files in `004-zarish-index/`, `005-zarish-standards/`, `006-infrastructure/`, `007-tech-stack/`, `008-adrs/`, `009-operations/`, and `001-meta/004-writing-rules.md`
- Adds any missing required front matter fields: `doc-type`, `entity-type`, `summary`, `tags`, `audience`
- **Never overwrites** existing values — only adds missing fields
- Uses `iter_md_files()` which only scans folders matching the `\d{3}-` pattern — automatically skips `.opencode/`, `scripts/`, and any non-document directories

#### Step 2 — Generate INDEX.md files
- **Scan scope:** All `.md` files in folders `001-meta/` through `010-ecosystem/`
- Regenerates INDEX.md for all 10 folders plus root INDEX.md
- Reads actual file metadata from YAML front matter (title, summary, status)
- The file table, descriptions, and status are always current
- INDEX.md lists every primary document with its title, summary, and status

#### Step 3 — Generate llms.txt
- **Scan scope:** Same as Step 2
- Regenerates `llms.txt` from file front matter summaries
- Grouped by folder with one-line descriptions per file
- Designed for AI-agent consumption (used as the third file in the instruction chain)

#### Step 4 — Fix license footers
- **Scan scope:** Same as Step 2 + root files (`INDEX.md`, `AGENTS.md`, `README.md`, `TODO.md`)
- Ensures every `.md` file ends with the canonical 3-line license footer:
  ```
  *ZarishSphere Foundation · V1 · {current date}*
  *License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
  *GitHub: https://github.com/zarishsphere*
  ```
- Detects and removes: duplicate footers, stale license text, non-canonical variants, stale cross-reference lines

### Expected output

```
  OK    <folder>/<file>.md         ← file already correct, no change
  FIX   <folder>/<file>.md         ← file was repaired (new field, footer, etc.)
  UPDATE <folder>/INDEX.md         ← INDEX.md regenerated (content changed)
```

At the end:
```
  Fixed: N, Already OK: M          ← step 1 summary
  Updated: N, Unchanged: M         ← step 2 summary
  All steps complete.
```

### Next steps based on output

| If you see… | Then… |
|---|---|
| `FIX` on any file | Run `010-refresh-files.py` again to confirm it stabilises, then run `001-zuss-validate.sh` |
| Only `OK` and `UPDATE` | Run `001-zuss-validate.sh` to confirm zero compliance failures |
| Errors/stack trace | File may have malformed YAML. Check the mentioned file's front matter. |

### Internal architecture

The script uses a generator function `iter_md_files()` (line 131) that:
1. Lists all folders at the repository root matching `^\d{3}-` (e.g., `001-meta`, `010-ecosystem`)
2. Within each folder, collects all `.md` files (optionally skipping INDEX.md)
3. Also includes root-level files: `INDEX.md`, `AGENTS.md`, `README.md`, `TODO.md`
4. This pattern naturally excludes `.opencode/`, `scripts/`, `node_modules/`, and any other directory without a `\d{3}-` prefix

The front matter parser (line 52) is a lightweight YAML parser that handles:
- Simple key-value pairs (`key: value`)
- Block scalars with `>-` (folded) and `|` (literal)
- Arrays with `- ` list items
- JSON inline arrays `[item1, item2]`

---

## 2. `001-zuss-validate.sh` — ZUSS compliance validator

**Path:** `scripts/001-zuss-validate.sh`
**Run:** `bash scripts/001-zuss-validate.sh`
**Takes:** ~2–5 seconds
**Exit code:** 0 = all pass, 1 = failures exist

### What it checks (7 checks in sequence)

| # | Check | What it validates | Failures expected? |
|---|---|---|---|
| 1 | File naming | Every `.md` file matches `nnn-descriptive-name.md` (lowercase, hyphens, 3-digit prefix). INDEX.md, AGENTS.md, README.md, TODO.md, llms.txt are exempt. | 0 — all must pass |
| 2 | Sequential numbering | Within each folder, numbers run 001–N with no gaps. INDEX.md is skipped. | 0 — no gaps allowed |
| 3 | YAML front matter | Every document has `---` delimiters and 12 required fields. INDEX.md has a shorter field set (6 fields). | 0 — all must pass |
| 4 | License footer | Every file ends with the canonical 3-line footer. | 0 — all must pass |
| 5 | Banned words | No occurrences of "genuinely", "honestly", "straightforward". | 0 — zero tolerance |
| 6 | Heading case | Heuristic check for non-sentence-case headings. | Advisory only |
| 7 | No `latest` tag | No bare `latest` references outside code blocks/backtick context. | 0 — strict enforcement |

### File scan logic

The script uses `find` commands with the following exclusion patterns:

```bash
find "$ROOT_DIR" -name '*.md' \
  -not -path '*/scripts/*' \
  -not -path '*/.git/*' \
  -not -path '*/_raw/*' \
  -not -path '*/.opencode/*' \
  -not -name 'PRD_zs-ui-*.md'
```

This ensures:
- `scripts/` — the scripts themselves are never validated
- `.git/` — Git metadata is never scanned
- `_raw/` — raw source files are skipped
- `.opencode/` — agent definitions, skill files, MCP server are never validated
- Files matching `PRD_zs-ui-*.md` are skipped

### Expected output

```
═══ 1. File naming ═══
  ✓ All non-index files match pattern

═══ 2. Sequential numbering ═══
  ✓ 001-meta: sequential (001-007)
  ✓ 002-foundation: sequential (001-004)
  ...

═══ 3. YAML front matter ═══
  ✓ 001-zarishsphere-constitution.md

═══ 4. License footer ═══
  (no output = all pass)

═══ 5. Banned words ═══
  (no output = all pass)

═══ 6. Heading case ═══
  ⚠  (warnings are advisory, not failures)

═══ 7. No latest tag ═══
  (no output = all pass)
```

### Next steps based on output

| If you see… | Then… |
|---|---|
| All sections pass, exit 0 | Documentation is compliant. Run `002-pipeline-status.sh` for status overview. |
| `✗` on any check | Read the specific file and fix the reported issue. Re-run to confirm. |
| Warnings on heading case | Advisory only — check if the flagged heading is intentional (e.g., proper noun). |
| `✗` on YAML front matter | Run `010-refresh-files.py` first — it may fix missing fields. |

### Check 1: File naming (lines 39-57)

The naming check iterates over all `.md` files (excluding exempted paths) and
validates each filename matches the regex `^[0-9]{3}-[a-z0-9]+(-[a-z0-9]+)*\.md$`.
This enforces the ZUSS rule: 3-digit prefix, lowercase, hyphens only.

INDEX.md is the only allowed exception for non-prefixed names.

### Check 2: Sequential numbering (lines 59-82)

For each folder matching `[0-9][0-9][0-9]-*` (at depth 2), extracts the numeric
prefix from each `.md` file (excluding INDEX.md) and verifies there are no gaps.
Numbers must start at 001 and increment by exactly 1.

Example failure: if a folder has files `001-foo.md` and `003-bar.md`, the
validator reports a gap at expected `002`.

### Check 3: YAML front matter (lines 84-124)

For each `.md` file (skipping AGENTS.md, README.md, TODO.md):
1. Checks the first line is `---` (YAML opening delimiter)
2. Checks for a closing `---` delimiter
3. Extracts the YAML block between delimiters
4. For INDEX.md: checks 6 required fields (id, title, domain, doc-type, summary, entity-type)
5. For all other docs: checks 12 required fields (id, title, domain, doc-type, entity-type, summary, version, status, last_updated, isolation_tier, capabilities, audience)

### Check 4: License footer (lines 126+)

Checks that each file ends with the canonical 3-line footer block.
Uses grep to find the Foundation name line and verifies the footer structure.

### Check 5: Banned words (lines after footer check)

Searches all `.md` files for the exact strings "genuinely", "honestly",
"straightforward" (case-insensitive). These words are banned by ZUSS for
professional tone enforcement.

### Check 6: Heading case (lines after banned words)

Uses a heuristic to detect headings that may not use sentence case.
All `##` and `###` headings are checked. Warnings indicate possible violations
but these are advisory — proper nouns and technical terms may legitimately use
non-sentence-case.

### Check 7: No latest tag (lines after heading check)

Searches for the word "latest" outside of code blocks and backtick-delimited
inline code. This enforces the ZUSS rule that versions must be explicitly pinned.

---

## 3. `002-pipeline-status.sh` — Document completion status

**Path:** `scripts/002-pipeline-status.sh`
**Run:** `bash scripts/002-pipeline-status.sh`
**Takes:** ~1 second
**Exit code:** 0 (always informational)

### What it does

Shows a status overview of all 10 documentation folders with:
- Total file count per folder
- Number of authored (substantive) documents vs skeleton (placeholder) documents
- Visual progress bar per folder

A "skeleton" document is defined as:
- Fewer than 30 lines total, OR
- Fewer than 3 lines of substantive prose content (non-header, non-YAML)

### Expected output

```
  ████░░░░░░░░░░░░░░░░  001-meta  (7/7)  7 draft
  ░░░░░░░░░░░░░░░░░░░░  006-infrastructure  (6/6)  6 draft
  ...

  Total: 67 documents  |  0 stable  |  67 draft  |  0 skeleton
  ✓ No skeleton documents
```

### Next steps

| If you see… | Then… |
|---|---|
| All green, no skeleton | No action needed |
| Any skeleton documents | Those files need substantive content. Check file sizes. |
| Discrepancies with INDEX.md counts | Run `010-refresh-files.py` to regenerate indexes |

---

## 4. `003-resolve-cross-refs.sh` — Cross-reference validation

**Path:** `scripts/003-resolve-cross-refs.sh`
**Run:** `bash scripts/003-resolve-cross-refs.sh`
**Takes:** ~2-10 seconds (depends on file count and ref density)
**Exit code:** 0 = all cross-refs valid, 1 = at least one broken ref

### What it does

Scans all `.md` files for cross-references and validates that the target file
exists in the repository. It checks two patterns:

1. **Markdown links:** `[text](target.md)` — standard markdown link syntax
2. **ZUSS cross-references:** `→ **[target.md]** — description` — the specific
   ZUSS convention for document references

Both patterns are resolved relative to the source file's directory.

### File scan logic

Uses the same exclusion patterns as the ZUSS validator:
```bash
find "$ROOT_DIR" -name '*.md' -not -path '*/scripts/*' -not -path '*/.git/*' -not -path '*/.opencode/*'
```

### Cross-reference patterns detected

**Pattern 1 — Markdown links (lines 33-88):**
- Finds all `](path/to/file.md)` patterns in every `.md` file
- Resolves relative to the source file's directory
- Skips external URLs (https://...) and absolute paths (/...)
- Reports each link as ✓ (found) or ✗ (not found)

**Pattern 2 — ZUSS cross-refs (lines 92-125):**
- Finds all `→ **[filename.md]**` patterns
- First tries to resolve relative to the source file's directory
- If not found, tries to resolve relative to the repository root
- Reports each ref as ✓ (resolved), ✓ (root-relative), or ✗ (not found)

### Expected output

```
═══ 1. Markdown link references ═══
  ✓ 001-constitution.md → 002-profile.md
  ✓ AGENTS.md → INDEX.md
  ✗ agents-index.md → orchestrator.md (not found)

═══ 2. ZUSS cross-reference notation ═══
  ✓ 001-platform-overview.md → **002-module-architecture.md**
  ✗ 001-platform-overview.md → nonexistent-file.md (not found)

Cross-reference summary
  Resolved: 290
  Broken: 0
  Skipped (external/absolute): 10
  ✓ All cross-references resolve.
```

### Next steps

| If you see… | Then… |
|---|---|
| All `✓`, exit 0 | Cross-references intact |
| Any `✗` errors | Fix the broken reference: either create the missing file or update the ref |
| Warnings/skipped | External and absolute-path refs are skipped (intentional) |

---

## 5. `004-zarishsphere-init.sh` — GitHub repository initialisation

**Path:** `scripts/004-zarishsphere-init.sh`
**Run:** `bash scripts/004-zarishsphere-init.sh`
**Takes:** ~30-60 seconds (depends on GitHub API)
**Exit code:** 0 on success, non-zero on failure
**Prerequisites:** `gh` CLI authenticated with GitHub

### What it does

Creates and configures all ZarishSphere GitHub repositories under the
`zarishsphere` organisation. This script is designed to be run once during
initial project setup.

### Repository creation sequence

1. `zarishsphere/zs-docs` — Documentation repository (this repo)
2. `zarishsphere/zs-platform` — Platform backend (Go)
3. `zarishsphere/zs-zarish-index` — ZARISH-INDEX data engine
4. `zarishsphere/zs-zarish-standards` — ZARISH-STANDARDS transformation layer
5. `zarishsphere/zs-console` — Console frontend
6. `zarishsphere/zs-marketplace` — Marketplace
7. `zarishsphere/zs-builder` — Builder
8. `zarishsphere/zs-apps` — Applications catalog
9. `zarishsphere/zs-forms` — Forms engine
10. `zarishsphere/zs-sdk` — SDK
11. `zarishsphere/zs-cli` — CLI tool
12. `zarishsphere/zs-api` — Public API gateway
13. `zarishsphere/zs-engine` — Engine
14. `zarishsphere/.github` — Org-level config, templates, Actions

Each repository is created with:
- Public visibility
- README.md placeholder
- Apache 2.0 LICENSE file
- .gitignore for the relevant technology stack

### Expected output

```
Creating zarishsphere/zs-docs... ✓
Creating zarishsphere/zs-platform... ✓
...
All 14 repositories created successfully.
```

### Next steps

After running, push the local content to each repository:
```bash
git remote add origin git@github.com:zarishsphere/zs-docs.git
git push -u origin main
```

---

## Exclusion reference

All scripts share a consistent exclusion policy. Files at these paths are
**never** scanned, modified, or validated:

| Path | Reason |
|---|---|
| `.opencode/` | Agent ecosystem — agents, skills, MCP server. Not documentation. |
| `scripts/` | The scripts themselves. Not documentation. |
| `node_modules/` | Third-party dependencies. Not documentation. |
| `.git/` | Git metadata. Never modify Git internals. |
| Hidden files/dirs (`.`) | Config files, IDE settings, OS artifacts. |

This exclusion is implemented in:
- **Shell scripts:** via `-not -path '*/.opencode/*'` in `find` commands
- **Python script:** via `iter_md_files()` which only scans `\d{3}-` folders

---

## Dependency chain between scripts

```
010-refresh-files.py
  ├── Fixes footers (affects 001-zuss-validate.sh check 4)
  ├── Regenerates INDEX.md (affects 002-pipeline-status.sh data)
  └── Regenerates llms.txt (affects AI agent context)
       │
       ▼
001-zuss-validate.sh
  └── Must pass before cross-ref validation is useful
       │
       ▼
002-pipeline-status.sh
  └── Informational — can run at any time
       │
       ▼
003-resolve-cross-refs.sh
  └── Final check before commit
```

Always run scripts in this order: `010` → `001` → `002` → `003`.

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
