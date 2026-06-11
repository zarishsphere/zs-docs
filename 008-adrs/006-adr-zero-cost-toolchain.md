---
id: "ZS-006-ADR"
title: "006 adr zero cost toolchain"
domain: "008-adrs"
doc-type: "adr"
entity-type: "decision-record"
summary: >-
  ADR-006: Structural requirement for open-source, zero-cost toolchain
  dependencies across the entire ZarishSphere ecosystem. No paid tools,
  licenses, or services required.
version: "1.0.0"
status: "stable"
tags:
  - "adr"
  - "zero-cost"
  - "open-source"
  - "toolchain"
  - "constraint"
isolation_tier: "global"
capabilities:
  - "agent-skill: parse_006_adr_zero_cost_toolchain"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
last_updated: "2026-06-11"
last_verified: "2026-06-11"
verified_by: "Mohammad Ariful Islam"
next_review: "2026-09-11"
---

# ADR-006: Structural Requirement for Open-Source, Zero-Cost Toolchain Dependencies
## ADR-006: Structural Requirement for Open-Source, Zero-Cost Toolchain
### Every tool, library, service, and dependency must be permanently free at no cost

**Document type:** Architecture Decision Record
**Date:** June 10, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** Apache 2.0 (code) · CC BY 4.0 (documentation)
**Status:** Accepted — V1

---

## Decision

Every tool, library, framework, service, and dependency in the ZarishSphere ecosystem must be open-source and available at zero cost with a genuine perpetual free tier. No paid licenses, no expiring trials, no credit-card-gated features, no freemium tiers that restrict essential functionality. The complete toolchain from development through production must be usable without any payment to any vendor.

## Context

Constitution Law 5 (zero cost is a structural guarantee) mandates that the platform remains "permanently, unconditionally zero-cost for all humanitarian, public health, public sector, civil society, and resource-constrained deployments." This is not a business model — it is encoded in the Apache 2.0 license.

The practical context:

- **No budget:** ZarishSphere has zero funding. There is no revenue, no grant, no sponsorship (founder profile §5.3).
- **Single founder:** No organization to absorb costs or justify paid tool subscriptions.
- **Global from Day 1:** The platform is designed for deployment in the most resource-constrained settings on earth. A toolchain dependency that requires payment blocks deployment in exactly the contexts ZarishSphere is built to serve.
- **No credit card dependency:** Deployers in low-infrastructure settings may not have access to international payment methods. The toolchain must work without ever requiring a credit card.

Every tool, service, and dependency is evaluated against a zero-cost criterion that goes beyond the standard open-source definition: the tool must be usable at scale (within realistic limits) without paying any vendor, with no time limit, and without providing payment information.

## Alternatives Considered

| Alternative | Pros | Cons |
|---|---|---|
| **Open-source, zero-cost only** | Aligns with Constitution Law 5; no vendor dependency; deployable anywhere; no billing surprises; full source access for customization | Limited to community-supported tools; may miss features of paid alternatives; free-tier limits require design constraints (e.g., 100K Workers/day); some tooling must be self-built (no Sentry, no Datadog) |
| **Freemium with free tier** | Access to polished commercial tools with limited free usage; easier onboarding | Free tiers often expire (AWS free tier: 12 months); credit card required (Vercel, AWS); usage limits may be too restrictive; risk of surprise billing; violates Law 5 for the "resource-constrained" commitment |
| **Open-core with paid enterprise features** | Community edition is free; enterprise features available if funding appears later | Core features may be gated (e.g., SSO, audit logs, RBAC); creates feature disparity between resource-constrained and funded deployers — violates the principle of equal access (Law 5) |
| **Self-host all the things** | Maximum control, no third-party dependency, no limits | Requires server management; 8 GB RAM machine cannot run every service (e.g., self-hosted Sentry needs 4 GB RAM minimum); operational overhead contradicts single-founder reality |

## Reason for Decision

