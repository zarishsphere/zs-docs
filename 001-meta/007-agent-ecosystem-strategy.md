---
id: "ZS-007-AGE"
title: "007 agent ecosystem strategy"
domain: "001-meta"
doc-type: "blueprint"
summary: >-
  Strategic blueprint for making the entire ZarishSphere ecosystem agent-native
  and MCP-consumable. Covers enhanced front matter, knowledge graphs, skills
  packaging, MCP layer, and lifecycle management for all ecosystem components
  — from Constitution through Console, Marketplace, Builder, and all 19 ecosystem components.
tags:
  - strategy
  - ai-agents
  - mcp
  - skills
  - knowledge-graph
  - agent-native
entity-type: "strategic-blueprint"
version: "1.0.0"
status: "stable"
last_updated: 2026-06-11
last_verified: 2026-06-11
verified_by: "Mohammad Ariful Islam"
next_review: 2026-09-11
isolation_tier: "global"
canonical: true
depends_on:
  - "ZS-001-ZAR"
  - "ZS-004-WRI"
  - "ZS-005-ECO"
related:
  - "ZS-002-ZAR"
  - "ZS-006-GLO"
capabilities:
  - agent-skill: "parse_007_agent_ecosystem_strategy"
  - mcp-resource: "agent_ecosystem_strategy"
audience:
  - "ai-agents"
  - "contributors"
---

# 007-agent-ecosystem-strategy.md
## ZarishSphere agent-native documentation strategy
### Making every document a machine-consumable asset — V1

