'''
Template class for the back-end model.  May be implemented
according to whatever database model meets the developer's
needs.  (In the current project, we will use Datastore)
'''

class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, phone, address, website, classes, lat, lng, yelpURL):
        """
        Inserts entry into database
        :param name: String
        :param phone: String
        :param address: String
        :param website: String
        :param classes: String
        :param lat: String
        :param lng: String
        :param yelpURL: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

