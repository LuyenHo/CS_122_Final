import numpy as np
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

def generate_chart():
    # Read the CSV file
    df = pd.read_csv('static/California_Fire_Incidents.csv')
    acres_sum = df.groupby(by='ArchiveYear').AcresBurned.sum()

    # plot Acres Burned vs Year
    # fig, ax = plt.subplots(figsize=(16, 4))
    # ax.plot(acres_sum.index, acres_sum, color='red')
    # ax.set_xlabel('Archive Year')
    # ax.set_ylabel('Acres Burned')
    # plt.ylabel('AcresBurned')
    # ax.grid(True)
    # ax.set_title('Wildfire from 2013 to 2019')
    # image_path = 'static/chart.png'
    # fig.savefig(image_path)

    #window
    plt.figure(figsize=(16, 4))
    plt.plot(acres_sum.index, acres_sum, color='red')
    plt.xlabel('Archive Year')
    plt.ylabel('AcresBurned')
    plt.title('Wildfire from 2013 to 2019')
    plt.grid()
    plt.show()
    
    plt.close()
    # return image_path