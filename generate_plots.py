"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic sensor readings and timestamps.

    Parameters
    ----------
    seed : int
        Seed for NumPy's random number generator.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of 200 temperature readings for Sensor A in Celsius.
    sensor_b : numpy.ndarray
        Array of 200 temperature readings for Sensor B in Celsius.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly sampled from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)

    timestamps = np.sort(rng.uniform(0, 10, size=200))
    sensor_a = rng.normal(loc=25, scale=3, size=200)
    sensor_b = rng.normal(loc=27, scale=4.5, size=200)

    return sensor_a, sensor_b, timestamps

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.