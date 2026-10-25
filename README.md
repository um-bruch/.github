# um-bruch/.github

<!-- public-index-last-checked: 2026-10-20 -->

[English documentation](README.md) | [Deutsche Dokumentation](README_de.md)

This repository maintains the public GitHub landing page for [Um:bruch](https://github.com/um-bruch), the independent think tank and development lab for health care, prescribing transparency, civic tech, open analysis, and public-interest software.

## Public Profile Surfaces

| Path | Purpose |
|---|---|
| [`profile/README.md`](profile/README.md) | Public organization profile on `github.com/um-bruch` (English version) |
| [`profile/README_de.md`](profile/README_de.md) | Public organization profile on `github.com/um-bruch` (German version) |
| [`profile/assets/um-bruch-logo.png`](profile/assets/um-bruch-logo.png) | Curated Um:bruch logo for the organization profile |
| [`llms.txt`](llms.txt) | Machine-readable context for crawlers, LLMs, and search systems |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history and profile maintenance log |
| [`SECURITY.md`](SECURITY.md) | Organization-wide security policy |
| [`tests/test_profile_parity.py`](tests/test_profile_parity.py) | Parity, date, and invariant tests |
| [`README.md`](README.md) | Maintenance note and public repository index for this profile repository |
| [`README_de.md`](README_de.md) | German version of this maintenance note and public repository index |

## Public Repository Directory

Checked on **2026-10-20** against the live `um-bruch` organization. There are 6 public, active, non-forked repositories:

| Repository | Branch | Last push | Role and coverage |
|---|---:|---:|---|
| [`.github`](https://github.com/um-bruch/.github) | `main` | 2026-10-20 | Organization profile, community context, `llms.txt`, test suite, and landing page |
| [`locuterra`](https://github.com/um-bruch/locuterra) | `master` | 2026-08-25 | Civic-tech concept and Next.js demonstrator for location-based public-interest communication and PWA |
| [`system-medicine`](https://github.com/um-bruch/system-medicine) | `main` | 2026-08-21 | Research prototype for functional medical knowledge graphs, differential diagnosis, and rare diseases |
| [`verordnungsampel`](https://github.com/um-bruch/verordnungsampel) | `main` | 2026-09-20 | Research-use software draft for local ICD-10-GM / ATC checks against German prescribing rule sets |
| [`multiaxial-diagnostic-system`](https://github.com/um-bruch/multiaxial-diagnostic-system) | `master` | 2026-08-05 | Six-axis documentation prototype with DSM-5-TR, ICD-11, ICF, Streamlit, and Flask Testcenter |
| [`regressangst`](https://github.com/um-bruch/regressangst) | `master` | 2026-07-27 | Working Paper ST-001 on recourse anxiety, prescribing recoupments, transparency, and the PP-003 portal concept |

## Discoverability

This landing page is the public entry point for:

- `Um:bruch Think Tank GitHub`
- `Um:bruch health policy research software`
- `VerordnungsAmpel ICD-10 ATC AM-RL PRISCUS`
- `Regressangst prescribing audit recourse anxiety`
- `functional pathway medical knowledge graph rare disease`
- `rare disease differential diagnosis knowledge graph`
- `German healthcare research software local-first`
- `multiaxial diagnostic system DSM-5-TR ICD-11 ICF`
- `German prescribing transparency research`
- `public-interest location based civic tech Next.js`
- `LOCUTERRA municipal digital commons PWA`

## Maintenance Notes

- Add new public repositories to `profile/README.md`, `profile/README_de.md`, `llms.txt`, and the Public Repository Directory.
- Do not name private or internal repositories publicly.
- Keep medical and diagnostic repositories labelled as research, analysis, or concept software, not as advice or medical devices.
- Before committing, run `pytest tests/` and require it to pass. Preview Mermaid diagrams on GitHub after content changes.
- German end-user text must use actual umlauts.

<!-- public-index-last-checked: 2026-10-20 -->
