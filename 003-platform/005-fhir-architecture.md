---
id: "ZS-005-PLA"
title: "005 fhir architecture"
domain: "003-platform"
doc-type: "specification"
summary: >-
  FHIR R5 integration architecture for the ZarishSphere Platform. Covers the
  Go-native FHIR server, resource model, SMART on FHIR, offline capability,
  and the FHIR R5 compliance roadmap.
tags:
  - fhir
  - r5
  - interoperability
  - health
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
  - "ZS-007-PLA"
capabilities:
  - agent-skill: "parse_005_fhir_architecture"
  - mcp-resource: "fhir_architecture"
audience:
  - "contributors"
  - "deployers"
---

# 005-fhir-architecture.md
## FHIR R5 integration architecture
### Go-native FHIR server, resource model, compliance roadmap

**Document type:** Specification
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [FHIR in the ecosystem](#1-fhir-in-the-ecosystem)
2. [Go-native FHIR server](#2-go-native-fhir-server)
3. [R5 vs R4 decision](#3-r5-vs-r4-decision)
4. [Core resource profiles](#4-core-resource-profiles)
5. [SMART on FHIR](#5-smart-on-fhir)
6. [Offline FHIR](#6-offline-fhir)
7. [FHIR compliance roadmap](#7-fhir-compliance-roadmap)
8. [Cross-references](#8-cross-references)

---

## 1. FHIR in the ecosystem

FHIR is the canonical health data standard for the ZarishSphere Platform. It is used for:
- All clinical data exchange
- Form definitions (FHIR Questionnaire)
- Decision rules (FHIR PlanDefinition)
- Care plans (FHIR CarePlan)
- Data export and interoperability

Non-health modules may use simpler data models, but must be able to produce FHIR-equivalent outputs for cross-domain reporting.

## 2. Go-native FHIR server

HAPI FHIR (Java) is explicitly rejected forever (ADR-007). The Go-native FHIR server (`zs-fhir-server`) is the only FHIR server in the ecosystem.

| Metric | HAPI FHIR (Java) | zs-fhir-go (Go) |
|---|---|---|
| RAM at rest | 2-3 GB | 50-150 MB |
| Startup time | 30-90 seconds | Under 1 second |
| Requests/second | 500-1,000 | 5,000-10,000 |
| Docker image | 600-800 MB | 15-25 MB |
| RPi 5 viable | No | Yes |
| Cold start | Impossible | Under 100 ms |

### 2.1 Dependencies

| Library | Version | Purpose |
|---|---|---|
| `fhir-toolbox-go` (damedic) | Pinned | FHIR types and operations |
| `gofhir-models` (fastenhealth) | 0.0.7 | Generated Go structs for R5 |

## 3. R5 vs R4 decision

FHIR R5 (5.0.0) is the canonical version. R4 bridge maintained for partner compatibility.

| Reason for R5 | Detail |
|---|---|
| Topic-based Subscriptions | Enables event-driven architecture natively |
| WHO SMART Guidelines | All new guidelines built on R5 |
| Future-proof | Avoids R4 to R5 migration later |

R4 compatibility is provided via a translation layer that converts R4 requests to R5 internally and maps responses back.

## 4. Core resource profiles

| Resource | Profile | Purpose |
|---|---|---|
| Patient | zs-patient | Patient demographics with ZS-UID |
| Encounter | zs-encounter | Clinical encounters |
| Observation | zs-observation | Vital signs, lab results |
| Condition | zs-condition | Diagnoses and problems |
| MedicationRequest | zs-medication | Prescriptions |
| Questionnaire | zs-questionnaire | Form definitions |
| QuestionnaireResponse | zs-questionnaire-response | Submitted form data |
| CarePlan | zs-careplan | Care plans |
| PlanDefinition | zs-plan-definition | Clinical decision rules |

Each profile is documented at `https://zarishsphere.org/fhir/StructureDefinition/zs-[resource]`.

## 5. SMART on FHIR

SMART on FHIR 2.1 is supported for:

- Third-party app integration
- OAuth 2.1 scoped access
- Launch context for patient and encounter

Keycloak is the authorization server. Scope enforcement happens at the API gateway.

## 6. Offline FHIR

All FHIR operations work offline at Plane 0 and Plane 1:
- Resources are cached locally
- Writes queue in a local NATS buffer
- Sync occurs when connectivity is available
- Conflict resolution uses last-write-wins with audit trail

## 7. FHIR compliance roadmap

| Phase | Resources | Milestone |
|---|---|---|
| V1 | Patient, Encounter, Observation, Condition, MedicationRequest, Questionnaire | Camp 1W NCD clinic |
| V1.1 | CarePlan, CareTeam, ServiceRequest, Task, DiagnosticReport | Multi-site scale |
| V1.2 | R5 topic-based Subscriptions, Bulk export, SMART on FHIR 2.1 | National deployment |
| V2 | Full R5 resource set, CapabilityStatement | Global SaaS |

## 8. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
