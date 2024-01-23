from flask import render_template, request
from . import routes
from .db import *
from routes.db import db
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password_field_random']
        user = User.query.filter_by(username=username).first()
        if user:
            return "register has been registered"
        user = User(username = username,password = password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return render_template('register.html' )

    return render_template('register.html')