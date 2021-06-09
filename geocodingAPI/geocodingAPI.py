import requests
from typing import Optional

from geocodingAPI.location import Location

class GeoCoords:
    """Holds data for a geo coordinates.
       Invalid coordinates have city = '#UNDEF#'

    Attributes:
        city: Name of the city
        lat (float): Latitude 
        lon (float): Longitude 
        alt (int): Altitude, optional
    """
    def __init__(self, city: str, lat: float, lon: float, alt: Optional[int] = None):
        self._city = city
        self._lat = lat
        self._lon = lon
        if alt is not None:
            self._alt = int(round(alt,0))
        else:
            self._alt = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def lat(self):
        return self._lat
    
    @lat.setter
    def lat(self, lat):
        self._lat = lat

    @property
    def lon(self):
        return self._lon
    
    @lon.setter
    def lon(self, lon):
        self._lon = lon

    @property
    def alt(self):
        return self._alt
    
    @alt.setter
    def alt(self, alt):
        self._alt = alt
    
    def __repr__(self) -> str:
        return (
            f"GeoCoords({self._city}, {self._lat}, {self._lon}, "
            + f"alt={self._alt})"
        )

class GeoCodingAPI:
    def __init__(self, location: Location):
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
    def search_deprecated(self):
        # Initialize the result dict object
        geo_coord = {'lat': 'None', 'lon': 'None', 'status': 'Not valid'}
        
        # Initialize the parameters for the API call
        payload = self.search_url_payload()
        
        # Query the server for the geo coordinates
        r = requests.get('https://nominatim.openstreetmap.org/search', params=payload)
        geo_coord['status'] = r.status_code
        if r.ok:
            # REMEMBER: 
            #   Nominatim returns a list of 1 json objects, thus double indeces
            r_dict = r.json()
            geo_coord['lat'] = r_dict[0]['lat']
            geo_coord['lon'] = r_dict[0]['lon']

        return geo_coord

    # Improved version with better data model design of the search() methon
    def search(self) -> GeoCoords:
        
        # Initialize the geo coord object
        geo_coord = GeoCoords('#UNDEF#', 0.0, 0.0)
        print(geo_coord)
        
        # Initialize the parameters for the API call
        payload = self.search_url_payload()
        
        # Query the server for the geo coordinates
        r = requests.get('https://nominatim.openstreetmap.org/search', params=payload)
        if r.ok:
            # REMEMBER: 
            #   Nominatim returns a list of 1 json objects, thus double indeces
            r_dict = r.json()
            geo_coord.city = self.location.city
            geo_coord.lat = float(r_dict[0]['lat'])
            geo_coord.lon = float(r_dict[0]['lon'])

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

    
        
