import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from _diameter import _average_diameter
from _func_dist_earth import _dist_earth
from matplotlib.colors import LinearSegmentedColormap

def visualize_asteroids(_average_diameter, _dist_earth):

    _average_diameter = np.array(_average_diameter)
    _dist_earth = np.array(_dist_earth)
    fig, ax = plt.subplots(figsize=(12, 8))

    min_size = _average_diameter.min()
    max_size = _average_diameter.max()
    point_sizes = 20 + 480 * 2 * (_average_diameter - min_size) / (max_size - min_size)

    colors = ['darkblue', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red']
    cmap = LinearSegmentedColormap.from_list('карта цветов', colors, N=256)

    scatter = ax.scatter(
        range(len(_average_diameter)),
        [0] * len(_average_diameter),
        s=point_sizes,
        c='blue',
        cmap=cmap,
        alpha=0.8,
        edgecolors='white',
        linewidth=1.5,
        zorder=3
    )

    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Dist to Earthи', fontsize=12)

    ax.set_title('Visualisation', fontsize=16, fontweight='bold')
    ax.set_xlabel('Average diameter', fontsize=12)
    ax.set_ylabel('')

    ax.set_yticks([])
    ax.grid(True, alpha=0.3)


    plt.savefig('static/hazardous.png')

visualize_asteroids(_average_diameter(), _dist_earth())