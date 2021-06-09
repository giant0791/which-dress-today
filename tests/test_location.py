import json
import unittest
import datetime as dt
from pathlib import Path

import geocodingAPI

from geocodingAPI.location import Location
from geocodingAPI.geocodingAPI import GeoCoords, GeoCodingAPI
from weatherAPI.weatherdata import WeatherTimeSeries, WeatherTimeSeriesDataPoint, YR_DATETIME_FORMAT

FIXTURES_PATH = './tests/fixtures/'

class TestLocation(unittest.TestCase):
    def setUp(self):
        loc_wo_pc_json_str = '''
       {
            "street_name": "Downing Street",
            "house_no": "10",
            "city": "London",
            "country": "UK"
        }
        '''
        self.loc_wo_pc = Location.from_json(loc_wo_pc_json_str)
        loc_w_pc_json_str = '''
        {
            "street_name": "Downing Street",
            "house_no": "10",
            "city": "London",
            "country": "UK",
            "postal_code": "SW1A 2AA"
        }
        '''
        self.loc_w_pc = Location.from_json(loc_w_pc_json_str)

    def test_from_json_wo_postcode(self):
        self.assertEqual(self.loc_wo_pc.street, '10 Downing Street')
        self.assertEqual(self.loc_wo_pc.city, 'London')
        self.assertEqual(self.loc_wo_pc.country, 'UK')
        self.assertFalse(self.loc_wo_pc.has_postal_code())
        
    def test_from_json_w_postcode(self):

        self.assertEqual(self.loc_w_pc.street, '10 Downing Street')
        self.assertEqual(self.loc_w_pc.city, 'London')
        self.assertEqual(self.loc_w_pc.country, 'UK')
        self.assertTrue(self.loc_w_pc.has_postal_code())
        self.assertEqual(self.loc_w_pc.postal_code,'SW1A 2AA')
        

