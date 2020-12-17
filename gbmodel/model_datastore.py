# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
A flask app for adding and viewing scuba dive shops, seeing them on a map,
and reading reviews via Yelp.  Data is stored in a Google datastore back-end 
that looks something like the following:

----------------------------------------------------------------------
| Name: Under Water Works                                            |
| Phone: 503-620-6993                                                |
| Address: 12170 SW Main St, Tigard, OR  97223                       |
| Website: uwwscuba.com                                              |
| Classes: yes                                                       |
| Lat: 45.5051                                                       |
| Lng: -122.6750                                                     |
| YelpURL: https://www.yelp.com/biz/under-water-works-portland-2?    |
|          adjust_creative=8FiozUVzkMct3q85V5RATw&utm_campaign=      |
|          yelp_api_v3&utm_medium=api_v3_business_search&utm_source= |
|          8FiozUVzkMct3q85V5RATw                                    |
----------------------------------------------------------------------
'''

from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, phone, address, website, classes, lat, lng, yelpURL ]
    where each argument is a Python string
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['phone'],entity['address'],entity['website'],entity['classes'],entity['lat'],entity['lng'],entity['yelpURL']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-f20-scott-rubey-scrubey')

    def select(self):
        """
        Gets all entities from the database
        Each entity contains: name, phone, address, website, classes
        :return: List of lists containing all entities from database
        """
        query = self.client.query(kind = 'testFinal')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,name,phone,address,website,classes,lat,lng,yelpURL):
        '''
        Inserts entry into database
        :param name: String
        :param phone: String
        :param address: String
        :param website: String
        :param classes: String
        :param lat: String
        :param lng: String
        :param yelpURL: String
        :return: True
        '''
        key = self.client.key('testFinal')
        rev = datastore.Entity(key)
        rev.update( {
            'name': name,
            'phone' : phone,
            'address': address,
            'website': website,
            'classes' : classes,
            'lat': lat,
            'lng': lng,
            'yelpURL': yelpURL
            })
        self.client.put(rev)
        return True

