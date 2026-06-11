---
id: "ZS-001-PLA"
title: "001 platform overview"
domain: "003-platform"
doc-type: "specification"
summary: >-
  Technical overview of the ZarishSphere Platform — a modular,
  Plane 0-compatible, Go-native platform-of-platforms for executing indexed
  global standards as digital services. Covers architecture principles, system
  boundaries, and the five-plane deployment model.
tags:
  - platform
  - architecture
  - overview
  - deployment-planes
  - platform-of-platforms
entity-type: "technical-specification"
version: "1.0.0"
status: "stable"
last_updated: 2026-06-10
last_verified: 2026-06-10
verified_by: "Mohammad Ariful Islam"
next_review: 2026-09-10
isolation_tier: "global"
canonical: true
depends_on:
  - "ZS-001-ZAR"
  - "ZS-005-ECO"
related:
  - "ZS-002-PLA"
  - "ZS-003-PLA"
  - "ZS-004-PLA"
  - "ZS-005-PLA"
  - "ZS-006-PLA"
  - "ZS-007-PLA"
  - "ZS-008-PLA"
  - "ZS-001-FOU"
capabilities:
  - agent-skill: "parse_001_platform_overview"
  - mcp-resource: "platform_overview"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
---

# 001-platform-overview.md
## ZarishSphere platform overview
### Architecture, deployment planes, and system boundaries

**Document type:** Specification
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [What the platform is](#1-what-the-platform-is)
2. [Architecture principles](#2-architecture-principles)
3. [System boundaries](#3-system-boundaries)
4. [Five-plane deployment model](#4-five-plane-deployment-model)
5. [Platform-of-platforms structure](#5-platform-of-platforms-structure)
6. [Technology stack summary](#6-technology-stack-summary)
7. [Cross-references](#7-cross-references)

---

## 1. What the platform is

The ZarishSphere Platform is the deployable infrastructure layer of the ZarishSphere ecosystem. It is a modular, Plane 0-compatible, Go-native platform-of-platforms that provides the execution environment for all ecosystem components.

### 1.1 What it does

- Hosts and executes domain modules (health, education, logistics, etc.)
- Runs the G2A Engine for standard-to-asset transformation
- Provides the Console, Marketplace, and Builder as browser-accessible services
- Manages forms, workflows, and data pipelines
- Synchronises data across deployment planes
- Provides identity, audit, and security infrastructure
- Exposes APIs for integration and extension

### 1.2 What it is not

The platform is not a hosted service (though a global SaaS instance will exist). It is deployable software. Anyone can deploy the full platform on their own infrastructure at zero cost.

## 2. Architecture principles

| Principle | Meaning |
|---|---|
| Plane 0 baseline | Every feature functions on a 4 GB air-gapped device with no internet |
| Go-native | All server-side components are Go binaries. No JVM, no Node.js runtime. |
| Module sovereignty | Every domain module is independently deployable. No module requires another. |
| GUI-first | Every function is accessible through the Console. CLI is always secondary (Law 6). |
| GitHub as control plane | All configuration, governance, and deployment state lives in GitHub. |
| Data portability | All data exportable in open formats (FHIR, CSV, JSON, Parquet) at any time. |
| Offline-first | Sync is asynchronous. No feature requires persistent connectivity. |
| Zero-cost | No paid tiers, no feature gates, no premium capabilities. |

## 3. System boundaries

### 3.1 What the platform includes

- Base system (IAM, encryption, audit, monitoring)
- Core runtime (G2A Engine, module runtime, form engine, workflow engine)
- All 13 ecosystem components (Console, Marketplace, Builder, Apps, Forms, SDK, CLI, API, Services, Modules, Distributions, Engine, System)
- FHIR R5 server (Go-native)
- Deployment tooling for all five planes

### 3.2 What the platform does not include

- ZARISH-INDEX content (separate repository group)
- ZARISH-STANDARDS transformation rules (separate repository group)
- Third-party standards documents (owned by their publishers)
- Deployer data (owned by the deployer)

## 4. Five-plane deployment model

| Plane | Environment | Hardware | Connectivity | Deployer manages |
|---|---|---|---|---|
| 0 — Air-gapped | No internet, single device | Any device, 4 GB+ RAM | None | Everything |
| 1 — Edge | Local network, intermittently connected | RPi 5 (8 GB) or equivalent | Occasional sync | OS + apps + data |
| 2 — District | Server with intermittent connectivity | Small server (8-16 GB) | Periodic | Apps + data |
| 3 — National | Self-hosted cloud | Server cluster (32+ GB) | Persistent | Config + data |
| 4 — Global SaaS | Fully managed multi-region | Cloud infrastructure | Always-on | Data only |

Every component of the platform must function across all five planes. No feature may be exclusive to higher planes.

## 5. Platform-of-platforms structure

The ZarishSphere Platform is not a monolithic system. It is a platform-of-platforms:

```
zarishsphere-platform/
├── system/              ← Base environment (IAM, encryption, audit, config)
├── engine/              ← Core runtime (G2A, module, form, workflow)
├── console/             ← Browser-based management center
├── marketplace/         ← Component discovery and deployment
├── builder/             ← No-code creation tool
├── apps/                ← Pre-built domain applications
├── forms/               ← Dynamic form engine
├── services/            ← Backend microservices
├── api/                 ← RESTful + GraphQL API gateway
├── modules/             ← Independently deployable domain packages
│   ├── health/
│   ├── education/
│   ├── logistics/
│   └── ... (40+ domains)
└── distributions/       ← Pre-packaged deployment bundles
```

Each component has its own specification in `zs-docs/010-ecosystem/`.

## 6. Technology stack summary

| Layer | Technology | Reason |
|---|---|---|
| Backend language | Go 1.26.4 | RAM efficiency, ARM64 cross-compile, single binary |
| Database | PostgreSQL 18.4 with JSONB | Open standard, planet-scale, Plane 0-capable |
| Message bus | NATS JetStream | 20 MB binary, offline queue, peer-to-peer mesh |
| Cache | Valkey 9.0.3 | Linux Foundation Redis fork, open-source |
| Object storage | MinIO | S3-compatible, self-hosted, ARM64 |
| Search | Typesense | Typo-tolerant, offline-capable |
| Vector DB | Qdrant | ARM64, local embeddings, RAG |
| Frontend | React 19.3.0 / TypeScript / Vite | PWA-capable, offline-first |
| Auth | Keycloak | OAuth 2.1, OIDC, SMART on FHIR |
| Orchestration | Docker Compose / K3s / Argo CD | Scales from RPi to cluster |
| Proxy | Traefik / Cloudflare Tunnel | Auto-TLS, edge routing |
| Monitoring | Grafana + Prometheus | Free tier, self-hosted |

All versions pinned. No `latest` tag in any production or pinned configuration.

## 7. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
