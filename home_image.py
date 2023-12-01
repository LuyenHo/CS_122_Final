import requests as rq

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





