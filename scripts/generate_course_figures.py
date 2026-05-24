from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PRODUCTION_CSV = ROOT / "01_explore_plan_code" / "sample_production.csv"


def load_production() -> pd.DataFrame:
    df = pd.read_csv(PRODUCTION_CSV, parse_dates=["date"])
    df = df.sort_values(["well", "date"]).reset_index(drop=True)
    df["liquid_bbl"] = df["oil_bbl"] + df["water_bbl"]
    df["water_cut"] = df["water_bbl"] / df["liquid_bbl"]
    df["gor_scf_stb"] = df["gas_mcf"] * 1000 / df["oil_bbl"]
    return df


def plot_production_diagnostics(df: pd.DataFrame) -> pd.DataFrame:
    fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
    colors = {"A-01": "#1f77b4", "B-02": "#d62728"}

    for well, well_df in df.groupby("well"):
        axes[0].plot(
            well_df["date"],
            well_df["oil_bbl"],
            marker="o",
            linewidth=2.5,
            label=f"{well} oil",
            color=colors[well],
        )
        axes[0].plot(
            well_df["date"],
            well_df["water_bbl"],
            marker="s",
            linewidth=2,
            linestyle="--",
            label=f"{well} water",
            color=colors[well],
            alpha=0.65,
        )
        axes[1].plot(
            well_df["date"],
            well_df["water_cut"] * 100,
            marker="o",
            linewidth=2.5,
            label=well,
            color=colors[well],
        )

    axes[0].set_title("Monthly Production Snapshot")
    axes[0].set_ylabel("Monthly volume")
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(ncols=2, fontsize=9)

    axes[1].set_title("Water-Cut Trend")
    axes[1].set_ylabel("Water cut, %")
    axes[1].set_xlabel("Production month")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(title="Well")

    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(ASSETS / "production_water_cut.png", dpi=180)
    plt.close(fig)

    first_last = (
        df.sort_values(["well", "date"])
        .groupby("well")
        .agg(
            first_water_cut=("water_cut", "first"),
            latest_water_cut=("water_cut", "last"),
            total_oil_bbl=("oil_bbl", "sum"),
            total_water_bbl=("water_bbl", "sum"),
            avg_gor_scf_stb=("gor_scf_stb", "mean"),
        )
        .reset_index()
    )
    first_last["water_cut_change_pct_points"] = (
        first_last["latest_water_cut"] - first_last["first_water_cut"]
    ) * 100
    return first_last


def plot_pvt_conversion() -> pd.DataFrame:
    api = np.linspace(10, 50, 200)
    sg = 141.5 / (api + 131.5)
    samples = pd.DataFrame({"api": [22, 30, 35, 42]})
    samples["specific_gravity"] = 141.5 / (samples["api"] + 131.5)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(api, sg, color="#005f73", linewidth=2.5)
    ax.scatter(samples["api"], samples["specific_gravity"], color="#ae2012", zorder=3)
    for _, row in samples.iterrows():
        ax.annotate(
            f"{row.api:.0f} API\nSG {row.specific_gravity:.3f}",
            (row.api, row.specific_gravity),
            xytext=(8, 8),
            textcoords="offset points",
            fontsize=8,
        )

    ax.set_title("API Gravity to Oil Specific Gravity")
    ax.set_xlabel("API gravity")
    ax.set_ylabel("Oil specific gravity, water = 1.0")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(ASSETS / "pvt_api_specific_gravity.png", dpi=180)
    plt.close(fig)
    return samples


def exponential_rate(qi: float, di: float, years: np.ndarray) -> np.ndarray:
    return qi * np.exp(-di * years)


def exponential_eur(qi: float, di: float, q_limit: float) -> float:
    if q_limit >= qi:
        return 0.0
    return (qi - q_limit) / di


