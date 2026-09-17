# um-bruch/.github

<!-- public-index-last-checked: 2026-09-17 -->

Dieses Repository pflegt die öffentliche GitHub-Startseite für [Um:bruch](https://github.com/um-bruch), den unabhängigen Think Tank und das Entwicklungslabor für Gesundheitsversorgung, Verordnungstransparenz, Civic Tech, offene Analysen und gemeinwohlorientierte Software.

## Öffentliche Profilflächen

| Pfad | Zweck |
|---|---|
| [`profile/README.md`](profile/README.md) | Sichtbares Organisationsprofil auf `github.com/um-bruch` (Internationale Fassung) |
| [`profile/README_de.md`](profile/README_de.md) | Sichtbares Organisationsprofil auf `github.com/um-bruch` (Deutsche Fassung) |
| [`profile/assets/um-bruch-banner.svg`](profile/assets/um-bruch-banner.svg) | Vektor-Header-Banner für das Organisationsprofil |
| [`llms.txt`](llms.txt) | Maschinenlesbarer Kurzkontext für Crawler, LLMs und Suchsysteme |
| [`CHANGELOG.md`](CHANGELOG.md) | Versionshistorie und Pflegeprotokoll des Profils |
| [`SECURITY.md`](SECURITY.md) | Organisationsweite Sicherheitsrichtlinie |
| [`tests/test_profile_parity.py`](tests/test_profile_parity.py) | Paritäts-, Datums- und Invarianten-Tests |
| `README.md` | Wartungsnotiz und öffentlicher Repo-Index dieses Profilrepos |

## Public Repository Directory

Geprüft am **2026-09-17** gegen die Live-Organisation `um-bruch`. Öffentlich, aktiv und nicht geforkt sind 6 Repositories:

| Repository | Branch | Letzter Push | Rolle & Abdeckung |
|---|---:|---:|---|
| [`.github`](https://github.com/um-bruch/.github) | `main` | 2026-09-10 | Organisationsprofil, Community-Kontext, `llms.txt`, Testsuite und Startseite |
| [`locuterra`](https://github.com/um-bruch/locuterra) | `master` | 2026-08-25 | Civic-Tech-Konzept und Next.js-Demonstrator für ortsbezogene Gemeinwohlkommunikation & PWA |
| [`system-medicine`](https://github.com/um-bruch/system-medicine) | `main` | 2026-08-21 | Forschungsprototyp für funktionale medizinische Wissensgraphen, Differentialdiagnostik & Seltene Erkrankungen |
| [`verordnungsampel`](https://github.com/um-bruch/verordnungsampel) | `main` | 2026-09-13 | Research-use Softwareentwurf für lokale ICD-10-GM-/ATC-Prüfungen gegen deutsche Verordnungsregelwerke |
| [`multiaxial-diagnostic-system`](https://github.com/um-bruch/multiaxial-diagnostic-system) | `master` | 2026-08-05 | 6-Achsen-Dokumentationsprototyp mit DSM-5-TR, ICD-11, ICF, Streamlit & Flask-Testcenter |
| [`regressangst`](https://github.com/um-bruch/regressangst) | `master` | 2026-07-27 | Working Paper ST-001 zu Regressangst, Verordnungsregressen, Transparenz & PP-003 Portalkonzept |

## Auffindbarkeit

Diese Startseite ist der öffentliche Einstieg für:

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

## Pflegehinweise

- Neue öffentliche Repositories müssen in `profile/README.md`, `profile/README_de.md`, `llms.txt` und im Public Repository Directory ergänzt werden.
- Private oder interne Repositories werden nicht öffentlich genannt.
- Medizinische und diagnostische Repositories bleiben als Forschungs-, Analyse- oder Konzeptsoftware markiert, nicht als Beratung oder Medizinprodukt.
- Vor Commits muss die Testsuite mit `pytest tests/` und der Mermaid-Linter mit `python _tools/lint_mermaid.py` fehlerfrei durchlaufen.
- Deutsche Endnutzertexte verwenden echte Umlaute.

<!-- public-index-last-checked: 2026-09-17 -->
