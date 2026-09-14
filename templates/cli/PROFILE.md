# CLI Profile

Use for command-line applications and developer-facing executables.

## Minimum

```text
<repository>/
├── <manifest>
├── source/
├── tests/
├── examples/            # recommended for command usage
├── documentation/
├── README.md
└── LICENSE
```

## Rules

- Keep command parsing, application flow, and reusable logic clearly separated by responsibility.
- Provide executable examples for important commands where practical.
- Preserve native CLI conventions of the selected language.
