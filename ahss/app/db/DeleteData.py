import sqlite3

conn = sqlite3.connect('ahss.db')
cursor = conn.cursor()

#cursor.execute('DELETE FROM sensors WHERE sensor_id=4')

conn.commit()
conn.close()
