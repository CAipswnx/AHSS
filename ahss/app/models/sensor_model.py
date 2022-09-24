import flask
from flask import request
from flask import jsonify
import sqlite3
import datetime
import pandas as pd
import numpy as np
from app.sql.sensor_sql import *

#新增感測資料
def add_sensor_data(sensor_name, sensor_type,temperature,humidity,dba):
    update_time = datetime.datetime.now() + datetime.timedelta(hours = 8)
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    sensor = cursor.execute(query_sensor, (sensor_name,sensor_type)).fetchone()
    if sensor is None:
        cursor.execute(insert_sensor, (None, sensor_name, sensor_type, None, update_time, None))
        sensor = result_sensor(sensor_name,sensor_type)
    sensor_id = sensor[0]
    music = sensor[1]
    cursor.execute(insert_sensor_data, (None, sensor_id, temperature, humidity, update_time, dba))
    result = ""
    if music is None:       
        result = "add sensor data successfully!"
    else:
        cursor.execute(update_music_data, (update_time, None, sensor_id))
        result = "music=" + music
    conn.commit()
    conn.close()
    return result

def get_real_data(account, sensor_name):
    real_datas = []
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result_user_id = cursor.execute(query_user_id, (account,)).fetchone()
    if result_user_id is None:
        return "Error: account is not exist!"
    result_sensor_id = cursor.execute(query_sensor_id, (sensor_name, result_user_id[0])).fetchone()
    if result_sensor_id is None:
        return "Error:" + sensor_name + " is not exist!"
    result_real_data = cursor.execute(query_real_data, (result_sensor_id[0],))
    for item in result_real_data: 
        real_data = {'temperature':item[2],'humidity':item[3],'dba':item[5],'update_time':item[4]}
        real_datas.append(real_data)
    conn.close()
    return real_datas

def get_his_data(account, sensor_name):
    dali = pd.read_json('dali.json')
    return dali

def update_music(account, sensor_name, music):
    update_time = datetime.datetime.now() + datetime.timedelta(hours = 8)
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result_user_id = cursor.execute(query_user_id, (account,)).fetchone()
    if result_user_id is None:
        return "Error: account is not exist!"
    result_sensor_id = cursor.execute(query_sensor_id, (sensor_name, result_user_id[0])).fetchone()
    if result_sensor_id is None:
        return "Error:" + sensor_name + " is not exist!"
    if music == 'bb.q':
        cursor.execute(update_music_data, ('bbq', update_time, result_sensor_id[0]))
    else:
        cursor.execute(update_music_data, (music, update_time, result_sensor_id[0]))
    return "music update successfully!"