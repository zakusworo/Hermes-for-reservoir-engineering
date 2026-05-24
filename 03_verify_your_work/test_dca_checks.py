import pytest

from dca_checks import exponential_eur, forecast_exponential_decline


def test_forecast_exponential_decline_known_value():
    assert round(forecast_exponential_decline(qi=1000, di=0.1, years=5), 2) == 606.53


def test_forecast_rejects_negative_time():
    with pytest.raises(ValueError):
        forecast_exponential_decline(qi=1000, di=0.1, years=-1)


def test_eur_increases_when_economic_limit_is_lower():
    high_limit = exponential_eur(qi=1000, di=0.1, q_limit=100)
    low_limit = exponential_eur(qi=1000, di=0.1, q_limit=50)

    assert low_limit > high_limit
