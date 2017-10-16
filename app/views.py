from flask import Flask, render_template, redirect
from datetime import datetime
from flask_pymongo import PyMongo
from app import app
import bcrypt, json, requests, bson.binary

#connections to the mongo database
app.config['MONGO_DBNAME'] = 'bktlist'
app.config['MONGO_URI'] = 'mongodb://kihara:kihara@ds151752.mlab.com:51752/bktlist'

mongo = PyMongo(app)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime('%A, %Y-%m-%d')

    return """
    <h1 style="text-align:center;">Welcome to EAZYTOI</h1>
    <p>It is currently {time}.</p>

    """.format(time=the_time)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/react')
def react():
    return render_template('react.html')

if  __name__ == '__main__':
    app.secret_key='mysecret'
    app.run(debug=True)