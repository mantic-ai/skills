"""Check that the marketplaces and the plugins they list agree.

Run from the repository root: python3 scripts/check-plugins.py
"""

import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent.parent
problems = []


def load(path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        problems.append(f"{path.relative_to(root)}: {error}")
        return None


claude_market = load(root / ".claude-plugin/marketplace.json") or {}
codex_market = load(root / ".agents/plugins/marketplace.json") or {}

# Each marketplace lists plugins by source path, and each plugin it lists
# needs that host's manifest, under the same name.
hosts = [
    (".claude-plugin/plugin.json", {p["name"]: p["source"] for p in claude_market.get("plugins", [])}),
    (".codex-plugin/plugin.json", {p["name"]: p["source"]["path"] for p in codex_market.get("plugins", [])}),
]
plugins = {}
for manifest_path, listed in hosts:
    for name, source in listed.items():
        plugin = root / source
        plugins[name] = plugin
        if not plugin.is_dir():
            problems.append(f"{name}: {source} does not exist")
            continue
        manifest = load(plugin / manifest_path)
        if manifest is not None and manifest.get("name") != name:
            problems.append(f"{name}: {manifest_path} names it {manifest.get('name')!r}")
        # Files the manifest points at, such as the Codex logo and MCP config.
        if manifest is not None:
            refs = [manifest.get("skills"), manifest.get("mcpServers")]
            refs += [manifest.get("interface", {}).get(key) for key in ("composerIcon", "logo")]
            for ref in refs:
                if isinstance(ref, str) and not (plugin / ref).exists():
                    problems.append(f"{name}: {manifest_path} points at missing {ref}")

for name, plugin in plugins.items():
    for skill in sorted(p for p in (plugin / "skills").glob("*") if p.is_dir()):
        if not (skill / "SKILL.md").is_file():
            problems.append(f"{name}: {skill.relative_to(root)} has no SKILL.md")
    if (plugin / ".mcp.json").exists():
        load(plugin / ".mcp.json")

for problem in problems:
    print(f"ERROR: {problem}", file=sys.stderr)
if problems:
    sys.exit(1)
print(f"OK: {', '.join(sorted(plugins))}")
