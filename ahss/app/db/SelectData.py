import sqlite3

conn = sqlite3.connect('ahss.db')
cursor = conn.cursor()
'''
for row in cursor.execute('SELECT * FROM sensors'):
    print(row)
for row in cursor.execute('SELECT * FROM users'):
    print(row)
'''
for row in cursor.execute('SELECT * FROM sensors_data order by ud_time desc limit 10'):
    print(row)
conn.commit()
conn.close()
