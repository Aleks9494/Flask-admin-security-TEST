from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config') #конфигурация настроек приложения из файла config.py
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app import views


