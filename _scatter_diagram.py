from _diameter import _average_diameter
from _func_dist_earth import _dist_earth
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def _draw_scatter(_average_diameter, _dist_earth):

    data = {
        "Average diameter": _average_diameter,
        "Dist to Earth": _dist_earth
    }

    df = pd.DataFrame(data)

    plt.figure(figsize=(25, 19))
    plt.scatter(df["Dist to Earth"], df["Average diameter"], color='green', edgecolor='black')

    plt.xticks(ticks=np.arange(0, 50, 10), fontsize=0)
    plt.yticks(ticks=np.arange(0, 50, 10), fontsize=15)

    plt.xlabel("Dist to Earth", size = 30)
    plt.ylabel("Average diameter", size = 30)

    plt.savefig('static/graph.png')


_draw_scatter(_average_diameter(), _dist_earth())