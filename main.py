import time_series_visualizer
from unittest import main


# Draw all plots
print("Drawing line plot...")
time_series_visualizer.draw_line_plot()

print("Drawing bar plot...")
time_series_visualizer.draw_bar_plot()

print("Drawing box plot...")
time_series_visualizer.draw_box_plot()

print("\nAll visualizations have been generated successfully!")
print("Check the following files:")
print("  - line_plot.png")
print("  - bar_plot.png")
print("  - box_plot.png")

# Run unit tests automatically
print("\n" + "="*50)
print("Running tests...")
print("="*50)
main(module='test_module', exit=False)
