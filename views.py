
from flask import render_template
from app import app
from datetime import datetime
from flask import Flask, request, render_template_string

@app.route('/')
def home():
   return "hello world! fodase em dobro"

@app.route('/template')
def template():
    return render_template('home.html')
@app.route('/hora')
def hora():
    return str(datetime.now())

@app.route('/soma')
def sum(a,b):
	return a+b

app.run()