def plot_dca_screening() -> pd.DataFrame:
    years = np.linspace(0, 12, 145)
    qi = 1000.0
    decline_cases = pd.DataFrame(
        {
            "case": ["low decline", "base decline", "high decline"],
            "di_per_year": [0.08, 0.12, 0.18],
            "color": ["#2a9d8f", "#264653", "#e76f51"],
        }
    )

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    for _, case in decline_cases.iterrows():
        rates = exponential_rate(qi, case.di_per_year, years)
        axes[0].plot(
            years,
            rates,
            linewidth=2.5,
            label=f"{case.case} ({case.di_per_year:.0%}/yr)",
            color=case.color,
        )
    axes[0].axhline(50, color="#555555", linestyle="--", linewidth=1.5, label="50 bopd limit")
    axes[0].set_title("Exponential Decline Rate Forecast")
    axes[0].set_xlabel("Years")
    axes[0].set_ylabel("Oil rate, bopd")
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(fontsize=8)

    limits = np.array([150, 100, 75, 50, 25])
    eur_by_case = []
    for _, case in decline_cases.iterrows():
        eur = [exponential_eur(qi, case.di_per_year, q) / 1000 for q in limits]
        eur_by_case.append(eur)
        axes[1].plot(
            limits,
            eur,
            marker="o",
            linewidth=2.5,
            label=case.case,
            color=case.color,
        )

    axes[1].invert_xaxis()
    axes[1].set_title("EUR Sensitivity to Economic Limit")
    axes[1].set_xlabel("Economic limit, bopd")
    axes[1].set_ylabel("EUR index, thousand rate-years")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(fontsize=8)

    fig.tight_layout()
    fig.savefig(ASSETS / "dca_decline_sensitivity.png", dpi=180)
    plt.close(fig)

    rows = []
    for case, eur_values in zip(decline_cases.to_dict("records"), eur_by_case):
        rows.append(
            {
                "case": case["case"],
                "di_per_year": case["di_per_year"],
                "rate_year_5_bopd": exponential_rate(qi, case["di_per_year"], np.array([5]))[0],
                "eur_to_50_bopd_index": exponential_eur(qi, case["di_per_year"], 50),
            }
        )
    return pd.DataFrame(rows)


def plot_ai_workflow_map() -> None:
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.axis("off")
    steps = [
        ("Explore", "Read code, CSV schema,\nunits, and tests"),
        ("Plan", "Name functions, edge cases,\nand acceptance checks"),
        ("Code", "Make the smallest\nengineering-safe edit"),
        ("Verify", "Run tests, plot results,\ncheck physical bounds"),
        ("Review", "Use domain review for\nunits and assumptions"),
    ]
    x_positions = np.linspace(0.08, 0.92, len(steps))
    for idx, ((title, body), x) in enumerate(zip(steps, x_positions)):
        box = plt.Rectangle((x - 0.085, 0.35), 0.17, 0.34, fill=True, color="#f8f9fa", ec="#264653", lw=1.8)
        ax.add_patch(box)
        ax.text(x, 0.61, title, ha="center", va="center", fontsize=13, weight="bold", color="#264653")
        ax.text(x, 0.47, body, ha="center", va="center", fontsize=9, color="#333333")
        if idx < len(steps) - 1:
            ax.annotate(
                "",
                xy=(x_positions[idx + 1] - 0.1, 0.52),
                xytext=(x + 0.1, 0.52),
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#6c757d"},
            )
    ax.text(
        0.5,
        0.18,
        "Reservoir engineering guardrail: never accept a smooth answer until units, assumptions, and sanity checks are visible.",
        ha="center",
        va="center",
        fontsize=11,
        color="#111111",
    )
    fig.tight_layout()
    fig.savefig(ASSETS / "claude_reservoir_workflow.png", dpi=180)
    plt.close(fig)


def write_results_markdown(
    production_summary: pd.DataFrame,
    pvt_summary: pd.DataFrame,
    dca_summary: pd.DataFrame,
) -> None:
    def markdown_table(df: pd.DataFrame) -> str:
        headers = [str(column) for column in df.columns]
        rows = [[str(value) for value in row] for row in df.to_numpy()]
        lines = [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(["---"] * len(headers)) + " |",
        ]
        lines.extend("| " + " | ".join(row) + " |" for row in rows)
        return "\n".join(lines)

    production = production_summary.copy()
    production["first_water_cut"] = (production["first_water_cut"] * 100).round(1)
    production["latest_water_cut"] = (production["latest_water_cut"] * 100).round(1)
    production["water_cut_change_pct_points"] = production["water_cut_change_pct_points"].round(1)
    production["avg_gor_scf_stb"] = production["avg_gor_scf_stb"].round(0)

    pvt = pvt_summary.copy()
    pvt["specific_gravity"] = pvt["specific_gravity"].round(3)

    dca = dca_summary.copy()
    dca["di_per_year"] = dca["di_per_year"].map(lambda value: f"{value:.0%}")
    dca["rate_year_5_bopd"] = dca["rate_year_5_bopd"].round(1)
    dca["eur_to_50_bopd_index"] = dca["eur_to_50_bopd_index"].round(0)

    content = "\n".join(
        [
            "# Generated Course Results",
            "",
            "These tables are generated by `python3 scripts/generate_course_figures.py`.",
            "",
            "## Production Diagnostics",
            "",
            markdown_table(production),
            "",
            "## PVT Conversion Reference Points",
            "",
            markdown_table(pvt),
            "",
            "## DCA Screening Cases",
            "",
            markdown_table(dca),
            "",
        ]
    )
    (ASSETS / "generated_results.md").write_text(content)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    production_df = load_production()
    production_summary = plot_production_diagnostics(production_df)
    pvt_summary = plot_pvt_conversion()
    dca_summary = plot_dca_screening()
    plot_ai_workflow_map()
    write_results_markdown(production_summary, pvt_summary, dca_summary)


if __name__ == "__main__":
    main()
