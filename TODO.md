# TODO.md
## zs-docs — Live Progress Tracker

**Repository:** `zarishsphere/zs-docs`
**Status:** V1 — Active documentation phase

> Tasks are marked: `[ ]` not started · `[~]` in progress · `[x]` complete
> No time estimates. No phase durations. Tasks describe work to be done, not when.

---

## Legacy Resource Analysis — What Holds Real Value?

> **Source:** `/home/health-pm/Desktop/_raw/` — original health-system-focused ZarishSphere design
> **Assessment completed:** 2026-06-11
> **Principle:** Only content that adds real value to the CURRENT Foundation ecosystem. 
> **No archive folders. No reference dumps.** Every new document must be ZUSS-compliant and belong in an existing zs-docs folder.

### Filtering criteria

| Include | Exclude |
|---------|---------|
| Platform-level technical standards | Domain-specific implementation details |
| Architecture decisions still relevant | Health-only clinical workflows |
| FHIR/API conventions | Per-microservice PRDs (go in code repos) |
| Security & compliance architecture | Clinical protocols (go in zs-content-protocols) |
| Operational procedures | Country-specific infrastructure |
| Governance frameworks | Bootstrap/setup scripts |
| Technology reference | Donor/compliance reports (old scope) |

---

## Phase A — Foundation (001-meta/)

- [x] `001-meta/001-zarishsphere-constitution.md` — 12-law constitution
- [x] `001-meta/002-zarishsphere-profile.md` — Foundation identity, mission, vision
- [x] `001-meta/003-founder-profile.md` — Founder context, working environment
- [x] `001-meta/004-writing-rules.md` — ZUSS naming and formatting rules
- [x] `001-meta/005-ecosystem-architecture.md` — Master map of repos, folders, relationships
- [x] `001-meta/006-glossary.md` — All ZarishSphere terms defined
- [x] `001-meta/007-agent-ecosystem-strategy.md` — AI agent, MCP, and skills strategy

**Phase A status:** 7 of 7 complete ✓

---

## Phase B — Foundation governance (002-foundation/)

- [x] `002-foundation/001-foundation-charter.md` — Foundation mission, scope, obligations
- [x] `002-foundation/002-governance-model.md` — How decisions are made
- [x] `002-foundation/003-licensing-policy.md` — Apache 2.0 + CC BY 4.0 application rules
- [x] `002-foundation/004-contributor-guidelines.md` — How anyone contributes to any project

**Phase B status:** 4 of 4 complete ✓

> **NEW from legacy:** The Country Adoption Maturity Model (CAMM) is a genuine governance framework that the current Foundation can use for domain/country adoption. It belongs here in governance.
> 
> - [ ] `002-foundation/005-country-adoption-model.md` — **NEW** — CAMM L0-L5 framework adapted to current Foundation context (source: `_raw/zarishsphere-docs-repo/zs-docs-camm/model/` + `templates/` + `governance/`)

---

## Phase C — Platform architecture (003-platform/)

- [x] `003-platform/001-platform-overview.md` — What the platform is, five planes, G2A
- [x] `003-platform/002-module-architecture.md` — Module sovereignty rules
- [x] `003-platform/003-deployment-planes.md` — Plane 0 through Plane 4
- [x] `003-platform/004-g2a-engine.md` — G2A Engine specification
- [x] `003-platform/005-fhir-architecture.md` — FHIR R5 integration
- [x] `003-platform/006-api-design.md` — API contracts and versioning
- [x] `003-platform/007-data-model.md` — Core data entities and ZS-UID patterns
- [x] `003-platform/008-domain-registry.md` — All 40 domains

**Phase C status:** 8 of 8 complete ✓

> **NEW from legacy:** Two platform-level reference documents from the original design are clearly useful:
> 
> - [ ] `003-platform/009-repository-catalog.md` — **NEW** — Complete repository catalog across all layers (adapted from `_raw/CATALOGS.md` — the 212-repo map is a valuable platform reference even in the current expanded scope)
> - [ ] `003-platform/010-free-tier-resource-map.md` — **NEW** — All zero-cost services with versions, free-tier limits, and usage notes (adapted from `_raw/BLUEPRINT.md` Section 7 + `_raw/SKILLS.md` Section 6)

---

## Phase D — ZARISH-INDEX (004-zarish-index/)

