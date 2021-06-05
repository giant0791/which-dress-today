import requests

import geocodingAPI

from geocodingAPI.location import Location

class GeoCodingAPI:
    def __init__(self, location):
        self.location = location

    # Queries the OSM server to get lat and lon
    # Return a dictionary with lat and lon as keys
    # If the geo coordinates could not be found, the status key reports the error
    #
    # Intended use:
    # geo_cod_API = GeoCodingAPI(my_location)
    # if geo_cod_API.check_server_status():
    #     geo_coord = geo_cod_API.search()
    #     if geo_coord['status'] == 'ok':
    #         succesfully retrieved lat and lon for my-location
    #     else:
    #         something went wrong, geo_coord['status'] contains details
    # else:
    #     cannot contact server
    def search(self):
        # Initialize the result dict object
        geo_coord = {'lat': 'None', 'lon': 'None', 'status': 'Not valid'}
        
        # Initialize the parameters for the API call
        payload = self.request_url_payload()
        
        # Query the server for the geo coordinates
        r = requests.get('https://nominatim.openstreetmap.org/search', params=payload)
        geo_coord['status'] = r.status_code
        if r.ok:
            json_obj = r.json()
            geo_coord['lat'] = json_obj['lat']
            geo_coord['lon'] = json_obj['lon']

        return geo_coord

    # Construct the payload for the /search API
    # Helper method to enable unit testing (kind of introspection)
    def search_url_payload(self):    
        # Initialize the parameters for the API call
        payload = {}
        payload['street'] = self.location.street
        payload['city'] = self.location.city
        payload['country'] = self.location.country
        if self.location.has_postal_code():
            payload['postalcode'] = self.location.postal_code
        payload['format'] = 'json'
        payload['addressdetails'] = '1'
        payload['limit'] = '1'

        return payload


    # Checks the status of the nominatim server
    # In the first version, this method returns either True or False
    # In a later version, it can provide more detailed status info based on the
    # server returned json structure 
    def check_server_status(self):
        r = requests.get('https://nominatim.openstreetmap.org/status.php?format=json')
        return r.ok

    
        
