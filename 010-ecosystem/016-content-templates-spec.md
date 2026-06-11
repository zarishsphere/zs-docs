---
id: "ZS-016-ECO"
title: "016 content templates spec"
domain: "010-ecosystem"
doc-type: "component spec"
summary: >-
  Specification for zs-content-templates — the repository for pre-configured
  deployment templates and distribution packages across all five planes.
  Templates enable repeatable, one-click deployments with variable substitution.
tags:
  - content
  - templates
  - deployment
  - distribution
  - plane
  - configuration
entity-type: "component-specification"
version: "1.0.0"
status: "stable"
last_updated: 2026-06-11
last_verified: 2026-06-11
verified_by: "Mohammad Ariful Islam"
next_review: 2026-09-11
isolation_tier: "global"
canonical: true
depends_on:
  - "ZS-011-ECO"
  - "ZS-003-PLA"
related:
  - "ZS-014-ECO"
  - "ZS-015-ECO"
  - "ZS-017-ECO"
  - "ZS-010-ECO"
capabilities:
  - agent-skill: "parse_016_content_templates_spec"
  - mcp-resource: "content_templates_spec"
audience:
  - "contributors"
  - "deployers"
---

# 016-content-templates-spec.md
## zs-content-templates specification
### Deployment templates and distribution packages

