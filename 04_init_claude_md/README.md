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
- Generate plots or tables when the result is easier to audit visually.

Compare your result to the repository root `CLAUDE.md`.

## Why Memory Matters

Without project memory, every prompt has to restate the same domain constraints. In reservoir engineering that repetition is where mistakes creep in: one prompt says psia, the next says bara, and a later calculation quietly mixes both.

Good `CLAUDE.md` guidance should make these defaults explicit:

- field vs metric unit conventions
- preferred libraries for standard correlations
- when a result is screening-level only
- required verification commands
- expected output style for tables and figures
- rules for handling missing data, impossible values, and correlation limits

## Illustrated Standard

Use the root workflow figure as the standard quality loop for later exercises.

![Claude reservoir workflow](../assets/claude_reservoir_workflow.png)

The useful memory entry is not "be careful." A better entry is:

```text
For engineering calculations, report inputs, units, method, output units, assumptions, and at least one sanity check. Prefer generated plots for trends, sensitivities, and forecast comparisons.
```
