from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

#setting key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDrCRkJ8gsUbZlX2BxMje5ii9qd-kGkuQ8"

#initialize the extension
GoogleMaps(app)
