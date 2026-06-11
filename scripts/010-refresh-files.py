#!/usr/bin/env python3
"""
010-refresh-files.py — Refresh all generated files in zs-docs.

This is the single script you need to run after adding/changing any .md file.
It performs 4 steps, each idempotent (skips if already correct):

  1. NORMALIZE — Ensures every .md file has required front matter fields
     (doc-type, entity-type, summary, tags, audience). Only adds missing
     fields; never overwrites existing values.

  2. INDEX — Regenerates INDEX.md for all 10 folders + root INDEX.md.
     Reads actual file metadata from front matter; table is always current.

  3. LLMS — Regenerates llms.txt (AI-agent-readable file index) from
     actual file front matter summaries.

  4. FOOTER — Ensures every .md file ends with the canonical license footer.
     Detects and removes duplicate footers, fixes stale license text.

Usage:
  python3 scripts/010-refresh-files.py          # run all 4 steps
  python3 scripts/010-refresh-files.py --steps  # interactive step selection

Expected outcome:
  - All front matter fields present and correct
  - All INDEX.md files accurately reflect current file set
  - llms.txt is up to date
  - All footers are canonical (3-line block)

Next steps after a successful run:
  Run scripts/001-zuss-validate.sh to confirm zero compliance failures.
"""

import os, re, json, shutil, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().strftime('%B %d, %Y')
STEP_STATE = {'ran': False, 'changed': 0, 'unchanged': 0}

# ─── Helpers ──────────────────────────────────────────────────────────

def blue(t): return f"\033[1;36m{t}\033[0m"
def green(t): return f"\033[0;32m{t}\033[0m"
def red(t): return f"\033[0;31m{t}\033[0m"
def yellow(t): return f"\033[1;33m{t}\033[0m"

def banner(title):
    print(f"\n{blue('═══')} {title} {blue('═' * (60 - len(title)))}")

def parse_front_matter(content):
    """Extract YAML front matter dict from file content. Simple parse (no pyyaml)."""
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', content, re.DOTALL)
    if not m:
        m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    data = {}
    current_key = None
    current_list = None
    block_scalar = None
    block_lines = None
    for line in m.group(1).split('\n'):
        kv = re.match(r'^(\w[\w-]*):\s*(.*)', line)
        if kv:
            if block_scalar and current_key and block_lines:
                val_joined = ' '.join(block_lines) if block_scalar == 'folded' else '\n'.join(block_lines)
                data[current_key] = val_joined
                block_scalar = None
                block_lines = None
            if current_list is not None and current_key:
                data[current_key] = current_list
                current_list = None
            current_key = kv.group(1)
            val = kv.group(2).strip()
            if val in ('>-', '>'):
                block_scalar = 'folded'
                block_lines = []
                continue
            elif val in ('|', '|-',):
                block_scalar = 'literal'
                block_lines = []
                continue
            elif val == '':
                current_list = []
                continue
            elif val.startswith('['):
                try: data[current_key] = json.loads(val)
                except: data[current_key] = val.strip('"').strip("'")
            elif val.lower() in ('true', 'false'):
                data[current_key] = val.lower() == 'true'
            elif val == '~' or val == 'null':
                data[current_key] = None
            else:
                data[current_key] = val.strip('"').strip("'")
        elif block_scalar and current_key and line.startswith('  '):
            block_lines.append(line.strip())
        elif current_key and line.strip().startswith('- '):
            if current_list is None:
                current_list = []
            current_list.append(line.strip()[2:].strip('"').strip("'"))
    if block_scalar and current_key and block_lines:
        val_joined = ' '.join(block_lines) if block_scalar == 'folded' else '\n'.join(block_lines)
        data[current_key] = val_joined
    if current_list is not None and current_key:
        data[current_key] = current_list
    return data

