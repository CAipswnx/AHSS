from flask import Flask
from flask_cors import *
from flask import request
from flask import jsonify
from app import app
from app.models.sensor_model import *

@app.route('/test1', methods=['GET', 'POST'])
def test1():
    test = request.values['test']
    test1 = request.values['test1']
    if test == 'abc' and test1 == 'abd':
        return "OK"
    else:
        return "NO"

@app.route('/sensor/addData', methods=['GET', 'POST'])
def addsensorData():
    sensor_name = request.values['sensor_name']
    sensor_type = request.values['sensor_type']
    temperature = request.values['temperature']
    humidity = request.values['humidity']
    dba = request.values['dba']
    return add_sensor_data(sensor_name,sensor_type,temperature,humidity,dba)

@app.route('/sensor/getRealData', methods=['GET', 'POST'])
def getRealData():
    account = request.values['account']
    sensor_name = request.values['sensor_name']
    return get_real_data(account,sensor_name)

@app.route('/sensor/getHisData', methods=['GET', 'POST'])
def getHisData():
    account = request.values['account']
    sensor_name = request.values['sensor_name']
    return get_his_data(account,sensor_name)

@app.route('/sensor/updateMusic', methods=['GET', 'POST'])
def updateMusic():
    account = request.values['account']
    sensor_name = request.values['sensor_name']
    music = request.values['music']
    return update_music(account,sensor_name,music)
