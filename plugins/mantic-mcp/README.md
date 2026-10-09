# Mantic MCP plugin

[Mantic](https://mantic.com) is an AI forecasting system. This plugin bundles
the Mantic MCP server (`https://api.mantic.com/mcp`) to search questions, view
forecasts and render CDF charts, plus two skills:

- `using-mantic` presents forecasts with their date and link, keeping Mantic's
  view separate from the agent's own.
- `forecast-explainer` explains what Mantic predicts, why, how the forecast has
  moved, and what would change it.

## Install

See the [mantic-ai/skills README](https://github.com/mantic-ai/skills) for
every app. In Claude Code:

```
claude plugin marketplace add mantic-ai/skills
claude plugin install mantic-mcp@mantic
```

## Layout

```
mantic-mcp/
├── .claude-plugin/plugin.json     Claude manifest
├── .codex-plugin/plugin.json      Codex manifest, with the marketplace listing
├── .mcp.json                      the Mantic MCP server, shared by both
├── assets/mantic-icon.svg         plugin logo
└── skills/
    ├── using-mantic/SKILL.md      presentation rules for any Mantic tool call
    └── forecast-explainer/SKILL.md
```
