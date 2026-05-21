from __future__ import annotations

import math


def forecast_exponential_decline(qi: float, di: float, years: float) -> float:
    if qi < 0:
        raise ValueError("Initial rate must be nonnegative")
    if di < 0:
        raise ValueError("Decline rate must be nonnegative")
    if years < 0:
        raise ValueError("Forecast time must be nonnegative")
    return qi * math.exp(-di * years)


def exponential_eur(qi: float, di: float, q_limit: float) -> float:
    if qi <= 0 or di <= 0 or q_limit <= 0:
        raise ValueError("qi, di, and q_limit must be positive")
    if q_limit >= qi:
        return 0.0
    return (qi - q_limit) / di

