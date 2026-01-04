# Quantitative Growth Model for Brazil

This repository implements a reproducible quantitative macroeconomic model to evaluate Brazil’s long-run growth potential under structural reform scenarios.

The model demonstrates that Brazil’s low growth is primarily driven by allocative inefficiency rather than technological backwardness, and that realistic reductions in misallocation can sustain growth rates above 3% during a long transition to a higher steady state.

## Model Overview

The framework is an augmented Solow growth model with:

- Capital accumulation and capital deepening
- Human capital dynamics
- Exogenous technological frontier growth
- Endogenous allocative efficiency dynamics inspired by Hsieh & Klenow (2009)

Total factor productivity is decomposed as:

A_t = A*_t × E_t

where E_t captures allocative efficiency and converges under reform scenarios.

## Scenarios

- **Inertial (Status Quo)**: marginal efficiency gains
- **Structural Reform**: convergence to Southern European efficiency levels
- **High Convergence**: upper-bound scenario inspired by fast reformers

## Key Result

Under conservative assumptions, structural reallocation alone is sufficient to generate sustained growth above 3% during the transition period, leading to large long-run income gains without requiring frontier technological breakthroughs.

## Data & Calibration

Parameters are calibrated using IMF World Economic Outlook, Penn World Table, and IBGE benchmarks.

## Reproducibility

All results and figures can be reproduced by running:

```bash
python simulation.py
