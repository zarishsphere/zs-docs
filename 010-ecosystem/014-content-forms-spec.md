---
id: "ZS-014-ECO"
title: "014 content forms spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for zs-content-forms — the repository for domain-agnostic form
  definitions stored and versioned as FHIR R5 Questionnaire resources. Forms
  are authored once and deployed across all planes without modification.
tags:
  - content
  - forms
  - fhir-questionnaire
  - repository
  - versioning
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
  - "ZS-005-ECO"
  - "ZS-005-PLA"
related:
  - "ZS-015-ECO"
  - "ZS-016-ECO"
  - "ZS-017-ECO"
  - "ZS-004-PLA"
capabilities:
  - agent-skill: "parse_014_content_forms_spec"
  - mcp-resource: "content_forms_spec"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
---

# 014-content-forms-spec.md
## zs-content-forms specification
### Form definitions repository

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
3. [Form definition format](#3-form-definition-format)
4. [Form lifecycle](#4-form-lifecycle)
5. [Plane 0 operation](#5-plane-0-operation)
6. [Cross-references](#6-cross-references)

---

## 1. Purpose

The `zs-content-forms` repository stores, versions, and distributes all domain-agnostic form definitions used across the ZarishSphere ecosystem. Forms are authored as FHIR R5 Questionnaire resources and consumed by the Forms Engine at runtime.

Key design principles:

- **Author once, deploy everywhere** — forms are plane-agnostic
- **Versioned immutably** — every change creates a new version
- **Domain-agnostic** — forms may reference any of the 40 domains
- **FHIR-native** — all forms are valid FHIR R5 Questionnaire resources

## 2. Repository structure

```
zs-content-forms/
├── forms/
│   ├── health/
│   │   ├── ncd-intake-v1.json
│   │   ├── maternal-registration-v2.json
│   │   └── immunization-record-v1.json
│   ├── education/
│   │   ├── student-enrollment-v1.json
│   │   └── attendance-record-v2.json
│   ├── protection/
│   │   ├── case-intake-v1.json
│   │   └── referral-form-v2.json
│   ├── logistics/
│   │   ├── supply-request-v1.json
│   │   └── inventory-count-v1.json
│   └── cross-domain/
│       ├── demographic-registration-v3.json
│       └── consent-form-v1.json
├── schemas/
│   ├── questionnaire-schema.json
│   └── form-manifest-schema.json
├── examples/
│   ├── ncd-intake-complete.json
│   ├── maternal-with-referral.json
│   └── multi-language-form.json
├── tests/
│   ├── validate-questionnaire.go
│   └── test-fixtures/
└── manifests/
    ├── health-forms.yaml
    └── education-forms.yaml
```

### 2.1 Directory conventions

| Directory | Purpose |
|---|---|
| `forms/{domain}/` | Form definitions organized by domain taxonomy |
| `schemas/` | JSON Schema for validating Questionnaire resources |
| `examples/` | Complete working examples with all fields populated |
| `tests/` | Automated validation and integration tests |
| `manifests/` | Indexing manifests for bulk loading and release packaging |

## 3. Form definition format

All forms are FHIR R5 Questionnaire resources. Every form must include:

### 3.1 Required fields

| Field | Description | Example |
|---|---|---|
| `resourceType` | Must be `Questionnaire` | `"Questionnaire"` |
| `id` | Unique form identifier | `"zs-ncd-intake-v1"` |
| `url` | Canonical URL | `"https://zarishsphere.org/fhir/Questionnaire/zs-ncd-intake"` |
| `version` | Semantic version | `"1.0.0"` |
| `status` | FHIR lifecycle status | `"active"` |
| `date` | Last modified date | `"2026-06-11"` |
| `name` | Machine-readable name | `"ZS_NCD_Intake"` |
| `title` | Human-readable title | `"NCD Intake Assessment"` |
| `item` | Question items array | Array of QuestionnaireItem |

### 3.2 Example

```json
{
  "resourceType": "Questionnaire",
  "id": "zs-ncd-intake-v1",
  "url": "https://zarishsphere.org/fhir/Questionnaire/zs-ncd-intake",
  "version": "1.0.0",
  "status": "active",
  "date": "2026-06-11",
  "name": "ZS_NCD_Intake",
  "title": "NCD Intake Assessment",
  "description": "Non-communicable disease intake assessment form",
  "purpose": "Initial patient assessment for NCD screening",
  "item": [
    {
      "linkId": "demographics",
      "text": "Patient Demographics",
      "type": "group",
      "item": [
        { "linkId": "full-name", "text": "Full Name", "type": "string", "required": true },
        { "linkId": "date-of-birth", "text": "Date of Birth", "type": "date" },
        { "linkId": "sex", "text": "Sex", "type": "choice",
          "answerOption": [
            { "valueCoding": { "code": "male", "display": "Male" } },
            { "valueCoding": { "code": "female", "display": "Female" } }
          ]
        }
      ]
    },
    {
      "linkId": "vitals",
      "text": "Vital Signs",
      "type": "group",
      "item": [
        { "linkId": "systolic", "text": "Systolic BP", "type": "integer", "unit": "mmHg" },
        { "linkId": "diastolic", "text": "Diastolic BP", "type": "integer", "unit": "mmHg" },
        { "linkId": "heart-rate", "text": "Heart Rate", "type": "integer", "unit": "bpm" }
      ]
    }
  ]
}
```

### 3.3 Multi-language support

Forms support multiple languages via the FHIR `Questionnaire.questionnaire` extension or by maintaining parallel translation files in `forms/{domain}/{form-id}/{locale}.json`.

## 4. Form lifecycle

```
[Draft] → [Review] → [Published] → [Deprecated]
```

| Stage | Description | Criteria |
|---|---|---|
| Draft | Initial development, may change | In progress, not ready for production |
| Review | Under review by domain experts | Submitted via PR, awaiting approval |
| Published | Ready for production use | Reviewed, tested, approved, and merged |
| Deprecated | Superseded by newer version | Newer version available, usage discouraged |

### 4.1 Versioning

Forms follow semantic versioning (`MAJOR.MINOR.PATCH`):

- **MAJOR** — breaking changes (field removed, type changed)
- **MINOR** — backward-compatible additions (new optional field)
- **PATCH** — fixes, translations, metadata updates

The version is reflected in both the `version` field and the form `id` suffix. Every release increments the form version.

> **Constraint:** The `latest` tag must never be used. Consumers must pin to a specific semantic version.

### 4.2 Deprecation policy

When a form is deprecated:

1. The `status` field changes to `"retired"`
2. A `replaces` or `replacedBy` field points to the successor form
3. The form remains in the repository for historical reference
4. Consumers receive a warning when loading a deprecated form

## 5. Plane 0 operation

At Plane 0, form definitions ship as pre-loaded static bundles:

- Forms are bundled into the distribution at deployment time
- No network access is required to load any form
- Form validation happens locally using the bundled schema
- Form responses queue locally and sync when connectivity permits
- Multi-language forms include all translations in the bundle

## 6. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
