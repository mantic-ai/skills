# Contributing

## This repository is a read-only mirror

The plugins under `plugins/` are published here automatically from Mantic's
own source. A sync runs after each Mantic release, overwrites each plugin
directory to match the source, and commits only when something changed.

**Anything committed directly inside `plugins/<plugin>/` is wiped by the next
sync.** Please open an issue rather than a pull request for changes to a
plugin's skills, manifests or MCP configuration, and we will make the change at
the source.

The repository-level files are maintained here and can be edited directly:

- `README.md`, `CONTRIBUTING.md` and `.gitignore`
- `.claude-plugin/marketplace.json`, the Claude Code marketplace
- `.agents/plugins/marketplace.json`, the Codex marketplace
- `.github/` and `scripts/`

## Checks

CI runs `scripts/check-plugins.py`, which checks that both marketplaces parse,
that every plugin they list exists with a manifest of the same name, and that
every skill has a `SKILL.md`. Run it locally from the repository root:

```bash
python3 scripts/check-plugins.py
```

## Testing a plugin locally

Load a plugin straight from a checkout in Claude Code:

```bash
claude --plugin-dir ./plugins/mantic-mcp
```

Or add the checkout as a marketplace, which tests the marketplace files as well:

```bash
claude plugin marketplace add ./
claude plugin install mantic-mcp@mantic
```
