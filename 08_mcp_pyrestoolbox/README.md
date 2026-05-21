# Exercise 8: pyResToolbox MCP

**Best practice:** use MCP tools for live reservoir calculations instead of asking Claude to invent formulas.

## Setup Direction

Install and run the pyrestoolbox MCP server from:

```text
https://github.com/gabrielserrao/pyrestoolbox-mcp
```

Then connect it to Claude Desktop or Claude Code according to that repository's instructions.

## Engineering Context

This exercise is about tool discipline. Claude can write formulas, but standard reservoir correlations should come from a trusted implementation when one is available. The engineer's job is to specify the inputs, units, method preference, and sanity checks.

Before calling a PVT tool, make Claude restate:

- API gravity and oil specific gravity convention
- reservoir temperature units
- solution GOR units
- gas gravity basis
- selected correlation or fallback method
- output pressure units

The API-to-specific-gravity plot below is a simple example of the type of pre-call sanity check that prevents bad inputs from reaching a correlation.

![PVT input sanity check](../assets/pvt_api_specific_gravity.png)

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

## Better Result Format

Ask Claude to return results like this:

```text
Inputs:
- oil gravity: 35 API
- temperature: 180 degF
- solution GOR: 800 scf/stb
- gas gravity: 0.75 air = 1.0

Method:
- pyResToolbox oil bubble point
- requested correlation: Valko-McCain

Result:
- bubble point pressure: ... psia

Sanity checks:
- bubble point is positive
- result is in the expected screening range for this fluid
- method and parameter names are reported exactly
```

If the MCP call fails, the correct next step is to inspect tool names and parameter names, not to invent a replacement correlation silently.
