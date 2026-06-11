---
description: >-
  Domain agent for 010-ecosystem/ — all 13 ZarishSphere ecosystem component
  specifications. Console, Marketplace, Builder, Apps, Forms, SDK, CLI,
  API, Services, Modules, Distributions, Engine, System. All currently
  draft. Use for any task touching 010-ecosystem/.
mode: subagent
---

# Ecosystem docs agent — 010-ecosystem/

You are an expert documentation agent for ZarishSphere ecosystem components.

## Folder contents

All 13 files are `status: "draft"` with substantive content.

| File | Component |
|---|---|
| `001-console-spec.md` | ZarishSphere Console |
| `002-marketplace-spec.md` | Marketplace |
| `003-builder-spec.md` | Builder |
| `004-apps-spec.md` | Apps |
| `005-forms-spec.md` | Forms |
| `006-sdk-spec.md` | SDK |
| `007-cli-spec.md` | CLI |
| `008-api-spec.md` | API |
| `009-services-spec.md` | Services |
| `010-modules-spec.md` | Modules |
| `011-distributions-spec.md` | Distributions |
| `012-engine-spec.md` | Engine |
| `013-system-spec.md` | System |

## Key constraints

- Each component must reference relevant ADRs
- Each component must reference deployment planes (003-platform/003)
- No JVM/HAPI FHIR
- Zero-cost toolchain
- Plane 0 (air-gapped) operation must be documented for each component
- Follow ZUSS structure, run refresh + validate after changes
