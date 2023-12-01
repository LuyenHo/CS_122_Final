import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

def generate_chart():
    # Read the CSV file
    df = pd.read_csv('static/California_Fire_Incidents.csv')

    burned_data = list(df.AcresBurned)
    year_data = list(df.ArchiveYear)

    first_year = year_data[1]
    burn_list = []
    year_list = []

    burn_sum = 0
    for i in range(len(year_data)):
        if year_data[i] == first_year:
            if str(burned_data[i]) != 'nan':
                burn_sum += burned_data[i]
            else:
                burn_sum += 0
        else:
            burn_list.append(burn_sum)
            year_list.append(first_year)
            first_year +=1
            burn_sum = 0

    burn_list.append(burn_sum)
    year_list.append(first_year)

    
    # Make a new figure object
    fig, ax = plt.subplots(figsize=(16, 4))

    # Plot the time series
    ax.plot(year_list, burn_list, color='red')

    # Add labels to the data
    ax.set_xlabel('Year')
    ax.set_ylabel('Acres Burned')


    # Add gridlines
    ax.grid(True)

    # Show the plot
    ax.set_title('Wildfire from 2013 to 2019')

    image_path = 'static/chart.png'
    plt.show()
    fig.savefig(image_path)
    plt.close()
    
    return image_path