# Exercise 9: Parallel Fan-Out

**Best practice:** split independent scenarios across subagents or parallel tool calls, then aggregate results.

## Scenario

A reservoir engineer wants a screening sensitivity across:

- bubble point methods: `STAN`, `VALMC`, `VELAR`
- gas Z-factor methods: `DAK`, `HY`, `WYW`
- skin cases: `-2`, `0`, `5`

## Prompt

```text
Run a parallel fan-out study.
Assign independent workers to PVT method comparison, gas Z-factor comparison, and skin sensitivity.
Each worker should return inputs, method choices, result table, and sanity checks.
Aggregate the results into a short screening recommendation.
```

## What To Notice

Parallelization is useful only when scenarios are independent. Use a final aggregation step to compare assumptions and avoid mixing units or methods.