- [x] `004-zarish-index/001-zarish-index-overview.md` — Platform-level view
- [x] `004-zarish-index/002-domain-taxonomy-40.md` — 40-domain classification
- [x] `004-zarish-index/003-metadata-schema.md` — ZI-[DOMAIN]-[NNNNN] schema
- [x] `004-zarish-index/004-harvesting-policy.md` — License compliance rules
- [x] `004-zarish-index/005-zarish-index-to-platform.md` — Integration specification

**Phase D status:** 5 of 5 complete ✓

---

## Phase E — ZARISH-STANDARDS (005-zarish-standards/)

- [x] `005-zarish-standards/001-zarish-standards-overview.md` — Strategic direction, scope, architecture
- [x] `005-zarish-standards/002-transformation-model.md` — Data mapping, structural transformation
- [x] `005-zarish-standards/003-standards-schema.md` — Validation pipeline schemas
- [x] `005-zarish-standards/004-standards-to-platform-pipeline.md` — Real-time enforcement pipeline

**Phase E status:** 4 of 4 complete ✓ (all drafted)

> **HIGH VALUE from legacy:** The old `zs-docs-standards/` has 16 richly detailed technical standards docs covering FHIR conventions, API design, form schemas, and terminology — all directly relevant to the current ZARISH-STANDARDS layer.
>
> **ZUSS-adapted new docs:**
>
> ### FHIR Conventions (5 docs)
> - [ ] `005-zarish-standards/005-fhir-r5-conventions.md` — **NEW** — FHIR R5 resource ID format (UUID v7), tenant isolation via meta.tag, required metadata, AuditEvent requirements, search response format, OperationOutcome error format (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/fhir/FHIR-R5-CONVENTIONS.md`)
> - [ ] `005-zarish-standards/006-fhir-profiling-policy.md` — **NEW** — When to create profiles, FSH/SUSHI authoring, mandatory ZarishSphere extensions, profile naming convention, terminology binding strength, CI validation (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/fhir/FHIR-PROFILING-POLICY.md`)
> - [ ] `005-zarish-standards/007-fhir-search-standards.md` — **NEW** — Search parameter implementation, pagination, modifiers, chaining, reverse chaining (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/fhir/FHIR-SEARCH-STANDARDS.md`)
> - [ ] `005-zarish-standards/008-fhir-audit-policy.md` — **NEW** — FHIR AuditEvent generation requirements, mandatory fields, privacy controls (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/fhir/FHIR-AUDIT-POLICY.md`)
> - [ ] `005-zarish-standards/009-fhir-r4-bridge-policy.md` — **NEW** — When and how to translate between R4↔R5 for partner system integration (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/fhir/FHIR-R4-BRIDGE-POLICY.md`)
>
> ### API Design (3 docs)
> - [ ] `005-zarish-standards/010-api-rest-design-guide.md` — **NEW** — RESTful API conventions, URL structure, versioning, pagination, error handling, HATEOAS (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/api/REST-DESIGN-GUIDE.md`)
> - [ ] `005-zarish-standards/011-api-openapi-conventions.md` — **NEW** — OpenAPI 3.1 specification requirements, documentation standards, codegen expectations (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/api/OPENAPI-CONVENTIONS.md`)
> - [ ] `005-zarish-standards/012-api-asyncapi-conventions.md` — **NEW** — AsyncAPI 3.0 event catalog requirements, event naming, schema standards (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/api/ASYNCAPI-CONVENTIONS.md`)
>
> ### Clinical Content Standards (3 docs)
> - [ ] `005-zarish-standards/013-form-schema-specification.md` — **NEW** — Complete ZS Form Schema v1: structure, field types, FHIRPath mapping, LOINC coding, i18n keys, validation rules (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/clinical-content/FORM-SCHEMA-SPEC.md`)
> - [ ] `005-zarish-standards/014-form-validation-rules.md` — **NEW** — Form validation rules, CI enforcement, schema conformance checks (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/clinical-content/FORM-VALIDATION-RULES.md`)
> - [ ] `005-zarish-standards/015-i18n-key-conventions.md` — **NEW** — Internationalization key naming, locale file structure, translation workflow (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/clinical-content/I18N-KEY-CONVENTIONS.md`)
>
> ### Terminology Governance (2 docs)
> - [ ] `005-zarish-standards/016-terminology-governance.md` — **NEW** — Terminology source selection, update cycles, license compliance, caching strategy (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/terminology/TERMINOLOGY-GOVERNANCE.md`)
> - [ ] `005-zarish-standards/017-terminology-code-systems.md` — **NEW** — LOINC, ICD-11, SNOMED CT, CIEL, RxNorm, CVX usage policies and domain mappings (source: `_raw/zarishsphere-docs-repo/zs-docs-standards/terminology/LOINC-USAGE.md`, `ICD11-USAGE.md`, `SNOMED-USAGE.md`)

