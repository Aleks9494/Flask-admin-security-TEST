from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #конфигурация настроек приложения из файла config.py
db = SQLAlchemy(app)

from app import views


