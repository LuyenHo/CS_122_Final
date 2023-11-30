import numpy as np
import pandas as pd
import folium
import io

def generate_map_html():
    # Read the CSV file
    df = pd.read_csv('California_Fire_Incidents.csv')

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
