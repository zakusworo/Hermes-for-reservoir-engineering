# Exercise 2: Give Specific Context

**Best practice:** name the file, function, failing test, and observed symptom.

## Scenario

`pvt_conversions.py` has a subtle unit conversion bug. The function is supposed to convert API gravity to oil specific gravity and back.

## Before Prompt

```text
Fix the PVT bug.
```

## After Prompt

```text
The test test_round_trip_api_specific_gravity in 02_specific_context/test_pvt_conversions.py fails.
Read 02_specific_context/pvt_conversions.py and fix api_to_specific_gravity or specific_gravity_to_api.
The petroleum engineering relationship is SG = 141.5 / (API + 131.5).
Run python3 -m pytest 02_specific_context/ -v after the edit.
```
