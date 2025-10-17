import sqlite3


def _average_diameter():
    connection = sqlite3.connect('db/asteroid_dataset.db')
    cursor = connection.cursor()


    cursor.execute('SELECT "Est Dia in KM(max)" FROM asteroids_')
    d_max = cursor.fetchall()
    cursor.execute('SELECT "Est Dia in KM(min)" FROM asteroids_')
    d_min = cursor.fetchall()
    connection.close()

    average_diameter = []
    for i in range(len(d_max)):
        average_diameter.append((float(d_max[i][0]) + float(d_min[i][0])) / 2)

    return average_diameter