class TestWeatherTSDataPoint(unittest.TestCase):
    def setUp(self) -> None:
        # Read multiple test data from files
        fp = Path(FIXTURES_PATH).joinpath('time_series_1.json')
        time_series_1_json_str = fp.read_text()
        time_series_1_json_dict = json.loads(time_series_1_json_str)

        fp = Path(FIXTURES_PATH).joinpath('time_series_2.json')
        time_series_2_json_str = fp.read_text()
        time_series_2_json_dict = json.loads(time_series_2_json_str)

        
        # Parse the time series data point objects and create corresponing python objects
        self.time_series_1 = WeatherTimeSeriesDataPoint(
            dt.datetime.strptime(time_series_1_json_dict['time'], YR_DATETIME_FORMAT),
            time_series_1_json_dict['data']
        )

        self.time_series_2 = WeatherTimeSeriesDataPoint(
            dt.datetime.strptime(time_series_2_json_dict['time'], YR_DATETIME_FORMAT),
            time_series_2_json_dict['data']
        )

    def test_time_series_datapoint_1(self):
        # Check data fields consistency and availability
        details_items = self.time_series_1.get_instant_details()
        if details_items is None:
            print('FAILED: details_items expected not to be None')

        next_1_hr_details = self.time_series_1.get_next_1_hours_details()
        if next_1_hr_details is not None:
            print('FAILED: next_1_hr_details expected to be None')
            return

        next_6_hr_details = self.time_series_1.get_next_6_hours_details()
        if next_6_hr_details is not None:
            print('FAILED: next_6_hr_details expected to be None')
            return

        # Check data contents
        self.assertEquals(
            dt.datetime.strftime(self.time_series_1.get_time(), YR_DATETIME_FORMAT), 
            '2021-06-07T12:00:00Z'
        )

        self.assertEquals(details_items['air_pressure_at_sea_level'], 1020.0, 'air_pressure_at_sea_level: 1020.0')
        self.assertEquals(details_items['air_temperature'], 22.7, 'Expected air_temperature: 22.7')
        self.assertEquals(details_items['air_temperature_percentile_10'], 22.3, 'Expected air_temperature_percentile_10: 22.3')
        self.assertEquals(details_items['air_temperature_percentile_90'], 23.1)
        self.assertEquals(details_items['cloud_area_fraction'], 98.7)
        self.assertEquals(details_items['cloud_area_fraction_high'], 98.1)
        self.assertEquals(details_items['cloud_area_fraction_low'], 0.5)
        self.assertEquals(details_items['cloud_area_fraction_medium'], 48.8)
        self.assertEquals(details_items['dew_point_temperature'], 12.5)
        self.assertEquals(details_items['fog_area_fraction'], 0.0)
        self.assertEquals(details_items['relative_humidity'], 52.2)
        self.assertEquals(details_items['ultraviolet_index_clear_sky'], 4.8)    

    def test_time_series_datapoint_2(self):
        # Check data fields consistency and availability
        details_items = self.time_series_2.get_instant_details()
        if details_items is None:
            print('FAILED: details_items expected not to be None')

        next_1_hr_summary = self.time_series_2.get_next_1_hours_summary()
        if next_1_hr_summary is None:
            print('FAILED: next_1_hr_summary expected not to be None')
            return
        
        next_1_hr_details = self.time_series_2.get_next_1_hours_details()
        if next_1_hr_details is None:
            print('FAILED: next_1_hr_details expected not to be None')
            return

        next_6_hr_summary = self.time_series_2.get_next_6_hours_summary()
        if next_6_hr_summary is None:
            print('FAILED: next_6_hr_summary expected not to be None')
            return

        next_6_hr_details = self.time_series_2.get_next_6_hours_details()
        if next_6_hr_details is None:
            print('FAILED: next_6_hr_details expected not to be None')
            return

        next_12_hr_summary = self.time_series_2.get_next_12_hours_summary()
        if next_12_hr_summary is None:
            print('FAILED: next_12_hr_summary expected not to be None')
            return

        # Check data contents
        self.assertEquals(
            dt.datetime.strftime(self.time_series_2.get_time(), YR_DATETIME_FORMAT), 
            '2021-06-07T12:03:59Z'
        )

        self.assertEquals(next_1_hr_summary['symbol_code'], 'cloudy')
        self.assertEquals(next_6_hr_summary['symbol_code'], 'partlycloudy_day')
        self.assertEquals(next_12_hr_summary['symbol_code'], 'partlycloudy_day')
        self.assertEquals(next_12_hr_summary['symbol_confidence'], 'certain')

        self.assertEquals(details_items['air_pressure_at_sea_level'], 1020.0, 'air_pressure_at_sea_level: 1020.0')
        self.assertEquals(details_items['air_temperature'], 22.7, 'Expected air_temperature: 22.7')
        self.assertEquals(details_items['air_temperature_percentile_10'], 22.3, 'Expected air_temperature_percentile_10: 22.3')
        self.assertEquals(details_items['air_temperature_percentile_90'], 23.1)
        self.assertEquals(details_items['cloud_area_fraction'], 98.7)
        self.assertEquals(details_items['cloud_area_fraction_high'], 98.1)
        self.assertEquals(details_items['cloud_area_fraction_low'], 0.5)
        self.assertEquals(details_items['cloud_area_fraction_medium'], 48.8)
        self.assertEquals(details_items['dew_point_temperature'], 12.5)
        self.assertEquals(details_items['fog_area_fraction'], 0.0)
        self.assertEquals(details_items['relative_humidity'], 52.2)
        self.assertEquals(details_items['ultraviolet_index_clear_sky'], 4.8)

class TestWeatherTimeSeries(unittest.TestCase):
    def setUp(self) -> None:
        # Read multiple test data from files
        fp = Path('./tests/').joinpath('weather_data_time_series_testdata_1.json')
        time_series_1_json_str = fp.read_text()
        time_series_1_json_dict = json.loads(time_series_1_json_str)
        self.time_series_1 = WeatherTimeSeries(
            dt.datetime.strptime(time_series_1_json_dict['properties']['meta']['updated_at'], YR_DATETIME_FORMAT),
            list(time_series_1_json_dict['properties']['timeseries'])
        )

    def test_iter_through_time_series(self):
        print('\n')
        for data_point in self.time_series_1.get_time_series():
            print(data_point)

       
if __name__ == '__main__':
    unittest.main()