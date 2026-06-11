---
id: "ZS-005-ECO"
title: "005 forms spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for ZarishSphere Forms — a dynamic form engine that generates
  browser-based forms from ZARISH-STANDARDS definitions. Forms work offline
  and support all data types across all domains.
tags:
  - forms
  - engine
  - offline
  - fhir-questionnaire
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
  - "ZS-004-PLA"
related:
  - "ZS-003-ECO"
  - "ZS-004-ECO"
  - "ZS-012-ECO"
capabilities:
  - agent-skill: "parse_005_forms_spec"
  - mcp-resource: "forms_spec"
audience:
  - "contributors"
  - "deployers"
---

# 005-forms-spec.md
## ZarishSphere Forms specification
### Dynamic form engine

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [How forms work](#2-how-forms-work)
3. [Form definition format](#3-form-definition-format)
4. [Offline operation](#4-offline-operation)
5. [Customization](#5-customization)
6. [Cross-references](#6-cross-references)

---

## 1. Purpose

ZarishSphere Forms is a dynamic form engine that generates browser-based forms directly from ZARISH-STANDARDS definitions. It is the primary data collection interface for the entire ecosystem.

## 2. How forms work

1. A standard is indexed in ZARISH-INDEX (e.g., WHO nutrition protocol)
2. ZARISH-STANDARDS transforms it into a form definition
3. The Form Engine renders it as a browser-based form
4. Collected data populates the appropriate module
5. Forms can be customized via the Builder without code
6. Forms work offline on all planes

## 3. Form definition format

Forms are defined as FHIR Questionnaire resources:

```json
{
  "resourceType": "Questionnaire",
  "id": "zs-ncd-intake-v1",
  "status": "active",
  "item": [
    {
      "linkId": "blood-pressure",
      "text": "Blood Pressure",
      "type": "group",
      "item": [
        { "linkId": "systolic", "text": "Systolic", "type": "integer" },
        { "linkId": "diastolic", "text": "Diastolic", "type": "integer" }
      ]
    }
  ]
}
```

This is the canonical form definition format. XLSForm (KoboToolbox) import/export is supported for interoperability.

## 4. Offline operation

Forms work fully offline:
- Form definitions are cached locally on first load
- Submitted data is queued in local storage
- Sync occurs automatically when connectivity is available
- No data loss on connectivity interruption

## 5. Customization

Forms can be customized through the Builder:
- Add or remove fields
- Change field types
- Modify validation rules
- Update display logic
- Translate labels
- Change styling

All customizations are saved as new form versions. Original definitions remain available.

## 6. Cross-references

→ **003-builder-spec.md** — Form customization
→ **004-apps-spec.md** — Forms used by apps
→ **012-engine-spec.md** — Form engine runtime
→ **003-platform/004-g2a-engine.md** — G2A form generation
→ **001-meta/004-writing-rules.md** — Form ID patterns

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
