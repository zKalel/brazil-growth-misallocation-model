# Brazil Growth & Misallocation Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository implements a reproducible quantitative macroeconomic framework to evaluate Brazil’s long-run growth potential through the lens of **allocative efficiency**. 

The model demonstrates that Brazil’s persistently low growth is primarily driven by microeconomic distortions (misallocation) rather than technological backwardness. [cite_start]By reducing these distortions, the economy can achieve sustained transitional growth rates above 3% without requiring frontier technological breakthroughs[cite: 305, 557, 734].

## Model Structure

The framework is an **augmented Solow-Swan growth model** that incorporates:
- [cite_start]**Endogenous Efficiency Dynamics:** Inspired by Hsieh & Klenow (2009), mapping micro-distortions to aggregate TFP[cite: 307, 559, 785].
- [cite_start]**Capital Deepening:** Modeled through a gradually adjusting capital-output ratio ($\kappa$)[cite: 358, 610, 803].
- [cite_start]**Human Capital Accumulation:** Exogenous skill dynamics based on educational attainment[cite: 374, 626, 799].

### Total Factor Productivity (TFP) Decomposition
The model decomposes aggregate productivity $A_t$ as:

$$A_{t} = A_{t}^{*} \cdot E_{t}$$

Where:
- [cite_start]$A_{t}^{*}$ represents the exogenous global technological frontier[cite: 193, 501, 780].
- [cite_start]$E_{t} \in (0,1]$ captures **allocative efficiency**, reflecting the impact of institutional and regulatory distortions[cite: 198, 506, 785].

The transition is governed by a partial convergence process:
$$E_{t+1} = E_{t} + \lambda_{E}(E^{*} - E_{t})$$
[cite_start]where $\lambda_{E}$ captures the pace of structural reforms[cite: 202, 509, 788].

## Scenarios & Results

[cite_start]We simulate the Brazilian economy over a 30-year horizon (2025–2055) under three distinct regimes[cite: 385, 640]:

| Scenario | Efficiency Target ($E^*$) | Description |
| :--- | :---: | :--- |
| **Inertial** | 0.42 | [cite_start]Status quo with fragmented, minor reforms[cite: 392, 645, 706]. |
| **Structural Reform** | 0.60 | [cite_start]Credible improvements in tax neutrality and regulation (Southern Europe levels)[cite: 393, 647, 711]. |
| **High Convergence** | 0.70 | [cite_start]Upper-bound scenario reaching OECD/South Korean efficiency standards[cite: 463, 716]. |

## Data & Calibration

The model is calibrated using international macroeconomic benchmarks:
- [cite_start]**Capital Share ($\alpha$):** 0.40[cite: 73, 370, 622].
- [cite_start]**Frontier Growth ($g_f$):** 1.0%[cite: 77, 375, 627].
- [cite_start]**Initial Efficiency ($E_0$):** 0.40 (consistent with Penn World Table and Hsieh-Klenow estimates)[cite: 82, 379, 635].

## Reproducibility

To reproduce the results and figures:
1. Ensure you have `numpy` and `matplotlib` installed.
2. Run the simulation script:
   ```bash
   python simulation.py
