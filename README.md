# Mantic Skills

[Mantic](https://mantic.com) plugins for [Claude](https://claude.com) and
[Codex](https://openai.com/codex). Mantic is an AI forecasting system that
predicts global events across geopolitics, business, policy, markets,
technology and culture, with explicit reasoning and supporting references,
updated as new information arrives. These plugins bring its forecasts into
your agent.

## Plugins

| Plugin                              | Hosts         | Description                                                    | Capabilities                                         |
| ----------------------------------- | ------------- | -------------------------------------------------------------- | ---------------------------------------------------- |
| [mantic-mcp](plugins/mantic-mcp/)   | Claude, Codex | Explore and request forecasts                                  | Mantic MCP server; `using-mantic` and `forecast-explainer` skills |

## Install in Claude

The marketplace is called `mantic`, so plugins install as
`<plugin>@mantic`.

### Claude Code (CLI)

Add the marketplace, then install the plugin:

```bash
claude plugin marketplace add mantic-ai/skills
claude plugin install mantic-mcp@mantic
```

Inside a Claude Code session, the same steps are
`/plugin marketplace add mantic-ai/skills` and
`/plugin install mantic-mcp@mantic`.

### claude.ai and the Claude Desktop app

Plugins added to your claude.ai account are available in chat on the web,
desktop and mobile apps.

1. Open [Customize → Plugins](https://claude.ai/customize/plugins).
2. Choose **Add → Add marketplace** and enter `mantic-ai/skills`.
3. Select **mantic-mcp** and choose **Add**.

### The Code tab in Claude Desktop

1. In the **Code** tab, choose **+** next to the prompt box, then
   **Plugins → Add plugin**.
2. Choose **Add → Add marketplace** and enter `mantic-ai/skills`.
3. Select **mantic-mcp** and choose **Add**.

### Updating

Third-party marketplaces don't update automatically by default. In Claude
Code, update with:

```bash
claude plugin marketplace update mantic
claude plugin update mantic-mcp@mantic
```

or turn on auto-update from `/plugin` → **Marketplaces** → `mantic`. On
claude.ai, turn on **Sync automatically** for the marketplace under
**Customize → Plugins**.

## Install in Codex

### Codex CLI

Add the marketplace, then add the plugin:

```bash
codex plugin marketplace add mantic-ai/skills
codex plugin add mantic-mcp@mantic
```

You can also add it from the plugin browser: run `/plugins` in a Codex session,
choose the **Mantic** marketplace and install **mantic-mcp**. If Codex doesn't
prompt you to sign in to Mantic, run `codex mcp login mantic`.

Update later with `codex plugin marketplace upgrade mantic`.

### ChatGPT desktop app

The desktop app shares its marketplaces with the Codex CLI.

1. Run `codex plugin marketplace add mantic-ai/skills` in a terminal.
2. Restart the ChatGPT desktop app.
3. Open **Plugins**, choose the **Mantic** marketplace, open **mantic-mcp**
   and install it. Connect your Mantic account when prompted.

### ChatGPT and Codex on the web

Individual accounts can't add custom marketplaces on the web. Instead,
install Mantic from the ChatGPT plugin directory: open **Plugins** in the
sidebar, search for **Mantic** and connect it.

Workspace admins can make this marketplace available to everyone in a
workspace from **Admin → Plugins → Add → Import marketplace**, using
`https://github.com/mantic-ai/skills`.
