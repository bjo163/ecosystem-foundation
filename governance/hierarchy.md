# Ecosystem Hierarchy

## Canonical model

```text
ECOSYSTEM
└── ORGANIZATION
    └── DOMAIN
        └── PROJECT
            └── REPOSITORY
                └── SOURCE
                    └── UNIT
                        └── MODULE
                            └── COMPONENT
                                └── ELEMENT
                                    └── IMPLEMENTATION
```

`DOMAIN` is optional. The lower structure is language-agnostic at the semantic level while allowing native repository conventions.

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

### Source
The implementation area of a repository. The universal concept is `SOURCE`; a language profile may map it to native layouts such as Rust `src/`, a Node `apps/` tree, or another native structure.

### Unit
A logical native implementation container recognized inside Source. Examples include a Rust crate, Node package/application/library, Go package/command/service, Python package, or Java module/package/application.

`UNIT` is semantic vocabulary, not a required directory name. A repository MUST NOT create a `unit/` directory solely for conformance.

### Module
A logical grouping of related implementation inside a Unit. Native module systems may use different names or structures.

### Component
A cohesive implementation part with a defined responsibility. The concrete representation is language/framework dependent.

### Element
A smaller meaningful implementation construct inside a Component, such as a function, method, type, interface, handler, or constant.

### Implementation
The concrete logic or behavior that realizes an Element or Component.

### Manifest / Metadata
Root-level files describing the repository, dependencies, build system, package manager, workspace, or project metadata. Examples include `Cargo.toml`, `package.json`, `go.mod`, `pyproject.toml`, `pom.xml`, and `build.gradle`.

## Native mapping

Native terminology remains valid inside a repository. Canonical tools normalize native concepts to the universal terms:

```text
UNIT
├── Rust      → crate
├── Node      → package / application / library
├── Go        → package / command / service
├── Python    → package / module
└── Java      → module / package / application
```

Native directory names such as `src`, `apps`, `packages`, `crates`, `libs`, `cmd`, `pkg`, `internal`, `modules`, and `components` are implementation mappings, not additional universal hierarchy levels.

A repository may keep its native structure. Conformance does not require renaming or wrapping native directories with universal names.

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
assets
```

Do not force these dimensions into every repository.
