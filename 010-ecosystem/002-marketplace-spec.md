---
id: "ZS-002-ECO"
title: "002 marketplace spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for the ZarishSphere Marketplace — the discovery and
  deployment hub for all ecosystem components. All items are open-source and
  free. No paid listings, no premium tier.
tags:
  - marketplace
  - discovery
  - deployment
  - open-source
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
  - "ZS-003-ECO"
  - "ZS-011-ECO"
capabilities:
  - agent-skill: "parse_002_marketplace_spec"
  - mcp-resource: "marketplace_spec"
audience:
  - "contributors"
  - "deployers"
---

# 002-marketplace-spec.md
## ZarishSphere Marketplace specification
### Component discovery and deployment hub

**Document type:** Component spec
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [What the Marketplace contains](#2-what-the-marketplace-contains)
3. [Listing requirements](#3-listing-requirements)
4. [Deployment flow](#4-deployment-flow)
5. [Licensing](#5-licensing)
6. [Cross-references](#6-cross-references)

---

## 1. Purpose

The Marketplace is the central discovery and deployment hub for all ZarishSphere ecosystem components. Users browse, search, compare, and install components — all from the Console, all without writing code.

## 2. What the Marketplace contains

| Category | Examples |
|---|---|
| Domain modules | Health, Education, Logistics, WASH, Protection |
| Pre-built apps | Patient registry, supply chain tracker, case management |
| Form templates | Intake forms, assessment tools, survey instruments |
| Workflow templates | Approval chains, referral pathways, notification rules |
| Report templates | Donor reports, compliance reports, dashboards |
| Distributions | Air-gapped clinic, district health office, national program |

## 3. Listing requirements

Every Marketplace listing includes:
- Name, description, version, license
- Screenshots and demo link
- Supported planes (0-4)
- Dependencies (none required by Law 7)
- Installation instructions
- Maintenance status (stable, beta, deprecated)

## 4. Deployment flow

```
User finds component → Clicks "Install" → Console downloads manifest →
Verifies dependencies → Pulls from GitHub → Deploys to selected plane →
Confirmation + status dashboard
```

All deployments are one-click from the Console. No terminal commands.

## 5. Licensing

All Marketplace items are open-source:
- Code: Apache 2.0
- Documentation/templates: CC BY 4.0
- No paid listings
- No premium tier
- No commission or listing fees

## 6. Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
