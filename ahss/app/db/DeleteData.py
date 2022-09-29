import sqlite3

conn = sqlite3.connect('ahss.db')
cursor = conn.cursor()

#cursor.execute('DELETE FROM sensors ')

conn.commit()
conn.close()
