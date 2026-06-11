# ZarishSphere Documentation Ecosystem (`zs-docs`)

> **Single source of truth for the ZarishSphere ecosystem.**
> Platform documentation · Foundation governance · Master index for all three projects.

**Status:** V1 — Active development · Not yet live
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)
**Organization:** [github.com/zarishsphere](https://github.com/zarishsphere)
**Website:** [zarishsphere.com](https://zarishsphere.com)

---

## What this repository is

`zs-docs` is the documentation backbone of the ZarishSphere ecosystem. It serves three functions simultaneously:

1. **Platform documentation** — the authoritative specification for the ZarishSphere Platform
2. **Foundation governance** — the constitutional and governance documents of the ZarishSphere Foundation
3. **Master index** — the navigation hub that connects ZARISH-INDEX and ZARISH-STANDARDS documentation

If you are an AI agent, a contributor, or a new reader: start with **[INDEX.md](INDEX.md)** for navigation, then read the constitution.

---

## Repository structure

| Folder | Documents | Purpose | Status |
|---|---|---|---|---|---|
| [001-meta/](001-meta/INDEX.md) | 7 | Foundation constitution, architecture, writing rules, glossary, agent strategy | ✅ 7 stable |
| [002-foundation/](002-foundation/INDEX.md) | 5 | Charter, governance model, licensing, contributor guidelines, CAMM | ✅ 5 stable |
| [003-platform/](003-platform/INDEX.md) | 10 | Platform architecture, modules, deployment, G2A, FHIR, API, data, domains, catalog, resource map | ✅ 10 stable |
| [004-zarish-index/](004-zarish-index/INDEX.md) | 5 | ZARISH-INDEX specifications | ✅ 5 stable |
| [005-zarish-standards/](005-zarish-standards/INDEX.md) | 17 | ZARISH-STANDARDS specifications (FHIR, API, forms, i18n, terminology) | ✅ 17 stable |
| [006-infrastructure/](006-infrastructure/INDEX.md) | 10 | GitHub, Cloudflare, domains, email, CI/CD, security, compliance, threat models | ✅ 10 stable |
| [007-tech-stack/](007-tech-stack/INDEX.md) | 6 | Tech stack master, Go FHIR, frontend, pipeline, no-code, OSS catalog | ✅ 6 stable |
| [008-adrs/](008-adrs/INDEX.md) | 23 | Architecture Decision Records (001-023) | ✅ 23 stable |
| [009-operations/](009-operations/INDEX.md) | 15 | Standard Operating Procedures (001-015) | ✅ 15 stable |
| [010-ecosystem/](010-ecosystem/INDEX.md) | 19 | Ecosystem component specs (Console through FHIR Hub) | ✅ 19 stable |
| [`.opencode/`](.opencode/agents/) | 13 agents, 10 skills | **Single agent ecosystem** — orchestrator + 12 domain sub-agents + GitHub MCP | ✅ Stable |

**Total: 117 documents** (117 authored, all substantive — 0 skeleton, 117 stable, 0 draft)

---

## Quick navigation

| I want to understand... | Go to |
|---|---|
| What ZarishSphere is | [001-meta/001-zarishsphere-constitution.md](001-meta/001-zarishsphere-constitution.md) |
| How all repos relate | [001-meta/005-ecosystem-architecture.md](001-meta/005-ecosystem-architecture.md) |
| Writing and naming rules | [001-meta/004-writing-rules.md](001-meta/004-writing-rules.md) |
| Any ZarishSphere term | [001-meta/006-glossary.md](001-meta/006-glossary.md) |
| Platform architecture | [003-platform/001-platform-overview.md](003-platform/001-platform-overview.md) |
| ZARISH-INDEX | [004-zarish-index/001-zarish-index-overview.md](004-zarish-index/001-zarish-index-overview.md) |
| ZARISH-STANDARDS | [005-zarish-standards/001-zarish-standards-overview.md](005-zarish-standards/001-zarish-standards-overview.md) |
| Infrastructure setup | [006-infrastructure/001-infrastructure-overview.md](006-infrastructure/001-infrastructure-overview.md) |
| Technology choices | [007-tech-stack/001-tech-stack-master.md](007-tech-stack/001-tech-stack-master.md) |
| Why a decision was made | [008-adrs/](008-adrs/INDEX.md) |
| How to do a specific task | [009-operations/](009-operations/INDEX.md) |

---

## Three projects, one organization

All ZarishSphere projects live under `github.com/zarishsphere`:

| Project | Repository | Docs location |
|---|---|---|
| ZarishSphere Platform | `zs-platform` | `003-platform/` in this repo |
| ZARISH-INDEX | `zs-zarish-index` | `zs-zarish-index/docs/` |
| ZARISH-STANDARDS | `zs-zarish-standards` | `zs-zarish-standards/docs/` |

---

## Validation

Run these scripts before any push:

```bash
scripts/001-zuss-validate.sh      # Naming, serialing, front matter, footers, banned words
scripts/002-pipeline-status.sh    # Document completion status
scripts/003-resolve-cross-refs.sh # Cross-reference validation
```

---

## License

- **Documentation:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Code:** Apache License 2.0

Both licenses are permanently free. Neither may be changed to restrict access for humanitarian, public health, or public sector use.

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
