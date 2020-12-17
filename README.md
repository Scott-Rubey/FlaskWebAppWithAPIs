# FlaskWebAppWithAPIs
A web-based Python/Flask application that utilizes GoogleMaps and Yelp APIs.  Created for educational purposes as part
of Internet, Web and Cloud course, Fall 2020.  The user may add info pertaining to a business (in this case, SCUBA diving
shops), including its name, address, phone number, website, etc.  The app includes functionality for obtaining latitude
and longitude coordiates via Google's Maps Embed API, which are used in order to open Maps locations and Yelp URL's (via 
information obtained via their associated APIs) in a separate tab.

The /gbmodel directory includes a template for back-end storage with implementations for Google's Datastore as well as 
local SQLite3 storage.  This app includes a Dockerfile so that it can be run using a Docker container; can be run locally 
using the container image, or via Google's Cloud Run.
