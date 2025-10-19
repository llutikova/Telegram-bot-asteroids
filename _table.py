import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

from top import top
from _diameter import _average_diameter
from _finding_id import _id_asteroids





def _draw_table(list_info):
    id_asteroid = []
    magnitude = []
    epoch = []
    v = []
    dist = []
    hazardous = []

    connection = sqlite3.connect("db/asteroid_dataset.db")
    cursor = connection.cursor()

    cursor.execute('''SELECT Diameter FROM average''')
    elements = cursor.fetchall()

    diameter = []
    for i in range(len(elements)):
        diameter.append(float(elements[i][0]))
    diameter = list(sorted(diameter, reverse=True))[:10]


    for i in range(len(list_info)):
        id_asteroid.append(list_info[i][0])
        magnitude.append(list_info[i][2])
        epoch.append(list_info[i][11])
        v.append(list_info[i][14])
        dist.append(list_info[i][18])
        hazardous.append(list_info[i][39])


    properties = {
        "ID": id_asteroid,
        "Absolute Magnitude": magnitude,
        "Average diameter in KM": diameter,
        "Epoch Date Close Approach": epoch,
        "Relative Velocity km per hr": v,
    }

    df = pd.DataFrame(properties)


    fig, ax = plt.subplots()
    ax.axis('off')
    t = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    t.scale(1.26, 2)

    plt.axis('off')

    plt.savefig('static/table.png')

_draw_table(top())

