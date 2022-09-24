import sqlite3

conn = sqlite3.connect('ahss.db')
cursor = conn.cursor()

#cursor.execute('UPDATE sensors SET user_id=1 WHERE sensor_id=4')

conn.commit()
conn.close()
