from flask import Flask
from flask_cors import *

app = Flask(__name__)
CORS(app, resources=r'/*')

# use controller
from app.controller import user_controller
from app.controller import sensor_controller
