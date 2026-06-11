---
id: "ZS-008-ECO"
title: "008 api spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for the ZarishSphere API — RESTful and GraphQL APIs for all
  ecosystem components. API-first design with OpenAPI 3.1 specifications.
  Free to use with no paid tiers.
tags:
  - api
  - rest
  - graphql
  - openapi
  - webhooks
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
  - "ZS-006-PLA"
related:
  - "ZS-006-ECO"
  - "ZS-007-ECO"
  - "ZS-009-ECO"
capabilities:
  - agent-skill: "parse_008_api_spec"
  - mcp-resource: "api_spec"
audience:
  - "contributors"
  - "deployers"
---

# 008-api-spec.md
## ZarishSphere API specification
### REST, GraphQL, webhooks

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [API types](#2-api-types)
3. [Authentication](#3-authentication)
4. [Rate limiting](#4-rate-limiting)
5. [OpenAPI specifications](#5-openapi-specifications)
6. [Cross-references](#6-cross-references)

---

## 1. Purpose

The ZarishSphere API is the programmatic interface for all ecosystem components. It provides RESTful and GraphQL endpoints, webhook support, and OpenAPI 3.1 specifications. All APIs are free to use with no paid tiers.

## 2. API types

| Type | Endpoint | Purpose |
|---|---|---|
| REST | `api.zarishsphere.com/v1/` | Core CRUD operations |
| FHIR REST | `fhir.zarishsphere.com/R5/` | Health data operations |
| GraphQL | `api.zarishsphere.com/graphql` | Dashboards and complex queries |
| Webhooks | Configured per integration | Event-driven notifications |
| ZARISH-INDEX | `data.zarishsphere.com/v1/` | Standard index queries |

## 3. Authentication

| Method | Use case |
|---|---|
| GitHub OAuth | Console and developer access |
| API tokens | Automated and CI/CD access |
| SMART on FHIR OAuth | Third-party health app integration |
| Keycloak JWT | Service-to-service communication |

## 4. Rate limiting

All tiers are free:
- Anonymous: 10 req/min
- Authenticated: 100 req/min
- API token: 1,000 req/min
- Partner: Custom (by arrangement)

## 5. OpenAPI specifications

Every API endpoint is documented with an OpenAPI 3.1 specification at:
- `https://api.zarishsphere.com/openapi/v1.yaml`
- `https://fhir.zarishsphere.com/openapi/r5.yaml`

Specifications are version-controlled and published through CI/CD.

## 6. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
