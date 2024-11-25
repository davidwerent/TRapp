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


def check_auth_data(phone, password):
    cursor.execute('SELECT * FROM users WHERE phone=?', (phone,))
    user = cursor.fetchone()
    if user is None:
        response = {
            'status': 401,
            'message': 'Invalid credentials',
            'user': {}
        }
        return response
    if password == user[2]:
        response = {
            'status': 200,
            'message': 'Login successfull',
            'user': {
                'id': user[0],
                'phone': user[1],
                'firstname': user[3],
                'lastname': user[4],
                'flat': user[5]
            }
        }
        return response
    else:
        response = {
            'status': 401,
            'message': 'Invalid credentials',
            'user': {}
        }
        return response

#1 123382
def create_new_user(user_data):
    cursor.execute('SELECT phone FROM users WHERE phone =?', (user_data.phone,))
    user = cursor.fetchone()
    if user is not None:
        response = {
            'status': 1001,
            'message': 'User already exist',
            'user': {}
        }
        return response

    # 12
    cursor.execute('INSERT INTO users(phone, password, firstname, lastname, device_id, flat) VALUES (?,?,?,?,?,?)',
                   (user_data.phone, user_data.password, user_data.firstname, user_data.lastname, user_data.device_id, user_data.flat))
    conn.commit()
    last_id = cursor.lastrowid
    response = {
        'status': 200,
        'message': f'new user with ID={last_id} had been created!',
        'user':{
            'id': last_id
        }
    }
    return response



