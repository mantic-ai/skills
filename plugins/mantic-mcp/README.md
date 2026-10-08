# Mantic MCP plugin

[Mantic](https://mantic.com) is an AI forecasting system that predicts global
events — geopolitics, business, policy, markets, technology and culture — with
explicit reasoning and supporting references, updated as new information
arrives.

This plugin bundles the **Mantic MCP server** (`https://api.mantic.com/mcp`)
for interactive lookups: search questions, view a question, read forecasts
and render CDF charts. Your agent authenticates with it on first use; there is
nothing to configure.

It also includes two skills:

- `using-mantic` sets out how Claude presents Mantic forecasts: always with
  their date and link, and with Mantic's view kept separate from Claude's own.
- `forecast-explainer` explains a single forecast: what Mantic predicts, why,
  how the forecast has moved, and which scenarios would change it.

## Install

The plugin is published in the [mantic-ai/skills](https://github.com/mantic-ai/skills)
marketplace, whose README has install steps for Claude Code, Claude Desktop,
claude.ai and Codex. In Claude Code:

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
