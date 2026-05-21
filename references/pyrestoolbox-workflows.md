# pyResToolbox Workflow Notes

## PVT Quick Check

Inputs: API, reservoir temperature, pressure range, solution GOR, gas gravity, separator conditions if available.

Outputs: bubble point, Rs, Bo, viscosity, density, compressibility, black-oil table if simulation needs it.

Quality checks:

- Bo should generally increase toward bubble point from undersaturated pressures.
- Viscosity should be positive.
- Rs should not exceed saturated solution GOR above bubble point without an explicit model.

## DCA Quick Check

Inputs: time, rate, optional cumulative, uptime, economic limit.

Outputs: fitted model, qi, Di, b, forecast, EUR, residual diagnostics.

Quality checks:

- Forecast rates are nonnegative.
- EUR is larger than cumulative produced.
- Hyperbolic `b` should be constrained to a defensible range.

## Material Balance Quick Check

Inputs: pressure history, cumulative production, temperature, fluid properties, aquifer assumptions.

Outputs: OGIP/OOIP, regression quality, drive indices, diagnostic plots.

Quality checks:

- Pressure and cumulative production should be monotonic in the expected directions.
- P/Z analysis needs consistent gas Z-factor method and units.

