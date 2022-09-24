import sqlite3

conn = sqlite3.connect('ahss.db')

cursor = conn.cursor()

#cursor.execute('ALTER TABLE users ADD phone VARCHAR(20)')
#cursor.execute('ALTER TABLE sensors_data ADD dba FLOAT')
#cursor.execute('ALTER TABLE sensors ADD music VARCHAR(20)')
conn.commit()

conn.close()