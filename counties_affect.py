import pandas as pd
import matplotlib.pyplot as plt

def generate_counties_plot():
    df = pd.read_csv('static/California_Fire_Incidents.csv')
    plt.figure(figsize=(14,4))
    df.Counties.value_counts()[0:20].plot(kind='bar')
    plt.title('Top 20 affected Counties')
    plt.grid()
    plt.show()
    plt.close()
    # return plt.subplots()