---

## Phase F — Infrastructure (006-infrastructure/)

- [x] `006-infrastructure/001-infrastructure-overview.md` — Enterprise infrastructure mapping
- [x] `006-infrastructure/002-github-org-architecture.md` — GitHub org, teams, branch protection
- [x] `006-infrastructure/003-cloudflare-architecture.md` — Edge routing, WAF, nameservers
- [x] `006-infrastructure/004-domain-architecture.md` — Domain hierarchy, routing
- [x] `006-infrastructure/005-email-architecture.md` — Secure relay infrastructure
- [x] `006-infrastructure/006-ci-cd-architecture.md` — CI/CD via GitHub Actions

**Phase F status:** 6 of 6 complete ✓ (all drafted)

> **HIGH VALUE from legacy:** The old `zs-docs-security/` has comprehensive security and compliance documentation — a critical gap in current zs-docs. No security architecture doc exists yet.
>
> **ZUSS-adapted new docs:**
>
> - [ ] `006-infrastructure/007-security-architecture.md` — **NEW** — Defense-in-depth security architecture: Cloudflare WAF, Traefik TLS, SMART on FHIR scopes, FHIR resource RBAC, PostgreSQL RLS, field-level encryption, AuditEvent logging. Secrets management with Vault. (source: `_raw/ARCHITECTURE.md` Section 8 + `_raw/zarishsphere-docs-repo/zs-docs-security/policies/`)
> - [ ] `006-infrastructure/008-security-policies.md` — **NEW** — Access control policy (RBAC/SMART), encryption policy (AES-256/TLS 1.3), vulnerability disclosure, secret management (source: `_raw/zarishsphere-docs-repo/zs-docs-security/policies/*`)
> - [ ] `006-infrastructure/009-compliance-controls.md` — **NEW** — HIPAA technical safeguards, GDPR data subject rights, data residency policy per country, compliance control mapping matrix (source: `_raw/zarishsphere-docs-repo/zs-docs-security/compliance/*`)
> - [ ] `006-infrastructure/010-threat-models.md` — **NEW** — Consolidated threat models: FHIR API (injection, excessive data exposure), Authentication (token theft, scope escalation), Data layer (SQL injection, tenant escape), Mobile offline (device theft, sync tampering) (source: `_raw/zarishsphere-docs-repo/zs-docs-security/threat-models/*`)

---

## Phase G — Technology stack (007-tech-stack/)

- [x] `007-tech-stack/001-tech-stack-master.md` — **Stable** — Master tech stack mapping
- [x] `007-tech-stack/002-go-fhir-server.md` — Go-native FHIR R5 server spec
- [x] `007-tech-stack/003-frontend-stack.md` — React 19 / Next.js 15 frontend
- [x] `007-tech-stack/004-data-pipeline.md` — Real-time data pipeline
- [x] `007-tech-stack/005-no-code-tools.md` — Offline-capable, low-code integration

**Phase G status:** 5 of 5 complete ✓ (1 stable, 4 drafted)

> **VALUE from legacy:** The old `SKILLS.md` is a comprehensive 424-line open-source tool catalog with versions, licenses, and import paths — a useful reference companion to the tech-stack master.
>
> - [ ] `007-tech-stack/006-technology-skills-catalog.md` — **NEW** — Complete open-source tool catalog: Go libraries (FHIR, HTTP, DB, messaging, auth, observability), frontend (React, Next.js, Carbon DS, form engines, charts, maps), mobile (Flutter, PowerSync), desktop (Tauri), infrastructure (K8s, OpenTofu, ArgoCD, NATS, Valkey), observability (Prometheus, Grafana, Loki, Tempo) — all with version pins, license info, and import paths. (adapted from `_raw/SKILLS.md`)

---

## Phase H — Architecture Decision Records (008-adrs/)

