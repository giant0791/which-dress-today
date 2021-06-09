import json
import datetime as dt

YR_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

# Class modelling a single time series data point of weather data
# Data points have the following structure:
# {
#    "time":"2021-06-07T12:00:00Z",
#    "data":{}
# }
# 
# Assuming dp_json_str contains the json str of object, 
# proper WeatherTimeSeriesDataPoint object init is as follows:
#
#   data_point = WeatherTimeSeriesDataPoint(
#       dt.datetime.strptime(dp_2_json_dict['time'], YR_DATETIME_FORMAT),
#       dp_json_dict['data']
#   )
#
#
# Attributes:
#   _data_point (dict): weather data corresponding to the data point of the time series
# 
# Methods:
#   get_time (datetime): the timestamp of the field "time"
#   get_instant_details(dict): the contents of the field "details" in the "instant" object
#   get_next_1_hours_details (dict): the contents of the field "details" in the "next_1_hours" object
class WeatherTimeSeriesDataPoint:
    def __init__(self, time: dt.datetime, data_point: dict) -> None:
        self._time = time
        self._data_point = data_point

    def get_time(self) -> dt.datetime:
        return self._time
    
    def get_instant_details(self):
        instant_details = None
        if 'instant' in self._data_point:
            if 'details' in self._data_point['instant']:
                instant_details = dict(self._data_point['instant']['details'])
        
        return instant_details
    
    def get_next_1_hours_details(self):
        next_1_hours_details = None
        if 'next_1_hours' in self._data_point:
            if 'details' in self._data_point['next_1_hours']:
                next_1_hours_details = dict(self._data_point['next_1_hours']['details'])
        
        return next_1_hours_details

    def get_next_1_hours_summary(self):
        next_1_hours_summary = None
        if 'next_1_hours' in self._data_point:
            if 'summary' in self._data_point['next_1_hours']:
                next_1_hours_summary = dict(self._data_point['next_1_hours']['summary'])
        
        return next_1_hours_summary

    def get_next_6_hours_details(self):
        next_6_hours_details = None
        if 'next_6_hours' in self._data_point:
            next_6_hours_details = dict(self._data_point['next_6_hours']['details'])
        
        return next_6_hours_details       

    def get_next_6_hours_summary(self):
        next_6_hours_summary = None
        if 'next_6_hours' in self._data_point:
            if 'summary' in self._data_point['next_6_hours']:
                next_6_hours_summary = dict(self._data_point['next_6_hours']['summary'])
        
        return next_6_hours_summary       

    def get_next_12_hours_details(self):
        next_12_hours_details = None
        if 'next_12_hours' in self._data_point:
            next_12_hours_details = dict(self._data_point['next_12_hours']['details'])
        
        return next_12_hours_details       

    def get_next_12_hours_summary(self):
        next_12_hours_summary = None
        if 'next_12_hours' in self._data_point:
            if 'summary' in self._data_point['next_12_hours']:
                next_12_hours_summary = dict(self._data_point['next_12_hours']['summary'])
        
        return next_12_hours_summary       

# Class modelling a list of time series data point of weather data
# This class is iterable
# 
# Attributes:
#   _updated_at (datetime): timestamp of the weather data
#   _ts_list (list): time series list of all data points
#    
class WeatherTimeSeries:
    def __init__(
        self,
        updated_at: dt.datetime, 
        ts_list: list
    ) -> None:
        self._updated_at = updated_at
        self._ts_list = ts_list

    def get_updated_at(self) -> dt.datetime:
        return self._updated_at

    def get_time_series(self) -> list:
        return self._ts_list

    def get_time_series_at(self, time: dt.datetime) -> WeatherTimeSeriesDataPoint:
        returned_dp = None
        for dp in self._ts_list:
            if time == dp.get_time():
                returned_dp = dp

        return returned_dp


    
        
 
