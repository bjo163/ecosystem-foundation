# Ecosystem Foundation Contract

Version: `0.2`
Status: `normative-baseline`

## Purpose

Define stable boundaries for organizing software work across languages, frameworks, package managers, and hosting platforms.

## Canonical hierarchy

```text
ECOSYSTEM > ORGANIZATION > DOMAIN > PROJECT > REPOSITORY > SOURCE > UNIT > MODULE > COMPONENT > ELEMENT > IMPLEMENTATION
```

`DOMAIN` is optional. `UNIT` through `IMPLEMENTATION` provide universal semantic vocabulary for the internal implementation hierarchy. They do not prescribe directory names or language constructs.

## Mandatory principles

- Organization governance must not be hidden inside an individual application's source tree.
- Repository manifests belong to the repository root by default.
- Repository conventions must remain language-agnostic at the semantic level.
- Native ecosystem conventions may be preserved by a language profile.
- Generated artifacts are not source by default.
- A directory must have one clear responsibility.
- Do not create duplicate directories with overlapping responsibility.
- Profiles must prefer the smallest structure that communicates responsibility.
- Universal hierarchy terms MUST NOT be turned into mandatory physical directory names.

## Canonical vocabulary

```text
source
unit
module
component
element
implementation
tests
examples
fixtures
tools
scripts
configuration
data
documentation
specifications
infrastructure
deployment
assets
```

These are canonical **concepts**. A concrete repository does not need every concept as a physical directory and may use native equivalents.

## Internal implementation semantics

### Source
The implementation area of a repository.

### Unit
A logical native implementation container inside Source. A Unit may correspond to a crate, package, application, library, service, command, or similar construct.

### Module
A logical grouping of related implementation within a Unit.

### Component
A cohesive implementation part with a defined responsibility.

### Element
A smaller meaningful implementation construct inside a Component, such as a function, method, type, interface, handler, or constant.

### Implementation
The concrete logic or behavior that realizes an Element or Component.

## Native aliases

The following remain valid when required by a language or framework:

```text
src
apps
packages
crates
libs
cmd
pkg
internal
modules
components
docs
config
deploy
infra
```

Native terms such as `crate`, `package`, `app`, `library`, `service`, `class`, `struct`, `function`, and `method` are not additional universal hierarchy levels. They are mapped to the universal concepts by the relevant language/framework profile.

For example:

```text
UNIT
├── Rust      → crate
├── Node      → package / application / library
├── Go        → package / command / service
├── Python    → package / module
└── Java      → module / package / application
```

A repository should not keep both canonical and alias directories for the same responsibility without an explicit reason.

## Manifest rule

Project/package/build/workspace manifests are repository-root metadata unless the native ecosystem requires another location.

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

Monorepos may additionally contain child manifests in their workspace members.

## Change control

Changes to hierarchy, canonical vocabulary, or profile semantics require a standards/architecture decision and an update to the machine-readable contract before templates are changed.
