import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data')

    # Calculate line of best fit using all data
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    line_fit_all_data = [slope * year + intercept for year in years]
    plt.plot(years, line_fit_all_data, 'r', label='Best Fit Line (1880-2050)')

    # Calculate line of best fit using data from year 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line_fit_recent_data = [slope_recent * year + intercept_recent for year in range(2000, 2051)]  # Calculate line only for 2000-2050
    plt.plot(range(2000, 2051), line_fit_recent_data, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to generate and save the plot
draw_plot()
