---
id: "ZS-005-ADR"
title: "005 adr fhir r5 over r4"
domain: "008-adrs"
doc-type: "adr"
entity-type: "decision-record"
summary: >-
  ADR-005: Enforcement of FHIR R5 as the canonical FHIR version for the
  ZarishSphere Platform. Decision to implement FHIR R5 natively rather than
  using R4 with extensions.
version: "1.0.0"
status: "stable"
tags:
  - "adr"
  - "fhir"
  - "r5"
  - "r4"
  - "standards"
isolation_tier: "global"
capabilities:
  - "agent-skill: parse_005_adr_fhir_r5_over_r4"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
last_updated: "2026-06-11"
last_verified: "2026-06-11"
verified_by: "Mohammad Ariful Islam"
next_review: "2026-09-11"
---

# ADR-005: Enforcement of FHIR R5 Standard Native Implementations
## ADR-005: Enforcement of FHIR R5 as the Canonical FHIR Version
### FHIR R5 only — no R4 compatibility layer, no mixed-version support

**Document type:** Architecture Decision Record
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)
**Status:** Accepted — V1

---

## Decision

Enforce FHIR Release 5 (R5) as the sole canonical FHIR version across the entire ZarishSphere ecosystem. No R4 or R4B compatibility layer will be maintained. All FHIR resources, operations, search parameters, and interactions follow the R5 specification. The Go-native FHIR server (ADR-004) implements R5 natively with no backward compatibility code paths for earlier versions.

## Context

FHIR is the interoperability standard for the ZarishSphere Platform (Constitution Law 3 — every standard is executable). Every data entity stored or exchanged by the platform — patient records, observations, conditions, medications, immunizations, care plans, service requests — uses FHIR resource models.

At the time of this decision (June 2026), the FHIR landscape includes:

- **FHIR R4** (v4.0.1): Current normative release, widely adopted, stable, largest ecosystem of tools and servers
- **FHIR R4B** (v4.3.0): Bridge release between R4 and R5, backports some R5 features to R4
- **FHIR R5** (v5.0.0): Most recent release, introduces significant simplifications and new resources, still being adopted

The ZarishSphere Platform starts from zero — there is no existing data in any FHIR version, no legacy R4 systems to integrate with, and no migration burden. This is a greenfield FHIR decision.

## Alternatives Considered

| Alternative | Pros | Cons |
|---|---|---|
| **FHIR R5 exclusively** | Most current standard with simplified resources (Medication, Immunization, BiologicallyDerivedProduct); new resources aligned with ZarishSphere 40 domains (e.g., DeviceAssociation, EvidenceReport, NutritionOrder); improved RESTful search (composite search parameters, `_filter`); no legacy debt; naturally aligned with ADR-004 (building custom server from scratch) | Smaller ecosystem of R5 tools; fewer third-party R5 validators; some implementers (national health systems, EHR vendors) still on R4; must keep up with R5 errata and future releases |
| **FHIR R4 exclusively** | Most widely adopted FHIR release; largest ecosystem of tools (HAPI FHIR, Firely, Smile CDR); extensive documentation and community support; stable normative resources | Lacks R5 simplifications; would need to carry R5-like extensions for ZarishSphere domains; building custom R4 server is more work than building R5 server (R4 has more resource types); will eventually need to migrate to R5 — causing painful transition later |
| **R4 with R5 backport extensions** | Access to R5 features while maintaining R4 compatibility; allows integration with existing R4 systems | Complexity of maintaining R4 base with R5 extension mapping; no existing tooling supports mixed R4+R5; increases Go server implementation complexity significantly; violates KISS principle for a solo developer |
| **Dual version support (R4 + R5)** | Maximum interoperability with external systems | 2x implementation and testing burden; version negotiation logic in every API call; most complex to implement and hardest to maintain; ADR-004 custom Go server would take 2x longer |

## Reason for Decision

1. **Greenfield advantage:** ZarishSphere has zero existing FHIR data. There is no R4 database to migrate, no R4 API clients consuming endpoints, and no R4-dependent workflows. Choosing R5 today avoids an inevitable R4-to-R5 migration later — a migration that some national health systems are currently spending millions of dollars and years of effort to execute.

2. **Reduced implementation scope for custom server:** ADR-004 rejects HAPI FHIR in favor of a custom Go FHIR server. FHIR R5 simplified several complex resource structures:
   - MedicationRequest, MedicationAdministration, MedicationDispense → consolidated Medication resource
   - More consistent event resource pattern (e.g., Immunization simplified)
   - New `canonical` and `uri` patterns reduce validator complexity
   - Fewer resource types with overlapping semantics mean less code to write

   Building a custom server for R5 requires significantly less implementation effort than R4.

3. **Alignment with 40-domain taxonomy:** FHIR R5 introduced resources that align directly with ZarishSphere's 40-domain master taxonomy (see **004-zarish-index/002-domain-taxonomy-40.md**):
   - DeviceAssociation → biomedical engineering domain
   - EvidenceReport → research and clinical trials domain
   - NutritionOrder → nutrition domain
   - Transport → logistics domain
   These resources would require extensions in R4, adding complexity.

4. **No interoperability debt to carry:** Organizations still on R4 can use ZarishSphere's FHIR API at the R5 version. If a ZarishSphere deployment needs to exchange data with an R4 system, a gateway adapter can be built as a separate component — but the core server remains R5-only. This preserves architectural integrity (Constitution Law 7 — module sovereignty, each adapter is an independent module).

## Consequences

**Positive:**

- Go FHIR server implements a single, internally consistent FHIR version
- No R4-specific code paths reduce codebase size by an estimated 30-40%
- R5 resources map directly to ZarishSphere 40 domains without extension hacks
- Improved R5 search (`_filter`, composite parameters) enables richer queries with less code
- Forward-looking — the industry is moving toward R5 (HL7 normative ballot for R5 ongoing)
- Can participate in R5 interoperability pilots with early-adopter health systems

**Negative:**

- Cannot directly integrate with EHR systems still on FHIR R4 without a gateway adapter
- Smaller ecosystem: fewer R5 validators, fewer reference implementations, less community knowledge
- Some R5 resources are not yet normative (trial-use) — may change in R5.1 or R6
- Training materials and documentation for R5 are less comprehensive than R4
- Contributors familiar with FHIR R4 must learn R5 differences
- Risk if HL7 releases R5.1 with breaking changes before ZarishSphere V1 launches

## Status

Accepted. This decision is closely coupled with ADR-004 (no HAPI FHIR) — R5's resource simplification makes the custom Go server viable. If HL7 releases a breaking R5.1 before V1 launch, the ADR will be updated with a migration plan, but the principle of "newest normative release, not R4 compatibility" remains.

---

## Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
