from flask import Flask, render_template, redirect
from datetime import datetime
from flask_pymongo import PyMongo
app = Flask(__name__)

#connections to the mongo database
app.config['MONGO_DBNAME'] = 'bktlist'
app.config['MONGO_URI'] = 'mongodb://kihara:kihara@ds151752.mlab.com:51752/bktlist'

mongo = PyMongo(app)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1 style="text-align:center;">Welcome to EAZYTOI</h1>
    <p>It is currently {time}.</p>

    """.format(time=the_time)
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8000)