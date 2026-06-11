---
id: "ZS-CRED-INV-001"
title: "008 credential inventory"
domain: "009-operations"
doc-type: "reference"
entity-type: "inventory"
summary: "Central credential inventory for the ZarishSphere ecosystem. Every credential entry follows the template defined in SOP-006 §5.1."
version: "1.0.0"
status: "stable"
tags:
  - "credentials"
  - "inventory"
  - "secrets"
  - "succession"
isolation_tier: "global"
capabilities:
  - "agent-skill: parse_credential_inventory"
audience:
  - "maintainers"
  - "deployers"
last_updated: "2026-06-11"
---
# 008-credential-inventory.md
## ZarishSphere ecosystem — credential inventory
### Maintained per SOP-006: Credential documentation, rotation, and succession procedures

**Document type:** Reference inventory  
**Date:** June 11, 2026  
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation  
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)  
**Status:** Active — V1  

---

## Template entry

Each credential entry follows this structure:

```markdown
## Credential: [Name]

| Field | Value |
|---|---|
| **Purpose** | What this credential is used for |
| **Location** | Where it is stored (e.g., GitHub Actions secret, Cloudflare dashboard, env file) |
| **Rotation schedule** | Every N days (max 90) |
| **Last rotated** | YYYY-MM-DD |
| **Next rotation due** | YYYY-MM-DD |
| **Successor** | Name / GitHub handle of person who can rotate |
| **Rotation procedure** | See SOP-006 §5. [step] |
| **Emergency contact** | Successor Designee contact info |
```

---

## Credential entries

*No entries yet. Add entries following the template above.*

---

## Cross-references

- → **[006-sop-credential-succession.md](006-sop-credential-succession.md)** — SOP-006: Credential succession procedures
- → **[008-adrs/012-adr-no-single-person-dependency.md](../008-adrs/012-adr-no-single-person-dependency.md)** — ADR-012: No single-person dependency
- → **[006-infrastructure/002-github-org-architecture.md](../006-infrastructure/002-github-org-architecture.md)** — GitHub organisation credentials
- → **[006-infrastructure/003-cloudflare-architecture.md](../006-infrastructure/003-cloudflare-architecture.md)** — Cloudflare API token configuration
- → **[006-infrastructure/006-ci-cd-architecture.md](../006-infrastructure/006-ci-cd-architecture.md)** — CI/CD secrets management

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
