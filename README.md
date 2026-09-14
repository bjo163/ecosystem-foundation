# Ecosystem Foundation

A language-agnostic foundation for organizing software ecosystems from ecosystem-level governance down to project repositories and source code.

## Purpose

This repository is the source of truth for ecosystem vocabulary, hierarchy, boundaries, repository profiles, and machine-checkable rules used to keep software projects consistent across languages and platforms.

## Canonical hierarchy

```text
ECOSYSTEM
└── ORGANIZATION
    └── DOMAIN (optional)
        └── PROJECT
            └── REPOSITORY
                ├── MANIFEST / METADATA
                ├── SOURCE
                │   └── MODULE / COMPONENT
                └── SUPPORTING MATERIAL
```

The hierarchy is conceptual. Git hosting may represent organization, domain, project, and repository through different native mechanisms.

## Repository vocabulary

```text
source             source code responsibility
tests              automated verification
examples           runnable/documented examples
fixtures           stable test/reference data
tools              developer/internal software tools
scripts             automation glue
configuration      configuration and templates
data               project-owned/reference data
documentation      human-facing explanation
specifications     formal contracts, schemas, protocols, requirements
infrastructure     infrastructure definitions
deployment         deployment/release definitions
assets              non-code resources
```

These are canonical concepts, not mandatory physical directory names. A concrete repository creates only what it needs.

## Manifest rule

Project, dependency, package, workspace, and build manifests live at repository root by default.

Examples:

```text
Cargo.toml
package.json
pnpm-workspace.yaml
go.mod
pyproject.toml
pom.xml
build.gradle
```

Monorepos may also have child manifests inside workspace members.

## Language neutrality

The foundation governs responsibility and boundaries, not compiler-specific naming. Rust can keep `src/` and `Cargo.toml`; Go can keep `package`/`internal`; TypeScript can keep `packages/`; Python can keep its package/module layout.

## Profiles

Profiles under `templates/` cover:

- library
- application
- service
- cli
- monorepo

Each profile selects the smallest useful structure and preserves native language conventions.

## Validation

The repository includes a dependency-free Python validator:

```bash
python tools/validate-foundation.py
```

CI runs the validator, verifies the machine-readable contract, and checks Python tooling syntax on pushes and pull requests.

## Governance

Changes to the canonical hierarchy, vocabulary, or profile semantics require an architecture/standards decision and an update to the normative contract.

## Version

Foundation contract: `0.2` — normative baseline with machine-readable contract, profiles, validator, regression tests, and CI.
