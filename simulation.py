"""
Allocative Efficiency and Long-Run Growth: A Quantitative Assessment for Brazil
Author: João Víctor Medeiros (2026)

Implementation of an augmented Solow-Swan model with endogenous allocative efficiency.
Reproducible research code.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ======================================================
# 1. PARAMETERS & CALIBRATION
# ======================================================

params = {
    # Production
    "alpha": 0.40,
    "delta": 0.045,

    # Exogenous growth
    "g_L": 0.003,
    "g_h": 0.002,
    "g_frontier": 0.01,

    # Capital deepening
    "ky_initial": 2.85,
    "ky_target": 3.80,
    "eta_ky": 0.04,

    # Allocative efficiency
    "E_initial": 0.40,
    "lambda_E": 0.03,

    # Simulation horizon
    "start_year": 2025,
    "years": 31
}

scenarios = {
    "Inertial": 0.42,
    "Structural_Reform": 0.60,
    "High_Convergence": 0.70
}

# Output directory
OUTPUT_DIR = "results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ======================================================
# 2. SIMULATION ENGINE
# ======================================================

def simulate_economy(params, E_target):
    years = params["years"]

    # Containers
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
    E[0] = params["E_initial"]
    A[0] = A_frontier[0] * E[0]
    ky[0] = params["ky_initial"]

    Y[0] = 100.0
    K[0] = ky[0] * Y[0]

    for t in range(1, years):
        # Exogenous processes
        L[t] = L[t-1] * (1 + params["g_L"])
        h[t] = h[t-1] * (1 + params["g_h"])
        A_frontier[t] = A_frontier[t-1] * (1 + params["g_frontier"])

        # Allocative efficiency convergence
        E[t] = E[t-1] + params["lambda_E"] * (E_target - E[t-1])
        A[t] = A_frontier[t] * E[t]

        # Capital-output ratio convergence
        ky[t] = ky[t-1] + params["eta_ky"] * (params["ky_target"] - ky[t-1])

        # Capital accumulation (reduced-form)
        K[t] = ky[t] * Y[t-1]

        # Production function
        Y[t] = (K[t] ** params["alpha"]) * ((A[t] * h[t] * L[t]) ** (1 - params["alpha"]))

        # Growth rate
        gY[t] = (Y[t] / Y[t-1] - 1) * 100

    # Time index
    years_index = np.arange(
        params["start_year"],
        params["start_year"] + params["years"]
    )

    # Output DataFrame
    df = pd.DataFrame({
        "Year": years_index,
        "GDP_Index": Y / Y[0],
        "GDP_Growth_Rate": gY,
        "Allocative_Efficiency": E,
        "Capital_Output_Ratio": ky
    })

    return df

# ======================================================
# 3. RUN SIMULATIONS
# ======================================================

results = {}

for scenario, E_target in scenarios.items():
    df = simulate_economy(params, E_target)
    results[scenario] = df

    # Save CSV
    df.to_csv(f"{OUTPUT_DIR}/results_{scenario}.csv", index=False)

# ======================================================
# 4. PLOTS
# ======================================================

# GDP paths
plt.figure(figsize=(10, 6))

for scenario, df in results.items():
    plt.plot(df["Year"], df["GDP_Index"], label=scenario)

plt.title("Brazil – Long-Run Growth Scenarios")
plt.xlabel("Year")
plt.ylabel("GDP Index (2025 = 1)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Allocative efficiency paths
plt.figure(figsize=(10, 6))

for scenario, df in results.items():
    plt.plot(df["Year"], df["Allocative_Efficiency"], label=scenario)

plt.title("Allocative Efficiency Convergence (Eₜ)")
plt.xlabel("Year")
plt.ylabel("Efficiency Level")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
