from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import *

@routes.route('/', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if (not user or not user.check_password(password)):
            return "Invalid username or password"

        session['username'] = username
        session["link"] = None
        print(session['username'])

        return redirect(url_for('routes.dashboard'))
    return render_template('login.html')
@routes.route('/logout', methods=["POST", "GET"])
def logout():
    session.clear()
    
    # Redirect to the login page (replace 'login' with your actual login route)
    return redirect(url_for('routes.login'))