def is_skeleton(filepath):
    """Detect skeleton files (under ~30 lines, no substantive prose)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if len(lines) < 30:
            return True
        body_started = False
        content_lines = 0
        for line in lines:
            if line.startswith('---'):
                body_started = not body_started
                continue
            if body_started and line.strip() and not line.strip().startswith('#'):
                clean = line.strip().strip('*')
                if len(clean) > 15:
                    content_lines += 1
        return content_lines < 3
    except:
        return True

def iter_md_files(root=ROOT, exclude_index=False, exclude_root_info=False):
    """Yield (relpath, abspath) for all .md files."""
    skip_names = set()
    if exclude_root_info:
        skip_names.update({'AGENTS.md', 'README.md', 'TODO.md'})
    for folder in sorted(os.listdir(root)):
        fp = os.path.join(root, folder)
        if not os.path.isdir(fp) or not re.match(r'^\d{3}-', folder):
            continue
        for f in sorted(os.listdir(fp)):
            if not f.endswith('.md'):
                continue
            if exclude_index and f == 'INDEX.md':
                continue
            yield f"{folder}/{f}", os.path.join(fp, f)
    # Root files
    for f in ['INDEX.md', 'AGENTS.md', 'README.md', 'TODO.md']:
        if f in skip_names:
            continue
        fp = os.path.join(root, f)
        if os.path.exists(fp):
            yield f, fp

# ─── Step 1: Normalize labels ────────────────────────────────────────

DEFAULTS = {
    "001-meta/004-writing-rules.md": {
        "doc-type": "normative standard", "entity-type": "rulebook",
        "summary": "ZarishSphere Universal Serialization Standard (ZUSS) — the single, consistent rule set governing how every file, folder, repository, workflow, identifier, and document is named, structured, and written within the ZarishSphere ecosystem.",
        "tags": ["zuss", "standards", "documentation", "naming", "formatting"], "audience": ["all"],
    },
    "004-zarish-index/001-zarish-index-overview.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Project charter and platform-level view of ZARISH-INDEX — the first free, open-source, machine-readable unified index of every global standard, framework, treaty, guideline, and technical specification across all domains of human civilization.",
        "tags": ["zarish-index", "overview", "charter", "standards-index"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "004-zarish-index/002-domain-taxonomy-40.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Complete 40-domain master taxonomy for the ZARISH-INDEX. Every global standard maps to exactly one of 40 primary domains across 6 meta-layers, each with a unique prefix code.",
        "tags": ["zarish-index", "taxonomy", "domains", "classification"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "004-zarish-index/003-metadata-schema.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Data schema for ZARISH-INDEX entries. Every record contains exactly 22 structured fields across 4 supplementary tables — covering standards bodies, inter-standard relationships, ratification tracking, and research tasks.",
        "tags": ["zarish-index", "metadata", "schema", "data-model"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "004-zarish-index/004-harvesting-policy.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Strategic direction and harvesting policy for ZARISH-INDEX — an autonomous open research project maintaining the most complete freely accessible machine-readable index of global standards.",
        "tags": ["zarish-index", "harvesting", "policy", "strategic-direction"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "004-zarish-index/005-zarish-index-to-platform.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Integration architecture connecting ZARISH-INDEX to the ZarishSphere Platform. Defines the two-project pipeline from standards index through G2A transformation to deployable digital assets.",
        "tags": ["zarish-index", "platform-integration", "architecture", "pipeline"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "005-zarish-standards/001-zarish-standards-overview.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Strategic direction for ZARISH-STANDARDS — ZarishSphere's curated, implementation-focused registry of every international, regional, national, and humanitarian standard the platform enforces, implements, or references.",
        "tags": ["zarish-standards", "overview", "strategic-direction", "standards-registry"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "005-zarish-standards/002-transformation-model.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Data mapping and structural transformation model that converts ZARISH-INDEX entries into ZARISH-STANDARDS executable definitions. Defines the INDEX-to-STANDARDS pipeline rules.",
        "tags": ["zarish-standards", "transformation", "data-mapping", "pipeline"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "005-zarish-standards/003-standards-schema.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Validation pipeline machine-readable schemas for ZARISH-STANDARDS. Defines the formal schema that every standard entity must conform to for platform consumption.",
        "tags": ["zarish-standards", "schema", "validation", "data-model"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "005-zarish-standards/004-standards-to-platform-pipeline.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Real-time standards enforcement pipeline connecting ZARISH-STANDARDS to the ZarishSphere Platform G2A Engine. Defines how standards are deployed, updated, and enforced across all deployment planes.",
        "tags": ["zarish-standards", "pipeline", "platform-integration", "g2a"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "006-infrastructure/001-infrastructure-overview.md": {
        "doc-type": "architecture", "entity-type": "architecture-document",
        "summary": "Enterprise infrastructure and zero-touch deployment mapping for the ZarishSphere ecosystem. Covers all infrastructure layers, design principles, and deployment automation strategy.",
        "tags": ["infrastructure", "overview", "architecture", "deployment"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "006-infrastructure/002-github-org-architecture.md": {
        "doc-type": "architecture", "entity-type": "architecture-document",
        "summary": "GitHub organisation architecture and configuration for the ZarishSphere Foundation. Defines repository structure, team models, branch protection rules, and governance automation.",
        "tags": ["infrastructure", "github", "organisation", "architecture"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "006-infrastructure/003-cloudflare-architecture.md": {
        "doc-type": "architecture", "entity-type": "architecture-document",
        "summary": "Cloudflare edge routing, WAF, and nameserver architecture for the ZarishSphere ecosystem. Covers DNS, CDN, DDoS protection, SSL/TLS, Pages, and Tunnel configuration.",
        "tags": ["infrastructure", "cloudflare", "dns", "edge", "waf"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "006-infrastructure/004-domain-architecture.md": {
        "doc-type": "architecture", "entity-type": "architecture-document",
        "summary": "Domain hierarchy and internal routing subsystem for ZarishSphere. Defines all domains, subdomains, DNS zones, and routing rules across all deployment planes.",
        "tags": ["infrastructure", "domains", "dns", "routing", "architecture"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "006-infrastructure/005-email-architecture.md": {
        "doc-type": "architecture", "entity-type": "architecture-document",
        "summary": "Secure decentralised communication and relay infrastructure for ZarishSphere. Covers email routing, SMTP configuration, DKIM/DMARC/SPF, and identity-based addressing.",
        "tags": ["infrastructure", "email", "smtp", "security", "architecture"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "006-infrastructure/006-ci-cd-architecture.md": {
        "doc-type": "architecture", "entity-type": "architecture-document",
        "summary": "CI/CD orchestration layout via GitHub Actions for the ZarishSphere ecosystem. Defines pipeline stages, workflow definitions, artifact management, and deployment automation.",
        "tags": ["infrastructure", "ci-cd", "github-actions", "automation", "pipeline"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "007-tech-stack/001-tech-stack-master.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Master production tech stack mapping for the ZarishSphere ecosystem. Defines all technology choices including Go, React, Next.js, and the complete backend-frontend-data pipeline.",
        "tags": ["tech-stack", "go", "react", "nextjs", "architecture"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "007-tech-stack/002-go-fhir-server.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Go-native high-performance FHIR R5 server module specification. Defines the zero-JVM, Plane 0-compatible FHIR server architecture, resource model, and API contracts.",
        "tags": ["tech-stack", "go", "fhir", "r5", "server", "api"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "007-tech-stack/003-frontend-stack.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "UI component library layer specification using React 19, Next.js 15, and Tailwind CSS. Defines the frontend architecture, component design system, and PWA capabilities.",
        "tags": ["tech-stack", "frontend", "react", "nextjs", "tailwind", "ui"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "007-tech-stack/004-data-pipeline.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Analytical real-time data infrastructure pipeline specification. Defines data ingestion, transformation, storage, and analytics architecture for the ZarishSphere Platform.",
        "tags": ["tech-stack", "data", "pipeline", "analytics", "architecture"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "007-tech-stack/005-no-code-tools.md": {
        "doc-type": "specification", "entity-type": "specification",
        "summary": "Offline-capable extensibility layout via declarative low-code integration. Defines the no-code tooling stack for form builders, workflow designers, and module creators.",
        "tags": ["tech-stack", "no-code", "low-code", "extensibility", "tools"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/001-adr-go-as-primary-language.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-001: Selection of Go as the primary engine language for the ZarishSphere Platform. Decision to use Go 1.26+ for all backend services, FHIR server, and G2A Engine implementation.",
        "tags": ["adr", "go", "language", "decision", "technology"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/002-adr-cloudflare-as-edge-platform.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-002: Selection of Cloudflare as the edge platform for WAF, CDN, DNS, and global hosting for all ZarishSphere web properties.",
        "tags": ["adr", "cloudflare", "edge", "waf", "cdn", "dns"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/003-adr-github-as-government.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-003: GitOps and GitHub as the operational rule ownership and governance control plane for the ZarishSphere Foundation.",
        "tags": ["adr", "github", "governance", "gitops"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/004-adr-no-hapi-fhir.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-004: Rejection of Java HAPI FHIR and decision to build a Go-native FHIR server. Motivated by the Plane 0 constraint and 8GB RAM limit (Constitution Law 11).",
        "tags": ["adr", "fhir", "hapi", "go", "architecture", "constraint"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/005-adr-fhir-r5-over-r4.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-005: Enforcement of FHIR R5 as the canonical FHIR version for the ZarishSphere Platform. Decision to implement FHIR R5 natively rather than using R4 with extensions.",
        "tags": ["adr", "fhir", "r5", "r4", "standards"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/006-adr-zero-cost-toolchain.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-006: Structural requirement for open-source, zero-cost toolchain dependencies across the entire ZarishSphere ecosystem. No paid tools, licenses, or services required.",
        "tags": ["adr", "zero-cost", "open-source", "toolchain", "constraint"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/007-adr-markdown-first-documentation.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-007: Plaintext markdown-first documentation architecture standard for all ZarishSphere documentation. Every document is a markdown file with YAML front matter.",
        "tags": ["adr", "markdown", "documentation", "standard"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/008-adr-apache-cc-dual-license.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-008: Dual-licensing rules for open-source modularity — Apache 2.0 for code, CC BY 4.0 for documentation across all ZarishSphere projects.",
        "tags": ["adr", "license", "apache", "cc-by", "open-source"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/009-adr-no-vendor-lock-in.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-009: Decoupling the platform layer from cloud infrastructure provider specific dependencies. Ensures ZarishSphere can run on any infrastructure without vendor lock-in.",
        "tags": ["adr", "vendor-lock-in", "portability", "architecture", "constraint"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "008-adrs/010-adr-gui-first-ux.md": {
        "doc-type": "adr", "entity-type": "decision-record",
        "summary": "ADR-010: High-fidelity UI/UX interactivity standards for field deployment. The Console is the primary interface; CLI is always secondary.",
        "tags": ["adr", "ui", "ux", "gui-first", "console", "design"], "audience": ["contributors", "deployers", "ai-agents"],
    },
    "009-operations/001-sop-new-document-creation.md": {
        "doc-type": "sop", "entity-type": "procedure",
        "summary": "SOP-001: How to provision and validate a new documentation node following ZUSS conventions. Covers file creation, front matter setup, and compliance validation.",
        "tags": ["sop", "documentation", "creation", "workflow"], "audience": ["contributors", "ai-agents"],
    },
    "009-operations/002-sop-github-workflow.md": {
        "doc-type": "sop", "entity-type": "procedure",
        "summary": "SOP-002: Repository branching, protecting, merging, and pull request models for ZarishSphere projects. Defines the complete GitHub-based workflow.",
        "tags": ["sop", "github", "branching", "pr", "workflow"], "audience": ["contributors", "deployers"],
    },
    "009-operations/003-sop-contribution-process.md": {
        "doc-type": "sop", "entity-type": "procedure",
        "summary": "SOP-003: Review pipeline and external patch merge processing. Covers the complete contribution lifecycle from issue to merge for all ZarishSphere projects.",
        "tags": ["sop", "contribution", "review", "pipeline", "workflow"], "audience": ["contributors"],
    },
    "009-operations/004-sop-zuss-compliance-audit.md": {
        "doc-type": "sop", "entity-type": "procedure",
        "summary": "SOP-004: Systematic compliance and formatting audit checks. How to run validation scripts and verify ZUSS compliance across all documentation.",
        "tags": ["sop", "compliance", "audit", "zuss", "validation"], "audience": ["contributors", "ai-agents"],
    },
    "009-operations/005-sop-deployment-checklist.md": {
        "doc-type": "sop", "entity-type": "procedure",
        "summary": "SOP-005: Automated documentation build and synchronisation production checklist. Pre-deployment validation and release procedure for zs-docs.",
        "tags": ["sop", "deployment", "checklist", "release", "automation"], "audience": ["contributors", "deployers"],
    },
}

REQUIRED_FIELDS = ["doc-type", "entity-type", "summary", "tags", "audience"]

def step_normalize():
    """Add missing required front matter fields to known files."""
    STEP_STATE['ran'] = False
    STEP_STATE['changed'] = 0
    banner("Step 1/4: Normalize front matter labels")
    changed = 0
    ok = 0
    for relpath, defaults in sorted(DEFAULTS.items()):
        filepath = os.path.join(ROOT, relpath.replace('/', os.sep))
        if not os.path.exists(filepath):
            print(f"  {yellow('SKIP')} {relpath} — file not found")
            continue
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        data = parse_front_matter(content)
        if not data:
            print(f"  {yellow('SKIP')} {relpath} — no YAML front matter")
            continue
        # Check which fields are missing
        missing = {}
        for field in REQUIRED_FIELDS:
            val = defaults.get(field)
            if field not in data or data[field] is None or data[field] == '':
                missing[field] = val
            elif isinstance(data[field], list) and len(data[field]) == 0 and isinstance(val, list):
                missing[field] = val
        if not missing:
            print(f"  {green('OK')}{'':>8} {relpath}")
            ok += 1
            continue
        # Remove old front matter and rebuild
        body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, count=1, flags=re.DOTALL)
        for field, val in missing.items():
            data[field] = val
        yaml_str = _build_yaml(data)
        new_content = f"---\n{yaml_str}\n---\n{body}"
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  {green('FIX')}{'':>8} {relpath} — added {', '.join(missing.keys())}")
            changed += 1
        else:
            print(f"  {green('OK')}{'':>8} {relpath}")
            ok += 1
    STEP_STATE['ran'] = True
    STEP_STATE['changed'] = changed
    STEP_STATE['unchanged'] = ok
    print(f"  {'─' * 55}")
    print(f"  {green(f'Fixed: {changed}')}, {green(f'Already OK: {ok}')}")
    print(f"  {green('✓ Labels normalized.')}")

# ─── Step 2: Generate INDEX.md ───────────────────────────────────────

FOLDER_META = {
    "001-meta": { "title": "001 meta index", "h1": "# 001-meta/ index", "h2": "## Foundation and meta-governance documents",
        "desc": "Everything starts here. These 7 documents define the ZarishSphere ecosystem's identity, rules, architecture, and strategy. Read in numerical order.",
        "audience": ["all"], "tags": ["index", "navigation", "foundation", "meta"], },
    "002-foundation": { "title": "002 foundation index", "h1": "# 002-foundation/ index", "h2": "## Foundation governance documents",
        "desc": "Governance and legal framework for the ZarishSphere Foundation. Covers the institution's charter, decision-making model, licensing, and contribution guidelines.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "governance", "foundation"], },
    "003-platform": { "title": "003 platform index", "h1": "# 003-platform/ index", "h2": "## Platform architecture specifications",
        "desc": "Technical architecture for the ZarishSphere Platform. 8 documents covering the full platform design from overview through domain taxonomy.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "platform", "architecture"], },
    "004-zarish-index": { "title": "004 zarish-index index", "h1": "# 004-zarish-index/ index", "h2": "## ZARISH-INDEX specifications",
        "desc": "ZARISH-INDEX is the autonomous open research data product that indexes every global standard. These documents define its structure, taxonomy, and integration with the platform.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "zarish-index", "standards"], },
    "005-zarish-standards": { "title": "005 zarish-standards index", "h1": "# 005-zarish-standards/ index", "h2": "## ZARISH-STANDARDS specifications",
        "desc": "ZARISH-STANDARDS is the transformation layer that converts ZARISH-INDEX entries into machine-executable assets via the G2A pipeline.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "zarish-standards", "transformation"], },
    "006-infrastructure": { "title": "006 infrastructure index", "h1": "# 006-infrastructure/ index", "h2": "## Infrastructure architecture documents",
        "desc": "Infrastructure design and configuration for the ZarishSphere ecosystem. Covers GitHub organisation, Cloudflare setup, domain architecture, email routing, and CI/CD pipelines.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "infrastructure", "cloudflare", "github"], },
    "007-tech-stack": { "title": "007 tech-stack index", "h1": "# 007-tech-stack/ index", "h2": "## Technology stack documents",
        "desc": "Technology choices and stack specifications for the ZarishSphere ecosystem. Covers backend, frontend, data, and no-code tooling.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "tech-stack", "technology"], },
    "008-adrs": { "title": "008 adrs index", "h1": "# 008-adrs/ index", "h2": "## Architecture Decision Records",
        "desc": "Every significant technical and governance decision is recorded as an ADR. Each ADR follows the format defined in ZUSS §7.1: Decision, Context, Alternatives Considered, Reason, Consequences, Status.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "adrs", "decisions"], },
    "009-operations": { "title": "009 operations index", "h1": "# 009-operations/ index", "h2": "## Standard Operating Procedures",
        "desc": "Operational procedures for the ZarishSphere ecosystem. Every SOP follows the format defined in ZUSS §7.2: Purpose, Scope, Roles, Preconditions, Steps (GUI-first), Expected Outcome, Escalation.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "operations", "sop"], },
    "010-ecosystem": { "title": "010 ecosystem index", "h1": "# 010-ecosystem/ index", "h2": "## Ecosystem component specifications",
        "desc": "Complete component specifications for the ZarishSphere ecosystem. 13 documents covering every platform component from the browser-based Console through the base System environment.",
        "audience": ["contributors", "deployers", "ai-agents"], "tags": ["index", "navigation", "ecosystem", "components"], },
}
SORTED_FOLDERS = sorted(FOLDER_META.keys())

def _build_yaml(data):
    """Build YAML front matter string from dict, preserving field order."""
    order = ['id', 'title', 'domain', 'doc-type', 'entity-type', 'summary',
             'tags', 'version', 'status', 'last_updated', 'isolation_tier',
             'canonical', 'audience']
    lines = []
    for key in order:
        if key not in data:
            continue
        val = data[key]
        if val is None or (isinstance(val, list) and len(val) == 0):
            continue
        if isinstance(val, bool):
            lines.append(f"{key}: {'true' if val else 'false'}")
        elif isinstance(val, list):
            if len(val) == 1 and len(str(val[0])) < 40:
                lines.append(f"{key}: [{', '.join(v for v in val)}]")
            else:
                lines.append(f"{key}:")
                for v in val:
                    lines.append(f"  - \"{v}\"")
        elif isinstance(val, str) and ('\n' in val or len(val) > 80):
            clean = val.replace('\n', ' ').strip()
            lines.append(f"{key}: >-")
            words = clean.split()
            line = "  "
            for word in words:
                if len(line) + len(word) + 1 > 78:
                    lines.append(line)
                    line = "  " + word
                else:
                    line = line + (" " if line != "  " else "") + word
            if line:
                lines.append(line)
        else:
            lines.append(f"{key}: \"{val}\"")
    return '\n'.join(lines)

def gen_folder_index(folder_name):
    """Generate INDEX.md content for one folder."""
    meta = FOLDER_META[folder_name]
    fpath = os.path.join(ROOT, folder_name)
    files = []
    for f in sorted(os.listdir(fpath)):
        if not f.endswith('.md') or f == 'INDEX.md':
            continue
        fp = os.path.join(fpath, f)
        fm = parse_front_matter(open(fp, 'r', encoding='utf-8', errors='replace').read())
        num = f.split('-')[0]
        title = fm.get('title', f.replace('.md', ''))
        summary = fm.get('summary', '')
        doc_type = fm.get('doc-type', '')
        status_raw = fm.get('status', '')
        is_s = is_skeleton(fp)
        if status_raw and status_raw.lower() != 'active':
            status = status_raw.capitalize()
        elif is_s:
            status = 'Skeleton'
        else:
            status = 'Stable'
        files.append({'num': num, 'filename': f, 'title': title, 'summary': summary, 'doc_type': doc_type, 'status': status})
    total = len(files)
    stable_n = sum(1 for f in files if f['status'].lower() in ('active', 'stable'))
    draft_n = sum(1 for f in files if f['status'].lower() == 'draft')
    skeleton_n = sum(1 for f in files if f['status'].lower() == 'skeleton')
    summary_parts = []
    if stable_n: summary_parts.append(f'{stable_n} stable')
    if draft_n: summary_parts.append(f'{draft_n} draft')
    if skeleton_n: summary_parts.append(f'{skeleton_n} skeleton')
    summary_str = ', '.join(summary_parts) if summary_parts else f'{total} documents'
    ydata = {'id': f"ZS-INDEX-{folder_name.split('-')[0]}", 'title': meta['title'],
        'domain': folder_name, 'doc-type': 'index',
        'summary': f"Index for the {folder_name}/ folder. {total} documents ({summary_str}).",
        'tags': meta['tags'], 'entity-type': 'folder-index', 'version': '1.0.0', 'status': 'stable',
        'last_updated': date.today().isoformat(), 'isolation_tier': 'global', 'canonical': True, 'audience': meta['audience']}
    lines = [f"---\n{_build_yaml(ydata)}\n---", '', meta['h1'], meta['h2'], '', f'> {meta["desc"]}', '', '---', '', '## File index', '',
        f'| # | File | Description | Type | Status |', f'|---|---|---|---|---|']
    for f in files:
        desc = (f['summary'][:100] + '...') if len(f['summary']) > 100 else f['summary']
        lines.append(f'| {f["num"]} | [{f["filename"]}]({f["filename"]}) | {desc} | {f["doc_type"]} | {f["status"]} |')
    lines += ['', '---', '', '## Navigation', '', '- **Parent:** [Root index](../INDEX.md)']
    idx = SORTED_FOLDERS.index(folder_name)
    if idx > 0:
        lines.append(f'- **Previous:** [{SORTED_FOLDERS[idx-1]}/](../{SORTED_FOLDERS[idx-1]}/INDEX.md)')
    if idx < len(SORTED_FOLDERS) - 1:
        lines.append(f'- **Next:** [{SORTED_FOLDERS[idx+1]}/](../{SORTED_FOLDERS[idx+1]}/INDEX.md)')
    lines += ['', '---', '', '', f'*ZarishSphere Foundation · V1 · {TODAY}*',
        '*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*', '*GitHub: https://github.com/zarishsphere*', '']
    return '\n'.join(lines)

def gen_root_index():
    """Generate root INDEX.md."""
    ydata = {'id': 'ZS-INDEX-ROOT', 'title': 'zs-docs root index', 'domain': 'zs-docs', 'doc-type': 'root-index',
        'summary': 'Root navigation index for the zs-docs repository — single source of truth for ZarishSphere Foundation governance, platform architecture, ZARISH-INDEX, ZARISH-STANDARDS, infrastructure, tech stack, ADRs, operations, and ecosystem integration.',
        'tags': ['index', 'navigation', 'root'], 'entity-type': 'root-index', 'version': '1.0.0', 'status': 'stable',
        'last_updated': date.today().isoformat(), 'isolation_tier': 'global', 'canonical': True, 'audience': ['all']}
    total_docs = total_s = 0
    by_status = {}
    rows = []
    for fn in SORTED_FOLDERS:
        fp = os.path.join(ROOT, fn)
        counts = {'stable': 0, 'draft': 0, 'skeleton': 0}
        for f in sorted(os.listdir(fp)):
            if not f.endswith('.md') or f == 'INDEX.md':
                continue
            fp2 = os.path.join(fp, f)
            fm2 = parse_front_matter(open(fp2, 'r', encoding='utf-8', errors='replace').read())
            s = fm2.get('status', '').lower().strip()
            if s in ('active', 'stable'):
                counts['stable'] += 1
            elif s == 'draft' and is_skeleton(fp2):
                counts['skeleton'] += 1
            else:
                counts['draft'] += 1
        total = sum(counts.values())
        total_docs += total
        total_s += counts['skeleton']
        by_status[fn] = counts
        meta = FOLDER_META[fn]
        if counts['skeleton'] == total:
            icon = '⬜ Skeleton'
        elif counts['skeleton'] > 0:
            a = counts['stable'] + counts['draft']
            icon = f'🔶 {a}/{total} authored'
        elif counts['stable'] == total:
            icon = '✅ Complete'
        else:
            icon = f'🔶 Draft'
        rows.append((fn, total, meta['desc'].split('.')[0], icon, meta['tags']))
    lines = [f"---\n{_build_yaml(ydata)}\n---", '', '# zs-docs root index', '## ZarishSphere Foundation — documentation repository', '',
        '> **Single source of truth** for governance, architecture, and platform design.',
        f'> Contains **{total_docs} documents** across **{len(SORTED_FOLDERS)} folders** managed by ZUSS conventions.', '',
        '---', '', '## Repository structure', '', '| # | Folder | Documents | Purpose | Status |', '|---|---|---|---|---|']
    for i, (fn, count, purpose, status, _) in enumerate(rows, 1):
        lines.append(f'| {fn.split("-")[0]} | [{fn}/]({fn}/INDEX.md) | {count} | {purpose} | {status} |')
    lines += ['', f'**Total: {total_docs} documents** ({total_docs - total_s} authored, {total_s} skeleton)', '', '---', '',
        '## Recommended reading order', '', 'Read folders in sequence. Within each folder, read files in numerical order.', '']
    for i, (fn, _, _, _, tags) in enumerate(rows, 1):
        tag_str = ', '.join(t for t in tags if t not in ('index', 'navigation'))
        lines.append(f'{i}. **{fn}/** — {tag_str}')
    lines += ['', '---', '', '## Quick links', '', '| Purpose | File |', '|---|---|',
        '| Constitution (start here) | [001-meta/001-zarishsphere-constitution.md](001-meta/001-zarishsphere-constitution.md) |',
        '| Writing rules (ZUSS) | [001-meta/004-writing-rules.md](001-meta/004-writing-rules.md) |',
        '| Architecture overview | [001-meta/005-ecosystem-architecture.md](001-meta/005-ecosystem-architecture.md) |',
        '| Glossary | [001-meta/006-glossary.md](001-meta/006-glossary.md) |',
        '| Agent strategy | [001-meta/007-agent-ecosystem-strategy.md](001-meta/007-agent-ecosystem-strategy.md) |',
        '| Platform overview | [003-platform/001-platform-overview.md](003-platform/001-platform-overview.md) |',
        '| Console (main UI) | [010-ecosystem/001-console-spec.md](010-ecosystem/001-console-spec.md) |',
        '', '---', '', '## Cross-repository map', '', '| Repo | Purpose | Docs reference |', '|---|---|---|',
        '| `zarishsphere/zs-docs` | Documentation (this repo) | This index |',
        '| `zarishsphere/zs-platform` | Platform implementation | `003-platform/` |',
        '| `zarishsphere/zs-zarish-index` | ZARISH-INDEX implementation | `004-zarish-index/` |',
        '| `zarishsphere/zs-zarish-standards` | ZARISH-STANDARDS implementation | `005-zarish-standards/` |',
        '| `zarishsphere/zs-fhir-hub` | FHIR Integration Hub | `010-ecosystem/` |',
        '| `zarishsphere/zs-home` | ZarishSphere Home landing site | `010-ecosystem/` |',
        '', '---', '', '## Validation', '', 'Run these scripts before any push:', '', '```bash',
        'scripts/001-zuss-validate.sh       # Naming, serialing, front matter, footers, banned words',
        'scripts/002-pipeline-status.sh     # Document completion status',
        'scripts/003-resolve-cross-refs.sh  # Cross-reference validation',
        '```', '', '---', '', '', f'*ZarishSphere Foundation · V1 · {TODAY}*',
        '*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*', '*GitHub: https://github.com/zarishsphere*', '']
    return '\n'.join(lines)

def step_index():
    """Regenerate all INDEX.md files."""
    STEP_STATE['ran'] = False
    STEP_STATE['changed'] = 0
    STEP_STATE['unchanged'] = 0
    banner("Step 2/4: Generate INDEX.md files")
    changed = unchanged = 0
    for fn in SORTED_FOLDERS:
        ipath = os.path.join(ROOT, fn, 'INDEX.md')
        content = gen_folder_index(fn)
        existing = open(ipath, 'r', encoding='utf-8').read() if os.path.exists(ipath) else ''
        if content == existing:
            print(f"  {green('OK')}{'':>8} {fn}/INDEX.md")
            unchanged += 1
        else:
            with open(ipath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  {green('UPDATE')} {fn}/INDEX.md")
            changed += 1
    # Root
    ripath = os.path.join(ROOT, 'INDEX.md')
    rcontent = gen_root_index()
    existing = open(ripath, 'r', encoding='utf-8').read() if os.path.exists(ripath) else ''
    if rcontent == existing:
        print(f"  {green('OK')}{'':>8} INDEX.md (root)")
        unchanged += 1
    else:
        with open(ripath, 'w', encoding='utf-8') as f:
            f.write(rcontent)
        print(f"  {green('UPDATE')} INDEX.md (root)")
        changed += 1
    STEP_STATE['ran'] = True
    STEP_STATE['changed'] = changed
    STEP_STATE['unchanged'] = unchanged
    print(f"  {'─' * 55}")
    print(f"  {green(f'Updated: {changed}')}, {green(f'Unchanged: {unchanged}')}")
    print(f"  {green('✓ INDEX.md files up to date.')}")

# ─── Step 3: Generate llms.txt ──────────────────────────────────────

FOLDER_LABELS = {
    "001-meta": "Foundation and governance (001-meta/)",
    "002-foundation": "Foundation governance (002-foundation/)",
    "003-platform": "Platform architecture (003-platform/)",
    "004-zarish-index": "ZARISH-INDEX (004-zarish-index/)",
    "005-zarish-standards": "ZARISH-STANDARDS (005-zarish-standards/)",
    "006-infrastructure": "Infrastructure (006-infrastructure/)",
    "007-tech-stack": "Technology stack (007-tech-stack/)",
    "008-adrs": "Architecture Decision Records (008-adrs/)",
    "009-operations": "Standard Operating Procedures (009-operations/)",
    "010-ecosystem": "Ecosystem components (010-ecosystem/)",
}

def gen_llmstxt():
    """Generate llms.txt content from actual file front matter."""
    lines = ['# zs-docs', '> ZarishSphere Foundation — master documentation repository',
        '> Single source of truth for governance, architecture, and platform documentation.',
        '> URL: https://github.com/zarishsphere/zs-docs', '',
        '## Navigation', '',
        '- [INDEX.md](INDEX.md): Root index with navigation routes for all 10 folders',
        '- [AGENTS.md](AGENTS.md): AI agent working memory — reading order, ZUSS rules, conventions', '',
        '## Essentials (read first)', '',
        '- [001-zarishsphere-constitution.md](001-meta/001-zarishsphere-constitution.md): Supreme governing document — 12 laws, 4 tiers',
        '- [005-ecosystem-architecture.md](001-meta/005-ecosystem-architecture.md): Master repository map, entity relationships, folder architecture',
        '- [004-writing-rules.md](001-meta/004-writing-rules.md): ZUSS naming and formatting standard (non-negotiable)',
        '- [006-glossary.md](001-meta/006-glossary.md): Canonical definitions for all ZarishSphere terms',
        '- [007-agent-ecosystem-strategy.md](001-meta/007-agent-ecosystem-strategy.md): AI agent, MCP, and skills strategy', '']
    for fn in SORTED_FOLDERS:
        fpath = os.path.join(ROOT, fn)
        label = FOLDER_LABELS[fn]
        entries = []
        for f in sorted(os.listdir(fpath)):
            if not f.endswith('.md') or f == 'INDEX.md':
                continue
            fp = os.path.join(fpath, f)
            fm = parse_front_matter(open(fp, 'r', encoding='utf-8', errors='replace').read())
            summary = fm.get('summary', '')
            desc = summary.split('.')[0] + '.' if '.' in summary else summary[:100]
            if not desc or desc == '.':
                desc = f.replace('.md', '').replace('-', ' ').title()
            entries.append((f, desc))
        lines.append(f'## {label}')
        lines.append('')
        for fname, desc in entries:
            lines.append(f'- [{fname}]({fn}/{fname}): {desc}')
        lines.append('')
    lines.append('## Validation scripts')
    lines.append('')
    lines.append('- [001-zuss-validate.sh](scripts/001-zuss-validate.sh): Naming, serialing, front matter, footers, banned words')
    lines.append('- [002-pipeline-status.sh](scripts/002-pipeline-status.sh): Document completion status')
    lines.append('- [003-resolve-cross-refs.sh](scripts/003-resolve-cross-refs.sh): Cross-reference validation')
    lines.append('')
    return '\n'.join(lines)

def step_llms():
    """Regenerate llms.txt."""
    STEP_STATE['ran'] = False
    STEP_STATE['changed'] = 0
    STEP_STATE['unchanged'] = 0
    banner("Step 3/4: Generate llms.txt")
    path = os.path.join(ROOT, 'llms.txt')
    content = gen_llmstxt()
    existing = open(path, 'r', encoding='utf-8').read() if os.path.exists(path) else ''
    if content == existing:
        print(f"  {green('OK')}{'':>8} llms.txt (unchanged)")
        STEP_STATE['unchanged'] = 1
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  {green('UPDATE')} llms.txt")
        STEP_STATE['changed'] = 1
    STEP_STATE['ran'] = True
    print(f"  {green('✓ llms.txt up to date.')}")

# ─── Step 4: Fix footers ────────────────────────────────────────────

FOOTER_PATTERNS = [
    r'\*ZarishSphere Foundation · V1 · [A-Za-z]+ \d+,? \d+\*',
    r'\*ZarishSphere Foundation · V1 · [A-Za-z]+ \d+\*',
    r'\*License: Apache 2\.0.*?\*',
    r'\*License: CC BY 4\.0\*',
    r'\*GitHub: https://github\.com/zarishsphere\*',
    r'\*License:.*?\*',
]
CANONICAL_FOOTER = [
    f"*ZarishSphere Foundation · V1 · {TODAY}*",
    "*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*",
    "*GitHub: https://github.com/zarishsphere*",
]
CANONICAL_BLOCK = '\n'.join(CANONICAL_FOOTER)

def step_footer():
    """Ensure all .md files have the canonical license footer."""
    STEP_STATE['ran'] = False
    STEP_STATE['changed'] = 0
    STEP_STATE['unchanged'] = 0
    banner("Step 4/4: Fix license footers")
    changed = unchanged = 0
    for relpath, filepath in iter_md_files():
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        original = content
        lines = content.split('\n')
        while lines and lines[-1].strip() == '':
            lines.pop()
        # Remove all existing footer-like lines
        footer_indices = set()
        for i, line in enumerate(lines):
            stripped = line.strip()
            for pat in FOOTER_PATTERNS:
                if re.match(pat + '$', stripped):
                    footer_indices.add(i)
                    break
            if stripped.startswith('→ **['):
                footer_indices.add(i)
        new_lines = [l for i, l in enumerate(lines) if i not in footer_indices]
        while new_lines and new_lines[-1].strip() == '':
            new_lines.pop()
        # Append canonical footer
        if new_lines and new_lines[-1].strip() == '---':
            new_lines.append('')
        else:
            new_lines.append('')
            new_lines.append('---')
        new_lines.append('')
        new_lines.extend(CANONICAL_FOOTER)
        new_lines.append('')
        result = '\n'.join(new_lines)
        if result != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"  {green('FIX')}{'':>8} {relpath}")
            changed += 1
        else:
            unchanged += 1
    STEP_STATE['ran'] = True
    STEP_STATE['changed'] = changed
    STEP_STATE['unchanged'] = unchanged
    print(f"  {'─' * 55}")
    if changed == 0 and unchanged > 0:
        print(f"  {green(f'All {unchanged} files already canonical.')}")
    else:
        print(f"  {green(f'Fixed: {changed}')}, {green(f'Already canonical: {unchanged}')}")
    print(f"  {green('✓ Footers canonical.')}")

# ─── Main ─────────────────────────────────────────────────────────────

def print_next_steps():
    print()
    print(blue("═══════════════════════════════════════════════════════"))
    print(blue("  All steps complete."))
    print(blue("═══════════════════════════════════════════════════════"))
    print()
    print("  Next steps:")
    print()
    print("  1. Run validation to confirm zero compliance failures:")
    print("     " + green("scripts/001-zuss-validate.sh"))
    print()
    print("  2. Check document completion status:")
    print("     " + green("scripts/002-pipeline-status.sh"))
    print()
    print("  3. Verify cross-references:")
    print("     " + green("scripts/003-resolve-cross-refs.sh"))
    print()
    print("  4. If all pass, your documentation is ready for commit.")

def main():
    print()
    print(blue("╔══════════════════════════════════════════════════════╗"))
    print(blue("║     zs-docs file refresh — normalise, index, llms  ║"))
    print(blue("║     Run after adding or changing any .md file      ║"))
    print(blue("╚══════════════════════════════════════════════════════╝"))
    print()
    print(f"  Root: {ROOT}")
    print(f"  Date: {TODAY}")
    print()

    steps = sys.argv[1:] if len(sys.argv) > 1 else ['all']
    if '--steps' in steps:
        print("  Available steps: all, normalize, index, llms, footer")
        return

    run_all = 'all' in steps
    if run_all or 'normalize' in steps:
        step_normalize()
    if run_all or 'index' in steps:
        step_index()
    if run_all or 'llms' in steps:
        step_llms()
    if run_all or 'footer' in steps:
        step_footer()

    if run_all:
        print_next_steps()

if __name__ == '__main__':
    main()
