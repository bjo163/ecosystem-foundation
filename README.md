# Ecosystem Foundation — Legacy / Superseded

> **Status: LEGACY.** New architecture MUST use [`bjo163/universe-foundation`](https://github.com/bjo163/universe-foundation) as the single normative foundation.

This repository is retained for historical continuity and existing consumers. It is no longer part of the active foundation chain and must not be treated as a required dependency by new repositories, launchers, or workspaces.

## Canonical foundation

The active hierarchy is governed end-to-end by Universe Foundation:

```text
UNIVERSE
└── ECOSYSTEM
    └── ORGANIZATION (optional)
        └── DOMAIN (optional)
            └── PROJECT
                └── REPOSITORY
                    └── SOURCE
                        └── UNIT
                            └── MODULE
                                └── COMPONENT
                                    └── ELEMENT
                                        └── IMPLEMENTATION
```

`UNIT` through `IMPLEMENTATION` remain semantic universal vocabulary; they do not require physical directories. Native structures such as Rust crates, Node packages, Go packages, Python modules, Java packages, `src/`, `apps/`, `packages/`, `crates/`, `cmd/`, and `internal/` remain valid through mappings defined by Universe Foundation.

## Migration rule

Do not introduce new dependencies on this repository. For new work, reference the Universe Foundation contract and tools instead.

Existing files here are preserved as legacy material; they do not override the canonical hierarchy or ownership rules in Universe Foundation.
