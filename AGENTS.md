# AGENTS.md — zs-docs

**What this is:** Documentation-only repo (`zarishsphere/zs-docs`). No code, no tests, no build steps. **117 markdown documents** across 10 folders — single source of truth for ZarishSphere Foundation governance, Platform architecture, ZARISH-INDEX, ZARISH-STANDARDS, infrastructure, tech stack, ADRs, operations, and ecosystem components.

**Current status:** 117 primary documents (117 `stable`, 0 `draft`) with substantive content (0 skeleton). 11 INDEX.md files are `status: stable`. Repo is **not yet initialized as a git repo** — no `.git/` directory, nothing pushed to GitHub.

## Agent memory snapshot (June 11, 2026 — post-Phase N completion)

This is the live state of the entire zs-docs ecosystem. Any AI agent entering this repo gets this as its bootstrap context.

### Document counts

| Folder | Total | Stable | Draft | Notes |
|---|---|---|---|---|---|
| 001-meta/ | 7 | 7 | 0 | Constitution (v1-authoritative), ZUSS, Architecture, Glossary, Profiles, Agent Strategy — all stable |
| 002-foundation/ | 5 | 5 | 0 | Charter, governance, licensing, contributor guidelines, CAMM — all stable |
| 003-platform/ | 10 | 10 | 0 | Platform overview, modules, planes, G2A, FHIR, API, data, domains, repo catalog, free-tier map — all stable |
| 004-zarish-index/ | 5 | 5 | 0 | Index overview, taxonomy, metadata, harvesting, integration — all stable |
| 005-zarish-standards/ | 17 | 17 | 0 | Overview, transformation, schema, pipeline + 13 FHIR/API/forms/terminology deep-docs — all stable |
| 006-infrastructure/ | 10 | 10 | 0 | GitHub, Cloudflare, domains, email, CI/CD, security, policies, compliance, threats — all stable |
| 007-tech-stack/ | 6 | 6 | 0 | Tech stack master, Go FHIR, frontend, pipeline, no-code, OSS catalog — all stable |
| 008-adrs/ | 23 | 23 | 0 | ADRs 001-023 — all stable (10 settled decisions + 2 governance + 11 infra selections) |
| 009-operations/ | 15 | 15 | 0 | SOPs 001-015 — documents, GitHub, contributions, compliance, deployment, incidents, security, backup/DR, onboarding, monitoring — all stable |
| 010-ecosystem/ | 19 | 19 | 0 | Console through FHIR Hub (19 component specs) — all stable |
| **Total** | **117** | **117** | **0** | **0 skeleton** |

### What was built across all sessions
- **Phase N (legacy incorporation):** 39 new documents across 7 batches
- **13 standards deep-docs** (005-017): FHIR R5 conventions, profiling, search, audit, R4 bridge, REST API, OpenAPI, AsyncAPI, form schema, validation rules, i18n, terminology governance, code systems
- **4 security docs** (006-007-010): Security architecture, policies, compliance controls (HIPAA/GDPR), threat models
- **11 infrastructure ADRs** (008-013-023): PostgreSQL, NATS, Valkey, OpenTofu, ArgoCD, Cilium, Carbon DS, Microfrontends, PowerSync, TypeScript strict, Flutter
- **7 operations SOPs** (009-009-015): Deployment, incident response, security incident, backup/DR, country onboarding, facility onboarding, monitoring
- **2 platform refs** (003-009-010): Repository catalog (212 repos), free-tier resource map
- **1 CAMM doc** (002-005): Country Adoption Maturity Model (6 levels)
- **1 OSS catalog** (007-006): ~200 tools cataloged with pinned versions

**Single ecosystem:** The agent ecosystem lives entirely under `.opencode/`. A previously duplicated sandbox environment inside `001-meta/` (agents, skills, plugins, tools, scripts) has been consolidated into `.opencode/`. There is exactly one set of agents, one set of skills, and one configuration.

**Instruction chain loaded by default** (from `opencode.jsonc`): `AGENTS.md` → `INDEX.md` → `llms.txt`. INDEX.md has the full file tree; llms.txt has AI-consumable summaries.

---

## Validation pipeline (exact order, run before any commit)

```bash
python3 scripts/010-refresh-files.py     # 1 — normalize YAML, regenerate INDEX.md + llms.txt, fix footers
bash   scripts/001-zuss-validate.sh      # 2 — naming, numbering, front matter (12 fields), footers, banned words
bash   scripts/002-pipeline-status.sh    # 3 — document completion overview (informational, always exits 0)
bash   scripts/003-resolve-cross-refs.sh # 4 — cross-reference integrity (→ **[target.md]** patterns)
```

- `010-refresh-files.py` **must** run first — validators read its regenerated INDEX.md and llms.txt.
- `001-zuss-validate.sh` exits 1 on failures (must fix). Warnings (heading case) are advisory.
- `003-resolve-cross-refs.sh` exits 1 on broken refs.
- **All validators automatically skip `.opencode/`** — they only scan documentation folders (001-010) and root doc files. They never touch agents, skills, MCP servers, or opencode configuration.
- `npm`/`npx` require user approval (set in `opencode.jsonc`). Not used in this repo anyway.

