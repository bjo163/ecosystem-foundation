# Canonical Repository Structure

The repository standard is intentionally language-agnostic.

## Core structure

```text
project/
├── <manifest and metadata files>
├── source/
├── tests/
├── examples/
├── fixtures/
├── tools/
├── scripts/
├── configuration/
├── data/
├── documentation/
├── specifications/
├── infrastructure/
├── deployment/
├── assets/
├── README.md
├── LICENSE
└── .gitignore
```

Only needed directories should exist. Empty-directory scaffolding is discouraged.

## Root manifest rule

Language/package/build manifests live at repository root unless the ecosystem natively requires another location.

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

A monorepo may additionally contain child manifests inside its workspace members.

## Directory boundaries

| Directory | Responsibility |
|---|---|
| `source/` | Production source and implementation | 
| `tests/` | Automated verification | 
| `examples/` | Usage examples that may be executed or built | 
| `fixtures/` | Stable data used by tests/examples | 
| `tools/` | Developer or internal software tools | 
| `scripts/` | Automation glue and repeatable commands | 
| `configuration/` | Non-secret configuration and configuration templates | 
| `data/` | Project-owned runtime/reference data where appropriate | 
| `documentation/` | Human-facing explanation and guides | 
| `specifications/` | Formal contracts, schemas, protocols, and requirements | 
| `infrastructure/` | Infrastructure definitions | 
| `deployment/` | Deployment and release definitions | 
| `assets/` | Static/non-code resources | 

## Native language layouts

A profile may preserve native ecosystem conventions. The canonical vocabulary describes responsibility rather than requiring literal directory names.

Example: a Rust repository may keep `src/` because Cargo expects it naturally; the conceptual role remains `source/`.
