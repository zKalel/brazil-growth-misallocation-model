Quantitative Growth Model for Brazil
This repository contains a reproducible quantitative macroeconomic model designed to study Brazil’s long-run growth through productivity, capital accumulation, and resource reallocation.

Model Overview
The framework is based on an augmented Solow model with:

Capital accumulation dynamics
Human capital
Exogenous technological frontier growth
Endogenous efficiency (misallocation) dynamics inspired by Hsieh & Klenow (2009)
The key mechanism is the convergence of allocative efficiency (E_t) towards higher steady-state levels under structural reform scenarios.

Scenarios
Inertial (status quo)
Structural reform
High convergence (upper bound)
Data & Calibration
Parameters are calibrated using IMF, Penn World Table, and IBGE benchmarks.

Reproducibility
All results can be reproduced by running:

python simulation.py
