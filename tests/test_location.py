import json
import unittest
import geocodingAPI

from geocodingAPI.location import Location
from geocodingAPI.geocodingAPI import GeoCodingAPI

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
        self.assertEqual(self.loc_wo_pc.street, '10+Downing Street')
        self.assertEqual(self.loc_wo_pc.city, 'London')
        self.assertEqual(self.loc_wo_pc.country, 'UK')
        self.assertFalse(self.loc_wo_pc.has_postal_code())
        
    def test_from_json_w_postcode(self):

        self.assertEqual(self.loc_w_pc.street, '10+Downing Street')
        self.assertEqual(self.loc_w_pc.city, 'London')
        self.assertEqual(self.loc_w_pc.country, 'UK')
        self.assertTrue(self.loc_w_pc.has_postal_code())
        self.assertEqual(self.loc_w_pc.postal_code,'SW1A 2AA')
        
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
       

if __name__ == '__main__':
    unittest.main()