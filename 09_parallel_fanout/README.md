# Exercise 9: Parallel Fan-Out

**Best practice:** split independent scenarios across subagents or parallel tool calls, then aggregate results.

## Scenario

A reservoir engineer wants a screening sensitivity across:

- bubble point methods: `STAN`, `VALMC`, `VELAR`
- gas Z-factor methods: `DAK`, `HY`, `WYW`
- skin cases: `-2`, `0`, `5`

## Engineering Context

Parallel work is useful only when cases are independent and the final aggregation compares like with like. A fan-out study should not hide method changes, unit changes, or different assumptions behind a single "best" number.

Use this mental model:

![Claude reservoir workflow](../assets/claude_reservoir_workflow.png)

Each worker should return:

- inputs and units
- method or correlation
- result table
- one plot if the output is trend-based
- sanity checks and warnings
- whether the result is screening-level or decision-grade

## Prompt

```text
Run a parallel fan-out study.
Assign independent workers to PVT method comparison, gas Z-factor comparison, and skin sensitivity.
Each worker should return inputs, method choices, result table, and sanity checks.
Aggregate the results into a short screening recommendation.
```

## What To Notice

Parallelization is useful only when scenarios are independent. Use a final aggregation step to compare assumptions and avoid mixing units or methods.

## Stronger Aggregation Prompt

```text
Aggregate the worker outputs into one screening memo.
Do not average unlike methods.
Show a compact table of method, units, key result, sanity check, and recommendation.
Flag any scenario that needs a reservoir engineer review before use.
```

The final answer should distinguish technical comparison from decision-making. Claude can organize the sensitivity study, but the engineer still owns the method choice and the consequence of carrying a screening result into a model.
