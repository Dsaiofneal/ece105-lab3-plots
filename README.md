<!-- Create a README.md with these sections:
     1. Project title and one-sentence description
     2. Installation (activate ece105 conda env, pip install numpy matplotlib)
     3. Usage (python generate_plots.py)
     4. Example output (describe the three plots briefly)
     5. AI tools used and disclosure -->

# Sensor Data Visualizations

This project generates synthetic temperature sensor data and saves a three-panel figure containing a scatter plot, histogram, and box plot for comparing two sensors.

## Installation

Activate the `ece105` conda environment, then install the required packages:

```bash
conda activate ece105
conda install numpy matplotlib
```

If you prefer `mamba`, the equivalent command is:

```bash
mamba activate ece105
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

The script generates synthetic data with NumPy, creates the plots, and saves the final figure as `sensor_analysis.png`.

## Example Output

The saved figure contains three plots:

- A scatter plot showing Sensor A and Sensor B temperature readings over time.
- An overlaid histogram comparing the temperature distributions of both sensors, with mean lines marked.
- A side-by-side box plot comparing the distributions and showing the overall mean across both sensors.

## AI Tools Used and Disclosure

Placeholder paragraph: describe any AI tools used to help write or revise this project, what they were used for, and what parts of the work were completed by you.