---
id: "ZS-001-SOP"
title: "001 sop new document creation"
domain: "009-operations"
doc-type: "sop"
entity-type: "procedure"
summary: >-
  SOP-001: How to provision and validate a new documentation node following
  ZUSS conventions. Covers file creation, front matter setup, and compliance
  validation.
version: "1.0.0"
status: "stable"
tags:
  - "sop"
  - "documentation"
  - "creation"
  - "workflow"
isolation_tier: "global"
capabilities:
  - "agent-skill: "parse_001_sop_new_document_creation"
audience:
  - "contributors"
  - "ai-agents"
last_updated: "2026-06-08"
---
# 001-sop-new-document-creation.md
## SOP-001: Provisioning and validating a new ZUSS-compliant document
### Standard Operating Procedure — documentation creation

**Document type:** Standard Operating Procedure  
**Date:** June 10, 2026  
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation  
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)  
**Status:** Active — V1  

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Scope](#2-scope)
3. [Roles](#3-roles)
4. [Preconditions](#4-preconditions)
5. [Steps](#5-steps)
6. [Expected outcome](#6-expected-outcome)
7. [Escalation](#7-escalation)

---

## 1. Purpose

To define the exact procedure for creating a new documentation file in the zs-docs repository that complies with the ZarishSphere Universal Serialization Standard (ZUSS), including naming, front matter, structure, and validation.

---

## 2. Scope

**In scope:** Creating any new `.md` document in any of the 10 folders in `zs-docs` (001-meta through 010-ecosystem). Updating INDEX.md files (handled automatically by `010-refresh-files.py`). Adding supplementary documents such as glossaries, appendices, or reference tables.

**Out of scope:** Creating files outside `zs-docs` (e.g., in `zs-platform`, `zs-zarish-index`, or `zs-zarish-standards`). Editing existing documents. Binary file attachments.

---

## 3. Roles

| Role | Who |
|---|---|
| **Creator** | Documentation Agent (AI) or human contributor who writes the new document |
| **Reviewer** | Reviewer Agent (AI) or maintainer who verifies ZUSS compliance |
| **Maintainer** | Mohammad Ariful Islam — final approval authority |

---

## 4. Preconditions

- The target folder exists and follows ZUSS numbering (no gaps in the sequence).
- The creator has read → **[001-meta/004-writing-rules.md](../001-meta/004-writing-rules.md)** — ZUSS rules.
- All validation scripts are available in `scripts/`:
  - `scripts/010-refresh-files.py`
  - `scripts/001-zuss-validate.sh`
- The editor is VS Code or any plain-text editor capable of YAML front matter and Markdown.

---

## 5. Steps

### 5.1 Determine the correct file name

1. Identify the next available 3-digit sequence number in the target folder.
   - Example: If folder contains `001-*.md`, `002-*.md`, `003-*.md`, the next number is `004`.
   - Check by listing files: **VS Code → Explorer pane → expand the folder**.
2. Construct the name using the pattern `nnn-descriptive-name.md`:
   - Lowercase only, hyphens between words, no underscores or spaces.
   - Example: `004-sop-backup-recovery.md` (not `004 SOP backup recovery.md`).
3. Verify uniqueness — no other file in the repo uses the same descriptive slug.

### 5.2 Create the file

1. **VS Code → Explorer pane → right-click the target folder → New File**.
2. Type the filename (e.g., `004-sop-backup-recovery.md`) and press **Enter**.
3. Open the file.

### 5.3 Add YAML front matter

Insert the following block at the very top of the file (between `---` delimiters). Fill in every field:

```yaml
---
id: "ZS-NNN-DESCRIPTOR"      # e.g., "ZS-004-SOP" — see pattern below
title: "nnn descriptive title"  # e.g., "004 sop backup recovery"
domain: "NNN-folder"           # e.g., "009-operations"
doc-type: "sop"                # one of: sop, spec, reference, adr, index, normative standard
entity-type: "procedure"       # one of: procedure, specification, index, rulebook, profile, glossary
summary: >-
  One paragraph describing the document's purpose. This appears in INDEX.md and llms.txt.
tags:
  - "sop"
  - "relevant-tag"
version: "1.0.0"
status: "stable"                # use "draft" for new files
last_updated: "2026-06-10"    # today's date in YYYY-MM-DD
isolation_tier: "global"       # global, foundation, platform, internal
capabilities:
  - "agent-skill: "parse_nnn_file_name"
audience:
  - "contributors"
  - "ai-agents"                # or "deployers", "all"
---
```

**ID pattern:** `ZS-NNN-XXX` where `NNN` is the folder number (001–010) and `XXX` is a 3-letter entity code (SOP, WRI, ARC, IND, STD, INF, TEC, ADR, OPS, ECO).

### 5.4 Add the header block

After the closing `---` of the front matter, add:

```markdown
# nnn-descriptive-name.md
## Human-readable title
### subtitle (optional)

**Document type:** Standard Operating Procedure
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)
**Status:** Active — V1
```

Separate the header block from the body with `---`.

### 5.5 Add the table of contents

If the document has more than 5 sections, add a numbered ToC immediately after the first `---` separator:

```markdown
## Table of contents

1. [Purpose](#1-purpose)
2. [Scope](#2-scope)
...
```

### 5.6 Write the numbered sections

Structure the body using numbered sections. Section headings use `## 1.`, `## 2.`, etc. Subsection headings use `### 1.1`, `### 1.2`, etc. Never skip heading levels.

For SOPs (this file type), the seven required sections are:

```markdown
## 1. Purpose
## 2. Scope
## 3. Roles
## 4. Preconditions
## 5. Steps
## 6. Expected Outcome
## 7. Escalation
```

### 5.7 Add cross-references

Use the standard cross-reference format for any reference to another document:

```
```

Example:
```
```

### 5.8 Verify the license footer

Every file must end with the canonical 3-line footer. It is usually present already:

```markdown
```

If missing, `python3 scripts/010-refresh-files.py` will add it automatically.

### 5.9 Run validation

1. Open a terminal: **VS Code → Terminal → New Terminal** (`` Ctrl+` ``).
2. Run the refresh script:
   ```bash
   python3 scripts/010-refresh-files.py
   ```
   Confirm no `ERROR` output. If you see `FIX` entries, run the script a second time to verify stability.
3. Run the ZUSS compliance validator:
   ```bash
   bash scripts/001-zuss-validate.sh
   ```
   Confirm exit code 0 (all checks pass). If any `✗` failures appear, fix the reported issue and re-run.
4. Run the cross-reference validator:
   ```bash
   bash scripts/003-resolve-cross-refs.sh
   ```
   Verify all cross-references resolve to existing files.

### 5.10 Set initial status to draft

The front matter `status` field should be `"draft"` for a newly created document. This will be promoted to `"stable"` only after review and approval.

---

## 6. Expected outcome

- A new `.md` file exists in the correct folder with ZUSS-compliant naming.
- The file contains valid YAML front matter with all required fields.
- The file passes all 7 checks of `001-zuss-validate.sh` (exit code 0).
- `INDEX.md` and `llms.txt` have been regenerated to include the new document.
- All cross-references point to existing files.

---

## 7. Escalation

| Issue | Action |
|---|---|
| Validation script errors after multiple fixes | Check the file for malformed YAML using a YAML linter. Open the file in VS Code and look for red squiggles in the front matter. |
| Naming conflict (descriptive slug already in use) | Choose a different descriptive name. Document titles need not be unique but filenames must be. |
| `010-refresh-files.py` throws an exception | Run `python3 scripts/010-refresh-files.py` with the `--verbose` flag (if available) or manually inspect the last-modified file. Report the error to the maintainer. |
| Unsure which folder the new document belongs to | Consult → **[001-meta/005-ecosystem-architecture.md](../001-meta/005-ecosystem-architecture.md)** for folder mapping, or ask the maintainer. |
| Scripts not found | Ensure you are in the repository root (`zs-docs/`). Run `ls scripts/` to verify. |

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
