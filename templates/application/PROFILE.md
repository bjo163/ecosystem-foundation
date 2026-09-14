# Application Profile

Use for end-user applications, desktop applications, web applications, or executable products.

## Minimum

```text
<repository>/
├── <manifest>
├── source/
├── tests/
├── configuration/       # when runtime/config templates are needed
├── deployment/          # when distribution/deployment is part of the repo
├── documentation/
├── README.md
└── LICENSE
```

## Rules

- Keep entrypoints and production implementation under the source responsibility.
- Keep environment/configuration concerns separate from source code where practical.
- Preserve framework-native layouts when they provide stronger tooling support.
