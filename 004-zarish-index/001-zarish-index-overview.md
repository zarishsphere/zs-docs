---
id: "ZS-001-ZAR"
title: "001 zarish index overview"
domain: "004-zarish-index"
doc-type: "specification"
entity-type: "specification"
summary: >-
  Project charter and platform-level view of ZARISH-INDEX — the first free,
  open-source, machine-readable unified index of every global standard,
  framework, treaty, guideline, and technical specification across all domains
  of human civilization.
version: "1.0.0"
status: "stable"
tags:
  - "zarish-index"
  - "overview"
  - "charter"
  - "standards-index"
isolation_tier: "global"
capabilities:
  - "agent-skill: parse_001_zarish_index_overview"
audience:
  - "contributors"
  - "deployers"
  - "ai-agents"
last_updated: "2026-06-08"
---
# 001-project-charter.md
## ZARISH-INDEX — Project Charter
### World's First Unified Global Standards Index · Authoritative Reference

**Document type:** Project Charter — Authoritative
**Date:** June 01, 2026
**Author:** Mohammad Ariful Islam / ZarishSphere Foundation
**License:** CC BY 4.0
**Status:** V1 — Active. This document governs all ZARISH-INDEX work.

---

## Table of Contents

- [001-project-charter.md](#001-project-chartermd)
  - [ZARISH-INDEX — Project Charter](#zarish-index--project-charter)
    - [World's First Unified Global Standards Index · Authoritative Reference](#worlds-first-unified-global-standards-index--authoritative-reference)
  - [Table of Contents](#table-of-contents)
  - [1. What ZARISH-INDEX Is](#1-what-zarish-index-is)
  - [2. The Problem It Solves](#2-the-problem-it-solves)
    - [2.1 The fragmentation crisis](#21-the-fragmentation-crisis)
    - [2.2 The access inequality problem](#22-the-access-inequality-problem)
    - [2.3 Why it is now possible](#23-why-it-is-now-possible)
  - [3. Vision and Mission](#3-vision-and-mission)
    - [3.1 Vision](#31-vision)
    - [3.2 Mission](#32-mission)
  - [4. Scope — Inclusion Criteria](#4-scope--inclusion-criteria)
    - [4.1 What is included](#41-what-is-included)
    - [4.2 Explicitly included categories](#42-explicitly-included-categories)
    - [4.3 Explicitly out of scope](#43-explicitly-out-of-scope)
  - [5. Guiding Principles](#5-guiding-principles)
  - [6. Relationship to ZarishSphere](#6-relationship-to-zarishsphere)
  - [7. Project Identity](#7-project-identity)
  - [8. Governance and Ownership](#8-governance-and-ownership)
  - [9. License](#9-license)

---

## 1. What ZARISH-INDEX Is

ZARISH-INDEX is the world's first free, open-source, machine-readable, human-navigable unified index of every global standard, framework, treaty, guideline, classification system, code of practice, and technical specification that governs human civilisation.

It covers all 40 domains of human society — from health and education to aerospace and cultural heritage, from financial regulation to humanitarian response. It is published under CC BY 4.0 on GitHub, downloadable in CSV, JSON, JSONL, and Parquet formats, and served as a live website with no registration or paywall.

**Codename:** `ZARISH-INDEX`
**GitHub:** `github.com/zarishsphere/zarish-index`
**Live site:** `zarishsphere.github.io/zarish-index`
**License:** CC BY 4.0 — free to use, share, and adapt with attribution.

---

## 2. The Problem It Solves

### 2.1 The fragmentation crisis

Global standards are the intellectual infrastructure of human civilisation. They define how medicines are tested, how buildings stand, how aircraft fly, how money moves, how data is protected, how children are protected in emergencies, and how nations cooperate on climate change.

This infrastructure is profoundly fragmented:

| Body | Coverage | Access |
|---|---|---|
| ISO | 25,703+ standards | USD 120–400 per document |
| IEC | 12,000+ standards | Paywalled |
| ITU | Thousands of recommendations | Partially free |
| WHO | Hundreds of guidelines | Free but scattered |
| UN Treaty Collection | 560+ treaties | Free but poorly structured |
| ILO NORMLEX | 190 Conventions | Free but siloed |
| Codex Alimentarius | 3,000+ food safety texts | Free but across 8 databases |
| National standards bodies | 200,000+ national standards | Mostly paywalled |

No single searchable, filterable, cross-referenced index covers even a fraction of this landscape.

### 2.2 The access inequality problem

The entities most harmed by this fragmentation are those with fewest resources: NGOs in humanitarian settings, government agencies in low-income countries, small businesses trying to export, researchers at underfunded institutions, and citizens trying to understand their rights.

A Bangladeshi health worker finding the relevant WHO standard, a refugee protection officer checking applicable UNHCR guidelines, or a WASH engineer in a camp needing the Sphere minimum standard — none of these people should need to know which organisation to look in, in which database, using which search syntax.

ZARISH-INDEX removes that barrier permanently.

### 2.3 Why it is now possible

Several developments make this project feasible for the first time:

- ISO Open Data provides metadata for all 25,703+ standards as free CSV/JSON/Parquet — no registration
- Wikidata contains structured data on thousands of standards bodies, queryable via free SPARQL
- GitHub provides free hosting, version control, and CI/CD for data of this size
- GitHub Pages provides free static website hosting with no server required
- ILO NORMLEX, OHCHR treaty databases, UN Treaty Collection, WHO IRIS, and dozens of UN agency registries are freely accessible
- The tools, the data seeds, and the global need all align

---

## 3. Vision and Mission

### 3.1 Vision

> A world in which any person, in any country, in any sector, can instantly find, verify, and understand any global standard that affects their work or life — for free, in their language, in the format they need.

### 3.2 Mission

> To build, maintain, and freely publish the world's most complete, accurate, and usable unified index of global standards, standards bodies, frameworks, treaties, and guidelines — covering every domain of human society, in a machine-readable and human-navigable format, requiring no subscription or payment to access.

---

## 4. Scope — Inclusion Criteria

### 4.1 What is included

A standard is included if it meets all three conditions:

1. **Formal issuance** — Published by an identifiable standards body, international organisation, intergovernmental body, recognised professional association, or national government agency acting in a standardisation capacity.
2. **Cross-jurisdictional reach** — Intended to apply across at least two countries, or formally adopted or referenced by international bodies, or forms the basis of national legislation in multiple jurisdictions.
3. **Referenceability** — Has a stable, citable identifier (standard number, convention number, resolution number, treaty name) and a verifiable primary source URL.

### 4.2 Explicitly included categories

| Category | Examples |
|---|---|
| ISO standards | All 25,703+ published across 250+ TCs |
| IEC standards | All 12,000+ electrotechnical standards |
| ITU Recommendations | ITU-T, ITU-R, ITU-D — thousands of documents |
| UN treaties and conventions | 560+ multilateral treaties |
| ILO Conventions and Recommendations | 190 Conventions, 206 Recommendations |
| WHO guidelines, frameworks, classifications | ICD-11, ICF, IHR 2005, EML, 100+ guidelines |
| UN specialised agency standards | ICAO SARPs, IMO Conventions, IAEA Safety Standards, Codex, WIPO, WMO, UNESCO |
| Financial stability standards | Basel accords, IOSCO, FATF, IFRS, ISSB, ISAs |
| Human rights instruments | UDHR, ICCPR, ICESCR, CRC, CEDAW, CRPD, CAT, all Optional Protocols |
| Humanitarian standards | Sphere, CHS, INEE, IASC guidelines, UNHCR policies |
| Environmental treaties | Paris Agreement, CBD, UNFCCC, UNCLOS, CITES, Montreal Protocol |
| Regional standards | CEN/CENELEC/ETSI, ARSO, ASEAN, AIDMO, SARSO, MERCOSUR |
| National standards bodies | All 175 ISO member NSBs and their nationally-originated standards |
| Industry and professional standards | IEEE, IETF RFCs, W3C, ASTM, ASME, NFPA, SAE, GRI, SASB |
| Development and aid standards | IATI, OECD DAC, World Bank ESF, UN Evaluation Norms |
| Sports governance | WADA Code, IOC Charter, FIFA, World Athletics |
| Cultural heritage | UNESCO World Heritage, ICOMOS Charters, ICOM Code |
| Space and defence (declassified) | CCSDS, ECSS, NATO public documents, UN ATT, Ottawa Treaty |

### 4.3 Explicitly out of scope

- Proprietary company-specific standards not adopted as industry or national standards
- Draft standards not yet formally adopted (noted as "Under Development" only)
- Purely local or municipal standards with no cross-jurisdictional reference
- Classified military technical specifications where the full text is not publicly available
- Academic citation style guides (APA, MLA, Chicago) — these are not formal standards

---

## 5. Guiding Principles

| # | Principle | What it means in practice |
|---|---|---|
| 1 | Free forever | No paywall. No credit card. No registration. No subscription. Ever. |
| 2 | Completeness over perfection | Include everything with a credible claim to global standing, then verify iteratively. An incomplete entry is better than no entry. |
| 3 | Source truth over opinion | Every entry cites its primary authoritative source. ZARISH describes standards; it does not evaluate them. |
| 4 | Open by default | CC BY 4.0. All data on GitHub. All formats available for download. |
| 5 | Machine-readable first | CSV, JSON, JSONL, Parquet are primary outputs. Excel and web portal are derived views. |
| 6 | Community maintained | No single point of failure. Anyone can contribute via GitHub pull request. |
| 7 | Layer neutral | International, regional, and national standards are equally valid. No governance level is privileged. |
| 8 | Politically neutral | ZARISH describes what a standard says and who issued it. No positions on contested standards, disputed territories, or political classifications. |
| 9 | Continuously updated | Automated monthly checks and community corrections keep the index current. |
| 10 | Domain agnostic | No domain is too obscure or too niche. Sports, arts, space, esoteric trade — all are in scope. |

---

## 6. Relationship to ZarishSphere

ZARISH-INDEX is an **autonomous upstream data project**. It is not a sub-module of ZarishSphere.

The relationship is one-directional: ZARISH-INDEX produces structured standards metadata → ZarishSphere G2A Engine consumes it to auto-generate deployable digital workflows.

Key separation rules:

| Rule | Reason |
|---|---|
| ZARISH-INDEX changes do not require ZarishSphere approval | ZARISH-INDEX serves 40+ domains globally, not just ZarishSphere |
| ZarishSphere changes do not affect ZARISH-INDEX content | ZarishSphere is a consumer, not a contributor, of standards metadata |
| ZARISH-INDEX uses CC BY 4.0 | ZarishSphere uses Apache 2.0 for code — no license conflict |
| ZARISH-INDEX can be used by any project | It is not ZarishSphere property |
| ZarishSphere can use any data source | ZARISH-INDEX is the preferred source, not the only one |

Full integration architecture is documented in `006-zarish-index-integration.md`.

---

## 7. Project Identity

| Field | Value |
|---|---|
| Project codename | ZARISH-INDEX |
| Full name | Unified Index of All Global Standards |
| Tagline | Standards are the architecture of trust. ZARISH-INDEX is the map of that architecture. |
| GitHub org | `zarish-standards` |
| Repository | `zarish-standards/zarish-index` |
| Live site | `zarish-standards.github.io/zarish-index` |
| License | CC BY 4.0 |
| Target entry count (v1.0) | 5,000+ fully verified entries |
| Target entry count (v3.0) | 50,000+ entries |
| Primary output formats | CSV, JSON, JSONL, Parquet |
| Build system | Python + Makefile + GitHub Actions |
| Hosting | GitHub (free) + GitHub Pages (free) |

---

## 8. Governance and Ownership

| Role | Person | Commitment |
|---|---|---|
| Lead Curator | Mohammad Ariful Islam | Overall direction, final PR review, annual releases, partner outreach |
| Technical Maintainer | Volunteer | GitHub Actions, website, pipeline scripts |
| Domain Researchers | Volunteers (per domain) | Initial population and ongoing maintenance |
| Community Manager | Volunteer | Issue triage, contributor onboarding |
| External Reviewers | Subject matter experts | Quarterly domain accuracy audits |

All decisions are documented as GitHub commits. Governance disputes are resolved by the Lead Curator.

---

## 9. License

All data in ZARISH-INDEX is published under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

You are free to share, copy, redistribute, adapt, and build upon this data for any purpose, including commercial use, provided you give appropriate credit: *"ZARISH-INDEX, ZarishSphere Foundation, CC BY 4.0, github.com/zarish-standards/zarish-index"*.

---

*GitHub: https://github.com/zarish-standards/zarish-index*

---


*ZarishSphere Foundation · V1 · June 11, 2026*
*License: Apache 2.0 (code) · CC BY 4.0 (documentation)*
*GitHub: https://github.com/zarishsphere*
