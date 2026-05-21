# Exercise 4: Initialize Project Memory

**Best practice:** put recurring project context in `CLAUDE.md` so every Claude Code session starts with the same engineering rules.

## Prompt

```text
/init
```

After Claude creates or updates `CLAUDE.md`, refine it with reservoir engineering rules:

- Always state units and correlation methods.
- Prefer pyResToolbox or pyrestoolbox-mcp tools for PVT, gas, brine, DCA, matbal, nodal, layer, simtools, and sensitivity work.
- Check parameter names before calling MCP tools.
- Verify calculations with tests, known values, monotonicity checks, or sensitivity cases.

Compare your result to the repository root `CLAUDE.md`.

