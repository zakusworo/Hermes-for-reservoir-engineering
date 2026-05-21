# Exercise 1: Explore, Plan, Then Code

**Best practice:** make Claude read the code and data before it edits anything.

## What You Have

- `production_analysis.py` loads monthly well production and computes basic summaries.
- `sample_production.csv` contains small fictional well data.
- `test_production_analysis.py` covers the existing behavior.

## Task

Add `compute_water_cut_trend(df)` to report each well's first water cut, latest water cut, and change in percentage points.

## Before Prompt

```text
Add water cut trend analysis.
```

## After Prompt

```text
Read 01_explore_plan_code/production_analysis.py, sample_production.csv, and test_production_analysis.py.
Plan how to add compute_water_cut_trend(df), where water cut is water_bbl / (oil_bbl + water_bbl).
Return one row per well with first_water_cut, latest_water_cut, and water_cut_change_pct_points.
Then implement it and add focused pytest coverage.
```

## Verification

```bash
python3 -m pytest 01_explore_plan_code/ -v
```
