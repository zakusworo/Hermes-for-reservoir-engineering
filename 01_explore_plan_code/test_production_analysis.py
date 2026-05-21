from pathlib import Path

from production_analysis import compute_basic_stats, find_top_oil_months, load_production_data


DATA = Path(__file__).with_name("sample_production.csv")


def test_load_production_data_sorts_by_well_and_date():
    df = load_production_data(DATA)

    assert list(df["well"].head(3)) == ["A-01", "A-01", "A-01"]
    assert str(df.loc[0, "date"].date()) == "2025-01-01"


def test_compute_basic_stats_by_well():
    df = load_production_data(DATA)
    stats = compute_basic_stats(df)

    a01 = stats.loc[stats["well"] == "A-01"].iloc[0]
    assert a01["total_oil_bbl"] == 3370
    assert a01["total_water_bbl"] == 410
    assert round(a01["avg_gas_mcf"], 2) == 468.33


def test_find_top_oil_months():
    df = load_production_data(DATA)
    top = find_top_oil_months(df, n=2)

    assert list(top["oil_bbl"]) == [1200, 1120]

