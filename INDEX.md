---
id: "ZS-INDEX-ROOT"
title: "zs-docs root index"
domain: "zs-docs"
doc-type: "root-index"
entity-type: "root-index"
summary: >-
  Root navigation index for the zs-docs repository — single source of truth
  for ZarishSphere Foundation governance, platform architecture, ZARISH-INDEX,
  ZARISH-STANDARDS, infrastructure, tech stack, ADRs, operations, and
  ecosystem integration.
tags:
  - "index"
  - "navigation"
  - "root"
version: "1.0.0"
status: "stable"
last_updated: "2026-06-11"
isolation_tier: "global"
canonical: true
audience: [all]
---

# zs-docs root index
## ZarishSphere Foundation — documentation repository

> **Single source of truth** for governance, architecture, and platform design.
> Contains **117 documents** across **10 folders** managed by ZUSS conventions.

---

## Repository structure

| # | Folder | Documents | Purpose | Status |
|---|---|---|---|---|
| 001 | [001-meta/](001-meta/INDEX.md) | 7 | Everything starts here | ✅ Complete |
| 002 | [002-foundation/](002-foundation/INDEX.md) | 5 | Governance and legal framework for the ZarishSphere Foundation | ✅ Complete |
| 003 | [003-platform/](003-platform/INDEX.md) | 10 | Technical architecture for the ZarishSphere Platform | ✅ Complete |
| 004 | [004-zarish-index/](004-zarish-index/INDEX.md) | 5 | ZARISH-INDEX is the autonomous open research data product that indexes every global standard | ✅ Complete |
| 005 | [005-zarish-standards/](005-zarish-standards/INDEX.md) | 17 | ZARISH-STANDARDS is the transformation layer that converts ZARISH-INDEX entries into machine-executable assets via the G2A pipeline | ✅ Complete |
| 006 | [006-infrastructure/](006-infrastructure/INDEX.md) | 10 | Infrastructure design and configuration for the ZarishSphere ecosystem | ✅ Complete |
| 007 | [007-tech-stack/](007-tech-stack/INDEX.md) | 6 | Technology choices and stack specifications for the ZarishSphere ecosystem | ✅ Complete |
| 008 | [008-adrs/](008-adrs/INDEX.md) | 23 | Every significant technical and governance decision is recorded as an ADR | ✅ Complete |
| 009 | [009-operations/](009-operations/INDEX.md) | 15 | Operational procedures for the ZarishSphere ecosystem | ✅ Complete |
| 010 | [010-ecosystem/](010-ecosystem/INDEX.md) | 19 | Complete component specifications for the ZarishSphere ecosystem | ✅ Complete |

**Total: 117 documents** (117 authored, 0 skeleton)

---

## Recommended reading order

Read folders in sequence. Within each folder, read files in numerical order.

1. **001-meta/** — foundation, meta
2. **002-foundation/** — governance, foundation
3. **003-platform/** — platform, architecture
4. **004-zarish-index/** — zarish-index, standards
5. **005-zarish-standards/** — zarish-standards, transformation
6. **006-infrastructure/** — infrastructure, cloudflare, github
7. **007-tech-stack/** — tech-stack, technology
8. **008-adrs/** — adrs, decisions
9. **009-operations/** — operations, sop
10. **010-ecosystem/** — ecosystem, components

---

## Quick links

| Purpose | File |
|---|---|
| Constitution (start here) | [001-meta/001-zarishsphere-constitution.md](001-meta/001-zarishsphere-constitution.md) |
| Writing rules (ZUSS) | [001-meta/004-writing-rules.md](001-meta/004-writing-rules.md) |
| Architecture overview | [001-meta/005-ecosystem-architecture.md](001-meta/005-ecosystem-architecture.md) |
| Glossary | [001-meta/006-glossary.md](001-meta/006-glossary.md) |
| Agent strategy | [001-meta/007-agent-ecosystem-strategy.md](001-meta/007-agent-ecosystem-strategy.md) |
| Platform overview | [003-platform/001-platform-overview.md](003-platform/001-platform-overview.md) |
| Console (main UI) | [010-ecosystem/001-console-spec.md](010-ecosystem/001-console-spec.md) |

---

## Cross-repository map

| Repo | Purpose | Docs reference |
|---|---|---|
| `zarishsphere/zs-docs` | Documentation (this repo) | This index |
| `zarishsphere/zs-platform` | Platform implementation | `003-platform/` |
| `zarishsphere/zs-zarish-index` | ZARISH-INDEX implementation | `004-zarish-index/` |
| `zarishsphere/zs-zarish-standards` | ZARISH-STANDARDS implementation | `005-zarish-standards/` |
| `zarishsphere/zs-fhir-hub` | FHIR Integration Hub | `010-ecosystem/` |
| `zarishsphere/zs-home` | ZarishSphere Home landing site | `010-ecosystem/` |

---

## Validation

Run these scripts before any push:

```bash
scripts/001-zuss-validate.sh       # Naming, serialing, front matter, footers, banned words
scripts/002-pipeline-status.sh     # Document completion status
scripts/003-resolve-cross-refs.sh  # Cross-reference validation
```

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
