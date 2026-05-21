from pvt_conversions import api_to_specific_gravity, field_to_metric_pressure, specific_gravity_to_api


def test_round_trip_api_specific_gravity():
    api = 35.0
    sg = api_to_specific_gravity(api)

    assert round(sg, 4) == 0.8498
    assert round(specific_gravity_to_api(sg), 6) == api


def test_field_to_metric_pressure():
    assert round(field_to_metric_pressure(14.6959), 5) == 1.01325

