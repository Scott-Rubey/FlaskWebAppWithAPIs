"""
A flask app for adding and viewing charities and social services.
Data is stored in a SQLite database that looks something like the following:

----------------------------------------------------------------------
| Name: Central City Concern                                         |
| Category: Homeless services                                        |
| Address: 1234 Fake St., Portland, OR  97201                        |
| Rating: 4                                                          |
| Phone Number: 503-111-1111                                         |
| Hours of Operation: 8am - 7pm                                      |
| Reviews: A great organization with many services.                  |
----------------------------------------------------------------------

This can be created with the following SQL (see bottom of this file):

    create table services (name text, category varchar, address text, rating int, phone varchar, hours varchar, reviews text);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'diveshops.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists; create new table if not present
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from diveshops")
        except sqlite3.OperationalError:
            cursor.execute("create table diveshops (name text, phone text, address text, website text, classes text, lat text, lng text, yelpURL text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, category, address, rating, phone number, hours of operation, reviews
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM diveshops")
        return cursor.fetchall()

    def insert(self, name, phone, address, website, classes, lat, lng, yelpURL):
        """
        Inserts entry into database
        :param name: String
        :param phone: String
        :param address: String
        :param website: String
        :param classes: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'phone':phone, 'address':address, 'website':website, 'classes':classes, 'lat':lat, 'lng':lng, 'yelpURL': yelpURL}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into diveshops (name, phone, address, website, classes, lat, lng, yelpURL) VALUES (:name, :phone, :address, :website, :classes, :lat, :lng, :yelpURL)", params)

        connection.commit()
        cursor.close()
        return True
