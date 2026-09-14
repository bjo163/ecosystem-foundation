# Repository Template Profiles

Templates are derived from the foundation contract. A profile selects the smallest useful structure for a repository type.

## Profiles

### Library

```text
library/
├── <manifest>
├── source/
├── tests/
├── examples/
├── documentation/
└── README.md
```

### Application

```text
application/
├── <manifest>
├── source/
├── tests/
├── configuration/
├── documentation/
├── deployment/
└── README.md
```

### Service

```text
service/
├── <manifest>
├── source/
├── tests/
├── configuration/
├── specifications/
├── infrastructure/
├── deployment/
└── README.md
```

### CLI

```text
cli/
├── <manifest>
├── source/
├── tests/
├── examples/
├── documentation/
└── README.md
```

### Monorepo

```text
monorepo/
├── <workspace/root manifest>
├── source/
├── tests/
├── examples/
├── tools/
├── scripts/
├── configuration/
├── documentation/
├── specifications/
├── infrastructure/
├── deployment/
└── README.md
```

Profiles are intentionally descriptive. They do not require every directory to be present in a concrete repository.