**Document type:** Strategic blueprint  
**Date:** June 10, 2026  
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation  
**License:** CC BY 4.0  
**Status:** V1 — Stable  
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [What this document is](#1-what-this-document-is)
2. [The big picture: docs as everything](#2-the-big-picture-docs-as-everything)
3. [Current state assessment](#3-current-state-assessment)
4. [The agent-native layer: what makes docs AI-ready](#4-the-agent-native-layer-what-makes-docs-ai-ready)
5. [Enhanced front matter schema](#5-enhanced-front-matter-schema)
6. [Knowledge graph: connecting every document](#6-knowledge-graph-connecting-every-document)
7. [Agent entry points: AGENTS.md and llms.txt](#7-agent-entry-points-agentsmd-and-llmstxt)
8. [Skills packaging: every doc folder as a skill](#8-skills-packaging-every-doc-folder-as-a-skill)
9. [MCP layer: exposing docs as AI resources](#9-mcp-layer-exposing-docs-as-ai-resources)
10. [Lifecycle management: keeping docs alive](#10-lifecycle-management-keeping-docs-alive)
11. [Practical roadmap: what to do in what order](#11-practical-roadmap-what-to-do-in-what-order)

---

## 1. What this document is

This document is a blueprint. It describes how to evolve `zs-docs` from a documentation repository into the **operating system for the entire ZarishSphere ecosystem** — where every document is simultaneously:

- A **law** (constitution, governance)
- A **blueprint** (architecture, design)
- A **template** (SOPs, workflows)
- A **skill** (loadable by AI agents)
- A **knowledge graph node** (connected to every other document)
- An **MCP resource** (consumable by any AI tool)

And where understanding all of this requires **zero coding skill** — only the ability to write plain markdown.

## 2. The big picture: docs as everything

The world of AI is moving in a direction that ZarishSphere already anticipated. In 2026, the industry has converged on a single truth:

> **Markdown is the universal interface between humans and AI agents.**

What this means for you:

- Every major AI tool (Claude, ChatGPT, VS Code Copilot, Cursor, GitHub Copilot) now reads **markdown files** natively
- The industry standard for AI agent configuration is **markdown files with YAML front matter** — exactly what ZUSS already specifies
- The Model Context Protocol (MCP) — the USB-C standard for AI connections — uses **markdown resources** as its primary data format
- Agent skills are packaged as **folders of markdown files** (SKILL.md + supporting docs)

Your documentation is not "just documentation." It is the **source code that AI agents will read, interpret, and act upon.** Every law, every architecture decision, every SOP you write is a set of instructions that future AI agents will execute.

## 3. Current state assessment

### What is already strong

| Strength | Why it matters for AI |
|---|---|
| ZUSS naming standard (nnn-prefix, lowercase, hyphens) | Agents can navigate predictably |
| YAML front matter with id, version, status | Agents can filter by maturity |
| Header block with document type and date | Agents can judge authority and freshness |
| Numbered sections with stable anchors | Agents can deep-link to specific sections |
| Cross-reference format (`→ **[filename.md]**`) | Agents can follow links like a graph |
| Constraint blocks (> **Constraint:**) | Agents recognize hard rules vs guidance |
| AGENTS.md already exists | Agents have an entry point |
| 12-law constitution | Supreme context for all decisions |
| Ecosystem architecture (005) | Master map for navigation |

### What needs to be added

| Gap | What it means for AI | Status |
|---|---|---|
| No `summary` field in front matter | Agent must read the whole file to know what it's about | ✅ Resolved — added to all INDEX.md and primary docs |
| No `tags` field in front matter | Agent cannot categorize or filter | ✅ Resolved — added to all INDEX.md and primary docs |
| No `related` cross-links in front matter | Agent doesn't know which docs to read next | ⬜ Pending — Phase 2 knowledge graph work |
| No `last_verified` field | Agent doesn't know if info is still accurate | ✅ Resolved — added to all stable docs |
| No `entity-type` or `doc-type` classification | Agent cannot distinguish laws from SOPs from ADRs | ✅ Resolved — added to all INDEX.md, present in primary docs |
| No llms.txt file | Agent has no quick index of what exists | ✅ Resolved — `llms.txt` created at root |
| No knowledge graph edges between documents | Agent sees isolated files, not a connected system | ⬜ Pending — Phase 2 |
| No INDEX.md navigation files | Agent has no folder-level index | ✅ Resolved — 11 INDEX.md files created |
| No validation scripts | No automated compliance checking | ✅ Resolved — 5 scripts in `scripts/` |
| No skills packaging | Agent cannot load a folder as a "capability" | ✅ Resolved — 10 skills in `.opencode/skills/` |
| No MCP server | Agent cannot query docs as a live resource | ✅ Resolved — MCP server at `.opencode/mcp-server-github.js` |
| No freshness/verification cadence | Docs get stale silently | ⬜ Pending — Phase 5 |
| No wikilinks ([[wikilink]]) pattern | Cross-references are hard-coded, not graph-navigable | ⬜ Pending — Phase 2 |

## 4. The agent-native layer: what makes docs AI-ready

An "agent-native" document is one that an AI agent can read, understand, and act upon **without a human explaining it.** This is different from "human-readable" documentation.

### The four-layer model

```
Layer 1: Discovery ─── Agent finds out the document exists
    │                    (llms.txt, AGENTS.md, folder structure)
    ▼
Layer 2: Routing ────── Agent decides if this doc is relevant
    │                    (front matter: summary, tags, status)
    ▼
Layer 3: Reading ────── Agent extracts the rules and facts
    │                    (numbered sections, constraint blocks, stable anchors)
    ▼
Layer 4: Acting ─────── Agent follows instructions or references
                         (cross-links, relationships, skills format)
```

### The "curl test"

A simple way to know if your docs are agent-ready: if an AI agent fetched the raw markdown of any document, could it do its job? Specifically:

1. Can it know what this document is about within 3 seconds? (summary field)
2. Can it know whether this document is current? (last_updated, status)
3. Can it know which other documents to read for context? (related, dependencies)
4. Can it know what type of document this is? (doc-type: law/architecture/sop/adr)
5. Can it follow a clear instruction without ambiguity? (constraint blocks, numbered steps)

## 5. Enhanced front matter schema

The current front matter is good. The enhanced version below adds the fields that AI agents need to operate independently.

### Current (what you have)

```yaml
---
id: "ZS-001-ZAR"
title: "001 zarishsphere constitution"
domain: "001-meta"
version: "1.0.0"
status: "stable"
last_updated: 2026-06-08
isolation_tier: "global"
capabilities:
  - agent-skill: "parse_001_zarishsphere_constitution"
---
```

### Enhanced (what AI agents need)

```yaml
---
id: "ZS-001-ZAR"
title: "001 zarishsphere constitution"
domain: "001-meta"
doc-type: "constitution"              # classification: constitution/law/architecture/sop/adr/specification/blueprint/template
summary: >                            # one-sentence routing hint for agents
  The supreme governing document of the ZarishSphere ecosystem.
  Defines 12 laws across 4 tiers that all projects, repositories,
  and decisions are subordinate to.
tags:                                 # flat list for categorization and filtering
  - governance
  - law
  - constitution
  - foundation
  - tier-I
  - tier-II
  - tier-III
  - tier-IV
entity-type: "governing-document"     # what kind of node in the knowledge graph
version: "1.0.0"
status: "stable"                       # draft / stable / deprecated
last_updated: 2026-06-08
last_verified: 2026-06-08             # when a human confirmed it's still accurate
verified_by: "Mohammad Ariful Islam"  # who confirmed
next_review: 2026-09-08               # suggested next review date (90 days)
isolation_tier: "global"
canonical: true                       # true = this is a defended source of truth
depends_on:                           # documents that must be read first
  - "ZS-000-README"
related:                              # documents that are closely connected
  - "ZS-004-WRI"
  - "ZS-005-ECO"
  - "ZS-006-GLO"
supersedes: ~                         # what this document replaces (if anything)
replaced_by: ~                        # what replaces this (when deprecated)
capabilities:
  - agent-skill: "parse_001_zarishsphere_constitution"
  - mcp-resource: "constitution"
audience:                             # who should read this
  - "all"
---
```

### Field-by-field explanation (plain language)

| Field | What it tells the AI agent |
|---|---|
| `doc-type` | What kind of document this is — so the agent knows how to interpret it |
| `summary` | One sentence that lets the agent decide "do I need to read this?" without reading the whole thing |
| `tags` | Labels for searching and filtering |
| `entity-type` | What this document represents in the knowledge graph |
| `last_verified` | When a human last confirmed the info is still correct (different from when it was edited) |
| `verified_by` | Who confirmed it — so the agent can weigh authority |
| `next_review` | When this doc should be checked again — creates a maintenance schedule |
| `canonical` | Is this a "blessed" source of truth? Agents treat canonical:true docs as authoritative |
| `depends_on` | What must be read before this — agents build their context in the right order |
| `related` | What is closely connected — agents build a complete picture |
| `supersedes/replaced_by` | Version chain — agents follow the lineage |
| `audience` | Who this is for — agents filter to what's relevant |

## 6. Knowledge graph: connecting every document

AI agents work best when documents form a connected graph, not isolated files.

### What a knowledge graph is (plain language)

Think of every document as a node, and every cross-reference as a directed connection between nodes. When an agent reads document A and it says "see document B," the agent follows that link. When enough links exist, the agent can navigate the entire ecosystem by following connections — just like a human browsing Wikipedia.

### Relationship types

When you link one document to another, specify **what kind** of relationship it is:

| Relationship | Meaning | Example |
|---|---|---|
| `depends_on` | Must read this first | Constitution depends on README |
| `related` | Closely connected, read alongside | Writing rules related to Glossary |
| `supersedes` | This document replaces another | ADR 002 supersedes ADR 001 |
| `implements` | This document implements something | Platform overview implements the Constitution's Law 7 |
| `references` | Mentions but doesn't depend on | Tech stack references Cloudflare architecture |
| `part_of` | This document is a section of a larger whole | SOP-001 is part of Operations |
| `conflicts_with` | These documents disagree (note it explicitly) | (rare, use with caution) |

### How to express relationships

**In front matter** (for machine reading):
```yaml
depends_on:
  - "ZS-001-ZAR"
  - "ZS-005-ECO"
related:
  - "ZS-004-WRI"
```

**In body text** (for both human and machine reading):
```markdown
```

**Using wikilinks** (for graph-aware tools):
```markdown
This architecture follows the [[001-zarishsphere-constitution]] and uses
the naming rules from [[004-writing-rules]].
```

### The graph shapes that emerge

```
                    ┌── 001-zarishsphere-constitution.md
                    │
    README.md ──────┼── 004-writing-rules.md (ZUSS) ──── 006-glossary.md
                    │
                    ├── 005-ecosystem-architecture.md ─── 009-operations/*.md
                    │
                    ├── 007-agent-ecosystem-strategy.md (this doc)
                    │
                    └── TODO.md
```

## 7. Agent entry points: AGENTS.md and llms.txt

AI agents need a front door — a short file they read first that tells them what exists and where to start.

### AGENTS.md (already created)

This is the file I created at the repo root. It serves as the **bootstrap loader** for any AI agent entering the repository for the first time. It should be kept short (under 100 lines) and point to the most critical docs.

**What it should contain:**
1. What this repo is (one sentence)
2. First-read order (4-5 critical docs)
3. Non-negotiable rules (ZUSS naming, document structure)
4. Current state and key constraints
5. Validation checklist before merging

### llms.txt (created)

An `llms.txt` file at the root of the repository gives AI agents a quick index of all available content. It is a simple markdown file with links organized by category.

**What it should contain:**
```markdown
# zs-docs
> ZarishSphere Foundation — master documentation index

## Essentials
- [001-zarishsphere-constitution.md](001-zarishsphere-constitution.md): Supreme governing document

- [004-writing-rules.md](004-writing-rules.md): ZUSS naming and formatting standard

- [005-ecosystem-architecture.md](005-ecosystem-architecture.md): Master repository map

- [006-glossary.md](006-glossary.md): All terms defined

## Foundation governance (002-foundation/)
- [001-foundation-charter.md](../002-foundation/001-foundation-charter.md): Mission and scope
... (continue for all documents)
```

### How agents use these files

```
Agent enters repo
       │
       ▼
  Reads AGENTS.md ───────────► Gets: what this repo is, first-read order,
       │                          non-negotiable rules, current state
       ▼
  Reads llms.txt ────────────► Gets: complete index of all documents
       │
       ▼
  Follows first-read order ──► Constitution → ZUSS → Architecture → Glossary
       │
       ▼
  Proceeds to task
```

## 8. Skills packaging: every doc folder as a skill

This is the most powerful pattern for making your documentation directly loadable by AI agents.

### What a skill is (plain language)

A skill is a folder of documents that teaches an AI agent how to do something. For example, a "Foundation Governance" skill would contain all the documents about how the foundation operates, its charter, its rules, its licensing policies.

When an AI agent loads a skill, it reads the folder and understands: "I now know how to handle foundation governance tasks."

### The industry standard skill format

```
002-foundation/                    ◄── skill folder (name = folder name)
├── SKILL.md                       ◄── required: the main skill instruction file
├── 001-foundation-charter.md      ◄── supporting documents
├── 002-governance-model.md
├── 003-licensing-policy.md
└── 004-contributor-guidelines.md
```

Every folder in `zs-docs` is already structured as a potential skill:

| Folder | Skill name | What the skill teaches |
|---|---|---|
| `001-meta/` | `meta` | Foundation rules, ZUSS, architecture, glossary |
| `002-foundation/` | `foundation` | Foundation governance, charter, licensing |
| `003-platform/` | `platform` | Platform architecture, modules, API design |
| `004-zarish-index/` | `zarish-index` | ZARISH-INDEX data engine |
| `005-zarish-standards/` | `zarish-standards` | ZARISH-STANDARDS transformation layer |
| `006-infrastructure/` | `infrastructure` | GitHub, Cloudflare, domain architecture |
| `007-tech-stack/` | `tech-stack` | Technology choices and decisions |
| `008-adrs/` | `adrs` | Architecture Decision Records |
| `009-operations/` | `operations` | SOPs, workflows, runbooks |
| `010-ecosystem/` | `ecosystem` | Ecosystem components: Console, Marketplace, Builder, Apps, Forms, SDK, CLI, API, Services, Modules, Distributions, Engine, System, Content repos, Home, FHIR Hub |

### SKILL.md format

Each folder gets a `SKILL.md` that describes what the skill does, when to load it, and what documents it contains. Example:

```yaml
---
name: "foundation"
title: "Foundation governance"
summary: "Governance documents for the ZarishSphere Foundation — charter, decision-making, licensing, contributor rules"
version: "1.0.0"
status: "stable"
tags: [governance, foundation, charter, licensing]
depends_on:
  - "meta"
documents:
  - "001-foundation-charter.md"
  - "002-governance-model.md"
  - "003-licensing-policy.md"
  - "004-contributor-guidelines.md"
---
# Foundation governance skill

Load this skill when the task involves:

- Understanding how the foundation is governed
- How to make decisions within the foundation
- Licensing rules for ZarishSphere projects
- How contributors can participate

## Documents


## Dependencies

This skill depends on the `meta` skill (constitution, ZUSS, architecture, glossary).
Load the `meta` skill first if it is not already in context.
```

## 9. MCP layer: exposing docs as AI resources

MCP (Model Context Protocol) is the industry standard for connecting AI agents to external data. It is like a USB-C port for AI — a universal way for any AI tool to read your documentation as a live resource.

### What MCP gives you

1. **Any AI tool can read your docs** — Claude, ChatGPT, VS Code Copilot, Cursor, and all MCP-compatible clients
2. **Live access** — agents read the current version, not a cached copy
3. **Structured access** — docs are organized as named resources with metadata
4. **Skill discovery** — agents can list available skills and load them on demand

### How to build the MCP layer

This is a **future step** (Phase 4 in the roadmap). You do not need to do this now. But the architecture should be designed so it is possible.

The MCP server would:
1. Read all markdown files from `zs-docs`
2. Parse YAML front matter to extract metadata
3. Expose each document as an MCP resource (e.g., `docs://001-meta/001-zarishsphere-constitution`)
4. Expose each skill (folder) as an MCP skill (e.g., `skill://foundation`)
5. Expose a search/discovery endpoint

### What you need to do now to prepare

Nothing technical. Just make sure every document has:
- A unique `id` in front matter (already done ✓)
- Clear section headings with stable anchors ✓
- Complete cross-references ✓
- Machine-readable metadata ✓

This is enough for any MCP server to consume your docs.

## 10. Lifecycle management: keeping docs alive

Documentation that is not maintained becomes misinformation. AI agents are worse than humans at detecting stale information — they will confidently cite a 2-year-old draft as truth.

### The three states every document goes through

```
     ┌──────────┐     ┌──────────┐     ┌──────────────┐
     │  DRAFT   │ ──► │  STABLE  │ ──► │  DEPRECATED  │
     │ (write)  │     │(maintain)│     │ (archive)    │
     └──────────┘     └──────────┘     └──────────────┘
```

- **DRAFT**: Being written, not yet authoritative. Agents should not cite drafts as truth.
- **STABLE**: Reviewed and approved. Agents can quote stable docs verbatim.
- **DEPRECATED**: No longer current. Agents should not use it; the document should point to its replacement.

### The verification cycle

Every document needs to be **verified** periodically — not just edited, but confirmed as still accurate.

| Document type | Suggested verification cadence |
|---|---|
| Constitution, laws | Every 6 months |
| Architecture docs | Every 3 months |
| ADRs | At project milestones |
| SOPs, runbooks | Every 3 months or after any process change |
| Tech stack docs | Monthly during active development |

### How to track this

The front matter fields `last_verified` and `next_review` create a simple tracking system. You can periodically run a review by checking which documents have `next_review` dates that have passed.

## 11. Practical roadmap: what to do in what order

This roadmap is designed for a single person with no coding experience. Every step uses plain markdown editing — no programming required.

### Phase 0: Foundation (complete)

- [x] Update this document with any changes from discussion
- [x] Update all existing front matter in `001-meta/` to add: `summary`, `tags`, `doc-type`, `related`, `canonical`
- [x] Create `llms.txt` at the root with a complete index of all documents
- [x] Update `AGENTS.md` to reference this strategy document
- [x] Create INDEX.md navigation files for all 10 folders and root
- [x] Create validation scripts (naming, status, cross-refs)

### Phase 1: Complete all 78 primary documents

- [x] Write all 7 documents in `001-meta/` (3 stable, 4 draft)
- [x] Write all 4 documents in `002-foundation/` (all stable)
- [x] Write all 8 documents in `003-platform/` (1 stable, 7 draft)
- [x] Write all 5 documents in `004-zarish-index/` (all draft)
- [x] Write all 4 documents in `005-zarish-standards/` (all draft)
- [x] Write all 6 documents in `006-infrastructure/` (all draft)
- [x] Write all 5 documents in `007-tech-stack/` (1 stable, 4 draft)
- [x] Write all 12 documents in `008-adrs/` (10 stable, 2 draft)
- [x] Write all 8 documents in `009-operations/` (all draft)
- [x] Write all 19 documents in `010-ecosystem/` (Console, Marketplace, Builder, Apps, Forms, SDK, CLI, API, Services, Modules, Distributions, Engine, System, Content Forms, Content Protocols, Content Templates, Content Reports, Home, FHIR Hub)

### Phase 2: Knowledge graph enrichment

As you write each document, add:

- [ ] Front matter: `depends_on`, `related`, `supersedes` as appropriate
- [ ] Body: wikilinks to related documents (`[[document-name]]`)
- [ ] Body: cross-reference format (`→ **[file.md]** — description`)
- [ ] End of document: `## Related` section listing all connected docs

### Phase 3: Skills packaging

After each folder has all its documents:

- [ ] Create `SKILL.md` in each of the 10 folders (001-meta through 010-ecosystem)
- [ ] Verify each SKILL.md has: name, title, summary, version, status, tags, document list
- [ ] Test: ask an AI agent to load a skill and confirm it works

### Phase 4: MCP server (future)

When the content is complete and verified:

- [ ] Set up a simple MCP server (can be done with minimal technical help)
- [ ] Expose all documents as MCP resources
- [ ] Expose all skills via the MCP skills extension
- [ ] Deploy on Cloudflare (free tier)

### Phase 5: Automation and maintenance

- [ ] Set up a 90-day review reminder for all documents
- [ ] Create a review template for verifying document accuracy
- [ ] Run a cross-reference validation script before any commit
- [ ] Set up GitHub repository and push all documents

---

## Summary: what success looks like

When this strategy is fully implemented, this is what happens:

1. A new AI agent enters `zs-docs`
2. It reads AGENTS.md → learns the repo's purpose and rules
3. It reads INDEX.md → gets navigation routes for all 10 folders
4. It reads llms.txt → sees all 117 documents organized by category
5. It reads the Constitution → learns the 12 laws
6. It reads ZUSS → learns the naming and formatting rules
7. It loads a skill (e.g., `foundation`) → gets all governance documents
8. It follows cross-references → navigates the entire knowledge graph
9. It checks last_verified → knows the information is current
10. It produces output that follows all ZarishSphere rules automatically

No coding. No programming. Just well-structured markdown documents connected by clear relationships.

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
