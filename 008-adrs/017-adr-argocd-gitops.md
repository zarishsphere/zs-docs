---
id: "ZS-017-ADR"
title: "017 adr argocd gitops"
domain: "008-adrs"
doc-type: "adr"
entity-type: "decision-record"
summary: >-
  ADR-017: Argo CD 2.14.10 as the GitOps deployment engine for the ZarishSphere
  Platform. CNCF graduated, app-of-apps pattern, auto-sync with self-healing,
  multi-cluster support, SSO integration, web UI for no-coder operation.
version: "1.0.0"
status: "stable"
tags:
  - "adr"
  - "argocd"
  - "gitops"
  - "kubernetes"
  - "deployment"
  - "cncf"
isolation_tier: "platform"
capabilities:
  - "agent-skill: parse_017_adr_argocd_gitops"
audience:
  - "architect"
  - "developer"
  - "operator"
last_updated: "2026-06-11"
---

# ADR-017: Argo CD for GitOps
## ADR-017: Argo CD 2.14.10 as GitOps Deployment Engine
### CNCF Graduated, App-of-Apps, Auto-Sync, Multi-Cluster, Web UI

**Document type:** Architecture Decision Record
**Date:** June 11, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)
**Status:** Draft

---

## Decision

Use Argo CD 2.14.10 as the GitOps deployment engine for all ZarishSphere Platform Kubernetes deployments. Every deployment is triggered by a git commit — no manual `kubectl apply`, no manual Helm installs. Argo CD's ApplicationSet controller manages the full application catalog via the app-of-apps pattern. The web UI provides visual deployment status for no-coder operation. Auto-sync with self-healing ensures cluster state always matches the git source of truth.

## Context

Constitution Law 1 (GitHub is the government) establishes that every ZarishSphere decision, configuration, and deployment flows from a git commit. This extends to infrastructure deployments: the state of every deployed service must be the automatic consequence of what is committed to the deployment repository.

Key requirements:

- **Automated deployment from git:** Merging a PR to the main branch must automatically reconcile the cluster state. No human should need to SSH into a server or run `kubectl apply` to deploy a change.
- **No-coder operation:** Platform operators (NGO administrators, government health IT staff) should be able to monitor and manage deployments through a browser-based UI without terminal access. Constitution Law 6 (No-code first) requires GUI access as the primary interface.
- **App-of-apps management:** With 200+ services across multiple domains, a single ApplicationSet must manage the entire deployment catalog from a single configuration source. Individual services are added by updating a configuration file, not by creating new Argo CD Applications manually.
- **Rollback on failure:** If a deployment fails health checks, Argo CD must automatically roll back to the previous known-good state. Clinical deployments require this safety guarantee.
- **Drift detection and correction:** If someone manually modifies a deployed resource (via `kubectl edit`, for example), Argo CD must detect the drift and automatically reconcile back to the git-defined state.
- **Multi-cluster support:** Plane 2 (district server), Plane 3 (national cloud), and Plane 4 (global SaaS) may involve multiple Kubernetes clusters. Argo CD must manage deployments across all clusters from a single control plane.
- **SSO integration:** Argo CD must integrate with Keycloak 26.2.7 or other identity providers for authentication and authorization, preventing shared credentials and enabling audited access (Constitution Law 10).

## Alternatives Considered

- **Argo CD 2.14.10:** CNCF graduated project with the largest GitOps community. ApplicationSet controller enables single-configuration management of all 200+ services. The web UI provides full deployment visibility without terminal access. Auto-sync with self-healing ensures drift is automatically corrected. Supports multi-cluster management from a single Argo CD instance. SSO integration with Keycloak 26.2.7, GitHub, and OIDC providers. The app-of-apps pattern allows hierarchical management: a root Application deploys ApplicationSets, which deploy individual services. Automatic rollback on health check failure provides safety for clinical deployments.

- **Flux CD v2:** CNCF graduated, Git-native (no separate API server needed), supports kustomize and Helm, smaller resource footprint than Argo CD. However: lacks a mature web UI (Flux has no official UI — relies on third-party tools like Weave GitOps). The `kubectl`-heavy workflow conflicts with Constitution Law 6 (No-code first). Smaller community and fewer integrations than Argo CD. No built-in SSO — authentication requires a separate proxy. App-of-apps pattern is less natural in Flux's model (uses Kustomize overlays instead).

