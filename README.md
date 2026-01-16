## Exponential Smoothing Forecast: A Python vs. R Comparative Study
Project Overview

This project, developed as part of Reto 4 at UVEG, explores the implementation of the Exponential Smoothing algorithm for time-series forecasting. The goal is to predict values for the year 2020 based on historical data from 2015-2019 across various indicators.

Original data
| | HC | HI | HT | HTP | U6E | UI6E | UCHE | UITI | UIFH | UTC6E |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 44.90000 | 39.200 | 93.5000 | 43.70 | 51.30000 | 57.40000 | 51.30000 | 12.80000 | 29.1000 | 71.50000 |
| **2** | 45.60000 | 47.000 | 93.1000 | 52.10 | 47.00000 | 59.50000 | 52.20000 | 14.70000 | 20.5000 | 73.60000 |
| **3** | 45.40000 | 50.900 | 93.2000 | 49.50 | 45.30000 | 63.90000 | 46.80000 | 20.40000 | 16.7000 | 72.20000 |
| **4** | 44.90000 | 52.900 | 92.9000 | 47.30 | 45.00000 | 65.80000 | 46.70000 | 23.70000 | 13.4000 | 73.50000 |
| **5** | 44.30000 | 56.400 | 92.5000 | 45.90 | 43.00000 | 70.10000 | 44.60000 | 27.20000 | 10.7000 | 75.10000 |

Final table, with predicted values in 6th row
| | HC | HI | HT | HTP | U6E | UI6E | UCHE | UITI | UIFH | UTC6E |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 44.90000 | 39.200 | 93.5000 | 43.70 | 51.30000 | 57.40000 | 51.30000 | 12.80000 | 29.1000 | 71.50000 |
| **2** | 45.60000 | 47.000 | 93.1000 | 52.10 | 47.00000 | 59.50000 | 52.20000 | 14.70000 | 20.5000 | 73.60000 |
| **3** | 45.40000 | 50.900 | 93.2000 | 49.50 | 45.30000 | 63.90000 | 46.80000 | 20.40000 | 16.7000 | 72.20000 |
| **4** | 44.90000 | 52.900 | 92.9000 | 47.30 | 45.00000 | 65.80000 | 46.70000 | 23.70000 | 13.4000 | 73.50000 |
| **5** | 44.30000 | 56.400 | 92.5000 | 45.90 | 43.00000 | 70.10000 | 44.60000 | 27.20000 | 10.7000 | 75.10000 |
| **6** | 44.70625 | 53.175 | 92.7875 | 46.95 | 44.55625 | 66.79375 | 46.29375 | 23.79375 | 13.8875 | 74.01875 |

The Algorithm

Exponential smoothing is a technique for smoothing time series data using the exponential window function. The implementation follows the formula:
St​=α⋅Xt−1​+(1−α)⋅St−1​

Where:

    St​: Forecast for the current period.

    α: Smoothing factor (set to 0.5 in this project).

    Xt−1​: Actual value of the previous period.

    St−1​: Forecast of the previous period.

Comparative Implementation
Python Implementation

    Paradigm: Imperative and procedural.

    Key Libraries: numpy for data handling and matplotlib for high-quality visualization.

    Highlights: Focuses on explicit state management and granular control over the iteration process.

R Implementation

    Paradigm: Functional programming.

    Key Libraries: purrr (tidyverse) for functional operations and base graphics for plotting.

    Highlights: Utilizes the reduce function to synthesize the forecasting logic into a more compact and expressive syntax.

Visualization Results

The project generates comparative plots to visualize trends across 10 different indicators (HC, HI, HT, HTP, etc.). While the R implementation offers a concise statistical approach, the Python version provides a more modern and customizable graphical output, that looks prettier to me, and is even more versatile.

<img width="718" height="637" alt="image" src="https://github.com/user-attachments/assets/2e31b3eb-27cd-47f0-9eb7-9e744017c47b" />
