# Exercise 3: Verify Your Work

**Best practice:** give Claude tests with known values and engineering sanity checks.

## Task

Add a production forecast helper to `dca_checks.py` or refactor the current one. Use tests to verify:

- exponential decline matches a known analytic value
- forecast rates remain nonnegative
- EUR increases when the economic limit is lower

## Engineering Context

Decline-curve helpers are deceptively easy to write because the equations are compact. The risk is not syntax; the risk is accepting a smooth forecast that violates a physical or economic check.

For the teaching example:

```text
q(t) = qi * exp(-di * t)
```

where:

- `qi` is initial oil rate
- `di` is nominal decline per year
- `t` is time in years
- the output rate uses the same rate basis as `qi`

The generated DCA figure shows how a base case changes when decline rate and economic limit change.

![DCA decline sensitivity](../assets/dca_decline_sensitivity.png)

Expected screening behavior:

- at the same `qi`, higher `di` gives lower future rate
- lowering the economic limit increases EUR
- negative time, negative rates, and nonpositive decline inputs should be rejected
- EUR from this simplified formula is a teaching index, not a reserves estimate

## Prompt

```text
Read 03_verify_your_work/dca_checks.py and test_dca_checks.py.
Improve forecast_exponential_decline if needed and add one more engineering sanity test.
Run python3 -m pytest 03_verify_your_work/ -v.
```

## Better Follow-Up Prompt

```text
Now generate a small DCA sensitivity plot for qi=1000 bopd, di values of 8%, 12%, and 18% per year, and economic limits of 150, 100, 75, 50, and 25 bopd.
Save the figure, summarize which assumptions move EUR the most, and state that the example is screening-level only.
```

This follow-up is important because visual outputs often reveal mismatched units, reversed axes, or overconfident interpretations faster than a table alone.
