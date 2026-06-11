---
id: "ZS-001-TEC"
title: "001 tech stack master"
domain: "007-tech-stack"
doc-type: "specification"
entity-type: "specification"
summary: >-
  Master production tech stack mapping for the ZarishSphere ecosystem. Defines
  all technology choices including Go, React, Next.js, and the complete
  backend-frontend-data pipeline.
version: "1.0.0"
status: "stable"
tags:
  - "tech-stack"
  - "go"
  - "react"
  - "nextjs"
  - "architecture"
isolation_tier: "global"
capabilities:
  - "agent-skill: parse_001_tech_stack_master"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
last_updated: "2026-06-11"
last_verified: "2026-06-11"
verified_by: "Mohammad Ariful Islam"
next_review: "2026-09-11"
---

# 001-tech-stack-master.md
## Master production tech stack mapping
### Complete technology inventory across backend, frontend, infrastructure, data, and no-code layers

**Document type:** Specification
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)
**Status:** V1 — Draft
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose and scope](#1-purpose-and-scope)
2. [Technology inventory](#2-technology-inventory)
3. [Backend stack](#3-backend-stack)
4. [Frontend stack](#4-frontend-stack)
5. [Infrastructure stack](#5-infrastructure-stack)
6. [Data pipeline stack](#6-data-pipeline-stack)
7. [No-code stack](#7-no-code-stack)
8. [Zero-cost justification](#8-zero-cost-justification)
9. [Cross-references](#9-cross-references)

---

## 1. Purpose and scope

This document defines every technology choice in the ZarishSphere ecosystem. It is the single authoritative reference for what tools, frameworks, libraries, and services are used across all layers of the platform.

All technology decisions are governed by three binding constraints:

> **Constraint:** Every dependency must be zero-cost, open-source, or available on a free tier. No paid tools, licenses, or services are permitted. See ADR-006.

> **Constraint:** No JVM-based dependency may be introduced anywhere in the platform. Go-native alternatives are required for all server-side components. See Law 11 of the constitution and ADR-004.

> **Constraint:** FHIR R5 is the canonical health data standard. R4 compatibility is provided through a translation layer, not by running R4 natively. See ADR-005.

The stack is optimized for a single constraint environment: a Lenovo i3 laptop with 8 GB RAM running Ubuntu (founder development machine) and Raspberry Pi 5 deployments (Plane 1). Every tool choice must function under these limits.

---

## 2. Technology inventory

### 2.1 Master technology table

| Layer | Technology | Version | Purpose | Zero-cost | License |
|---|---|---|---|---|---|
| Backend language | Go | 1.26.4 | All server-side services, FHIR server, G2A Engine | Native binary, no runtime cost | BSD-3-Clause |
| Backend router | Chi (go-chi) | v5.2.1 | HTTP routing for all Go services | Open source | MIT |
| Backend database | SQLite | 3.46+ | Primary data store for all planes | Public domain | Public domain |
| FHIR implementation | Custom Go (zs-fhir-go) | V1 | FHIR R5 server, no Java/HAPI | Custom build | Apache 2.0 |
| FHIR Go models | gofhir-models (fastenhealth) | v0.0.7 | Generated Go structs for FHIR R5 | Open source | Apache 2.0 |
| Frontend framework | React | 19.3.0 | UI component library | Open source | MIT |
| Frontend meta-framework | Next.js | 15.3.1 | App Router, SSR, SSG, API routes | Open source | MIT |
| Frontend language | TypeScript | 5.8.4 | Type-safe frontend code | Open source | Apache 2.0 |
| Styling | Tailwind CSS | 4.1.2 | Utility-first CSS framework | Open source | MIT |
| Component library | Shadcn UI | v4 | Accessible React components | Open source | MIT |
| Package manager | pnpm | 10 | Fast, disk-efficient package management | Open source | MIT |
| Build tool | Vite | 8.1.2 | Frontend build and dev server | Open source | MIT |
| Infrastructure DNS | Cloudflare DNS | Free tier | Authoritative DNS, zone management | Free tier | N/A |
| Infrastructure CDN | Cloudflare CDN | Free tier | Global caching and edge delivery | Free tier | N/A |
| Infrastructure hosting | Cloudflare Pages | Free tier | Static sites, Next.js SSR | Free tier | N/A |
| Edge functions | Cloudflare Workers | Free tier | API gateway, auth, transformations | Free tier (100k req/day) | N/A |
| Object storage | Cloudflare R2 | Free tier (10 GB) | File and backup storage | Free tier | N/A |
| Edge database | Cloudflare D1 | Free tier | Edge-cached SQLite replicas | Free tier | N/A |
| Version control | GitHub | Free org | All repositories, issues, Actions | Free tier | N/A |
| CI/CD | GitHub Actions | Free tier (2000 min/mo) | Automated build, test, deploy | Free tier | N/A |
| Container registry | GitHub Container Registry | Free | Docker image hosting | Free tier | N/A |
| ETL processing | Custom Go tooling | V1 | Data ingestion and transformation | Custom build | Apache 2.0 |
| Analytics format | Parquet | Arrow 18 | Columnar analytics storage | Open source | Apache 2.0 |
| Serialization | YAML / JSON | Standard | Configuration, form definitions, workflows | Standard | N/A |
| Offline queue | Custom Go + SQLite | V1 | Local write buffer with sync | Custom build | Apache 2.0 |
| Templating | Go html/template | stdlib | Server-side rendered dashboards | Standard (Go stdlib) | BSD-3-Clause |

### 2.2 Explicit non-choices

| Technology | Reason rejected | ADR or law |
|---|---|---|
| Java / JVM | 8 GB RAM limit, Plane 0 constraint | Law 11, ADR-004 |
| HAPI FHIR | Java dependency, heavy footprint | ADR-004 |
| Python (backend) | GIL, slow startup, weak concurrency | ADR-001 |
| Node.js (backend) | Non-native typed concurrency model | ADR-001 |
| Rust | Steep learning curve, slower iteration | ADR-001 (Go preferred for simplicity) |
| Kafka | Heavy dependency, Plane 0 incompatible | ADR-006 |
| PostgreSQL | Writes to filesystem, not viable on RPi | Chosen: SQLite for simplicity |
| MongoDB | Document store unnecessary for FHIR | Chosen: SQL for relational queries |
| Redux | Over-engineered for Plane 0 scope | Chosen: Context + hooks |
| Docker Swarm | Kubernetes ecosystem not needed | Chosen: Single-binary deployments |
| Kubernetes | Impractical for 8 GB laptop dev | Chosen: Go single-binary pattern |

---

## 3. Backend stack

### 3.1 Go as primary language

Go is mandated by ADR-001. All backend services — FHIR server, G2A Engine, module runtime, CLI tools — are written in Go.

**Rationale summary:**

- Single binary output — no runtime, no VM, no JIT warmup
- Cross-compilation to ARM64 for Raspberry Pi (Plane 1)
- Built-in concurrency with goroutines for parallel FHIR processing
- Static typing without generics complexity
- Sub-1-second startup times for cold-start deployments
- Memory footprint: 15-150 MB depending on module load

### 3.2 HTTP routing: Chi v5

Chi is the router for all Go HTTP services. Selected over standard `net/http` for middleware chaining and URL parameter support, and over Gin for its explicit `net/http` compatibility.

| Feature | Chi | Gin |
|---|---|---|
| `net/http` compatible | Yes (native) | Wrapper |
| Middleware chaining | Yes (idiomatic) | Custom context |
| Performance | Fast | Slightly faster |
| Community size | Moderate | Large |
| Explicit context | Yes (Go 1.26.4 context) | Custom gin.Context |

### 3.3 Database: SQLite

SQLite is the primary database for all deployment planes (Plane 0 through Plane 4). Selected because:

- Zero configuration — no server process, no connection pooling
- Single file per database — backups are `cp` commands
- Full SQL support with JSON functions for FHIR storage
- WAL mode for concurrent reads during writes
- Plane 4 (global SaaS) may use a SQLite-compatible managed service or read-replica fan-out

> **Constraint:** Every database operation must work on SQLite. No PostgreSQL-specific features may be used. If a migration to a different SQL engine becomes necessary, it must be documented as an ADR.

### 3.4 FHIR server

The FHIR server is a custom Go implementation using Chi for routing and SQLite for storage. See → **[002-go-fhir-server.md]** for the complete specification.

### 3.5 Backend service architecture

```
zs-fhir-server/     — FHIR R5 REST API
zs-g2a-engine/     — Guideline-to-Action transformation engine
zs-module-runtime/  — Domain module executor
zs-sync/            — Offline sync and conflict resolution
zs-export/          — Data export (CSV, JSON, Parquet, FHIR Bundle)
zs-cli/             — Command-line administration tool
zs-builder-api/     — Backend API for the Builder UI
```

---

## 4. Frontend stack

### 4.1 React 19 + Next.js 15

The frontend is built on React 19 with Next.js 15 App Router. Selected for server components, streaming, and static generation.

**Key version choices:**

| Package | Version | Purpose |
|---|---|---|
| react | 19.3.0 | UI component library |
| react-dom | 19.3.0 | DOM rendering |
| next | 15.3.1 | Meta-framework with App Router |
| typescript | 5.8.4 | Type safety |
| tailwindcss | 4.1.2 | Utility-first styling |
| shadcn/ui | v4 | Accessible component primitives |
| vite | 8.1.2 | Build tooling |

### 4.2 Styling and components

- **Tailwind CSS** provides utility-first CSS with zero runtime cost
- **Shadcn UI** provides accessible, copy-paste React components built on Radix UI primitives
- No third-party design system — all components are local to the project tree

### 4.3 State management

- **React hooks + Context** for global state (theme, auth, sidebar)
- **No Redux, Zustand, or Jotai** — unnecessary for Plane 0 deployments
- **Server state** managed through Next.js server components and fetch caching

### 4.4 Build and development

- **Vite 8.1.2** as the build tool (Next.js uses Turbopack in dev, webpack in production)
- **pnpm 10** as the package manager (faster, disk-efficient, strict)
- **TypeScript strict mode** enabled in all frontend packages

### 4.5 Frontend applications

| Application | Stack | Purpose |
|---|---|---|
| Console | Next.js 15, React 19, Shadcn UI | Browser-based management center |
| Forms engine | React 19, dynamic component loader | Renders declarative form definitions |
| Public site | Next.js 15 SSG | Documentation, marketing |
| Marketplace | Next.js 15, React 19 | Component discovery and deployment |

See → **[003-frontend-stack.md]** for the complete frontend specification.

---

## 5. Infrastructure stack

### 5.1 GitHub (free tier)

| Service | Usage | Monthly limit | Estimated usage |
|---|---|---|---|
| Public repositories | All code, docs, standards | Unlimited | 15-25 repos |
| GitHub Actions | CI/CD, lint, deploy | 2,000 min/mo | ~500 min/mo |
| GitHub Container Registry | Docker images | Free | ~10 images |
| GitHub Pages | Documentation sites | Free | zs-docs site |
| GitHub Issues + Projects | Issue tracking | Unlimited | Active |

### 5.2 Cloudflare (free tier)

| Service | Usage | Free tier limit | Notes |
|---|---|---|---|
| DNS | Authoritative DNS | Unlimited zones | All zarishsphere domains |
| CDN | Global asset caching | Unlimited bandwidth | Standard CDN |
| Pages | Static and SSR hosting | 500 builds/mo, 500 GB bandwidth | All frontend apps |
| Workers | Edge API, auth proxy | 100k req/day | API gateway functions |
| R2 | Object storage | 10 GB storage, 10M reads/mo | Backups, exports, uploads |
| D1 | Edge SQLite | 5 GB storage, 5M reads/mo | Read replica cache |

### 5.3 Network architecture

```
zarishsphere.com
  ├── Pages: Console, Public Site, Marketplace
  ├── Workers: API Gateway, Auth Proxy, Rate Limiter
  ├── R2: Form uploads, module assets, backups
  └── D1: Edge-cached read replicas of SQLite databases
```

See → **006-infrastructure/003-cloudflare-architecture.md** for the complete infrastructure specification.
See → **006-infrastructure/002-github-org-architecture.md** for GitHub configuration.

---

## 6. Data pipeline stack

### 6.1 Core components

| Component | Technology | Function |
|---|---|---|
| ETL processor | Custom Go | Ingests FHIR, CSVs, JSON, ZARISH-INDEX data |
| Primary storage | SQLite | Transactional FHIR resources |
| Analytics storage | Parquet files | Columnar format for reporting |
| Export engine | Custom Go | FHIR Bundle, CSV, JSON, Parquet |
| Scheduled sync | systemd timers / cron | Periodic ETL runs |
| Reporting | Go html/template | Lightweight server-side dashboards |

### 6.2 Data flow

```
Data Sources → Go ETL → SQLite (transactional) → Export Engine → Parquet/CSV/JSON
                         ↕
              Go Template Dashboards (local browser)
```

> **Constraint:** No Apache Kafka, Flink, Spark, or any JVM-based data processing tool may be introduced. Data pipelines must run on Go single-binary ETL processes.

See → **[004-data-pipeline.md]** for the complete pipeline specification.

---

## 7. No-code stack

### 7.1 Declarative definition formats

All no-code tools use YAML or JSON declarative formats. No custom scripting language is introduced.

| Asset | Format | Schema |
|---|---|---|
| Forms | YAML / JSON | ZARISH-STANDARDS form schema |
| Workflows | YAML DSL | ZS workflow schema |
| Module manifests | YAML (ZSM format) | ZS module manifest schema |
| Dashboards | YAML | ZS dashboard schema |

### 7.2 Runtime components

| Component | Technology | Purpose |
|---|---|---|
| Forms engine | React 19 (browser) + Go (server) | Renders forms from YAML/JSON |
| Workflow engine | Go | Executes workflow DSL |
| Module loader | Go | Installs and runs ZSM packages |
| Builder UI | React 19 | GUI for creating forms and workflows |

See → **[005-no-code-tools.md]** for the complete no-code specification.
See → **010-ecosystem/003-builder-spec.md** for the Builder component specification.
See → **010-ecosystem/005-forms-spec.md** for the Forms engine specification.

---

## 8. Zero-cost justification

Every technology in the stack is selected to meet the zero-cost requirement (ADR-006) and the single-developer constraint. The table below shows the cost justification for each layer.

### 8.1 Cost comparison

| Layer | Selected | Monthly cost | Alternative | Alternative monthly cost |
|---|---|---|---|---|
| Backend runtime | Go binary | $0 | Java VM + server | $50+ (cloud VM) |
| Database | SQLite | $0 | PostgreSQL RDS | $15+ (managed DB) |
| Hosting | Cloudflare Pages | $0 | Vercel Pro | $20/mo |
| CI/CD | GitHub Actions | $0 | CircleCI | $30/mo |
| CDN | Cloudflare CDN | $0 | Fastly | $50+ |
| Object storage | Cloudflare R2 | $0 (10 GB) | AWS S3 | ~$3/mo (small use) |
| Container registry | GHCR | $0 | Docker Hub Pro | $5/mo |
| Package manager | pnpm | $0 | N/A | $0 |
| Frontend build | Vite | $0 | Webpack commercial | $0 |
| Monitoring | Go stdlib logs | $0 | Datadog | $15+/mo |
| **Total** | | **$0** | | **$178+/mo** |

### 8.2 Platform-specific constraints

> **Constraint:** No toolchain component may require a credit card to start. Every free tier must have sufficient capacity for Plane 0 and Plane 1 deployments at full production load.

> **Constraint:** If a free-tier service changes its pricing model and becomes paid, a migration path to an alternative zero-cost tool must be documented within 90 days.

---

## 9. Cross-references

→ **002-go-fhir-server.md** — Go-native FHIR R5 server specification
→ **003-frontend-stack.md** — Frontend framework and UI architecture
→ **004-data-pipeline.md** — Data ingestion, transformation, storage
→ **005-no-code-tools.md** — No-code and low-code tools in the ecosystem
→ **003-platform/005-fhir-architecture.md** — FHIR R5 integration architecture
→ **003-platform/001-platform-overview.md** — Platform architecture context
→ **003-platform/004-g2a-engine.md** — G2A engine specification
→ **008-adrs/001-adr-go-as-primary-language.md** — ADR for Go language decision
→ **008-adrs/004-adr-no-hapi-fhir.md** — ADR for rejecting HAPI FHIR
→ **008-adrs/005-adr-fhir-r5-over-r4.md** — ADR for FHIR R5
→ **008-adrs/006-adr-zero-cost-toolchain.md** — ADR for zero-cost toolchain
→ **001-meta/001-zarishsphere-constitution.md** — Law 11 (no JVM dependency)
→ **010-ecosystem/001-console-spec.md** — Console frontend application
→ **010-ecosystem/003-builder-spec.md** — Builder no-code tool
→ **010-ecosystem/005-forms-spec.md** — Forms engine
→ **006-infrastructure/003-cloudflare-architecture.md** — Cloudflare infrastructure
→ **006-infrastructure/002-github-org-architecture.md** — GitHub organization architecture

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
