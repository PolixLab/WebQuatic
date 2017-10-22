from flask import render_template
from app import app
from flask import request
from flask import Flask,redirect
import models


@app.route('/')
@app.route('/index')
def index():
 return render_template('index.html')
@app.route('/login')
def login():
 return render_template('login.html')
@app.route('/logged',methods=["POST"])
def loged():
 task = {
    'user': request.form['user'],
    'pass': request.form['passw'],
    }
 models.newuser(task)
 #redirect("/", code=302)
 return redirect("/", code=302)#render_template('index.html')

