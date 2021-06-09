from _typeshed import NoneType
import requests
import json
import datetime as dt
from typing import Dict

from geocodingAPI.geocodingAPI import Location, GeoCodingAPI, GeoCoords 

# User agent setting to access the METNO Weather API
USER_AGENT = 'which-dress-today-app/1.0 https://github.com/giant0791/which-dress-today' 
WEATHER_API_URL = ''
WEATHER_API_PARAMS = ''


# Class container for weather data
#
# Attributes
#   _is_valid: True if the instance contains meaningful data, False otherwise 
#
# Methods
#   is_valid(): Property, True if the instance contains meaningful data, False in error case
class WeatherData:
    def __init__(self, geo_coords: GeoCoords) -> None:
        self._geo_coords = geo_coords
        self._is_valid = False

    # Side effects: Initialize all weather data related attributes
 
    @property
    def is_valid(self):
        return self._is_valid

    
 

# Class for storing the data retrieved as a cache
#
# Attributes:
#   _cached_data (str): the retrieved data as json object
#   _updated_at (datetime): the time point of data retrieval from the weather data service
# 
# Methods:
#   expired(): True if cached data are outdated 
class WeatherDataCache:
    def __init__(self, cached_data, updated_at) -> None:
        self._cached_data = cached_data
        self._updated_at = updated_at

    def _parse_json_data(self) -> None:
        self._updated_at = self._weather_data_json['properties']['meta']['updated_at']

    def store_data(self, weather_data_json: dict) -> None:
        # It initializes the cached data with the newly retrieved data from the weather service
        # Weather data are passed as json dict
        self._weather_data_json = weather_data_json
        self._is_valid = True

        # Iterate through the timeseries and extract the forecast data
        return

# Central class to update weather data from a weather service data provider
# It caches the retrieved weather data for set location managing retrieval 
# according to the terms of service
#
# Attributes:
#   _geo_coding_api: proxy to the Geo coordinates service
#   _data: the retrieved weather data stored in the class cache
#   _meta_data: date/time of data update, used to managed cached data
#   _url: url of the weather service
#   -params: parameters for the weather service
#   -headers: headers for the weeather service
#
# Methods:
#   update_forecast(): get the weather forecast for the location 
class WeatherAPI:
    def __init__(self, location: Location) -> None:
        self._geo_coding_api = GeoCodingAPI(location=location)
        self._data = None
        self._url = WEATHER_API_URL
        self._params = WEATHER_API_PARAMS
        headers = {'User-Agent': USER_AGENT}
        self._headers = headers
        self._response = None

