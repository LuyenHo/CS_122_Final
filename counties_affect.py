import pandas as pd
import matplotlib.pyplot as plt

def generate_counties_plot():
    df = pd.read_csv('static/California_Fire_Incidents.csv')
    fig, ax = plt.subplots(figsize=(16,4))
    df.Counties.value_counts()[0:20].plot(kind='bar')
    ax.set_title('Top 20 affected Counties')
    ax.grid()
    image_path = 'static/country_affect.png'
    plt.show()
    plt.close()
    fig.savefig(image_path)
    return image_path

