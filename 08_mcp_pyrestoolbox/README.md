# Exercise 8: pyResToolbox MCP

**Best practice:** use MCP tools for live reservoir calculations instead of asking Claude to invent formulas.

## Setup Direction

Install and run the pyrestoolbox MCP server from:

```text
https://github.com/gabrielserrao/pyrestoolbox-mcp
```

Then connect it to Claude Desktop or Claude Code according to that repository's instructions.

## Prompt

```text
Use the pyResToolbox MCP tools.
Calculate bubble point pressure for 35 API oil at 180 degF with solution GOR 800 scf/stb and gas gravity 0.75.
Use Valko-McCain if available.
State units, method, inputs, and one sanity check.
```

## Follow-Up Prompt

```text
Now compare Standing, Valko-McCain, and Velarde bubble point estimates for the same fluid.
Return a compact table and explain which result you would carry into a screening model.
```

## Parameter Reminder

- Oil tools use `sg_g`.
- Gas tools use `sg`.
- Some gas property tools use `zmethod`, not `method`.

