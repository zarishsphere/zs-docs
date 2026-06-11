---
id: "ZS-006-PLA"
title: "006 api design"
domain: "003-platform"
doc-type: "specification"
summary: >-
  API design principles and contracts for the ZarishSphere Platform. RESTful
  and GraphQL APIs with OpenAPI 3.1 specifications, versioning strategy, and
  authentication model.
tags:
  - api
  - rest
  - graphql
  - openapi
  - versioning
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
  - "ZS-005-PLA"
related:
  - "ZS-007-PLA"
capabilities:
  - agent-skill: "parse_006_api_design"
  - mcp-resource: "api_design"
audience:
  - "contributors"
  - "deployers"
---

# 006-api-design.md
## API design
### Contracts, versioning, authentication

**Document type:** Specification
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [API design principles](#1-api-design-principles)
2. [API types](#2-api-types)
3. [Versioning](#3-versioning)
4. [Authentication and authorization](#4-authentication-and-authorization)
5. [Rate limiting](#5-rate-limiting)
6. [OpenAPI specifications](#6-openapi-specifications)
7. [Error handling](#7-error-handling)
8. [Cross-references](#8-cross-references)

---

## 1. API design principles

| Principle | Meaning |
|---|---|
| API-first | All capabilities are exposed via API before any GUI is built |
| RESTful by default | REST for CRUD operations |
| GraphQL for complex queries | GraphQL for dashboards and reporting |
| OpenAPI 3.1 | All endpoints documented with machine-readable specs |
| Consistent errors | Standard error format across all endpoints |
| Backward compatibility | Breaking changes require a new version |
| Rate-limited but free | No paid API tiers |

## 2. API types

### 2.1 RESTful APIs

| Base path | Service | Purpose |
|---|---|---|
| `https://api.zarishsphere.com/v1/` | API gateway | Core platform operations |
| `https://fhir.zarishsphere.com/R5/` | FHIR server | FHIR R5 operations |
| `https://data.zarishsphere.com/v1/` | ZARISH-INDEX | Standard index queries |

### 2.2 GraphQL API

A single GraphQL endpoint at `https://api.zarishsphere.com/graphql` that federates across all services. Used primarily for dashboards and reporting.

### 2.3 Webhook API

Event-driven notifications via registered webhook URLs. Events follow NATS event naming: `domain.[module].[action]`.

## 3. Versioning

| Strategy | Detail |
|---|---|
| Major version in URL path | `https://api.zarishsphere.com/v1/` |
| Breaking changes | Increment major version, maintain old version for 6 months |
| Non-breaking changes | Additive only in same version |
| Deprecation | Header warning on deprecated endpoints for 6 months |
| Sunset | Old version removed after 6-month deprecation period |

## 4. Authentication and authorization

| Method | Use case |
|---|---|
| GitHub OAuth | Console login |
| API tokens | Automated access (CI/CD, scripts) |
| SMART on FHIR OAuth | Third-party health app integration |
| Keycloak JWT | Service-to-service auth |

### 4.1 Scope model

Scopes follow the format `[resource]:[action]`:
- `patient:read` — read patient records
- `patient:write` — create/update patient records
- `form:deploy` — deploy form definitions
- `admin:users` — manage users

## 5. Rate limiting

| Tier | Rate limit | Cost |
|---|---|---|
| Anonymous | 10 req/min | Free |
| Authenticated (GitHub OAuth) | 100 req/min | Free |
| API token | 1,000 req/min | Free |
| Partner integration | Custom | Free |

No paid API tiers. Rate limits exist to prevent abuse, not to create artificial scarcity.

## 6. OpenAPI specifications

Every API has an OpenAPI 3.1 specification at:

```
https://api.zarishsphere.com/openapi/v1.yaml
https://fhir.zarishsphere.com/openapi/r5.yaml
```

Specifications are version-controlled in each service's repository and published as part of the CI/CD pipeline.

## 7. Error handling

All APIs use a consistent error format:

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Patient with ZS-UID ZS-NCD-2025-000001 was not found",
    "details": [],
    "request_id": "req_abc123"
  }
}
```

HTTP status codes follow standard conventions: 200 (success), 201 (created), 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found), 409 (conflict), 422 (validation error), 429 (rate limited), 500 (server error).

## 8. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
