from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import logging
import requests as req
import gbmodel
import os

class Submit(MethodView):
    def get(self):
        return render_template('submit.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        name = request.form['name']
        address = request.form['address']
        lat, lng = Submit.getCoords(self, address)
        yelpURL = Submit.getYelpURL(self, name, lat, lng)
        model = gbmodel.get_model()

        model.insert(request.form['name'], request.form['phone'], request.form['address'], request.form['website'], request.form['classes'], lat, lng, yelpURL)

        return redirect(url_for('index'))


    #get lat/lon coordinates for the address
    def getCoords(self, address):
        #default coordinates = Portland, OR
        latitude = 45.5051
        longitude = -122.6750
        apiKey = os.environ['MAPSAPIKEY']
        url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
            .format(address.replace(' ','+'), apiKey))

        try:
            res = req.get(url)
            data = res.json()
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
        except:
            logging.info('Cannot find address')

        return latitude, longitude

    #get the yelp ID number of the business using name and coordinates
    def getYelpURL(self, name, lat, lng):
        yelpID = None
        apiKey = os.environ['YELPAPIKEY']
        url = ('https://api.yelp.com/v3/businesses/search?term={}&latitude={}&longitude={}'
            .format(name.replace(' ','-'), lat, lng))

        try:
            res = req.get(url, headers={'Authorization': 'Bearer ' + apiKey})
            data = res.json()
            yelpURL = data['businesses'][0]['url']
        except:
            logging.info('Cannot get id')

        return yelpURL
