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


def get_calendar(show_free_slot=True):
    cursor.execute('SELECT * FROM calendar')
    events = cursor.fetchall()
    [print(event) for event in events]
    records = []
    if show_free_slot:
        for event in events:
            is_free = bool(event[8])
            if not is_free:
                break
            id = event[0]
            title = 'СВОБОДНО'
            duration = event[2]
            try:
                timestamp = int(event[3])
                start = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%dT%H:%M:%Sz')
                timestamp = int(event[4])
                created_at = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%dT%H:%M:%SZ')
                timestamp = int(event[5])
                updated_at = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                start = event[3]
                created_at = event[4]
                updated_at = event[5]
            subtitle = '5000 руб'
            res = {
                'id': id,
                'title': title,
                'subtitle': subtitle,
                'duration': duration,
                'start_date': start,
                'created_at': created_at,
                'updated_at': updated_at
            }
            records.append(res)
    else:
        for event in events:
            is_free = bool(event[8])
            if is_free:
                continue
            id = event[0]
            title = event[1]
            duration = event[2]
            try:
                timestamp = int(event[3])
                start = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%dT%H:%M:%SZ')
                timestamp = int(event[4])
                created_at = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%dT%H:%M:%SZ')
                timestamp = int(event[5])
                updated_at = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                start = event[3]
                created_at = event[4]
                updated_at = event[5]

            subtitle = event[7]
            res = {
                'id': id,
                'title': title,
                'subtitle': subtitle,
                'duration': duration,
                'start_date': start,
                'created_at': created_at,
                'updated_at': updated_at
            }
            records.append(res)
    print(records)
    return records


get_calendar(show_free_slot=False)
