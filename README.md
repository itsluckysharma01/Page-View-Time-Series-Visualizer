# Page View Time Series Visualizer

This project analyzes and visualizes time series data using a line chart, bar chart, and box plots. The data represents the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.

## Features

- **Line Chart**: Visualizes daily freeCodeCamp forum page views over time
- **Bar Chart**: Shows average daily page views for each month grouped by year
- **Box Plots**: Displays year-wise and month-wise box plots showing trends and distribution

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn

## Installation

```bash
pip install pandas matplotlib seaborn
```

## Usage

Run the main script:

```bash
python main.py
```

This will generate three visualization files:

- `line_plot.png`
- `bar_plot.png`
- `box_plot.png`

## Project Structure

- `time_series_visualizer.py`: Main implementation file with visualization functions
- `main.py`: Entry point to run all visualizations
- `test_module.py`: Unit tests for the project

## Data

The project uses the `fcc-forum-pageviews.csv` dataset containing daily page view counts.
