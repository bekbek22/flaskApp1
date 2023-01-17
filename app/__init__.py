from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '44eb67b04da4c223a6b6529533cf0b21fbd65e6bee4781a9'
app.config['JSON_AS_ASCII'] = False

from app import views  # noqa