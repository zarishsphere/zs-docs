---
id: "ZS-013-ECO"
title: "013 system spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for the ZarishSphere System — the base operating environment
  providing IAM, encryption, configuration, monitoring, backup, and audit
  infrastructure. Every other component depends on the System layer.
tags:
  - system
  - infrastructure
  - iam
  - security
  - monitoring
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
  - "ZS-012-ECO"
  - "ZS-009-ECO"
  - "ZS-003-PLA"
capabilities:
  - agent-skill: "parse_013_system_spec"
  - mcp-resource: "system_spec"
audience:
  - "contributors"
  - "deployers"
---

# 013-system-spec.md
## ZarishSphere System specification
### Base operating environment

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [System components](#2-system-components)
3. [Security model](#3-security-model)
4. [Plane 0 adaptation](#4-plane-0-adaptation)
5. [Cross-references](#5-cross-references)

---

## 1. Purpose

The ZarishSphere System is the base operating environment for the entire ecosystem. It provides the foundational infrastructure — identity, security, audit, configuration, monitoring, and backup — that every other component depends on.

## 2. System components

| Component | Purpose | Technology |
|---|---|---|
| Identity and access management | Authentication, authorization, roles | Keycloak + Go middleware |
| Encryption and key management | Data at rest, in transit, emergency key destruction | Vault + AES-256-GCM |
| Configuration management | System and component configuration | GitHub + viper |
| Health monitoring | Service health, alerts, uptime | Grafana + Prometheus |
| Backup and recovery | Automated backup, point-in-time recovery | pg_dump + MinIO |
| Audit infrastructure | Immutable audit log, hash-chain | PostgreSQL + hash-chain |

## 3. Security model

### 3.1 Identity tiers

| Tier | Population | Auth method |
|---|---|---|
| Community worker | All | PIN (4-digit) |
| Clinician | All | Username + password |
| Manager | All | MFA |
| Admin | Host community | MFA + SSO |
| Patient | All | ZS-UID only |

### 3.2 Encryption

- Data at rest: AES-256-GCM (PostgreSQL pgcrypto + Vault-managed keys)
- Data in transit: TLS 1.3 (Cloudflare + mutual TLS for service mesh)
- Emergency key destruction: separate key store, 30-second destruction via GUI

### 3.3 Audit

Every operation generates an immutable audit log entry. Entries are hash-chained: each entry includes the hash of the previous entry. Tampering with any historical entry breaks the chain and triggers an alert.

## 4. Plane 0 adaptation

At Plane 0, the System layer is minimal:
- Identity: basic local auth (no Keycloak)
- Encryption: local key file with emergency destruction
- Config: local YAML file
- Monitoring: basic health endpoint
- Backup: SQLite dump to removable media
- Audit: local SQLite, exported on sync

## 5. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
