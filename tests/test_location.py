import unittest
import geocodingAPI

from geocodingAPI.location import Location

class TestLocation(unittest.TestCase):
    
    def test_init_wo_postal_code(self):
        loc_wo_postal_code = Location('10 Downing Street','London','United Kingdom')
        self.assertEqual(loc_wo_postal_code.street,'10 Downing Street')
        self.assertEqual(loc_wo_postal_code.city,'London')
        self.assertEqual(loc_wo_postal_code.country,'United Kingdom')

    def test_init_w_postal_code(self):
        loc_w_postal_code = Location('10 Downing Street','London','United Kingdom', 'SW1A 2AA')
        self.assertEqual(loc_w_postal_code.street, '10 Downing Street')
        self.assertEqual(loc_w_postal_code.city,'London')
        self.assertEqual(loc_w_postal_code.country,'United Kingdom')
        self.assertEqual(loc_w_postal_code.postal_code,'SW1A 2AA')

    def test_from_string(self):
        location = Location.from_string('Downing Street 10 London United Kingdom')
        self.assertEqual(location.street, 'Downing Street 10')
        self.assertEqual(location.city, 'London')
        self.assertEqual(location.country, 'United Kingdom')
        self.assertEqual(location.postal_code, None)

    def test_from_json(self):
        loc_wo_pc_json_str = '''
        {
            "street_name": "Downing Street",
            "house_no": "10",
            "city": "London",
            "country": "UK"
        }
        '''
        location_wo_pc = Location.from_json(loc_wo_pc_json_str)
        self.assertEqual(location_wo_pc.street, 'Downing Street 10')
        self.assertEqual(location_wo_pc.city, 'London')
        self.assertEqual(location_wo_pc.country, 'UK')

        if location_wo_pc.has_postal_code():
            self.assertEqual(location_wo_pc.postal_code,'SW1A 2AA')
        else:
            self.assertEqual(location_wo_pc.postal_code, None)
        
        loc_w_pc_json_str = '''
        {
            "street_name": "Downing Street",
            "house_no": "10",
            "city": "London",
            "country": "UK"
            "postal_code": "SW1A 2AA"
        }
        '''
        location_w_pc = Location.from_json(loc_w_pc_json_str)
        self.assertEqual(location_w_pc.street, 'Downing Street 10')
        self.assertEqual(location_w_pc.city, 'London')
        self.assertEqual(location_w_pc.country, 'UK')

        if location_w_pc.has_postal_code():
            self.assertEqual(location_w_pc.postal_code,'SW1A 2AA')
        else:
            self.assertEqual(location_w_pc.postal_code, None)

        
       

if __name__ == '__main__':
    unittest.main()