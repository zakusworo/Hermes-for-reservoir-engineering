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

