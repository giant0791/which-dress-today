import json
import unittest
import geocodingAPI

from geocodingAPI.location import Location
from geocodingAPI.geocodingAPI import GeoCoords, GeoCodingAPI

class TestGeoCodingAPI(unittest.TestCase):
    def setUp(self):
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
        self.geo_coding = GeoCodingAPI(location=self.loc_w_pc)
   
    def test_search_url_request(self):
        url_payload = self.geo_coding.search_url_payload()
        self.assertEqual(url_payload['street'], self.loc_w_pc.street)
        self.assertEqual(url_payload['city'], self.loc_w_pc.city)
        self.assertEqual(url_payload['country'], self.loc_w_pc.country)
        self.assertEqual(url_payload['postalcode'], self.loc_w_pc.postal_code)
        self.assertEqual(url_payload['format'], 'json')
        self.assertEqual(url_payload['addressdetails'], '1')
        self.assertEqual(url_payload['limit'], '1')

    def test_check_server_status(self):
        self.assertTrue(self.geo_coding.check_server_status(), 'Nominatim server check failed')

    def test_search_deprecated(self):
        response = self.geo_coding.search_deprecated()
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['lat'], '51.50344025')
        self.assertEqual(response['lon'], '-0.12770820958562096')
    
    def test_search(self):
        response = self.geo_coding.search()
        self.assertEqual(response.city, 'London')
        self.assertEquals(response.lat, 51.50344025)
        self.assertEquals(response.lon, -0.12770820958562096)

if __name__ == '__main__':
    unittest.main()