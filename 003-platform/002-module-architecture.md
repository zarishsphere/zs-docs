---
id: "ZS-002-PLA"
title: "002 module architecture"
domain: "003-platform"
doc-type: "specification"
summary: >-
  Defines the module architecture for the ZarishSphere Platform. Every domain
  module is independently deployable, communicates via standard APIs, and
  follows the module sovereignty principle (Law 7).
tags:
  - modules
  - architecture
  - sovereignty
  - domain
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
  - "ZS-001-PLA"
related:
  - "ZS-008-PLA"
capabilities:
  - agent-skill: "parse_002_module_architecture"
  - mcp-resource: "module_architecture"
audience:
  - "contributors"
  - "deployers"
---

# 002-module-architecture.md
## Module architecture
### Sovereignty rules, interfaces, lifecycle

**Document type:** Specification
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Module sovereignty principle](#1-module-sovereignty-principle)
2. [Module structure](#2-module-structure)
3. [Module lifecycle](#3-module-lifecycle)
4. [Module communication](#4-module-communication)
5. [Module registry](#5-module-registry)
6. [Cross-references](#6-cross-references)

---

## 1. Module sovereignty principle

Every domain module is independently deployable. No module requires another module to function (Law 7). Modules communicate via standard APIs, not shared databases. Modules can be combined but never coupled.

| Rule | Meaning |
|---|---|
| Independent deployment | A module can be deployed alone without any other module |
| Independent data | Each module has its own database schema, not shared |
| Independent lifecycle | Each module can be updated, rolled back, or removed independently |
| Standard interfaces | Modules communicate through APIs, not direct database access |
| No cross-module coupling | A module must never import or depend on another module's internals |

## 2. Module structure

Each module has the same internal structure:

```
zs-module-[domain]/
├── api/                  ← API definitions (OpenAPI 3.1)
├── cmd/                  ← Entry points
├── internal/
│   ├── handler/          ← HTTP handlers
│   ├── service/          ← Business logic
│   ├── repository/       ← Data access
│   └── model/            ← Domain models
├── migrations/           ← Database migrations
├── forms/                ← Form definitions
├── workflows/            ← Workflow definitions
├── tests/                ← Module tests
├── Dockerfile
├── go.mod
└── README.md
```

### 2.1 Required artefacts

| Artefact | Format | Required |
|---|---|---|
| API specification | OpenAPI 3.1 YAML | Yes |
| Database migrations | SQL (golang-migrate) | Yes |
| Form definitions | FHIR Questionnaire JSON | Yes |
| Module manifest | YAML | Yes |
| Dockerfile | Docker | Yes |
| README | Markdown | Yes |

### 2.2 Module manifest

Every module must have a `manifest.yaml` at its root:

```yaml
id: ZS-MOD-health
name: Health Module
version: 1.0.0
domain: health
description: Domain module for health services
dependencies: []  # Modules must not require other modules
forms:
  - patient-registration
  - ncd-assessment
workflows:
  - referral
  - prescription
apis:
  - rest: https://api.zarishsphere.com/fhir/R5
```

## 3. Module lifecycle

| State | Description |
|---|---|
| Draft | Module specification exists in zs-docs, no implementation |
| Development | Code being written in private branch |
| Alpha | Deployable for testing, not for production |
| Stable | Production-ready, validated, documented |
| Deprecated | Replacement available, migration period active |
| Archived | No longer available, removed from Marketplace |

## 4. Module communication

### 4.1 API-based communication

Modules communicate exclusively through the API gateway. No module directly accesses another module's database.

```
Module A → API Gateway → Module B
         ↕               ↕
     Module A DB      Module B DB
```

### 4.2 Event-based communication

Modules publish and subscribe to NATS JetStream events for asynchronous communication:

| Event type | Purpose | Example |
|---|---|---|
| `domain.[module].created` | Entity created | `domain.health.patient-registered` |
| `domain.[module].updated` | Entity updated | `domain.logistics.shipment-dispatched` |
| `domain.[module].deleted` | Entity deleted | `domain.protection.case-closed` |

### 4.3 Cross-module data access

If Module A needs data from Module B, it must use Module B's API. Caching is permitted but must respect cache invalidation from Module B's events.

## 5. Module registry

All available modules are registered in the module registry, which powers the Marketplace and deployment tooling.

The registry is a single YAML index in the `zs-infra-module-registry` repository. Each module entry includes its manifest, supported planes, and deployment instructions.

## 6. Cross-references

→ **001-platform-overview.md** — Platform architecture context
→ **008-domain-registry.md** — All 40 domains
→ **010-ecosystem/010-modules-spec.md** — Module component specification
→ **001-meta/001-zarishsphere-constitution.md** — Law 7 (module sovereignty)

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
