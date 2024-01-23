from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import *
from datetime import datetime, timedelta


@routes.route('/sensor', methods=["POST"])
def sensor():
    if request.method == "POST":
        # timer = request.form['timer']
        station_id = request.form['station_id']
        station_name = request.form['station_name']
        sensor_id = request.form['sensor_id']
        sensor_value = request.form['sensor_value']
        #timer = get real time please
        timer = datetime.now().strftime("%H:%M %d/%m/%Y ")
        save =History(timer = timer,station_id=station_id, station_name=station_name, sensor_id=sensor_id, sensor_value=sensor_value)
        db.session.add(save)
        db.session.commit()
        print(station_id,station_name,sensor_id,sensor_value)
        return "OK"
    


@routes.route("/<station_id>/<station_name>", methods=["GET"])
def getData(station_id, station_name):
    if request.method == "GET":
        # Use .all() to get a list of all matching records
        result = History.query.filter_by(station_id=station_id, station_name=station_name).all()

        # Print each record in the result
        sensor_list = []
        
        for record in result:
            sensor_data = {
                "timer": record.timer,
                "sensor_id": record.sensor_id,
                "sensor_value": record.sensor_value
            }
            sensor_list.append(sensor_data)
            print(record.timer, record.station_id, record.station_name, record.sensor_id, record.sensor_value)

        dict_result = {"station_id":station_id,"station_name":station_name,"sensors":sensor_list}
        return jsonify(dict_result)