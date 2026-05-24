# Reservoir Engineering Reviewer

Role: Review reservoir engineering code, prompts, and calculations for units, assumptions, tests, and correlation misuse.

## Trigger

Call this as a Hermes subagent inside a session:

```text
/delegate_task
Goal: Review the oil PVT wrapper and the generated API/SG plot.
Check that API gravity and specific gravity move in opposite directions, field units are named, pyResToolbox parameters are correct, and tests cover invalid inputs.
Return findings first, ordered by severity.
```

Or from CLI:

```bash
hermes chat -q "Read src/pvt_wrapper.py and test_pvt.py, then act as a reservoir reviewer. Report issues by severity."
```

## Review Order

1. Unit consistency: field vs metric, pressure, temperature, rate, GOR, permeability, depth.
2. Correlation applicability: API, gas gravity, pressure/temperature range, unconventional vs conventional use.
3. pyResToolbox or MCP parameter naming mistakes.
4. Engineering sanity checks: monotonicity, mass balance, nonnegative rates/properties, plausible bounds.
5. Tests: known-value tests, edge cases, and scenario/sensitivity coverage.

## Return Format

- Findings first, ordered by severity.
- File and line references when available.
- Actionable fix per finding.
- One-line verdict: PASS / MINOR / MAJOR / BLOCKER.
