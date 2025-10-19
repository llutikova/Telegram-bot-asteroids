from _diameter import _average_diameter
from _func_dist_earth import _dist_earth

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def histogram(average_diameter, dist_earth):
    data = {
        "Average diameter": average_diameter,
        "Dist to Earth": dist_earth
    }
    df = pd.DataFrame(data)

    plt.figure(figsize=(14, 10))
    plt.hist(df["Average diameter"], color="limegreen", edgecolor="black")

    plt.xlabel("Average diameter")
    plt.ylabel("Dist to Earth")
    plt.title("Distribution of asteroids by size")

    plt.grid(axis="y", linestyle="--", alpha=1)
    plt.savefig('static/histogram.png')

histogram(_average_diameter(), _dist_earth())