---

## Agent ecosystem

The orchestrator is the default agent (defined in `opencode.jsonc`). It delegates to 12 sub-agents via the `task` tool — it never writes documents itself. All agents live under `.opencode/agents/`.

| Agent | Domain |
|---|---|
| `orchestrator` | Master — all domains (default, primary mode) |
| `meta-docs` | 001-meta/ — Constitution, ZUSS rules, architecture, glossary |
| `foundation-docs` | 002-foundation/ — Charter, governance, licensing |
| `platform-docs` | 003-platform/ — Architecture, FHIR, API, data model |
| `zarish-index-docs` | 004-zarish-index/ — Standards index, taxonomy, schema |
| `standards-docs` | 005-zarish-standards/ — Transformation, schema, pipeline |
| `infrastructure-docs` | 006-infrastructure/ — GitHub, Cloudflare, DNS, CI/CD |
| `tech-stack-docs` | 007-tech-stack/ — Go, frontend, data pipeline, no-code |
| `adr-docs` | 008-adrs/ — Architecture Decision Records |
| `ops-docs` | 009-operations/ — SOPs, runbooks |
| `ecosystem-docs` | 010-ecosystem/ — Console, Marketplace, Builder, Apps, etc. |
| `github-ops` | gh CLI — repos, branches, PRs, Actions, Pages |
| `reviewer` | Read-only ZUSS compliance — runs all 4 validation scripts |

All skills live under `.opencode/skills/`. Load the `meta` skill first (constitution + ZUSS context), then delegate to domain-specific sub-agents in parallel.

---

## Critical rules (ZUSS)

- **Naming:** All files `nnn-descriptive-name.md` — lowercase, hyphens only, 3-digit prefix. INDEX.md is the only exception.
- **Front matter:** Every primary doc needs 12+ fields: id, title, domain, doc-type, entity-type, summary, tags, version, status, last_updated, isolation_tier, capabilities, audience.
- **`latest` tag forbidden** everywhere, even outside code blocks. Pin versions explicitly.
- **Banned words** (enforced by validator): three specific words are banned — see the validator script for the current list.
- **No JVM/HAPI FHIR** references without explicit ADR exception (Constitution Law 11 / ADR-004).
- **Law text** must never be duplicated. Cite `001-meta/001-zarishsphere-constitution.md` as source.
- **Cross-references** use `→ **[filename.md]** — description`. Validated by `003-resolve-cross-refs.sh`.
- **Document sections** are numbered: `## 1.`, `### 1.1`. Never skip levels. Never use `#` except the title.
- **Every doc** ends with the canonical 3-line footer (Foundation name + license + GitHub link). The refresh script enforces this.

---

## Repo-specific gotchas

- **No .git directory yet** — this repo has never been initialized or pushed. Init with `git init` when ready.
- **Single ecosystem:** All agents are under `.opencode/agents/`. All skills under `.opencode/skills/`. No duplicate environments.
- **Scripts are documentation-only:** The scripts in `scripts/` only validate documentation folders (001-010). They never modify `.opencode/` or any agent/skill/MCP files.
- **`session-ses_*.md`** files at root are transient session logs. Ignore or delete with `mv <path> /tmp/trash`; never commit.
- **`rm`/`rmdir` denied** in opencode permissions. Use `mv <path> /tmp/trash` to discard files.
- **.opencode/ directory** is the agent ecosystem (agents, skills, MCP server). The MCP server at `.opencode/mcp-server-github.js` wraps gh CLI. Edits to `.opencode/` should be rare.
- **No package.json or npm** in the repo itself — only `.opencode/package.json` (for the MCP server dependency `@opencode-ai/plugin`). Do not run npm in the repo root.
- **Cross-project refs:** Every doc in `004-zarish-index/` must cross-link to `zs-zarish-index/docs/`. `004-` docs → `zs-zarish-index`, `005-` docs → `zs-zarish-standards`, `003-` docs → `zs-platform`.
- **V1 until launch** — do not bump document versions during development. Status changes (draft → stable) are permitted and encouraged as documents mature.
- **Constraint blocks** use `> **Constraint:** [rule]` for hard requirements only.

---

## Quick commands

| Task | Command |
|---|---|
| Refresh all generated files | `python3 scripts/010-refresh-files.py` |
| Full validation | `bash scripts/001-zuss-validate.sh && bash scripts/002-pipeline-status.sh && bash scripts/003-resolve-cross-refs.sh` |
| Init GitHub repos | `bash scripts/004-zarishsphere-init.sh` (requires `gh` auth + org setup) |

---

## Document template (essentials)

Every primary document must have in order:

1. YAML front matter (`---` delimited, 12+ fields)
2. Header: `# filename.md`, `## Human title`, `### Subtitle`, metadata table
3. ToC (if >5 sections): `1. [Title](#1-title)`
4. Numbered body sections
5. License footer (auto-fixed by refresh script)

For ADRs (008-adrs/): Decision, Context, Alternatives Considered, Reason, Consequences, Status.
For SOPs (009-operations/): Purpose, Scope, Roles, Preconditions, Steps (GUI-first), Expected outcome, Escalation.

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
