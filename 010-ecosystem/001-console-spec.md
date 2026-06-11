---
id: "ZS-001-ECO"
title: "001 console spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for the ZarishSphere Console — the browser-based management
  center for the entire ecosystem. Every function is achievable through the
  Console without terminal access or programming knowledge.
tags:
  - console
  - gui
  - management
  - no-code
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
  - "ZS-002-ECO"
  - "ZS-003-ECO"
  - "ZS-005-ECO"
  - "ZS-008-ECO"
capabilities:
  - agent-skill: "parse_001_console_spec"
  - mcp-resource: "console_spec"
audience:
  - "contributors"
  - "deployers"
---

# 001-console-spec.md
## ZarishSphere Console specification
### Browser-based management center

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Capabilities](#2-capabilities)
3. [User interface principles](#3-user-interface-principles)
4. [Architecture](#4-architecture)
5. [Plane 0 operation](#5-plane-0-operation)
6. [Cross-references](#6-cross-references)

---

## 1. Purpose

The Console is the primary user interface for the entire ZarishSphere ecosystem. It provides browser-based access to every ecosystem function — browsing standards, managing modules, deploying apps, configuring users, monitoring health — without requiring terminal access, code editing, or programming knowledge.

## 2. Capabilities

| Capability | Description |
|---|---|
| Dashboard | System health, usage stats, recent activity |
| Index browser | Browse and search ZARISH-INDEX across all domains |
| Marketplace | Discover, install, and manage ecosystem components |
| Module manager | Deploy, configure, update, and remove domain modules |
| App launcher | Launch and manage pre-built applications |
| Form manager | Browse, customize, and deploy form templates |
| Builder | Launch the no-code Builder tool |
| User management | Manage users, roles, permissions |
| Deployment manager | Configure and monitor deployments across planes |
| Data export | Export data in open formats |
| Audit log viewer | View and search audit logs |
| Settings | System configuration, integrations, notifications |

## 3. User interface principles

- **No-code first** — every function via GUI. CLI is always secondary (Law 6).
- **Progressive disclosure** — simple views by default, advanced options on request.
- **Offline-capable** — Console works as PWA on Plane 0 and Plane 1.
- **Mobile-responsive** — full functionality on tablets and phones.
- **Multi-language** — English, Bengali, Rohingya languages from day one.
- **Accessible** — WCAG 2.2 AA compliance.

## 4. Architecture

| Component | Technology |
|---|---|
| Frontend framework | React 19 + TypeScript |
| Build tool | Vite 8 |
| PWA | Workbox 7 |
| State management | Zustand |
| API communication | REST + GraphQL |
| Authentication | Keycloak OIDC (GitHub OAuth optional) |

## 5. Plane 0 operation

The Console runs as a fully offline PWA on Plane 0. All management functions work without connectivity. Changes are queued locally and synced when connectivity is available.

## 6. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
