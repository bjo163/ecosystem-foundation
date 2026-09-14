# Service Profile

Use for APIs, workers, daemons, background processors, and other long-running services.

## Minimum

```text
<repository>/
├── <manifest>
├── source/
├── tests/
├── configuration/
├── specifications/      # recommended for API/protocol contracts
├── infrastructure/     # when service infrastructure is owned here
├── deployment/         # when deployment is owned here
├── documentation/
├── README.md
└── LICENSE
```

## Rules

- Treat external interfaces as specifications/contracts, not incidental source.
- Keep runtime configuration separate from application logic.
- Infrastructure and deployment may be omitted when owned by another repository.
