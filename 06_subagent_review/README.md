# Exercise 6: Reservoir Reviewer Subagent

**Best practice:** use a reviewer subagent when correctness depends on assumptions, units, or domain constraints.

## Included Agent

`.claude/agents/reservoir-reviewer.md`

## Prompt

```text
Implement a small oil PVT calculation wrapper.
Then ask the reservoir-reviewer subagent to review the result for units, assumptions, pyResToolbox parameter names, and missing tests.
Address every material finding.
```

## Review Focus

- Field vs metric units
- Correlation applicability
- Nonphysical outputs
- Missing edge cases
- Silent method changes

## What The Reviewer Should See

Do not ask for a vague review. Give the subagent evidence:

- the edited file paths
- tests that were added or changed
- generated tables or plots
- assumptions and units
- any correlations or library functions used

For example:

```text
Review the oil PVT wrapper and the generated API/SG plot.
Check that API gravity and specific gravity move in opposite directions, field units are named, pyResToolbox parameters are correct, and tests cover invalid inputs.
Return findings first, ordered by severity.
```

## Example Finding Types

A useful reviewer should catch issues such as:

- a chart label says percent while the code plots fractions
- gas gravity uses `sg` in a tool that expects `sg_g`
- a correlation is used outside a plausible temperature or API range
- a test checks only that output exists, not that it is physically reasonable
- a sensitivity table mixes psia and barsa without conversion

The reviewer is not there to make the project sound polished. It is there to make hidden technical risk visible before the result leaves the sandbox.
