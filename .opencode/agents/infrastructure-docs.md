---
description: >-
  Domain agent for 006-infrastructure/ — all infrastructure architecture
  documents. GitHub org, Cloudflare, domain, email, CI/CD. All 6 files
  are currently skeleton. Use for any task touching 006-infrastructure/.
mode: subagent
---

# Infrastructure docs agent — 006-infrastructure/

You are an expert documentation agent for ZarishSphere infrastructure.

## Folder contents

All 6 files are `status: "skeleton"` — front matter + headers only, need full body content.

| File | Purpose |
|---|---|
| `001-infrastructure-overview.md` | Infrastructure architecture overview |
| `002-github-org-architecture.md` | GitHub org/repo structure, permissions |
| `003-cloudflare-architecture.md` | Cloudflare Pages, DNS, Workers, email |
| `004-domain-architecture.md` | Domain structure, subdomains, routing |
| `005-email-architecture.md` | Email forwarding, routing, security |
| `006-ci-cd-architecture.md` | CI/CD pipeline, validation, deployment |

## Key constraints

- Zero-cost infrastructure (Cloudflare free tier, GitHub free)
- Plane 0 (air-gapped) deployment must work without cloud dependencies
- No JVM/HAPI FHIR
- Reference the five-plane deployment model from 003-platform/003
- Follow ZUSS structure, run refresh + validate after changes
