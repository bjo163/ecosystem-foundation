# Ecosystem Hierarchy

## Canonical model

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

## Definitions

### Ecosystem
The broadest software or technology environment whose organizations, domains, projects, repositories, standards, and shared resources are intentionally related.

### Organization
The ownership and governance boundary. It may correspond to a GitHub organization, company, foundation, team grouping, or another administrative unit.

### Domain
A business, technical, research, or product area. Domain is optional and must not be invented solely to add hierarchy.

### Project
A product, system, initiative, or bounded engineering effort.

### Repository
A version-controlled implementation unit. A project may consist of one repository or multiple repositories.

### Manifest / Metadata
Root-level files describing the repository, dependencies, build system, package manager, workspace, or project metadata. Examples include `Cargo.toml`, `package.json`, `go.mod`, `pyproject.toml`, `pom.xml`, and `build.gradle`.

### Source
The implementation area of a repository. The canonical vocabulary uses `source/` as the cross-language concept; a language profile may map this to its native layout such as Rust `src/`.

### Module / Component
Internal implementation concepts. These are not mandatory repository-level directories because their organization is architecture- and language-dependent.

## Supporting dimensions

The following are horizontal concerns rather than hierarchy levels:

```text
governance
standards
specifications
architecture
decisions
documentation
templates
infrastructure
deployment
```

Do not force these dimensions into every repository.
