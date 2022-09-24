import flask
from flask import request
from flask import jsonify
import sqlite3
import datetime

#insert
insert_user = 'INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)' 
insert_sensor_data = 'INSERT INTO sensors_data VALUES(?, ?, ?, ?, ?)'

#update
update_user = 'UPDATE users SET nickname=?, email=?, password=?, ud_time=?,phone=? WHERE account=?'
update_user_id = 'UPDATE sensors SET user_id=?,ud_time=? WHERE sensor_id=?'

#delete
delete_user = 'DELETE FROM users WHERE account=?'

#query
query_user_id = 'SELECT user_id FROM users WHERE account=?'
query_user_login = 'SELECT * FROM users WHERE account=? and password=?'
query_user_info = 'SELECT * FROM users WHERE account=?'
query_users = 'SELECT * FROM users'
query_sensor_info = 'SELECT * FROM sensors WHERE user_id=? '
query_sensor_infoN = 'SELECT * FROM sensors WHERE user_id IS NULL '

