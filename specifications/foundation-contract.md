# Ecosystem Foundation Contract

Version: `0.2`
Status: `normative-baseline`

## Purpose

Define stable boundaries for organizing software work across languages, frameworks, package managers, and hosting platforms.

## Canonical hierarchy

```text
ECOSYSTEM > ORGANIZATION > DOMAIN > PROJECT > REPOSITORY > SOURCE > MODULE/COMPONENT
```

`DOMAIN` is optional. `MODULE` and `COMPONENT` are implementation concepts, not mandatory repository levels.

## Mandatory principles

- Organization governance must not be hidden inside an individual application's source tree.
- Repository manifests belong to the repository root by default.
- Repository conventions must remain language-agnostic.
- Native ecosystem conventions may be preserved by a language profile.
- Generated artifacts are not source by default.
- A directory must have one clear responsibility.
- Do not create duplicate directories with overlapping responsibility.
- Profiles must prefer the smallest structure that communicates responsibility.

## Canonical vocabulary

```text
source
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

These are canonical **concepts**. A concrete repository does not need every directory and may use a native equivalent.

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

Aliases are mappings, not additional responsibilities. A repository should not keep both canonical and alias directories for the same responsibility without an explicit reason.

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
