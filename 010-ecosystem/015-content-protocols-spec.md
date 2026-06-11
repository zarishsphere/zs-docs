---
id: "ZS-015-ECO"
title: "015 content protocols spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for zs-content-protocols — the repository for machine-readable
  clinical and operational protocol definitions. Protocols drive the G2A Engine
  and define decision trees, workflows, and compliance rules.
tags:
  - content
  - protocols
  - clinical
  - workflows
  - decision-trees
  - g2a
entity-type: "component-specification"
version: "1.0.0"
status: "stable"
last_updated: 2026-06-11
last_verified: 2026-06-11
verified_by: "Mohammad Ariful Islam"
next_review: 2026-09-11
isolation_tier: "global"
canonical: true
depends_on:
  - "ZS-004-PLA"
  - "ZS-005-ZSI"
related:
  - "ZS-016-ECO"
  - "ZS-017-ECO"
  - "ZS-010-ECO"
  - "ZS-012-ECO"
capabilities:
  - agent-skill: "parse_015_content_protocols_spec"
  - mcp-resource: "content_protocols_spec"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
---

# 015-content-protocols-spec.md
## zs-content-protocols specification
### Protocol definitions repository

**Document type:** Component spec
**Date:** June 11, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Repository structure](#2-repository-structure)
3. [Protocol definition format](#3-protocol-definition-format)
4. [Protocol lifecycle](#4-protocol-lifecycle)
5. [Relation to G2A Engine](#5-relation-to-g2a-engine)
6. [Plane 0 operation](#6-plane-0-operation)
7. [Cross-references](#7-cross-references)

---

## 1. Purpose

The `zs-content-protocols` repository stores, versions, and distributes machine-readable protocol definitions — clinical guidelines, operational SOPs, decision trees, and workflow templates. These protocols are consumed by the G2A Engine to transform standards into executable actions.

Key design principles:

- **Machine-readable first** — protocols are structured data, not prose
- **Standards-aligned** — each protocol traces to a ZARISH-STANDARDS entry
- **Executable** — protocols drive automated decision support and workflow orchestration
- **Versioned immutably** — every change creates a new protocol version

## 2. Repository structure

```
zs-content-protocols/
├── protocols/
│   ├── health/
│   │   ├── ncd-screening-v1.yaml
│   │   ├── malnutrition-treatment-v2.yaml
│   │   └── immunization-schedule-v1.yaml
│   ├── protection/
│   │   ├── child-protection-intake-v1.yaml
│   │   └── gbv-clinical-care-v2.yaml
│   ├── wash/
│   │   └── water-quality-testing-v1.yaml
│   └── cross-domain/
│       ├── referral-guidelines-v1.yaml
│       └── consent-procedure-v1.yaml
├── workflows/
│   ├── approval-chains/
│   │   ├── emergency-funding-approval-v1.yaml
│   │   └── supply-request-approval-v2.yaml
│   └── notification-rules/
│       ├── critical-lab-alert-v1.yaml
│       └── referral-trigger-v1.yaml
├── decision-trees/
│   ├── triage-protocol-v1.yaml
│   ├── tb-screening-algorithm-v2.yaml
│   └── malnutrition-classification-v1.yaml
├── schemas/
│   ├── protocol-schema.json
│   └── workflow-schema.json
├── examples/
│   └── ncd-screening-complete.yaml
└── tests/
    ├── validate-protocols.go
    └── test-fixtures/
```

### 2.1 Directory conventions

| Directory | Purpose |
|---|---|
| `protocols/{domain}/` | Protocol definitions organized by domain taxonomy |
| `workflows/` | Operational workflow and approval chain definitions |
| `decision-trees/` | Decision support algorithms and triage protocols |
| `schemas/` | JSON Schema for protocol YAML validation |
| `examples/` | Complete working examples |
| `tests/` | Automated validation and integration tests |

## 3. Protocol definition format

Protocols are defined in YAML using a structured format that aligns with the FHIR R5 PlanDefinition and ActivityDefinition resources.

### 3.1 Core protocol structure

```yaml
# ncd-screening-v1.yaml
protocol:
  id: zs-ncd-screening-v1
  name: NCD Screening Protocol
  version: 1.0.0
  status: active
  domain: health
  source:
    standard: WHO PEN
    zarish-index-id: ZS-HLT-0014
    zarish-standards-id: ZS-STD-HLT-0014

  triggers:
    - event: patient-registration
      condition: age >= 40
      action: initiate-screening

  steps:
    - id: step-1
      name: Blood Pressure Measurement
      description: Measure blood pressure using automated device
      actor: clinician
      inputs:
        - systolic: integer
        - diastolic: integer
      outputs:
        - bp-category: choice
      rules:
        - if: systolic >= 180 OR diastolic >= 120
          then: set bp-category = "hypertensive-crisis"
          action: urgent-referral
        - if: systolic >= 140 OR diastolic >= 90
          then: set bp-category = "hypertensive"
          action: initiate-treatment
        - if: systolic >= 130 OR diastolic >= 85
          then: set bp-category = "pre-hypertensive"
          action: lifestyle-counseling
        - else: set bp-category = "normal"

    - id: step-2
      name: Blood Glucose Test
      description: Random blood glucose measurement
      actor: clinician
      inputs:
        - glucose-mgdl: integer
      rules:
        - if: glucose-mgdl >= 200
          then: action: diabetes-referral

  output:
    - risk-score: calculated
    - recommendations: list
```

### 3.2 Workflow definition

```yaml
# emergency-funding-approval-v1.yaml
workflow:
  id: zs-emergency-funding-approval-v1
  name: Emergency Funding Approval
  version: 1.0.0

  states:
    - name: submitted
      initial: true
    - name: manager-review
    - name: finance-review
    - name: approved
    - name: rejected

  transitions:
    - from: submitted
      to: manager-review
      action: submit-request
    - from: manager-review
      to: finance-review
      condition: amount <= 50000
      action: approve-manager
    - from: manager-review
      to: rejected
      condition: amount > 50000
    - from: finance-review
      to: approved
      action: approve-finance
    - from: finance-review
      to: rejected
      action: reject-finance
```

### 3.3 Decision tree definition

```yaml
# triage-protocol-v1.yaml
decision-tree:
  id: zs-triage-protocol-v1
  name: Emergency Triage Protocol
  version: 1.0.0

  root:
    question: Is the patient breathing?
    answers:
      - value: "no"
        action: immediate-resuscitation
        next:
          question: Is breathing restored?
          answers:
            - value: "yes"
              outcome: urgent-care
            - value: "no"
              outcome: deceased
              notify: manager
      - value: "yes"
        next:
          question: Is the patient conscious?
          answers:
            - value: "no"
              outcome: urgent-care
            - value: "yes"
              next:
                question: Trauma present?
                answers:
                  - value: "yes"
                    outcome: trauma-bay
                  - value: "no"
                    outcome: general-queue
```

## 4. Protocol lifecycle

```
[Draft] → [Review] → [Published] → [Deprecated]
```

| Stage | Description | Criteria |
|---|---|---|
| Draft | Initial development | In progress, not ready for production |
| Review | Under domain expert review | PR submitted, awaiting approval |
| Published | Ready for production | Reviewed, tested, and merged |
| Deprecated | Superseded | Newer version available |

### 4.1 Versioning

Protocols follow semantic versioning tied to the source standard version. When a referenced standard is updated (e.g., WHO releases new PEN guidelines), a new protocol version is created.

> **Constraint:** The `latest` tag must never be used. Consumers must pin to a specific semantic version.

### 4.2 Standards traceability

Every published protocol must include:

- `source.standard` — name of the source standard or guideline
- `source.zarish-index-id` — corresponding ZARISH-INDEX entry
- `source.zarish-standards-id` — corresponding ZARISH-STANDARDS entry

This traceability chain ensures every executable protocol is grounded in an indexed standard.

## 5. Relation to G2A Engine

The G2A Engine (Guideline-to-Action) consumes protocols from `zs-content-protocols` to:

1. **Transform standards** — convert ZARISH-STANDARDS entries into executable protocol steps
2. **Drive decision support** — evaluate protocol rules against patient data
3. **Orchestrate workflows** — manage approval chains and state transitions
4. **Generate alerts** — trigger notifications based on protocol conditions

The pipeline is:

```
ZARISH-INDEX → ZARISH-STANDARDS → zs-content-protocols → G2A Engine → Console/Forms
```

## 6. Plane 0 operation

At Plane 0, protocols ship as pre-loaded bundles:

- All protocols for the deployed distribution are bundled at deployment time
- Decision trees execute entirely locally — no network calls
- Workflow state is tracked in the local engine state store
- Protocol updates arrive via sync bundles from higher planes
- AI-dependent protocol features are disabled

## 7. Cross-references

→ **003-platform/004-g2a-engine.md** — G2A Engine that consumes protocols
→ **005-zarish-standards/002-transformation-model.md** — Standards-to-protocol transformation
→ **010-modules-spec.md** — Modules that define protocol-dependent features
→ **003-platform/003-deployment-planes.md** — Plane specifications for protocol deployment
→ **003-platform/005-fhir-architecture.md** — FHIR PlanDefinition resource alignment
→ **001-meta/001-zarishsphere-constitution.md** — Law 3 (every standard is executable)

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