- [x] `008-adrs/001-adr-go-as-primary-language.md` — **Stable** — Go as primary language
- [x] `008-adrs/002-adr-cloudflare-as-edge-platform.md` — **Stable** — Cloudflare as edge
- [x] `008-adrs/003-adr-github-as-government.md` — **Stable** — GitHub as governance
- [x] `008-adrs/004-adr-no-hapi-fhir.md` — **Stable** — No JVM/HAPI FHIR
- [x] `008-adrs/005-adr-fhir-r5-over-r4.md` — **Stable** — FHIR R5 canonical
- [x] `008-adrs/006-adr-zero-cost-toolchain.md` — **Stable** — Zero-cost toolchain
- [x] `008-adrs/007-adr-markdown-first-documentation.md` — **Stable** — Markdown-first docs
- [x] `008-adrs/008-adr-apache-cc-dual-license.md` — **Stable** — Dual licensing
- [x] `008-adrs/009-adr-no-vendor-lock-in.md` — **Stable** — No vendor lock-in
- [x] `008-adrs/010-adr-gui-first-ux.md` — **Stable** — GUI-first UX
- [x] `008-adrs/011-adr-privacy-by-architecture.md` — Privacy enforcement at infra layer
- [x] `008-adrs/012-adr-no-single-person-dependency.md` — No single-person dependency

**Phase H status:** 12 of 12 complete ✓ (10 stable, 2 drafted)

> **HIGH VALUE from legacy:** The old `zs-docs-adr/docs/` has 14 ADRs (0001-0014). Current zs-docs already covers the first 2 (Go, FHIR R5) plus 10 Foundation-specific ADRs. The remaining 11 legacy ADRs document real technical decisions already embedded in the platform but not formally captured as ADRs.
>
> **ZUSS-adapted new ADRs:**
>
> - [ ] `008-adrs/013-adr-postgresql-primary-database.md` — **NEW** — PostgreSQL as the single database: JSONB for FHIR, GIN search, TimescaleDB extension, RLS for multi-tenancy (source: legacy ADR-0003)
> - [ ] `008-adrs/014-adr-nats-jetstream-messaging.md` — **NEW** — NATS JetStream for async messaging: 20MB RAM, single binary, persistent streams, FHIR subscription support (source: legacy ADR-0004)
> - [ ] `008-adrs/015-adr-valkey-for-caching.md` — **NEW** — Valkey over Redis: Linux Foundation fork, fully OSS, drop-in compatible (source: legacy ADR-0005)
> - [ ] `008-adrs/016-adr-opentofu-infrastructure-as-code.md` — **NEW** — OpenTofu over Terraform: zero licensing cost, community fork, HashiCorp BSL concern (source: legacy ADR-0006)
> - [ ] `008-adrs/017-adr-argocd-gitops.md` — **NEW** — Argo CD for GitOps: CNCF graduated, UI dashboard, multi-cluster support, app-of-apps pattern (source: legacy ADR-0007)
> - [ ] `008-adrs/018-adr-cilium-service-mesh.md` — **NEW** — Cilium over Istio: eBPF-native, 60% less overhead, CNCF graduated (source: legacy ADR-0008)
> - [ ] `008-adrs/019-adr-carbon-design-system.md` — **NEW** — Carbon Design System: IBM healthcare-focused, WCAG 2.2 AA, actively maintained (source: legacy ADR-0009)
> - [ ] `008-adrs/020-adr-microfrontend-architecture.md` — **NEW** — Microfrontend architecture: independent deployability, team autonomy, country customization (source: legacy ADR-0011)
> - [ ] `008-adrs/021-adr-powersync-mobile-offline.md` — **NEW** — PowerSync for mobile offline sync: self-hosted, SQLite-to-PostgreSQL, clinical-safe conflict resolution (source: legacy ADR-0012)
> - [ ] `008-adrs/022-adr-typescript-strict-mode.md` — **NEW** — TypeScript strict mode for all frontend code (source: legacy ADR-0013)
> - [ ] `008-adrs/023-adr-flutter-cross-platform-mobile.md` — **NEW** — Flutter/Dart for cross-platform mobile development (source: legacy ADR-0014)

---

## Phase I — Operations (009-operations/)

