import requests as rq
from bs4 import BeautifulSoup

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

def get_data():
    # define the url to the station
    url = 'https://www.kaggle.com/code/docxian/wildfires-geospatial-visualization-and-eda/input?select=California_Fire_Incidents.csv'

    data_file = 'statis/California_Fire_Incidents.csv'

    # use the requests module to get the data
    response = rq.get(url)

    # define an output name for the image
    # output_file = 'Buoy Image.jpg'

    # open the file as a writable binary
    with open(data_file, 'wb') as f:
        # iterate through the chunks and write to the file
        for chunk in response:
            f.write(chunk)

    return data_file
