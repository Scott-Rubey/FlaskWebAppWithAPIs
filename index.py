from flask import render_template
from flask.views import MethodView
import gbmodel
import os

'''
Returns the default page for viewing the dive shop registry, along with
a dictionary of shop entries.
'''
class Index(MethodView):
    def get(self):
        #the Maps API key is passed to the template and used in the URL
        apiKey = os.environ['MAPSAPIKEY']
        model = gbmodel.get_model()
        entries = [dict(name=row[0], phone=row[1], address=row[2], website=row[3], classes=row[4], lat=row[5], lng=row[6], yelpURL=row[7]) for row in model.select()]

        return render_template('index.html',entries=entries, apiKey=apiKey)