- [x] `009-operations/001-sop-new-document-creation.md` — Document provisioning and validation
- [x] `009-operations/002-sop-github-workflow.md` — Branching, merging, PR models
- [x] `009-operations/003-sop-contribution-process.md` — Review pipeline, external patches
- [x] `009-operations/004-sop-zuss-compliance-audit.md` — Compliance formatting audit
- [x] `009-operations/005-sop-deployment-checklist.md` — Production deployment checklist
- [x] `009-operations/006-sop-credential-succession.md` — Credential rotation, Law 11 compliance
- [x] `009-operations/007-sop-audit-procedures.md` — Decision audit trail, Law 10 compliance
- [x] `009-operations/008-credential-inventory.md` — Central credential inventory template

**Phase I status:** 8 of 8 complete ✓ (all drafted)

> **VALUE from legacy:** The old `zs-docs-runbooks/` has operational procedures that complement the existing SOPs. These are clearly needed runbooks.
>
> **ZUSS-adapted new docs:**
>
> - [ ] `009-operations/009-sop-production-deployment.md` — **NEW** — Deployment runbook: pre-deploy checks, canary deployment, traffic shifting, rollback triggers, smoke tests (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/deployment/DEPLOY-RUNBOOK.md`, `ROLLBACK-RUNBOOK.md`)
> - [ ] `009-operations/010-sop-incident-response.md` — **NEW** — Incident lifecycle: severity classification (P0-P3), detection, response, mitigation, postmortem template, blameless culture (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/incidents/*`)
> - [ ] `009-operations/011-sop-security-incident-response.md` — **NEW** — Security incident playbook: compromise indicators, containment, forensic snapshot, Vault rotation, notification timeline (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/security/SECURITY-INCIDENT-PLAYBOOK.md`)
> - [ ] `009-operations/012-sop-backup-disaster-recovery.md` — **NEW** — Backup procedures (PostgreSQL WAL, R2 object storage), recovery point objectives, DR plan (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/backup-recovery/*`)
> - [ ] `009-operations/013-sop-country-onboarding.md` — **NEW** — End-to-end country onboarding: distro fork, infra setup, facility registry, training, go-live checklist (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/onboarding/NEW-COUNTRY-ONBOARDING.md`)
> - [ ] `009-operations/014-sop-facility-onboarding.md` — **NEW** — Facility/site onboarding: infrastructure provisioning, user setup, device configuration, offline sync enablement (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/onboarding/NEW-FACILITY-ONBOARDING.md`)
> - [ ] `009-operations/015-reference-monitoring-dashboards.md` — **NEW** — Monitoring dashboard reference: FHIR Engine Health, Patient Activity, Clinical Operations, Public Health, Infrastructure, Security — with metrics tracked per dashboard (source: `_raw/zarishsphere-docs-repo/zs-docs-runbooks/monitoring/GRAFANA-DASHBOARDS.md` + `_raw/ARCHITECTURE.md` Section 9)

---

## Phase J — Ecosystem components (010-ecosystem/)

- [x] `010-ecosystem/001-console-spec.md` — Browser-based management center
- [x] `010-ecosystem/002-marketplace-spec.md` — Discovery and deployment hub
- [x] `010-ecosystem/003-builder-spec.md` — No-code creation tool
- [x] `010-ecosystem/004-apps-spec.md` — Pre-built domain applications
- [x] `010-ecosystem/005-forms-spec.md` — Dynamic form engine
- [x] `010-ecosystem/006-sdk-spec.md` — Go/JS/Python SDKs
- [x] `010-ecosystem/007-cli-spec.md` — Command-line interface
- [x] `010-ecosystem/008-api-spec.md` — RESTful + GraphQL APIs
- [x] `010-ecosystem/009-services-spec.md` — Backend microservices
- [x] `010-ecosystem/010-modules-spec.md` — Independently deployable domain packages
- [x] `010-ecosystem/011-distributions-spec.md` — Pre-packaged deployment bundles
- [x] `010-ecosystem/012-engine-spec.md` — Core runtime, G2A execution, orchestration
- [x] `010-ecosystem/013-system-spec.md` — Base environment (IAM, encryption, config, monitoring)
- [x] `010-ecosystem/014-content-forms-spec.md` — FHIR R5 Questionnaire form definitions
- [x] `010-ecosystem/015-content-protocols-spec.md` — Machine-readable protocol definitions
- [x] `010-ecosystem/016-content-templates-spec.md` — Deployment templates, Plane 0-4
- [x] `010-ecosystem/017-content-reports-spec.md` — Report templates, dashboard configs
- [x] `010-ecosystem/018-home-spec.md` — ZarishSphere Home (zarishsphere.com)
- [x] `010-ecosystem/019-fhir-hub-spec.md` — FHIR Integration Hub

