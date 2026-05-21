# Exercise 1: Explore, Plan, Then Code

**Best practice:** make Claude read the code and data before it edits anything.

## What You Have

- `production_analysis.py` loads monthly well production and computes basic summaries.
- `sample_production.csv` contains small fictional well data.
- `test_production_analysis.py` covers the existing behavior.
- `../assets/production_water_cut.png` shows the expected diagnostic style for the sample data.

## Task

Add `compute_water_cut_trend(df)` to report each well's first water cut, latest water cut, and change in percentage points.

## Engineering Context

Water cut is one of the fastest ways to spot changing well behavior, but it is also easy to compute incorrectly when rows are not sorted or when oil and water volumes are mixed across wells.

For this exercise, use:

```text
water_cut = water_bbl / (oil_bbl + water_bbl)
```

Expected sample interpretation:

- `A-01` starts with lower water cut, then increases by about 6.9 percentage points.
- `B-02` is wetter at every sample month and increases by about 6.2 percentage points.
- The result should be one row per well, sorted by well name, with fractions for first/latest water cut and percentage points for the change.

![Production water-cut diagnostic](../assets/production_water_cut.png)

## What Claude Should Inspect First

Ask Claude to read the data and tests before editing. It should notice:

- `load_production_data` already sorts by `well` and `date`.
- `compute_basic_stats` groups by well and returns a tidy DataFrame.
- The new function should follow that style instead of introducing a separate output format.
- Tests should pin known values from `sample_production.csv`, not only check column names.

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

Optional visual check:

```bash
python3 ../scripts/generate_course_figures.py
```

Then compare the generated production plot and `../assets/generated_results.md` with the function output. This is a lightweight version of the workflow you would use before fitting DCA models or making a water-control recommendation.
