import requests as rq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
import io

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

def generate_map_html():
    # Read the CSV file
    df = pd.read_csv('static/California_Fire_Incidents.csv')

    # Select the fire data
    df_select = df[df.Longitude < -115]
    df_select = df_select[(df_select.Latitude < 44) & (df_select.Latitude > 30)]

    zoom_factor = 5
    radius_scaling = 50

    # Create a Folium map
    my_map_1 = folium.Map(location=[36, -120], zoom_start=zoom_factor)

    # Add the fire data to the map
    for i in range(0, df_select.shape[0]):
        folium.Circle(
            location=[df_select.iloc[i]['Latitude'], df_select.iloc[i]['Longitude']],
            radius=np.sqrt(df_select.iloc[i]['AcresBurned']) * radius_scaling,
            color='red',
            popup='CanonicalUrl:' + df_select.iloc[i]['CanonicalUrl'] + ' - Year:' + str(
                int(df_select.iloc[i]['ArchiveYear'])) + ' - Acres Burned:'
                + str(df_select.iloc[i]['AcresBurned']),
            fill=True,
            fill_color='red'
        ).add_to(my_map_1)

    # Get the HTML string representation of the map
    map_html = my_map_1._repr_html_()

    return map_html

def generate_counties_plot():
    df = pd.read_csv('static/California_Fire_Incidents.csv')
    plt.figure(figsize=(14,4))
    df.Counties.value_counts()[0:20].plot(kind='bar')
    plt.title('Top 20 affected Counties')
    plt.grid()
    plt.show()
    plt.close()
    # return plt.subplots()

def generate_chart():
    # Read the CSV file
    df = pd.read_csv('static/California_Fire_Incidents.csv')
    acres_sum = df.groupby(by='ArchiveYear').AcresBurned.sum()

    #window
    plt.figure(figsize=(14, 4))
    plt.plot(acres_sum.index, acres_sum, color='red')
    plt.xlabel('Archive Year')
    plt.ylabel('AcresBurned')
    plt.title('Wildfire from 2013 to 2019')
    plt.grid()
    plt.show()
    plt.close()
