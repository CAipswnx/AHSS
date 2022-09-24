from flask import Flask
from flask_cors import *
from flask import request
from flask import jsonify
from app import app
from app.models.user_model import *

@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Hello!</h1>"

@app.route('/user/add', methods=['GET', 'POST'])
def addUser():
    nickname = request.values['nickname']
    email = request.values['email']
    account = request.values['account']
    password = request.values['password']
    phone = request.values['phone']
    return add_user(nickname, email, account, password, phone)
        

@app.route('/user/update', methods=['GET', 'POST'])
def updateUser():
    nickname = request.values['nickname']
    email = request.values['email']
    account = request.values['account']
    password = request.values['password']
    phone = request.values['phone']
    return update_user(nickname, email, account, password,phone)

@app.route('/user/remove', methods=['GET', 'POST'])
def removeUser():
    account = request.values['account'] 
    return delete_user(account)

@app.route('/user/login', methods=['GET', 'POST'])
def getUser():
    account = request.values['account'] 
    password = request.values['password'] 
    return get_user(account,password)

@app.route('/user/info', methods=['GET', 'POST'])
def getUserInfo():
    account = request.values['account'] 
    return get_user_info(account)
    
@app.route('/users/all', methods=['GET', 'POST'])
def getAllUsers():
    return get_all_user()

@app.route('/user/getSensor', methods=['GET', 'POST'])
def getUserSensor():
    account = request.values['account'] 
    return get_user_sensor(account)

@app.route('/sensor/updateUser', methods=['GET', 'POST'])
def updateUserSensor():
    sensor_id = request.values['sensor_id']
    account = request.values['account'] 
    return update_user_sensor(sensor_id,account)

@app.route('/test', methods=['GET', 'POST'])
def test():
    test = request.values['test']
    test1 = request.values['test1']
    if test == 'abc' and test1 == 'abd':
        return "OK"
    else:
        return "NO"
