# Hermes Project Context — Reservoir Engineering

This repository teaches Hermes Agent workflows for reservoir engineering. Treat every calculation as an engineering artifact: preserve units, cite assumptions, avoid silent correlation changes, and verify against tests or known checks.

## Project Layout

- Numbered exercise folders are self-contained lessons.
- `.hermes/skills/reservoir-engineering/` contains pyResToolbox and MCP usage guidance.
- `AGENTS.md` defines a reviewer subagent for calculation quality.
- `references/` contains compact workflow notes copied into prompts when needed.

## Engineering Rules

- Always state field vs metric units.
- Prefer pyResToolbox or pyrestoolbox-mcp for PVT, gas, oil, brine, DCA, matbal, nodal, layer, simtools, and sensitivity calculations.
- Do not mix psia/barsa, degF/degC, STB/sm3, or scf/stb/sm3-sm3 without explicit conversion.
- For pyrestoolbox-mcp, pay attention to parameter names:
  - Oil gas gravity is usually `sg_g`.
  - Gas tools use `sg`.
  - Inflow tools use `psd` for sandface pressure.
  - Gas formation volume factor, viscosity, density, and compressibility use `zmethod`, not `method`.
- For workflows with material decisions, include uncertainty or sensitivity cases.

## Verification

Run focused tests after edits:

```bash
python3 -m pytest <exercise_folder>/ -v
```

For engineering calculations, add tests with known values, monotonicity checks, or conservation checks rather than only smoke tests.
