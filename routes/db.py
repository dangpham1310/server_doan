from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    coin = db.Column(db.Integer, default = 0)
    reference = db.Column(db.String,default = None)
    inTravel = db.Column(db.Boolean,default = False)
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)



class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timer = db.Column(db.String,default = None)
    station_id = db.Column(db.String)
    station_name = db.Column(db.String)
    sensor_id = db.Column(db.String)
    sensor_value = db.Column(db.String)



class Config:
    SECRET_KEY = 'n9b9monkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///main.db'
    PERMANENT_SESSION_LIFETIME =  timedelta(days=30)