# Exercise 3: Verify Your Work

**Best practice:** give Claude tests with known values and engineering sanity checks.

## Task

Add a production forecast helper to `dca_checks.py` or refactor the current one. Use tests to verify:

- exponential decline matches a known analytic value
- forecast rates remain nonnegative
- EUR increases when the economic limit is lower

## Prompt

```text
Read 03_verify_your_work/dca_checks.py and test_dca_checks.py.
Improve forecast_exponential_decline if needed and add one more engineering sanity test.
Run python3 -m pytest 03_verify_your_work/ -v.
```
