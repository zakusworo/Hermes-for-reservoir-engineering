# Exercise 5: Skills For Reservoir Workflows

**Best practice:** create skills for repeatable domain guidance.

## Included Skill

The repository includes:

- `.claude/skills/reservoir-engineering/SKILL.md`
- `.claude/skills/run-tests/SKILL.md`

## Prompt

```text
Use the reservoir-engineering skill.
Create a PVT workflow checklist for a black-oil model using pyResToolbox or pyrestoolbox-mcp.
Include required inputs, method choices, outputs, and sanity checks.
```

## What To Notice

The skill reduces repeated explanation. It keeps common parameter naming mistakes close to the model context and encourages consistent outputs.

## Stronger Exercise

After the checklist is drafted, ask Claude to turn it into a reusable deliverable:

```text
Expand the checklist into a one-page black-oil PVT workflow.
Include input data QA, method selection, expected plots, tabular outputs, and red flags that require engineer review.
```

The answer should include more than a list of tool names. A useful workflow separates:

- required measured inputs, such as API, temperature, gas gravity, and solution GOR
- chosen correlations and why they fit the screening problem
- generated outputs, such as bubble point, oil FVF, viscosity, and gas properties
- visual checks, such as API vs SG consistency or pressure-dependent property trends
- review gates for unit mismatches and correlation range violations

## Expected Visual Habit

When a skill is used for repeated engineering work, it should ask for figures when the output is trend- or sensitivity-based. For example, this course uses generated plots for production diagnostics, PVT conversion checks, and DCA sensitivities:

```bash
python3 scripts/generate_course_figures.py
```

That command is deliberately simple. The deeper lesson is that skills should encode the habit of making important assumptions visible.
