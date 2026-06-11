---
id: "ZS-003-ECO"
title: "003 builder spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for the ZarishSphere Builder — a GUI-based no-code creation
  tool for building forms, workflows, modules, and apps. Everything built in
  the Builder can be exported as code and committed to GitHub.
tags:
  - builder
  - no-code
  - forms
  - workflows
  - gui
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
  - "ZS-001-ECO"
  - "ZS-005-ECO"
  - "ZS-004-ECO"
capabilities:
  - agent-skill: "parse_003_builder_spec"
  - mcp-resource: "builder_spec"
audience:
  - "contributors"
  - "deployers"
---

# 003-builder-spec.md
## ZarishSphere Builder specification
### No-code creation tool

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Builder capabilities](#2-builder-capabilities)
3. [Output format](#3-output-format)
4. [GitHub integration](#4-github-integration)
5. [Cross-references](#5-cross-references)

---

## 1. Purpose

The Builder is a GUI-based creation tool that lets anyone build forms, workflows, modules, and apps without writing code. It is the mechanism through which deployers customize their ZarishSphere deployment to their specific needs — no programming knowledge required.

## 2. Builder capabilities

| Capability | Description |
|---|---|
| Drag-and-drop form builder | Create forms from a palette of field types (text, number, date, select, etc.) |
| Visual workflow designer | Design approval flows, data pipelines, notification rules |
| Module composer | Combine existing components into new configurations |
| App assembler | Create custom domain applications from available modules |
| Template creator | Save configurations as reusable templates for the Marketplace |

### 2.1 Form builder specifics

- Field types: text, number, date, datetime, select, multi-select, radio, checkbox, file, image, location, barcode
- Validation rules: required, min/max, pattern, conditional required
- Display logic: show/hide fields based on other field values
- Scoring: auto-calculate scores from field values
- Multi-language: labels in all configured languages

### 2.2 Workflow builder specifics

- Node types: start, form, decision, approval, notification, integration, end
- Transitions: conditional branching, parallel paths, timeouts
- Approvals: single, multi-stage, parallel
- Notifications: email, SMS, in-app

## 3. Output format

Everything built in the Builder can be exported as:

| Format | Purpose |
|---|---|
| YAML | Configuration files |
| JSON | Data exchange |
| Markdown | Documentation |
| FHIR Questionnaire JSON | Health form standards |
| XLSForm | KoboToolbox compatibility |

## 4. GitHub integration

The Builder can commit outputs directly to a GitHub repository. This ensures:
- All changes are version-controlled (Law 1)
- Changes are auditable
- Rollback is always possible
- Collaboration is enabled through PR review

The GitHub integration is optional. Builder outputs can be downloaded and used offline.

## 5. Cross-references

→ **001-console-spec.md** — Console-based access to Builder
→ **005-forms-spec.md** — Form engine that renders Builder outputs
→ **004-apps-spec.md** — Apps built with the Builder
→ **001-meta/001-zarishsphere-constitution.md** — Law 6 (GUI-first), Law 1 (GitHub as government)

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
