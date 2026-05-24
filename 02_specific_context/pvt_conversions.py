from __future__ import annotations


def api_to_specific_gravity(api: float) -> float:
    if api <= 0:
        raise ValueError("API gravity must be positive")
    return 141.5 / (api + 131.5)


def specific_gravity_to_api(sg: float) -> float:
    if sg <= 0:
        raise ValueError("Specific gravity must be positive")
    return 141.5 / sg - 131.5


def field_to_metric_pressure(psia: float) -> float:
    if psia < 0:
        raise ValueError("Pressure must be nonnegative")
    return psia * 0.0689476
