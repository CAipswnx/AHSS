import datetime
import time
import sqlite3

conn = sqlite3.connect('ahss.db')
cursor = conn.cursor()
'''
insert_query = 'INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)'

users = []
localtime = datetime.datetime.now() + datetime.timedelta(hours = 8)

users.append((None, 'Gary', 'gary@gmail.com', 'AAA123', '123456',localtime))

cursor.executemany(insert_query, users)
'''

insert_query = 'INSERT INTO sensors VALUES(?, ?, ?, ?, ?)'

sensors = []
localtime = datetime.datetime.now() + datetime.timedelta(hours = 8)

sensors.append((None, 'GarySensor2', 'fun2', None,localtime))
sensors.append((None, 'GarySensor3', 'fun3', None,localtime))

cursor.executemany(insert_query, sensors)
conn.commit()
conn.close()