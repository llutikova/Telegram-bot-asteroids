import sqlite3


def _id_asteroids():
    connection = sqlite3.connect('db/asteroid_dataset.db')
    cursor = connection.cursor()

    cursor.execute('SELECT "Neo Reference ID" FROM asteroids_')
    id_ref = cursor.fetchall()
    connection.close()

    id_asteroids = []
    for elem in id_ref:
        id_asteroids.append(elem[0])

    return id_asteroids