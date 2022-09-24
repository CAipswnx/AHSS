import flask
from flask import request
from flask import jsonify
import sqlite3
import datetime
from app.sql.user_sql import *

#新增使用者
def add_user(nickname, email,account, password,phone):
    update_time = datetime.datetime.now() + datetime.timedelta(hours = 8)
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result = cursor.execute(query_user_info, (account,)).fetchone()
    if result is None:
        cursor.execute(insert_user, (None, nickname, email, account, password, update_time,phone)) #執行SQL
    else:
        return "Error: account is exist!"
    conn.commit()
    conn.close()
    return "Add the user successfully!"

#修改使用者資料
def update_user(name, email, account, password,phone):
    update_time = datetime.datetime.now() + datetime.timedelta(hours = 8)
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    cursor.execute(update_user, (name, email, password, update_time, phone, account)) #執行SQL
    conn.commit()
    conn.close()
    return "Update the user successfully!"

#刪除使用者資料
def delete_user(account):
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    cursor.execute(delete_user, (account,)) #執行SQL
    conn.commit()
    conn.close()
    return "Remove the user successfully!"

#使用者登入
def get_user(account,password):
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result = cursor.execute(query_user_login, (account, password)).fetchone() #執行SQL
    if result is None:
        return "Error: account is not exist!"
    conn.close()
    return "login in"

#取得使用者資料
def get_user_info(account):
    users =[]
    sensors =[]
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result = cursor.execute(query_user_info, (account,)).fetchone() #執行SQL
    if result is None:
        return "Error: account is not exist!"
    user = {'nickname':result[1],'email':result[2],'phone':result[6]}
    users.append(user)
    conn.close()
    return user

#取得所有使用者資料
def get_all_user():
    users = {}
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    for item in cursor.execute(query_users):
        user = {'nickname': item[1], 'email': item[2],'account':item[3], 'password': item[4]};
        users.update({item[0]:user})
    conn.close()
    return users

#取得使用者已綁定sensor及未綁定sensor
def get_user_sensor(account):
    sensors = []
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result_user_id = cursor.execute(query_user_id, (account,)).fetchone() #執行SQL
    if result_user_id is None:
        return "Error: account is not exist!"
    for item in cursor.execute(query_sensor_info, (result_user_id[0],)): 
        sensor = {'status':'Y', 'sensor_id':item[0], 'sensor_name': item[1], 'sensor_type': item[2],'user_id':item[3]};
        sensors.append(sensor)
    for item in cursor.execute(query_sensor_infoN):
        sensor = {'status':'N', 'sensor_id':item[0], 'sensor_name': item[1], 'sensor_type': item[2],'user_id':item[3]};
        sensors.append(sensor)
    conn.close()
    return sensors

#sensor綁定使用者
def update_user_sensor(sensor_id, account):
    update_time = datetime.datetime.now() + datetime.timedelta(hours = 8)
    conn = sqlite3.connect('app/db/ahss.db')
    cursor = conn.cursor()
    result_user_id = cursor.execute(query_user_id, (account,)).fetchone() #執行SQL
    if result_user_id is None:
        return "account is not exist!"
    cursor.execute(update_user_id, (result_user_id[0],update_time, sensor_id)) #執行SQL
    conn.commit()
    conn.close()
    return "Update the sensor successfully!"

