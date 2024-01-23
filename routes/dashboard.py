from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import User
from routes.db import *

@routes.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    if request.method == 'POST':
        pass

    

