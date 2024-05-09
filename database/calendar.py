import sqlite3
from sys import platform
from datetime import date, datetime, timedelta

import os

# Определение абсолютного пути до корневой папки проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

if platform == 'darwin':
    db_name = os.path.join(ROOT_DIR, 'database.sqlite')
else:
    db_name = os.path.join(ROOT_DIR, 'database.sqlite')

conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def print_database():
    cursor.execute('SELECT * FROM calendar')
    print(cursor.fetchall())


def get_calendar():
    cursor.execute('SELECT * FROM calendar')
    events = cursor.fetchall()
    [print(event) for event in events]
    records = []
    for event in events:
        id = event[0]
        title = event[1]
        duration = event[2]
        start = event[3]
        created_at = event[4]
        updated_at = event[5]

        res = {
            'id': id,
            'title': title,
            'duration': duration,
            'start_date': start,
            'created_at': created_at,
            'updated_at': updated_at
        }
        records.append(res)
    print(records)
    return records


get_calendar()