**Document type:** Component spec
**Date:** June 11, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1
**GitHub:** https://github.com/zarishsphere

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Repository structure](#2-repository-structure)
3. [Template format](#3-template-format)
4. [Version pinning](#4-version-pinning)
5. [Distribution packages](#5-distribution-packages)
6. [Plane 0 operation](#6-plane-0-operation)
7. [Cross-references](#7-cross-references)

---

## 1. Purpose

The `zs-content-templates` repository provides pre-configured deployment templates and distribution packages for every deployment plane. Templates use YAML with variable substitution to enable repeatable, one-click deployments tailored to specific contexts.

Key design principles:

- **Every plane is first-class** — templates for Plane 0 through Plane 4
- **Variable-driven** — one template generates many configurations
- **Version-pinned** — every component reference points to a specific version
- **Distribution-ready** — templates bundle with distribution packages for offline deployment

## 2. Repository structure

```
zs-content-templates/
├── templates/
│   ├── plane-0/
│   │   ├── air-gapped-clinic.yaml
│   │   ├── mobile-health-unit.yaml
│   │   └── emergency-response.yaml
│   ├── plane-1/
│   │   ├── rpi-health-post.yaml
│   │   ├── edge-education.yaml
│   │   └── field-logistics.yaml
│   ├── plane-2/
│   │   ├── district-health-office.yaml
│   │   ├── sub-national-hub.yaml
│   │   └── camp-coordination.yaml
│   ├── plane-3/
│   │   ├── national-health-program.yaml
│   │   └── ministry-portal.yaml
│   └── plane-4/
│       ├── global-saas.yaml
│       └── multi-tenant-foundation.yaml
├── distributions/
│   ├── air-gapped-clinic/
│   │   ├── manifest.yaml
│   │   ├── config/
│   │   ├── forms/
│   │   ├── protocols/
│   │   └── scripts/
│   └── district-health/
│       ├── manifest.yaml
│       ├── config/
│       └── scripts/
├── schemas/
│   ├── template-schema.json
│   └── distribution-manifest-schema.json
├── examples/
│   └── variable-substitution-demo/
└── tests/
    └── validate-templates.go
```

### 2.1 Directory conventions

| Directory | Purpose |
|---|---|
| `templates/{plane}/` | Deployment templates organized by target plane |
| `distributions/{name}/` | Complete distribution packages with bundled content |
| `schemas/` | JSON Schema for template and manifest validation |
| `examples/` | Demonstrations of variable substitution |
| `tests/` | Automated template validation and rendering tests |

## 3. Template format

Templates are YAML files with Go template syntax for variable substitution.

### 3.1 Template structure

```yaml
# air-gapped-clinic.yaml
template:
  id: zs-template-airgap-clinic-v1
  name: Air-Gapped Clinic
  version: 1.0.0
  target_plane: 0
  description: >
    Single-device deployment for clinics with no internet connectivity.
    All forms, protocols, and modules bundled at deployment time.

  variables:
    - name: clinic_name
      type: string
      default: "Unnamed Clinic"
      description: Name of the clinic
    - name: locale
      type: choice
      default: "en"
      options: ["en", "fr", "ar", "bn", "my"]
      description: Primary language
    - name: modules
      type: list
      default: ["health-core", "ncd-screening"]
      description: Modules to include
    - name: storage_path
      type: string
      default: "/opt/zarishsphere/data"
      description: Data storage location

  include_forms:
    - zs-ncd-intake-v1
    - zs-patient-registration-v1
    - zs-consent-form-v1

  include_protocols:
    - zs-ncd-screening-v1
    - zs-triage-protocol-v1

  include_modules:
    {{- range .modules }}
    - {{ . }}
    {{- end }}

  system_config:
    identities:
      auth_mode: "local"
      default_admin: "admin"
    encryption:
      key_path: "{{ .storage_path }}/keys"
    storage:
      type: "local"
      path: "{{ .storage_path }}"
    sync:
      mode: "usb"
      export_path: "{{ .storage_path }}/export"

  docker_compose:
    version: "3.8"
    services:
      engine:
        image: "zarishsphere/engine:1.0.0"
        volumes:
          - "{{ .storage_path }}:/data"
        environment:
          - ZS_CLINIC_NAME={{ .clinic_name }}
          - ZS_LOCALE={{ .locale }}
          - ZS_STORAGE_PATH={{ .storage_path }}
```

### 3.2 Variable substitution

Template variables use the Go `text/template` syntax:

| Syntax | Description | Example |
|---|---|---|
| `{{ .variable_name }}` | Simple substitution | `{{ .clinic_name }}` |
| `{{- range .list }}` | List iteration | Iterate over modules |
| `{{ if .condition }}` | Conditional inclusion | Optional features |
| `{{ default .var "fallback" }}` | Default value | When variable is empty |

### 3.3 Rendering pipeline

```
Template (YAML + Go templates)
    ↓ (render with variable values)
Rendered configuration (pure YAML)
    ↓ (validate against schema)
Validated deployment spec
    ↓ (pass to deployment engine)
Running system
```

## 4. Version pinning

> **Constraint:** The `latest` tag must never be used. Every component reference in a template must pin to a specific semantic version.

### 4.1 Pinning rules

| Reference type | Format | Example |
|---|---|---|
| Docker image | `image:tag` | `zarishsphere/engine:1.0.0` |
| GitHub repo | `repo@ref` | `zarishsphere/zs-platform@v1.0.0` |
| Form | `id@version` | `zs-ncd-intake@1.0.0` |
| Protocol | `id@version` | `zs-ncd-screening@1.0.0` |
| Module | `id@version` | `health-core@1.0.0` |

### 4.2 Version update process

When a dependency version is updated:

1. A new template version is created
2. The old template remains available for existing deployments
3. Deployers receive a notification about the available update
4. Updates are applied via the Console with one click

## 5. Distribution packages

Distribution packages combine templates with bundled content for offline deployment.

### 5.1 Package structure

```
zs-distribution-airgap-clinic-v1/
├── manifest.yaml           ← Package metadata + version manifest
├── template.yaml           ← Main deployment template
├── config/
│   ├── default-variables.yaml
│   └── custom-variables.yaml
├── forms/                  ← Pre-loaded form definitions
│   ├── zs-ncd-intake-v1.json
│   └── zs-patient-registration-v1.json
├── protocols/              ← Pre-loaded protocol definitions
│   ├── ncd-screening-v1.yaml
│   └── triage-protocol-v1.yaml
├── docker-compose.yml      ← Rendered from template
└── scripts/
    ├── setup.sh
    └── configure.sh
```

### 5.2 Manifest format

```yaml
# manifest.yaml
distribution:
  id: zs-distro-airgap-clinic-v1
  name: Air-Gapped Clinic Distribution
  version: 1.0.0
  target_plane: 0
  min_ram_gb: 4
  min_storage_gb: 64

  components:
    engine: "1.0.0"
    forms:
      - zs-ncd-intake@1.0.0
      - zs-patient-registration@1.0.0
    protocols:
      - zs-ncd-screening@1.0.0
    modules:
      - health-core@1.0.0

  checksum: "sha256-abc123..."
  signature: "..."
```

## 6. Plane 0 operation

At Plane 0:

- Templates are pre-rendered at distribution build time — no template engine runs on the device
- All variable substitution happens on the build server before the bundle is finalized
- Distribution packages include all dependencies — no network fetch required
- The setup script reads the rendered configuration from the local filesystem
- Customization is possible post-deployment via local config file editing

## 7. Cross-references

→ **011-distributions-spec.md** — Distribution specification that packages templates
→ **003-platform/003-deployment-planes.md** — Plane specifications for template targeting
→ **010-modules-spec.md** — Modules referenced in templates
→ **014-content-forms-spec.md** — Forms bundled in templates
→ **015-content-protocols-spec.md** — Protocols bundled in templates
→ **001-meta/001-zarishsphere-constitution.md** — Law 4 (Plane 0 compliance)

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
