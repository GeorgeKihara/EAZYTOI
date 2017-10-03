from flask import Flask, render_template, redirect
from datetime import datetime
from flask.ext.pymongo import PyMongo
app = Flask(__name__)


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