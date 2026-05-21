# Exercise 7: CLI Workflow

**Best practice:** let Claude combine shell tools and Python checks for repeatable data QA.

## Scenario

You receive monthly production CSVs. Before DCA or material balance, ask Claude to inspect schema, missing values, duplicate dates, and monotonic cumulative production.

## Prompt

```text
Use shell commands to inspect 01_explore_plan_code/sample_production.csv.
Then write a short Python QA script that checks required columns, nonnegative rates, and duplicate well/date rows.
Run it and summarize the result.
```

## Extension

Use this same pattern on real exports before fitting decline curves or running material balance.

