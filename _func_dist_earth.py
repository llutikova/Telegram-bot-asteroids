import sqlite3


def _dist_earth():
    connection = sqlite3.connect('db/asteroid_dataset.db')
    cursor = connection.cursor()

    cursor.execute('SELECT "Miss Dist.(kilometers)" FROM asteroids_')
    dist = cursor.fetchall()
    connection.close()

    d_earth = []
    for d in dist:
        d_earth.append(d[0])

    return d_earth