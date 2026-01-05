"""
Allocative Efficiency and Long-Run Growth: A Quantitative Assessment for Brazil
Author: João Víctor Medeiros (2026)
Implementation of an augmented Solow model focusing on misallocation.

Cite as: 
Medeiros, J. V. (2026). Allocative Efficiency and Long-Run Growth: 
A Quantitative Assessment for Brazil. GitHub: zKalel/brazil-growth-misallocation-model
"""

import numpy as np
import matplotlib.pyplot as plt

# ======================================================
# 1. PARAMETERS & CALIBRATION
# ======================================================

alpha = 0.40          # Capital share
delta = 0.045         # Depreciation
g_L = 0.003           # Labor growth
g_h = 0.002           # Human capital growth
g_frontier = 0.01     # Global technology growth

# Capital deepening
ky_initial = 2.85
ky_target = 3.80
eta_ky = 0.04

# Efficiency dynamics
E_initial = 0.40
lambda_E = 0.03

scenarios = {
    "Inertial": 0.42,
    "Structural Reform": 0.60,
    "High Convergence": 0.70
}

start_year = 2025
years = 31
time = np.arange(start_year, start_year + years)

# ======================================================
# 2. SIMULATION ENGINE
# ======================================================

def simulate_economy(E_target):
    Y = np.zeros(years)
    K = np.zeros(years)
    L = np.zeros(years)
    h = np.zeros(years)
    A_frontier = np.zeros(years)
    E = np.zeros(years)
    A = np.zeros(years)
    ky = np.zeros(years)
    gY = np.zeros(years)

    # Initial conditions
    L[0] = 100.0
    h[0] = 3.25
    A_frontier[0] = 1.0
    E[0] = E_initial
    A[0] = A_frontier[0] * E[0]
    ky[0] = ky_initial

    Y[0] = 100.0
    K[0] = ky[0] * Y[0]

    for t in range(1, years):
        # Exogenous processes
        L[t] = L[t-1] * (1 + g_L)
        h[t] = h[t-1] * (1 + g_h)
        A_frontier[t] = A_frontier[t-1] * (1 + g_frontier)

        # Efficiency convergence
        E[t] = E[t-1] + lambda_E * (E_target - E[t-1])
        A[t] = A_frontier[t] * E[t]

        # Capital-output ratio convergence
        ky[t] = ky[t-1] + eta_ky * (ky_target - ky[t-1])

        # Capital accumulation
        K[t] = ky[t] * Y[t-1]

        # Production function
        Y[t] = (K[t] ** alpha) * ((A[t] * h[t] * L[t]) ** (1 - alpha))

        # Growth rate
        gY[t] = (Y[t] / Y[t-1] - 1) * 100

    return Y, gY, E

# ======================================================
# 3. RUN SIMULATIONS
# ======================================================

results = {}

for name, E_target in scenarios.items():
    results[name] = simulate_economy(E_target)

# ======================================================
# 4. PLOTS
# ======================================================

plt.figure(figsize=(10,6))

for name in scenarios:
    Y = results[name][0]
    plt.plot(time, Y / Y[0], label=name)

plt.title("Brazil – Long-Run Growth Scenarios")
plt.xlabel("Year")
plt.ylabel("GDP Index (2025 = 1)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))

for name in scenarios:
    E = results[name][2]
    plt.plot(time, E, label=name)

plt.title("Allocative Efficiency Convergence (E_t)")
plt.xlabel("Year")
plt.ylabel("Efficiency Level")
plt.legend()
plt.grid(True)
plt.show()
