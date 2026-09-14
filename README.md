# Ecosystem Foundation

A language-agnostic foundation for organizing software ecosystems from ecosystem-level governance down to project repositories and source code.

## Purpose

This repository defines the canonical vocabulary, hierarchy, boundaries, and templates used to create and maintain consistent software repositories across different languages and platforms.

## Hierarchy

```text
ECOSYSTEM
└── ORGANIZATION
    └── DOMAIN
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
source/             source code
 tests/              automated tests
examples/            runnable/documented examples
fixtures/            test/reference data
tools/              developer/internal tools
scripts/            automation
configuration/      configuration
data/               project data
documentation/      explanatory documentation
specifications/     formal contracts and specifications
infrastructure/     infrastructure definitions
deployment/         deployment/release definitions
assets/             non-code resources
```

These are **canonical concepts, not mandatory folders**. A repository only creates the directories it actually needs.

## Language neutrality

The foundation does not replace native language terminology.

- Rust may use Cargo, crates, modules, and `Cargo.toml`.
- JavaScript/TypeScript may use pnpm, npm packages, and `package.json`.
- Go may use modules and packages.
- Python may use packages and modules.
- Java may use Maven/Gradle modules and packages.

Language-specific organization belongs inside the repository's source/build model.

## Design rules

1. Keep organization/governance separate from repository implementation.
2. Keep repository conventions separate from language/framework conventions.
3. Treat manifest files as repository-root metadata.
4. Do not create parallel concepts merely because a language uses a different term.
5. Prefer the smallest structure that clearly communicates responsibility.
6. Do not commit generated build output unless a project explicitly requires it.

## Repository profiles

Profiles will be added under `templates/` for common repository types:

- library
- application
- service
- cli
- monorepo

## Status

Foundation v0.1 — vocabulary and boundaries established. Template profiles and machine-checkable contracts are the next layer.