**Phase J status:** 19 of 19 complete ✓

---

## Phase K — INDEX navigation files

- [x] Root `INDEX.md` — Navigation routes, quick links, cross-repo map
- [x] `001-meta/INDEX.md` — Foundation documents index
- [x] `002-foundation/INDEX.md` — Governance documents index
- [x] `003-platform/INDEX.md` — Platform architecture index
- [x] `004-zarish-index/INDEX.md` — ZARISH-INDEX index
- [x] `005-zarish-standards/INDEX.md` — ZARISH-STANDARDS index
- [x] `006-infrastructure/INDEX.md` — Infrastructure index
- [x] `007-tech-stack/INDEX.md` — Tech stack index
- [x] `008-adrs/INDEX.md` — ADR index
- [x] `009-operations/INDEX.md` — Operations index
- [x] `010-ecosystem/INDEX.md` — Ecosystem index

**Phase K status:** 11 of 11 complete ✓

> **Needs update:** When new docs are added to any folder, its INDEX.md must be updated to include the new entries.

---

## Phase L — Validation scripts

- [x] `scripts/001-zuss-validate.sh` — Naming, serialing, front matter, footers, banned words
- [x] `scripts/002-pipeline-status.sh` — Document completion status
- [x] `scripts/003-resolve-cross-refs.sh` — Cross-reference validation
- [x] `scripts/010-refresh-files.py` — Normalise, index, llms, footers
- [x] `scripts/004-zarishsphere-init.sh` — GitHub repo initialisation

**Phase L status:** 5 of 5 complete ✓

> Needs update: `scripts/002-pipeline-status.sh` must be updated to track new documents across phases E-I.

---

## Phase M — Single ecosystem consolidation (complete)

- [x] Consolidated sandbox (001-meta/agents/, skills/, plugins/, tools/, scripts/) into root .opencode/
- [x] Removed duplicate configs (001-meta/opencode.jsonc, sandbox.jsonc)
- [x] Updated orchestrator agent with ecosystem boundary section
- [x] All scripts now executable and scoped to documentation only
- [x] AGENTS.md, README.md, TODO.md updated with accurate status
- [x] All cross-references fixed
- [x] INSTRUCTION.md rewritten with comprehensive line-by-line documentation
- [x] ZUSS validator passes with 0 failures on main docs

**Phase M status:** 8 of 8 complete ✓

---

## Phase N — NEW: Selectively Adapt Valuable Legacy Content

> **Strategy:** Only content that serves the CURRENT Foundation ecosystem. Each document adapted to ZUSS standards (front matter, naming, structure, cross-refs). No archive folders. No reference dumps. No health-specific implementation details.

### Summary of what will be created

| Folder | New Docs | Source | Value |
|--------|----------|--------|-------|
| `002-foundation/` | 1 | CAMM framework | Adoption governance model |
| `003-platform/` | 2 | CATALOGS.md, BLUEPRINT.md, SKILLS.md | Repository catalog + free-tier map |
| `005-zarish-standards/` | 13 | FHIR/API/forms/terminology standards | **Critical** — FHIR conventions, profiling, API design, form schema, terminology |
| `006-infrastructure/` | 4 | Security policies, compliance, threat models | **Critical** — security architecture gap |
| `007-tech-stack/` | 1 | SKILLS.md | Comprehensive OSS tool catalog |
| `008-adrs/` | 11 | Legacy ADRs 0003-0014 | Technical decision formalization |
| `009-operations/` | 7 | Runbooks (deploy, incidents, backup, onboarding) | Operational completeness |
| **Total** | **~39** | | |

### What is intentionally excluded

| Content | Why |
|---------|-----|
| Clinical microservice PRDs (zs-svc-*) | Implementation specs for code repos, not zs-docs |
| UI microfrontend PRDs (zs-ui-*) | Implementation specs for code repos, not zs-docs |
| Mobile/desktop app PRDs | Implementation specs for code repos, not zs-docs |
| Clinical protocols (ANC, TB, malaria) | Content for zs-content-protocols repo |
| 209 PRD files | Implementation blueprints, not documentation |
| bootstrap.sh | Setup script, not documentation |
| Original README/BLUEPRINT/ARCHITECTURE | Superseded by current Foundation docs |
| Donor/compliance reports | Old health-system specific scope |
| Country infra docs | Implementation-level |
| RFC-0001, RFC-0002 | Original naming standards — already superseded by ZUSS |

