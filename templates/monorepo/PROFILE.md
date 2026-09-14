# Monorepo Profile

Use when one repository intentionally contains multiple related applications, components, libraries, or packages.

## Minimum

```text
<repository>/
├── <workspace/root manifest>
├── source/
├── tests/
├── tools/
├── scripts/
├── configuration/       # when shared configuration exists
├── documentation/
├── specifications/      # when contracts are shared
├── deployment/          # when centrally managed
├── infrastructure/      # when centrally managed
├── README.md
└── LICENSE
```

## Rules

- Keep the root manifest responsible for workspace/package orchestration.
- Child manifests may live beside their native source boundaries.
- Avoid inventing an additional abstraction level when the package manager already supplies one.
- Shared code belongs in an explicit component/library boundary, not in an unowned miscellaneous folder.