- **Jenkins X:** Full CI+CD combined platform with GitOps pipelines, preview environments, and environment promotion. However: extremely complex to set up and maintain — Jenkins X has a steep learning curve. Tightly coupled to Jenkins for CI, which adds JVM dependency (conflicts with ADR-004's prohibition on JVM). Heavy resource footprint. The combined CI/CD model is less flexible than the decoupled approach (GitHub Actions for CI + Argo CD for CD).

- **Spinnaker:** Enterprise-grade continuous delivery platform with canary deployments, blue-green deployments, and multi-cloud support. However: extremely complex to deploy and operate (requires Redis, Cassandra/MySQL, MinIO RELEASE.2026-05-29T18-24-33Z, and multiple microservices). JVM-dependent (conflicts with ADR-004). Over-provisioned for ZarishSphere's deployment model — the canary and blue-green capabilities are unnecessary for most deployment planes. Managing Spinnaker alone would consume more time than the actual application deployments.

- **Manual Helm + kubectl:** No GitOps tool — deployments performed manually via `helm upgrade --install` and `kubectl apply`. Simplest initial approach. However: violates Constitution Law 1 (GitHub is the government) because deployments are not git-driven. Drift undetected. Rollback requires manual `helm rollback`. No audit trail for who deployed what and when. Not reproducible from scratch. Unsuitable for any production deployment.

## Reason for Decision

1. **Constitutional alignment:** Argo CD directly implements Constitution Law 1 (GitHub is the government) — the deployment state is always the automatic consequence of what is in git. It also implements the auditability requirement of Constitution Law 10: every deployment is recorded in the Argo CD event log, linked to the git commit that triggered it.

2. **No-coder operation:** The Argo CD web UI provides full deployment lifecycle management (sync, rollback, health inspection, resource tree) without any terminal access. This satisfies Constitution Law 6 (No-code first) — a platform operator can manage deployments entirely through a browser.

3. **App-of-apps scalability:** The ApplicationSet controller allows a single YAML configuration file to define the deployment pattern for all 200+ services — one ApplicationSet generates an Application per service from a template. This is essential for a single-founder project that cannot manually manage 200 individual Application resources.

4. **Safety for clinical deployments:** Auto-sync with self-healing ensures that any manual modification to production resources is automatically reverted to the git-defined state — preventing configuration drift that could affect clinical workflows. Automatic rollback on health check failure prevents bad deployments from affecting patient care.

5. **CNCF graduation and community:** Argo CD is a CNCF graduated project with the largest GitOps community, most documentation, and the widest ecosystem integration (including native compatibility with OpenTofu for infrastructure provisioning — see ADR-016).

## Consequences

**Positive:**
- Every deployment flows from a git commit — full audit trail of who deployed what and when
- Web UI provides visual deployment management without terminal access (Law 6 compliance)
- ApplicationSet controller scales service management to 200+ services from a single configuration
- Auto-sync with self-healing prevents configuration drift in production
- Automatic rollback on health check failure protects clinical deployments
- Multi-cluster management from a single control plane
- SSO integration with Keycloak 26.2.7 for audited access
- CNCF graduated — community-governed, vendor-independent

**Negative:**
- Argo CD itself must be deployed and maintained — adds operational complexity for a single founder
- ApplicationSet patterns have a learning curve — writing Go templates in YAML requires practice
- The Argo CD web UI, while useful, has known limitations for complex deployment observability
- Argo CD adds resource overhead (2-4 GB RAM recommended) — may not be suitable for Plane 1 (Raspberry Pi) deployments where lighter alternatives or manual deployments may be used
- Over-reliance on auto-sync can mask manual debugging sessions where developers modify resources directly
- SSO configuration requires a running identity provider (Keycloak 26.2.7) — chicken-and-egg bootstrap problem

## Status

Accepted. Argo CD 2.14.10 is the GitOps deployment engine for all ZarishSphere Platform Kubernetes clusters (Plane 2+). Plane 0 and Plane 1 deployments may use lighter deployment mechanisms (single-binary Go service deployments) with documented deployment procedures. All Kubernetes deployments must be managed through Argo CD — manual `kubectl apply` is prohibited for production clusters.

---

## Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
