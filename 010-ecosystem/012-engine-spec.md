---
id: "ZS-012-ECO"
title: "012 engine spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for the ZarishSphere Engine — the core runtime that executes
  G2A transformations, runs domain modules, renders forms, orchestrates
  workflows, synchronizes offline data, and generates reports.
tags:
  - engine
  - runtime
  - g2a
  - modules
  - workflow
  - orchestration
entity-type: "component-specification"
version: "1.0.0"
status: "stable"
last_updated: 2026-06-10
last_verified: 2026-06-10
verified_by: "Mohammad Ariful Islam"
next_review: 2026-09-10
isolation_tier: "global"
canonical: true
depends_on:
  - "ZS-005-ECO"
related:
  - "ZS-013-ECO"
  - "ZS-004-PLA"
  - "ZS-005-ECO"
  - "ZS-009-ECO"
capabilities:
  - agent-skill: "parse_012_engine_spec"
  - mcp-resource: "engine_spec"
audience:
  - "contributors"
  - "deployers"
---

# 012-engine-spec.md
## ZarishSphere Engine specification
### Core runtime

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Engine sub-components](#2-engine-sub-components)
3. [Execution model](#3-execution-model)
4. [Plane 0 operation](#4-plane-0-operation)
5. [Cross-references](#5-cross-references)

---

## 1. Purpose

The ZarishSphere Engine is the core runtime that executes all platform operations. It is the execution layer beneath every other component — the Console, Marketplace, Builder, Apps, Forms, Services, and Modules all depend on the Engine.

## 2. Engine sub-components

| Sub-component | Purpose | Technology |
|---|---|---|
| G2A Engine | Guideline-to-action transformation | Go + Python |
| Module runtime | Execution environment for domain modules | Go |
| Form engine | Dynamic form rendering and data capture | Go + React |
| Workflow engine | Approval chains, data pipelines, automation | Go + NATS |
| Sync engine | Offline data synchronization | Go + NATS JetStream |
| Report engine | Dashboard and report generation | Go + Grafana |

## 3. Execution model

```
Request → API Gateway → Engine orchestrator → Sub-component
                                                  ↓
                                           PostgreSQL / NATS / MinIO
                                                  ↓
                                              Response
```

The Engine orchestrator routes requests to the appropriate sub-component based on the request type. Each sub-component is independently deployable.

## 4. Plane 0 operation

At Plane 0, the Engine runs in standalone mode:
- Single binary with embedded sub-components
- SQLite instead of PostgreSQL
- Local file storage instead of MinIO
- NATS in single-node mode
- AI-dependent features disabled
- Forms pre-rendered as static bundles

## 5. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