1. **Constitutional mandate:** Constitution Law 5 is a Tier II right — it cannot be qualified except by Tier I laws. The law states: "The ZarishSphere Platform, ZARISH-INDEX, and ZARISH-STANDARDS must remain permanently, unconditionally zero-cost for all humanitarian, public health, public sector, civil society, and resource-constrained deployments." Any paid dependency is a constitutional violation.

2. **Single founder reality:** There is no procurement department, no budget approval process, and no funding to pay for tools. The founder profile (§5.5) explicitly lists "Zero cost — No trial. No freemium that expires. Zero budget is absolute" as non-negotiable.

3. **Deployment plane sovereignty:** Planes 0 and 1 operate without internet connectivity and without cloud service access. A dependency on a SaaS tool (e.g., Sentry error tracking, Algolia search, Twilio SMS) would render these planes non-functional. The toolchain must work fully offline (Constitution Law 8).

4. **Precedent for all decisions:** This ADR influences every subsequent technology choice:
   - Go compiler → free, open-source (ADR-001)
   - Cloudflare → free tier (ADR-002)
   - GitHub → free tier (ADR-003)
   - PostgreSQL/SQLite → free, open-source
   - React/Next.js → free, open-source
   - VS Code → free, open-source
   - No JVM tools → free but RAM-infeasible (ADR-004)

### Zero-cost toolchain inventory

| Category | Tool | Version | Cost | Notes |
|---|---|---|---|---|
| Language | Go | 1.26.x | Free | Open-source compiler, no license |
| IDE | VS Code | Stable | Free | Open-source, with Go extension |
| VCS + CI/CD | GitHub | Free Org | Free | 2,000 Actions min/month |
| Edge/CDN | Cloudflare | Free tier | Free | 100K Workers req/day, unlimited CDN |
| Database (embedded) | SQLite | 3.x | Free | Public domain, zero-cost |
| Database (server) | PostgreSQL | 16.x | Free | Open-source, for Plane 2+ |
| Documentation | Markdown + GitHub Pages | — | Free | Static site, no build server needed |
| Frontend | React 19.3.0 + Next.js 15.3.1 | MIT | Free | Open-source frameworks |
| AI agents | opencode | — | Free | Open-source agent framework |
| Monitoring | Go pprof + structured logging | — | Free | Self-built, no SaaS needed |
| Fonts (UI) | Inter + JetBrains Mono | SIL OFL | Free | Open-source fonts |
| Design | Penpot (self-hosted or free tier) | Stable | Free | Open-source Figma alternative |

## Consequences

**Positive:**

- Zero-cost guarantee is structurally enforced — no tool can introduce a cost barrier
- Full transparency: the entire toolchain is inspectable, forkable, and modifiable
- Deployers in any context (including the most resource-constrained) can start without payment or credit card
- No vendor can hold the project hostage via price changes or license changes
- The ecosystem is truly forkable (Constitution Law 9) — anyone can replicate the full toolchain

**Negative:**

- Some premium tools are unavailable: no Datadog (self-hosted OpenTelemetry instead), no Sentry (Go error logging instead), no Figma (Penpot or hand-coded UI), no Algolia (SQLite FTS5 instead)
- Free-tier limits require architectural adaptation:
  - GitHub Actions: 2,000 minutes/month → need to cache efficiently, skip unnecessary builds
  - Cloudflare Workers: 100K requests/day → must design for low API call volume
  - Cloudflare Pages: 3 builds/minute → okay for docs
  - R2 storage: 1 GB free → may need to manage asset sizes
- Self-built alternatives for monitoring, error tracking, and analytics take development time away from core features
- If the project grows, migrating to scaled infrastructure while maintaining zero-cost for resource-constrained deployers requires careful architecture (see ADR-009)

## Status

Accepted. This ADR applies to all current and future dependencies. Every new tool introduced to the ecosystem must pass the zero-cost test before it is accepted. Compliance is verified during PR review (via scripts/001-zuss-validate.sh banned-word checks for paid service names).

---

## Cross-references


---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
