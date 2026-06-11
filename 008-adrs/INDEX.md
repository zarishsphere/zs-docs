---
id: "ZS-INDEX-008"
title: "008 adrs index"
domain: "008-adrs"
doc-type: "index"
entity-type: "folder-index"
summary: "Index for the 008-adrs/ folder. 23 documents (23 stable)."
tags:
  - "index"
  - "navigation"
  - "adrs"
  - "decisions"
version: "1.0.0"
status: "stable"
last_updated: "2026-06-11"
isolation_tier: "global"
canonical: true
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
---

# 008-adrs/ index
## Architecture Decision Records

> Every significant technical and governance decision is recorded as an ADR. Each ADR follows the format defined in ZUSS §7.1: Decision, Context, Alternatives Considered, Reason, Consequences, Status.

---

## File index

| # | File | Description | Type | Status |
|---|---|---|---|---|
| 001 | [001-adr-go-as-primary-language.md](001-adr-go-as-primary-language.md) | ADR-001: Selection of Go as the primary engine language for the ZarishSphere Platform. Decision to u... | adr | Stable |
| 002 | [002-adr-cloudflare-as-edge-platform.md](002-adr-cloudflare-as-edge-platform.md) | ADR-002: Selection of Cloudflare as the edge platform for WAF, CDN, DNS, and global hosting for all ... | adr | Stable |
| 003 | [003-adr-github-as-government.md](003-adr-github-as-government.md) | ADR-003: GitOps and GitHub as the operational rule ownership and governance control plane for the Za... | adr | Stable |
| 004 | [004-adr-no-hapi-fhir.md](004-adr-no-hapi-fhir.md) | ADR-004: Rejection of Java HAPI FHIR and decision to build a Go-native FHIR server. Motivated by the... | adr | Stable |
| 005 | [005-adr-fhir-r5-over-r4.md](005-adr-fhir-r5-over-r4.md) | ADR-005: Enforcement of FHIR R5 as the canonical FHIR version for the ZarishSphere Platform. Decisio... | adr | Stable |
| 006 | [006-adr-zero-cost-toolchain.md](006-adr-zero-cost-toolchain.md) | ADR-006: Structural requirement for open-source, zero-cost toolchain dependencies across the entire ... | adr | Stable |
| 007 | [007-adr-markdown-first-documentation.md](007-adr-markdown-first-documentation.md) | ADR-007: Plaintext markdown-first documentation architecture standard for all ZarishSphere documenta... | adr | Stable |
| 008 | [008-adr-apache-cc-dual-license.md](008-adr-apache-cc-dual-license.md) | ADR-008: Dual-licensing rules for open-source modularity — Apache 2.0 for code, CC BY 4.0 for docume... | adr | Stable |
| 009 | [009-adr-no-vendor-lock-in.md](009-adr-no-vendor-lock-in.md) | ADR-009: Decoupling the platform layer from cloud infrastructure provider specific dependencies. Ens... | adr | Stable |
| 010 | [010-adr-gui-first-ux.md](010-adr-gui-first-ux.md) | ADR-010: High-fidelity UI/UX interactivity standards for field deployment. The Console is the primar... | adr | Stable |
| 011 | [011-adr-privacy-by-architecture.md](011-adr-privacy-by-architecture.md) | ADR-011: All ZarishSphere platform data architectures enforce privacy at the infrastructure layer. I... | adr | Stable |
| 012 | [012-adr-no-single-person-dependency.md](012-adr-no-single-person-dependency.md) | ADR-012: No feature, workflow, critical function, API key, credential, or operational process in the... | adr | Stable |
| 013 | [013-adr-postgresql-primary-database.md](013-adr-postgresql-primary-database.md) | ADR-013: PostgreSQL 18.4 as the primary relational database for the ZarishSphere Platform. JSONB for... | adr | Stable |
| 014 | [014-adr-nats-jetstream-messaging.md](014-adr-nats-jetstream-messaging.md) | ADR-014: NATS JetStream as the async messaging backbone for the ZarishSphere Platform. Single 20MB b... | adr | Stable |
| 015 | [015-adr-valkey-for-caching.md](015-adr-valkey-for-caching.md) | ADR-015: Valkey 9.0.3 as the in-memory caching layer for the ZarishSphere Platform. Adopted over Red... | adr | Stable |
| 016 | [016-adr-opentofu-infrastructure-as-code.md](016-adr-opentofu-infrastructure-as-code.md) | ADR-016: OpenTofu 1.9.1 as the Infrastructure as Code tool for the ZarishSphere Platform. Adopted ov... | adr | Stable |
| 017 | [017-adr-argocd-gitops.md](017-adr-argocd-gitops.md) | ADR-017: Argo CD 2.14.10 as the GitOps deployment engine for the ZarishSphere Platform. CNCF graduat... | adr | Stable |
| 018 | [018-adr-cilium-service-mesh.md](018-adr-cilium-service-mesh.md) | ADR-018: Cilium 1.17.4 as the Kubernetes networking, observability, and security layer for the Zaris... | adr | Stable |
| 019 | [019-adr-carbon-design-system.md](019-adr-carbon-design-system.md) | ADR-019: IBM Carbon Design System 1.82.1 as the UI component library for the ZarishSphere Platform. ... | adr | Stable |
| 020 | [020-adr-microfrontend-architecture.md](020-adr-microfrontend-architecture.md) | ADR-020: Microfrontend architecture for the ZarishSphere Platform frontend using Vite 8.1.2 Module F... | adr | Stable |
| 021 | [021-adr-powersync-mobile-offline.md](021-adr-powersync-mobile-offline.md) | ADR-021: PowerSync 1.6.1 as the mobile offline database synchronization engine for the ZarishSphere ... | adr | Stable |
| 022 | [022-adr-typescript-strict-mode.md](022-adr-typescript-strict-mode.md) | ADR-022: TypeScript 5.8.4 with strict mode enabled for all ZarishSphere Platform frontend code. Stri... | adr | Stable |
| 023 | [023-adr-flutter-cross-platform-mobile.md](023-adr-flutter-cross-platform-mobile.md) | ADR-023: Flutter 3.29.2 (Dart 3.7.2) as the cross-platform mobile framework for all ZarishSphere Pla... | adr | Stable |

---

## Navigation

- **Parent:** [Root index](../INDEX.md)
- **Previous:** [007-tech-stack/](../007-tech-stack/INDEX.md)
- **Next:** [009-operations/](../009-operations/INDEX.md)

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