---

## Phase O — Pipeline updates

- [x] Update `scripts/002-pipeline-status.sh` — Extend tracking to cover all new docs in phases E-I
- [x] Update relevant INDEX.md files after each new document batch
- [x] Run full validation after each batch:
  ```bash
  python3 scripts/010-refresh-files.py
  bash scripts/001-zuss-validate.sh
  bash scripts/002-pipeline-status.sh
  bash scripts/003-resolve-cross-refs.sh
  ```
- [x] Promote all 97 draft documents to `status: stable`
- [x] Optimize cross-ref checker (bash → Python, ~100× faster)

---

## Implementation sequence (recommended order)

| Batch | Content | Dependencies | Effort |
|-------|---------|-------------|--------|
| **1** | 13 standards docs (`005-zarish-standards/`) | None — independent | High |
| **2** | 4 security docs (`006-infrastructure/`) | None — independent | Medium |
| **3** | 11 ADRs (`008-adrs/`) | None — independent | Medium |
| **4** | 7 operations docs (`009-operations/`) | None — independent | Medium |
| **5** | 2 platform refs (`003-platform/`) | None — independent | Low |
| **6** | 1 CAMM doc (`002-foundation/`) | None — independent | Low |
| **7** | 1 skills catalog (`007-tech-stack/`) | None — independent | Low |

**All 7 batches complete as of June 11, 2026.** See "Overall progress" below.

---

## Repository initialization tasks

- [x] `git init` in zs-docs (repo root)
- [x] Create `zarishsphere/zs-docs` repository on GitHub (public, no template)
- [x] Push all 117 documents, INDEX.md files, and validation scripts — **165 files, 40,112 lines**
- [ ] Create `zarishsphere/zs-zarish-index` repository (Phase D complete)
- [ ] Create `zarishsphere/zs-zarish-standards` repository (Phase E complete)

---

## Overall progress

| Phase | Folder / Area | Files | Stable | Draft | Skeleton |
|---|---|---|---|---|---|---|---|
| A | `001-meta/` | 7 | 7 | 0 | 0 |
| B | `002-foundation/` | 5 | 5 | 0 | 0 |
| C | `003-platform/` | 10 | 10 | 0 | 0 |
| D | `004-zarish-index/` | 5 | 5 | 0 | 0 |
| E | `005-zarish-standards/` | 17 | 17 | 0 | 0 |
| F | `006-infrastructure/` | 10 | 10 | 0 | 0 |
| G | `007-tech-stack/` | 6 | 6 | 0 | 0 |
| H | `008-adrs/` | 23 | 23 | 0 | 0 |
| I | `009-operations/` | 15 | 15 | 0 | 0 |
| J | `010-ecosystem/` | 19 | 19 | 0 | 0 |
| **Total** | | **117** | **117** | **0** | **0** |

---

## Agent-native roadmap (from 007-agent-ecosystem-strategy.md)

### Phase 0 — Foundation (complete)

- [x] Update front matter in all existing docs
- [x] Create `llms.txt` at root
- [x] Create `007-agent-ecosystem-strategy.md`
- [x] Update `AGENTS.md`
- [x] Create INDEX.md navigation files
- [x] Create validation scripts

### Phase 1 — Complete all primary documents

- [x] All 78 current primary documents complete
- [x] All 39 adapted documents created (Phase N — 7 batches complete)

### Phase 2 — Knowledge graph enrichment (deferred)

- [ ] Add `depends_on`, `related`, `supersedes` in front matter
- [ ] Add wikilinks (`[[document-name]]`) in body text
- [ ] Add `## Related` section at end of every document

> Deferred until after git push. Phase N completion takes priority.

### Phase 3 — Skills packaging (complete)

- [x] Create `SKILL.md` in each domain folder (10 skills in `.opencode/skills/`)

### Phase 4 — MCP server (setup complete)

- [x] GitHub MCP server at `.opencode/mcp-server-github.js`
- [ ] Deploy as Cloudflare Worker (future)

### Phase 5 — Automation and maintenance

- [ ] Set up 90-day review reminder
- [ ] Create review verification template
- [x] Run validation scripts before commits
- [x] Push to GitHub — **completed June 11, 2026**
- [ ] Enable GitHub Pages for public llms.txt hosting

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
