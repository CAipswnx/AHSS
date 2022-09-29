import flask
from flask import request
from flask import jsonify
import sqlite3
import datetime

#insert
insert_sensor = 'INSERT INTO sensors VALUES(?, ?, ?, ?, ?, ?)'
insert_sensor_data = 'INSERT INTO sensors_data VALUES(?, ?, ?, ?, ?, ?)'

#update
update_music_data = 'UPDATE sensors SET music=?,ud_time=? WHERE sensor_id=?'

#delete

#query
query_sensor = 'SELECT sensor_id,music FROM sensors WHERE sensor_name=? and sensor_type=?'
query_user_id = 'SELECT user_id FROM users WHERE account=?'
query_sensor_id = 'SELECT sensor_id FROM sensors WHERE sensor_name=? and user_id=?'
query_real_data = 'SELECT * FROM sensors_data WHERE sensor_id=? ORDER BY ud_time DESC LIMIT 10'

