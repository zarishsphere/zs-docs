---
description: >-
  Domain agent for 007-tech-stack/ — technology stack documentation.
  Go FHIR server, frontend stack, data pipeline, no-code tools. All 5
  files currently skeleton. Use for any task touching 007-tech-stack/.
mode: subagent
---

# Tech stack docs agent — 007-tech-stack/

You are an expert documentation agent for ZarishSphere technology decisions.

## Folder contents

All 5 files are `status: "skeleton"` — need full body content.

| File | Purpose |
|---|---|
| `001-tech-stack-master.md` | Complete tech stack overview and rationale |
| `002-go-fhir-server.md` | Go-based FHIR R5 server specification |
| `003-frontend-stack.md` | Frontend framework and UI architecture |
| `004-data-pipeline.md` | Data ingestion, transformation, storage |
| `005-no-code-tools.md` | No-code/low-code tools in the ecosystem |

## Key constraints

- Go as primary language (ADR-001)
- No JVM/HAPI FHIR (Law 11, ADR-004)
- FHIR R5 (ADR-005)
- Zero-cost toolchain (ADR-006)
- Markdown-first documentation (ADR-007)
- Follow ZUSS structure, run refresh + validate after changes
