# Ecosystem Foundation Contract

Version: `0.1`
Status: `draft-baseline`

## Purpose

Define stable boundaries for organizing software work across languages, frameworks, package managers, and hosting platforms.

## Canonical hierarchy

```text
ECOSYSTEM > ORGANIZATION > DOMAIN > PROJECT > REPOSITORY > SOURCE > MODULE/COMPONENT
```

`DOMAIN` is optional. `MODULE` and `COMPONENT` are implementation concepts, not mandatory repository levels.

## Mandatory principles

- Organization governance must not be hidden inside an individual application's source tree.
- Repository manifests belong to the repository root.
- Repository conventions must remain language-agnostic.
- Native ecosystem conventions may be preserved by a language profile.
- Generated artifacts are not source by default.
- A directory must have one clear ownership/responsibility.
- Do not create duplicate directories with overlapping responsibility.

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

## Non-canonical aliases

The following terms remain valid when required by a language or framework, but are not organization-wide vocabulary:

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
```

## Compatibility rule

A repository does not need to rename native directories solely for vocabulary compliance. The standard governs responsibility and boundaries first; physical names may be mapped by a profile.

## Change control

Changes to the canonical hierarchy or vocabulary require an architecture/standards decision and an update to this contract before templates are changed.
