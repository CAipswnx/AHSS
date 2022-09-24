import sqlite3

conn = sqlite3.connect('ahss.db')

cursor = conn.cursor()
'''
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('CREATE TABLE IF NOT EXISTS users('
               'user_id INTEGER PRIMARY KEY, '
               'nickname VARCHAR(20), '
               'email VARCHAR(40), '
               'account VARCHAR(20),'
               'password VARCHAR(20),'
               'ud_time TIMESTAMP)')

conn.commit()
'''
'''
cursor.execute('DROP TABLE IF EXISTS sensors')
cursor.execute('CREATE TABLE IF NOT EXISTS sensors('
               'sensor_id INTEGER PRIMARY KEY, '
               'sensor_name VARCHAR(20), '
               'sensor_type VARCHAR(20), '
               'user_id INTEGER, '
               'ud_time TIMESTAMP)')

conn.commit()
'''
'''
cursor.execute('DROP TABLE IF EXISTS sensors_data')
cursor.execute('CREATE TABLE IF NOT EXISTS sensors_data('
               'id INTEGER PRIMARY KEY, '
               'sensor_id INTEGER, '
               'temperature FLOAT, '
               'humidity FLOAT,'
               'ud_time TIMESTAMP)')

conn.commit()
'''
conn.close()