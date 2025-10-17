import sqlite3


def top():
    connection = sqlite3.connect("db/asteroid_dataset.db")
    cursor = connection.cursor()

    cursor.execute('''SELECT Diameter FROM average''')
    elements = cursor.fetchall()

    diameter = []
    for i in range(len(elements)):
        diameter.append(float(elements[i][0]))
    diameter = list(sorted(diameter, reverse=True))[:10]

    names = []
    for i in range(len(diameter)):
        cursor.execute(f'SELECT * FROM average WHERE Diameter LIKE "{str(diameter[i])}"')
        names.append(cursor.fetchall()[0][0])
    # 0 2 11 14 18 39
    info = []
    for i in range(len(names)):
        cursor.execute(f'SELECT * FROM asteroids_ WHERE Name LIKE "{names[i]}"')
        info.append(cursor.fetchall()[0])

    return info


top()
#отсортировать список от дистанции и запросить из базы данных по этому значению все элементы
