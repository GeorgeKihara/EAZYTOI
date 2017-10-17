from flask import Flask, render_template, redirect
from datetime import datetime
from app import app
from flask_pymongo import PyMongo
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

GoogleMaps(app)

#connections to the mongo database
app.config['MONGO_DBNAME'] = 'bktlist'
app.config['MONGO_URI'] = 'mongodb://kihara:kihara@ds151752.mlab.com:51752/bktlist'

mongo = PyMongo(app)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y")

    return """
    <h1 style="text-align:center;">Welcome to EAZYTOI</h1>
    <p>It is currently {time}.</p>

    """.format(time=the_time)
@app.route('/index')
def index():
    #creating a map
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon':'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat':37.4300,
                'lng':-122.1419,
                'infobox':"<b>Here is eazytoi map</b>"
            }
        ]
    )

    return render_template('index.html', mymap=mymap, sndmap=sndmap)    

if  __name__ == '__main__':
    app.secret_key='mysecret'
    app.run(debug=True)
    
	