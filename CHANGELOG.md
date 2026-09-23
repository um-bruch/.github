# Changelog - um-bruch/.github

All notable changes to the `um-bruch` organization profile and shared community files will be documented in this file.

## [1.1.3] - 2026-09-23

### Live Repository Index Verification
- **Repository Index Refresh:** Re-verified all six public, active, non-forked repositories against the live GitHub API on 2026-09-23.
- **Push Metadata Updated:** Updated `verordnungsampel` and `.github` to their live 2026-09-20 public push dates; all other repository entries remained unchanged.
- **Index Parity:** Synchronized the verification date across the root README, both profile READMEs, `llms.txt`, and the parity tests without changing the curated Um:bruch logo assets.

## [1.1.2] - 2026-09-20

### Brand Correction
- **Reverted auto-generated header banner:** The generic SVG header banner introduced in 1.1.0 (`profile/assets/um-bruch-banner.svg`, teal/network-node motif) did not match Um:bruch's actual, human-curated design assets and has been removed.
- **Restored curated logo:** Replaced it with `profile/assets/um-bruch-logo.png`, the existing Um:bruch letterhead logo, in both profile READMEs and the root README index.
- **Test suite updated:** `tests/test_profile_parity.py` now checks for the PNG logo instead of validating the removed SVG.
- **Root cause:** Automated profile-health run `GITHUBBOT_ORGA_README_MD_STARTSEITE_HEALTH` (2026-09-10) designed a new banner from scratch instead of reusing curated assets; see `profile/DESIGN-ASSETS.md`.

## [1.1.1] - 2026-09-17

### Live Repository Index Verification
- **Repository Index Refresh:** Re-verified the six public, active, non-forked repositories against `gh api orgs/um-bruch/repos --paginate` on 2026-09-17.
- **Push Metadata Updated:** Updated `verordnungsampel` from 2026-08-20 to its live `pushed_at` date 2026-09-13; all other documented push dates were unchanged.
- **Index Parity:** Synchronized the verification date across the root README, both profile READMEs, and `llms.txt` without changing repository descriptions or adding a parallel register.

## [1.1.0] - 2026-09-10

### Maintenance, Discoverability, Visual Identity & Parity Sync
- **Repository Index Refresh:** Re-verified complete public repository catalog for `um-bruch` via GitHub API on 2026-09-10. All 6 public repositories (`.github`, `locuterra`, `system-medicine`, `verordnungsampel`, `multiaxial-diagnostic-system`, `regressangst`) are 100% accounted for and mapped; no unlisted or private repos exist.
- **Push Metadata Updated:** Updated latest public push timestamps across all indexes: `locuterra` (`2026-08-25`), `system-medicine` (`2026-08-21`), `verordnungsampel` (`2026-08-20`), `multiaxial-diagnostic-system` (`2026-08-05`), `regressangst` (`2026-07-27`), and `.github` (`2026-09-10`).
- **Brand & Visual Header:** Designed and integrated modern widescreen SVG header banner `profile/assets/um-bruch-banner.svg` with teal/emerald/cyan palette, network nodes, and caduceus prescription cross motif.
- **Tool Showcase:** Added visual showcase featuring `verordnungsampel` official SVG banner and `locuterra` civic social network demonstrator preview.
- **Ecosystem Cross-Linking Parity:** Synchronized sister organization tables across English/German profile READMEs and `llms.txt` to include all 10 organizations (`open-bricks`, `ellmos-ai`, `file-bricks`, `doc-bricks`, `dev-bricks`, `research-line`, `biotec-line`, `assistassets-ai`, `entertain-and-more`, `um-bruch`) plus developer portal `lukisch`.
- **Mermaid Syntax Hardening:** Quoted node and edge labels containing slashes, brackets, and colons strictly per `HOOK-BANNER-ASSET-01` and validated with `lint_mermaid.py` (0 issues).
- **Shared Community Standards:** Added `CODE_OF_CONDUCT.md` (Contributor Covenant v2.1), `CONTRIBUTING.md`, `SECURITY.md`, `FUNDING.yml`, `ISSUE_TEMPLATE/` (`bug_report.md`, `feature_request.md`), `PULL_REQUEST_TEMPLATE.md`, and GitHub Actions workflows (`stale.yml`, `welcome.yml`).
- **Automated Profile Parity Testing:** Created comprehensive test suite `tests/test_profile_parity.py` asserting UTF-8 validity, code fence balance, repository mapping, timestamp synchronicity (2026-09-10), push date verification, ecosystem cross-linking, research-use disclaimer, banner XML validity, and no forbidden local path leaks.
- **Last-Checked Timestamps:** Synchronized `<!-- last-checked: 2026-09-10 -->` across `profile/README.md`, `profile/README_de.md`, root `README.md`, and `llms.txt`.

## [1.0.0] - 2026-08-22

### Initial Organization Profile Index
- Initial public organization profile, repository directory, English/German profile READMEs, and llms.txt crawler index for `um-bruch`.
