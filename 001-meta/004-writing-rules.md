---
id: "ZS-004-WRI"
title: "004 writing rules"
domain: "001-meta"
doc-type: "normative standard"
entity-type: "rulebook"
summary: >-
  ZarishSphere Universal Serialization Standard (ZUSS) — the single,
  consistent rule set governing how every file, folder, repository, workflow,
  identifier, and document is named, structured, and written within the
  ZarishSphere ecosystem.
version: "1.0.0"
status: "stable"
tags:
  - "zuss"
  - "standards"
  - "documentation"
  - "naming"
  - "formatting"
isolation_tier: "global"
capabilities: [agent-skill: "parse_004_writing_rules]
audience: [all]
last_updated: "2026-06-08"
last_verified: "2026-06-11"
verified_by: "Mohammad Ariful Islam"
next_review: "2026-09-11"
---
# 004-writing-rules.md
## ZarishSphere universal serialization standard (ZUSS)
### Documentation, naming, and formatting rules — V1

**Document type:** Normative standard  
**Date:** June 07, 2026  
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation  
**License:** CC BY 4.0  
**Status:** V1 — Authoritative. All ZarishSphere documents, repos, and workflows must comply.  
**GitHub:** https://github.com/zarishsphere  

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Core naming mechanics](#2-core-naming-mechanics)
3. [Repository naming](#3-repository-naming)
4. [Entity identifiers](#4-entity-identifiers)
5. [Document structure rules](#5-document-structure-rules)
6. [Writing style rules](#6-writing-style-rules)
7. [Technical documentation subtypes](#7-technical-documentation-subtypes)
8. [Version policy](#8-version-policy)
9. [License block](#9-license-block)
10. [Cross-reference standard](#10-cross-reference-standard)
11. [AI agent navigation rules](#11-ai-agent-navigation-rules)
12. [Prohibited patterns](#12-prohibited-patterns)

---

## 1. Purpose

ZUSS is the **single, consistent rule set** governing how every file, folder, repository, workflow, identifier, and document is named, structured, and written within the ZarishSphere ecosystem. Consistency at this level makes the ecosystem machine-explorable and human-navigable simultaneously.

Every repository matching the `zs-*` catalog format must align its taxonomy with ZUSS. No exceptions. When any document in the ecosystem contradicts ZUSS, ZUSS wins — unless the constitution (`001-zarishsphere-constitution.md`) takes precedence as the supreme document.

---

## 2. Core naming mechanics

### 2.1 Universal syntax rules

| Rule | Requirement |
|---|---|
| Case | Lowercase only. No uppercase anywhere in file or folder names. |
| Separator | Hyphen (`-`) only. No underscores, no spaces, no camelCase. |
| Index prefix | All files and folders begin with a 3-digit zero-padded sequence number: `001`, `002`, `099`. |
| Extension | Always explicit: `.md`, `.yml`, `.json`, `.go`, `.yaml`. Never omit. |
| Pattern | `nnn-descriptive-name.ext` |
| Strict sequence | Numbers within a folder must be sequential with **no gaps**. Every number from 001 to N must be assigned and present. |

**Valid examples:**

```
001-zarishsphere-constitution.md
002-foundation-profile.md
003-founder-profile.md
004-writing-rules.md
010-zarish-index-direction.md
099-appendix-references.md
```

> **Insertion rule:** When a new document must be added between existing numbered documents, renumber the file being inserted and all files that follow it in sequence. This is acceptable because the repository is under active development and files are not referenced by their number in URLs or permalinks — they are referenced by their descriptive name. After launch, consider locking the sequence at the then-current maximum to minimise renumbering.

**Invalid examples:**

```
Founder Profile.md        ← spaces + uppercase
founderProfile.md         ← camelCase
001_founder_profile.md    ← underscores
founder-profile           ← missing extension
```

### 2.2 Folder naming

Same rules as files, but without extensions:

```
001-core/
002-health/
003-geography/
010-zarish-index/
```

### 2.3 Workflow file naming

CI/CD and automation workflow files follow a three-segment format:

```
[id]--[trigger]--[process].yml
```

| Segment | Rules | Example |
|---|---|---|
| `[id]` | 3-digit zero-padded integer | `101` |
| `[trigger]` | What fires the workflow (kebab-case) | `on-push`, `on-schedule`, `on-release` |
| `[process]` | What the workflow does (kebab-case) | `validate-markdown`, `build-artifacts`, `publish-pages` |
| Separator | Double hyphen `--` between each segment | — |

**Valid examples:**

```
101--on-push--validate-markdown.yml
102--on-schedule--sync-iso-data.yml
201--on-release--publish-pages.yml
301--on-pull-request--lint-yaml.yml
```

---

## 3. Repository naming

All ZarishSphere repositories follow the `zs-` prefix convention. The canonical pattern is:

```
zs-{layer}-{module}[-{submodule}]
```

| Category | Pattern | Example |
|---|---|---|
| Core platform | `zs-core` | `zs-core` |
| Master documentation index | `zs-docs` | `zs-docs` |
| Platform documentation | `zs-platform-docs` | `zs-platform-docs` |
| Domain modules | `zs-[domain]` | `zs-health`, `zs-logistics` |
| FHIR engine | `zs-fhir-[component]` | `zs-fhir-server`, `zs-fhir-g2a` |
| Infrastructure | `zs-infra-[component]` | `zs-infra-cloudflare`, `zs-infra-k3s` |
| Content (data) | `zs-content-[type]` | `zs-content-forms`, `zs-content-protocols` |
| Standards index | `zs-module-zarish-index` | `zs-module-zarish-index` |
| Standards registry | `zs-module-zarish-standards` | `zs-module-zarish-standards` |
| ADRs (all repos) | `zs-adrs` | `zs-adrs` |

**Docker image naming:**

```
zarishsphere/[service-name]:[v1.0.0]
```

Example: `zarishsphere/zs-fhir-server:v1.0.0`

> **Rule:** Never use the `latest` tag in any production or pinned configuration. The sole exception is `cloudflared`, which is auto-updated by design.

### 3.1 `zs-docs` canonical folder structure

`zs-docs` is the master documentation index and single source of truth for the entire ecosystem. It hosts foundation governance, platform architecture, component specifications, and master cross-references for ZARISH-INDEX and ZARISH-STANDARDS.

```
zs-docs/
├── README.md
├── AGENTS.md
├── llms.txt
├── TODO.md
├── 001-meta/
├── 002-foundation/
├── 003-platform/
├── 004-zarish-index/
├── 005-zarish-standards/
├── 006-infrastructure/
├── 007-tech-stack/
├── 008-adrs/
├── 009-operations/
└── 010-ecosystem/
```

Each project docs repo (e.g., `zs-zarish-index/docs/`) follows the same `nnn-` prefixed structure within its own scope.

---

## 4. Entity identifiers

All system entities use the following identifier patterns:

| Entity | Pattern | Example |
|---|---|---|
| FHIR profile | `https://zarishsphere.org/fhir/StructureDefinition/zs-[resource]` | `zs-patient` |
| Form ID | `zh-form-[domain]-[name]-v1` | `zh-form-ncd-intake-v1` |
| Patient ID | `ZS-[MODULE]-[YEAR]-[NNNNNN]` | `ZS-NCD-2025-000001` |
| Service URL | `https://[service].zarishsphere.com/[path]` | `https://api.zarishsphere.com/fhir/R5/` |
| ADR | `ADR-[NNN]-[title-kebab-case]` | `ADR-001-go-as-primary-language` |
| Standard ID (ZARISH-INDEX) | `ZI-[DOMAIN_CODE]-[NNNNN]` | `ZI-HEALTH-00001` |
| RFC | `RFC-[NNN]-[title-kebab-case]` | `RFC-001-zuss-amendment-optional-fields` |
| Ecosystem component | `ZS-COMP-[name]` | `ZS-COMP-console`, `ZS-COMP-marketplace` |
| Application | `ZS-APP-[domain]-[name]` | `ZS-APP-health-patient-registry` |
| Module | `ZS-MOD-[domain]` | `ZS-MOD-health`, `ZS-MOD-education` |
| Distribution | `ZS-DIST-[name]` | `ZS-DIST-air-gapped-clinic` |
| Console resource | `ZS-CONSOLE/[resource]` | `ZS-CONSOLE/deployments`, `ZS-CONSOLE/modules` |

---

## 5. Document structure rules

### 5.1 Mandatory header block

Every primary document must begin with this block:

```markdown
# [nnn]-[document-name].md
## [Human-readable title]
### [Subtitle or scope]

**Document type:** [See §5.1.1 for valid types]
**Date:** [Full date — June 07, 2026]
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** [Apache 2.0 (code) · CC BY 4.0 (documentation) OR as applicable]
**Status:** V1 — [One-line status description]
**GitHub:** https://github.com/zarishsphere
```

The `GitHub` field is mandatory in all documents. The following optional fields may be included after `GitHub` where relevant:

| Optional field | When to include |
|---|---|
| `Domain:` | When the document belongs to a specific ZarishSphere domain module |
| `Contact:` | When the document has a designated point of contact beyond the author |
| `Supersedes:` | When this document replaces a prior document |
| `Depends on:` | When the document requires another document to be read first |

**Rule:** Optional fields must appear consistently across all documents that share the same context. Using an optional field in 2 of 4 sibling documents and omitting it from the others is a compliance violation.

#### 5.1.1 Valid document types

| Type | Used for |
|---|---|
| `Constitution` | Supreme governing document only — `001-zarishsphere-constitution.md` |
| `Normative standard` | Rules and specifications that must be followed — like this document |
| `Reference` | Context and background information — founder profile, foundation profile |
| `Specification` | Technical architecture, system design, deployment configuration |
| `Component spec` | Specification for an ecosystem component (Console, Marketplace, Builder, etc.) |
| `Blueprint` | High-level design and architectural vision documents |
| `Direction` | Strategic direction documents — roadmaps, vision, intent |
| `ADR` | Architecture decision record — see §7.1 |
| `SOP` | Standard operating procedure — see §7.2 |
| `PRD` | Product requirements document — see §7.3 |
| `Audit report` | Compliance audit findings |
| `Charter` | Founding document for a sub-project (Zarish Index, Zarish Standards) |
| `RFC` | Request for comments — proposed amendments or changes |
| `Changelog` | Version history and changes |
| `App spec` | Specification for a ZarishSphere pre-built application |
| `Module manifest` | Manifest for a domain module — contents, dependencies, APIs |
| `Distribution manifest` | Definition of a pre-packaged deployment distribution |
| `Marketplace listing` | Listing for a Marketplace component |

### 5.2 Table of contents

Required for all documents with more than 5 sections. Format:

```markdown
## Table of contents

1. [Section title](#1-section-title)
2. [Section title](#2-section-title)
```

> **Rule:** A ZUSS-compliant document with more than 5 sections and no ToC is an incomplete document. No document lacking a required ToC may be merged to `main`.

### 5.3 Section numbering

- Top-level sections: `## 1. Title`, `## 2. Title`
- Subsections: `### 1.1 Subtitle`, `### 1.2 Subtitle`
- Sub-subsections: `#### 1.1.1 Detail` (use sparingly)
- Never skip a level
- All sections — including appendices, progress tracking, and footers — must be numbered

### 5.4 Tables

Use tables for all comparisons, configurations, and lists of 3+ items with attributes. Minimum 2 columns.

```markdown
| Column A | Column B | Column C |
|---|---|---|
| Value | Value | Value |
```

Every column in a table must carry content. A single-column table is a list. Use a list instead.

### 5.5 Code blocks

All code, commands, configuration, and identifiers use fenced code blocks with language specifier:

````markdown
```bash
sudo apt update
```

```yaml
version: "3.8"
services:
```

```go
func main() {
```
````

Never show a command inline without a code block if it needs to be executed.

### 5.6 Constraint block pattern

The constraint block is the canonical pattern for expressing a non-negotiable rule, design requirement, or hard boundary. It is the primary visual element of ZUSS governance documents.

Format:

```markdown
> **Constraint:** [The rule in one or two sentences. Active voice. No hedging.]
```

Use the constraint block pattern:

- In the twelve laws (mandatory for each law)
- In ADRs (to state the binding decision)
- In SOPs (to state preconditions that must be met before proceeding)
- In any section where the content is a hard requirement, not a recommendation

Do not use the constraint block for general guidance, suggestions, or preferences. Those are prose.

---

## 6. Writing style rules

### 6.1 Tone

| Rule | What it means |
|---|---|
| Semi-formal to direct | No corporate fluff. No apologies. No padding. |
| Knowledgeable, not condescending | Assume the reader is competent in their domain. |
| Specific, not vague | Every claim must be actionable or verifiable. |
| Banned words | "carefully", "clearly", "clear" are banned in all ZarishSphere documents. |

### 6.2 Plain language first

Technical concepts always get a plain-language framing before the technical detail.

Pattern:

```
[What it is in one plain sentence.]
[Technical detail follows.]
```

Example (XaaS model):

> **Infrastructure as a Service (IaaS)** — You rent the raw foundation; you still build what goes on top.  
> *Technical:* On-demand provisioning of virtual machines, storage, and networking. The customer manages OS, runtime, middleware, and applications.

Apply this pattern to all ZarishSphere service descriptions and deployment plane documentation.

### 6.3 Service model language (XaaS mapping)

ZarishSphere uses the XaaS mental model to communicate deployment options:

| ZarishSphere tier | XaaS equivalent | What the deployer owns |
|---|---|---|
| Plane 0 — Air-gapped | On-premises | Everything |
| Plane 1 — Raspberry Pi | IaaS + self-managed | OS + apps + data |
| Plane 2 — District server | PaaS-like | Apps + data |
| Plane 3 — National cloud | SaaS + config | Config + data |
| Plane 4 — Global SaaS | Full SaaS | Data only |

### 6.4 Heading rules

- Use `##` for primary sections, `###` for subsections
- Never use `#` for anything other than the document title line (the filename)
- Never write headings longer than 8 words
- All headings: sentence case — first word capitalised, rest lowercase unless proper nouns or initialisms
- `GitHub`, `ZUSS`, `FHIR`, `ADR`, `ZI-UID`, `G2A` are initialisms — keep them uppercase in headings

**`001-zarishsphere-constitution.md` is the style reference.** When heading case is unclear, check the constitution.

### 6.5 Lists

- Use bullet lists (`-`) only for unordered items with no natural sequence
- Use numbered lists (`1.`, `2.`) for procedures, steps, or prioritised items
- Maximum 7 items in a bullet list before converting to a table
- No single-item lists. If there is only one item, it is prose

### 6.6 Emphasis and bold

- Use `**bold**` for principle names, constraint labels, key terms on first use, and header field names
- Do not use bold for general emphasis in running prose
- Do not use `*italic*` for structural emphasis — italics are for examples, citations, and non-English terms only

---

## 7. Technical documentation subtypes

### 7.1 ADR (architecture decision record)

File: `nnn-adr-[short-title].md` — stored in `zs-adrs/` repository.

Required sections:

1. Decision
2. Context
3. Alternatives considered
4. Reason for decision
5. Consequences
6. Status (`Accepted` / `Superseded` / `Proposed`)

> **Rule:** Inline compact ADRs (2-field summaries embedded in other documents) are not ZUSS-compliant ADRs. They may exist as quick-reference summaries only if they include a `→ link` to the full standalone ADR file. The standalone file in `zs-adrs/` is always the authoritative record.

### 7.2 SOP (standard operating procedure)

File: `nnn-sop-[process-name].md`

Required sections:

1. Purpose
2. Scope
3. Roles responsible
4. Preconditions
5. Step-by-step procedure (numbered, GUI-first)
6. Expected outcome
7. Escalation path

### 7.3 PRD (product requirements document)

File: `nnn-prd-[feature-name].md`

Required sections:

1. Problem statement
2. Goals and non-goals
3. User stories
4. Functional requirements
5. Non-functional requirements
6. Standards compliance
7. Acceptance criteria

### 7.4 README.md

Every repository must have a `README.md` at root level with:

1. One-line description
2. Status badge
3. Quick start (GUI-first, 5 steps maximum)
4. Architecture overview link
5. License block

---

## 8. Version policy

> **V1 until launch.** No version numbers are incremented during development. Everything is V1 from first document to platform launch. After launch, semantic versioning begins.

| Stage | Version label |
|---|---|
| All development | V1 |
| First production launch | v1.0.0 |
| Post-launch patches | v1.0.1, v1.0.2… |
| Feature releases | v1.1.0, v1.2.0… |

---

## 9. License block

Every document must end with this exact block:

```
---

*ZarishSphere Foundation · V1 · [Date]*
```

The license block is the last content in every document. Nothing follows it.

---

## 10. Cross-reference standard

When referencing another ZarishSphere document, use the format:

```markdown
```

Examples:

```markdown
→ **001-zarishsphere-constitution.md** — Supreme governing document; all other documents are subordinate
→ **005-ecosystem-architecture.md** — Complete map of all repositories, folders, subdomains, and routing rules
→ **008-adrs/001-adr-go-as-primary-language.md** — Decision record for Go as the platform's primary language
```

### 10.1 Cross-reference validation rule

> **Constraint:** Every cross-reference in a document must resolve to a file that exists in the repository at the time of the pull request merge. A pull request that introduces or modifies cross-references must include verification that all referenced files exist. Broken cross-references are a merge blocker.

---

## 11. AI agent navigation rules

ZarishSphere is built documentation-first. AI agents — including Claude and any future automated tooling — are primary consumers of the documentation alongside human contributors. Documents must be written to be machine-navigable, not only human-readable.

### 11.1 What AI agents need to function

An AI agent working on any ZarishSphere task should be given, at minimum:

1. `001-zarishsphere-constitution.md` — for governance constraints and law context
2. `004-writing-rules.md` — this document, for all formatting and naming rules
3. The relevant project docs repo entrypoint (e.g. `zs-platform-docs/README.md`)
4. The specific file being worked on

This is the minimum context set. Missing any of these four means the agent is working without full constraint context and may produce non-compliant output.

### 11.2 Document machine-readability requirements

All documents must meet these requirements to be machine-navigable:

| Requirement | Rule |
|---|---|
| Anchored headings | All section headings must be valid markdown anchors (auto-generated from the heading text) |
| Consistent field names | Header block field names must match the ZUSS template exactly — no paraphrasing |
| No ambiguous references | Every entity reference must use the canonical identifier (ZI-UID, ADR-NNN, etc.) |
| Self-contained sections | Each `##` section must be interpretable without requiring context from other sections |
| No implicit relationships | If document A depends on document B, it must state so explicitly in the header `Depends on:` field |

### 11.3 Prompt construction guidance

When constructing prompts for AI-assisted work on ZarishSphere documents:

1. Always specify the ZUSS document being worked on as the constraint reference
2. Always specify the document type (from §5.1.1) as the output target
3. Provide the relevant repository context from `005-repository-map.md`
4. State the exact section being modified, not just "the document"

Example prompt structure:

```
Context: ZarishSphere documentation system, governed by 004-writing-rules.md (ZUSS V1)
Task: Revise section 3.2 of [filename]
Document type: [type from §5.1.1]
Output: Full revised section in ZUSS-compliant markdown
Constraint: Sentence case headings, constraint blocks for hard rules, no banned words
```

### 11.4 `zs-docs` as the AI context entry point

`zs-docs` is the master index repository and single source of truth for the entire ZarishSphere ecosystem. An AI agent given the following files can navigate the entire ecosystem:

1. `AGENTS.md` — bootstrap entry point, first-read order, non-negotiable rules
2. `llms.txt` — complete index of all documents organized by folder
3. `001-meta/001-zarishsphere-constitution.md` — supreme governing document
4. `001-meta/005-ecosystem-architecture.md` — component map, repos, relationships
5. `001-meta/004-writing-rules.md` — this document, naming and formatting rules
6. `001-meta/006-glossary.md` — every term defined
7. `001-meta/007-agent-ecosystem-strategy.md` — AI agent and MCP strategy

---

## 12. Prohibited patterns

The following patterns are explicitly prohibited across all ZarishSphere documents and repositories. Each violation is a merge blocker.

### 12.1 Naming violations

| Prohibited | Reason | Compliant alternative |
|---|---|---|
| `latest` tag in Docker configs | Creates non-reproducible builds | Pin to exact version: `v1.2.3` |
| Uppercase in file or folder names | Breaks machine-sortability and cross-platform compatibility | Lowercase only |
| Underscores in file or folder names | Inconsistent with ZUSS separator rule | Hyphens only |
| CamelCase in file names | Same as above | Kebab-case only |
| Missing index prefix on document files | Breaks sorting and navigation | Always `nnn-` prefix |

### 12.2 Documentation violations

| Prohibited | Reason | Compliant alternative |
|---|---|---|
| Document with >5 sections and no ToC | Violates §5.2 | Add ToC before merging |
| Title Case in subsection headings | Violates §6.4 | Sentence case |
| Single-column table | Violates §5.4 | Use a list, or add a second meaningful column |
| Inline ADR without a link to the full standalone file | Violates §7.1 | Link to the canonical `zs-adrs/nnn-adr-*.md` |
| Broken cross-references | Violates §10.1 | Validate all links before merge |
| Non-ZUSS footer | Violates §9 | Use the exact license block from §9 |
| Header field label deviation | e.g., `Document status` instead of `Status` | Match the exact field names in §5.1 |
| Inconsistent optional header fields | Fields present in some sibling docs but not others | Decide: add to all or remove from all |

### 12.3 Content violations

| Prohibited | Reason | Compliant alternative |
|---|---|---|
| "carefully", "clearly", "clear" | Banned words per §6.1 | Remove or rephrase |
| JVM dependency reference without ADR exception | Violates Law 11 of the constitution | Use Go-native alternative or open a formal ADR |
| `latest` Docker tag | Violates §3 naming rule and Law 11 | Pin to exact semver |
| Unnumbered section in a numbered document | Violates §5.3 | Number it, or remove the unnumbered heading |
| Law text duplicated across documents | Creates divergence risk | Cite `001` as source; do not restate law text |

### 12.4 Structural anti-patterns

These are design-level problems that do not fail a single rule but indicate systemic drift:

- **God document:** A single file exceeding ~400 lines that serves as architecture reference, ADR log, tech stack, and roadmap simultaneously. Split it.
- **Law duplication:** The same law text appearing verbatim in both `001` and another document. The constitution is the canonical source. Other documents reference, not restate.
- **Orphaned sections:** Sections added during working sessions that are never numbered, never cross-referenced, and exist in only one document. Number them, reference them, or remove them.
- **Phase asymmetry:** Roadmap tables that have 2 columns in Phase 1 and 1 column in Phases 2–3. All phases must use identical table structure.

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
