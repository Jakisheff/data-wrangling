# Data Wrangling Exercises

This repository contains solutions for a series of data wrangling exercises using Python and Pandas. The goal is to master data manipulation techniques including concatenation, merging, multi-indexing, groupby operations, and unstacking.

## Prerequisites

- Python 3.9 or higher
- `pip` (Python package installer)

## Installation and Setup

A setup script is provided to create a virtual environment and install all necessary dependencies.

1.  **Run the setup script:**
    ```bash
    ./setup_env.sh
    ```
    This script will:
    - Create a virtual environment named `ex00`.
    - Install required libraries: `pandas`, `numpy`, `tabulate`, `jupyter`, `matplotlib`.

2.  **Activate the virtual environment:**
    ```bash
    source ex00/bin/activate
    ```

## Usage

You can run the solutions either as a Python script or interactively via Jupyter Notebook.

### Running as a Python Script
To execute all exercises and see the output in your terminal:
```bash
source ex00/bin/activate
python3 data_wrangling.py
```
This will print the results for all exercises to the console and save the plot for Exercise 6 as `stocks_2021.png`.

### Running with Jupyter Notebook
To explore the code interactively:
1.  Activate the environment: `source ex00/bin/activate`
2.  Start Jupyter:
    ```bash
    jupyter notebook
    ```
3.  Open `data_wrangling.ipynb` in the browser interface.

## Exercises Overview

-   **Exercise 0: Environment and Libraries** - Setup verification.
-   **Exercise 1: Concatenate** - Combining DataFrames along the index axis.
-   **Exercise 2: Merge** - Inner and outer joins with custom suffixes.
-   **Exercise 3: Merge MultiIndex** - Merging datasets with multi-level indices.
-   **Exercise 4: Groupby Apply** - Implementing winsorization using `groupby` and `apply`.
-   **Exercise 5: Groupby Agg** - Computing aggregations (min, max, mean) on grouped data.
-   **Exercise 6: Unstack** - Pivoting MultiIndex DataFrames and plotting time series data.

## Verification

The solutions have been verified against the project's audit questions. A validation report is available in the `brain` directory or upon request.
