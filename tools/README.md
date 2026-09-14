# Repository generator

`repo-init.py` scaffolds a new repository from a Foundation profile without external dependencies.

## Usage

```bash
python tools/repo-init.py library my-library
python tools/repo-init.py application my-app
python tools/repo-init.py service my-service
python tools/repo-init.py cli my-cli
python tools/repo-init.py monorepo my-workspace
```

Use `--path` when the destination should differ from `./<name>`:

```bash
python tools/repo-init.py library my-library --path ../my-library
```

The generator refuses to overwrite an existing destination. It creates only profile-required directories and writes `.ecosystem.json` identifying the Foundation contract/profile used.

This tool scaffolds structure; it does not choose a programming language, package manager, framework, CI provider, or cloud platform.
