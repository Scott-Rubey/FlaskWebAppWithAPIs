"""
A flask app for creating a list (scuba) dive shops.
Users may view and enter new shops, see their location
on GoogleMaps, and access reviews via Yelp.
"""
import flask
from flask.views import MethodView
from index import Index
from submit import Submit

app = flask.Flask(__name__)       # our Flask app

#URL of the main index page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

#URL of the page that allows for submissions of new dive shops
app.add_url_rule('/submit/',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

