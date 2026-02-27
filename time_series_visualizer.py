import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def draw_line_plot():
    """
    Draw a line chart showing daily page views over time.
    
    Returns:
        matplotlib.figure.Figure: The line plot figure
    """
    # Import data (Make sure to parse dates. Consider setting index column to 'date'.)
    df = None

    # Clean data
    df = None

    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    
    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """
    Draw a bar chart showing average daily page views for each month grouped by year.
    
    Returns:
        matplotlib.figure.Figure: The bar plot figure
    """
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    
    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    """
    Draw box plots showing year-wise and month-wise trends.
    
    Returns:
        matplotlib.figure.Figure: The box plot figure
    """
    # Prepare data for box plots
    df_box = None
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise Box Plot (Trend)
    
    
    # Month-wise Box Plot (Seasonality)
    
    
    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
