import requests as rq
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import pandas as pd

def download_map():
    # define a url to the web page
    url = 'https://www.caliper.com/featured-maps/maptitude-california-fire.jpg'

    # use the requests package to read the page to a response
    response = rq.get(url)

    output_file = 'static/map.png'

    # enter your code here
    with open(output_file, 'wb') as f:
        # iterate through the chunks and write to the file
        for chunk in response:
            f.write(chunk)

    return output_file

def generate_chart():
    # Read the CSV file
    df = pd.read_csv('static/California_Fire_Incidents.csv')

    burned_data = df.columns[0][1:]
    year_data = df.columns[3][1:]

    first_year = year_data[1]
    burn_list = []
    year_list = []

    burn_sum = 0
    for i in range(len(year_data)):
        if year_data[i] == first_year:
            burn_sum += burned_data[i]
        else:
            burn_list.append(burn_sum)
            year_list.append(first_year)
            first_year +=1
            burn_sum = 0

    burn_list.append(burn_sum)
    year_list.append(first_year)

    fig = plt.subplots()
    # Make a new figure object
    fig.figure(figsize=(10, 4))  # Adjust figsize as needed for the plot size

    # Plot the time series
    fig.plot(year_list,burn_list, color='red')

    # Add labels to the data
    fig.xlabel('Year')
    fig.ylabel('Acres Burned')

    # plt.text(2020.3, 2500, '$\leftarrow$ Covid 19 Lockdown')

    # Add gridlines
    fig.grid(True)

    # Show the plot
    fig.title('Wildfire from 2013 to 2019')
    html_string = mpld3.fig_to_html(fig)
    return html_string



