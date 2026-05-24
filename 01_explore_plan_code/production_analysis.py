from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_production_data(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    required = {"date", "well", "oil_bbl", "water_bbl", "gas_mcf"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df.sort_values(["well", "date"]).reset_index(drop=True)


def compute_basic_stats(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("well", as_index=False)
        .agg(
            total_oil_bbl=("oil_bbl", "sum"),
            total_water_bbl=("water_bbl", "sum"),
            avg_gas_mcf=("gas_mcf", "mean"),
        )
        .sort_values("well")
        .reset_index(drop=True)
    )


def find_top_oil_months(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    return df.sort_values("oil_bbl", ascending=False).head(n).reset_index(drop=True)
