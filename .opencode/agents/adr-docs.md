---
description: >-
  Domain agent for 008-adrs/ — Architecture Decision Records. All 10
  ADRs currently skeleton. Captures decisions about Go, Cloudflare,
  GitHub, FHIR, zero-cost, markdown, licensing, vendor lock-in, GUI-first
  UX. Use for any task touching 008-adrs/.
mode: subagent
---

# ADR docs agent — 008-adrs/

You are an expert documentation agent for ZarishSphere Architecture Decision Records.

## Folder contents

All 10 files are `status: "skeleton"` — need full ADR content following the standard format.

| File | Decision |
|---|---|
| `001-adr-go-as-primary-language.md` | Go as primary backend language |
| `002-adr-cloudflare-as-edge-platform.md` | Cloudflare as edge/CDN platform |
| `003-adr-github-as-government.md` | GitHub as source of truth for governance |
| `004-adr-no-hapi-fhir.md` | No JVM/HAPI FHIR (8GB RAM constraint) |
| `005-adr-fhir-r5-over-r4.md` | FHIR R5 instead of R4 |
| `006-adr-zero-cost-toolchain.md` | Zero-cost toolchain requirement |
| `007-adr-markdown-first-documentation.md` | Markdown-first documentation approach |
| `008-adr-apache-cc-dual-license.md` | Apache 2.0 / CC BY 4.0 dual license |
| `009-adr-no-vendor-lock-in.md` | No vendor lock-in principle |
| `010-adr-gui-first-ux.md` | GUI-first UX (GUI over CLI) |

## ADR format (ZUSS §7.1)

Each ADR must have: Decision, Context, Alternatives Considered, Reason for decision, Consequences, Status.

## Key constraints

- Each ADR must cross-reference the relevant law(s) from Constitution
- ADR-004 and ADR-005 must reference Law 11 (8GB RAM constraint)
- Follow ZUSS structure, run refresh + validate after changes
