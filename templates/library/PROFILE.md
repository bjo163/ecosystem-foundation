# Library Profile

Use for reusable libraries, SDKs, frameworks, and packages.

## Minimum

```text
<repository>/
├── <manifest>
├── source/              # or the language-native equivalent
├── tests/
├── examples/            # recommended when public API needs demonstration
├── documentation/       # recommended for non-trivial libraries
├── README.md
└── LICENSE
```

## Rules

- Keep public API and implementation boundaries explicit.
- Do not invent `apps/`, `services/`, or `packages/` just to satisfy the profile.
- A language-native layout such as Rust `src/` is valid.
- The profile describes responsibility, not literal directory names.
