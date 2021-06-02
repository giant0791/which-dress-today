import unittest
import geocodingAPI

from geocodingAPI.location import Location

class TestLocation(unittest.TestCase):
    
    def test_init_wo_postal_code(self):
        loc_wo_postal_code = Location('Kreuzsteinweg 79a','Fuerth','Germany')
        self.assertEqual(loc_wo_postal_code.street,'Kreuzsteinweg 79a')
        self.assertEqual(loc_wo_postal_code.city,'Fuerth')
        self.assertEqual(loc_wo_postal_code.country,'Germany')

    def test_init_w_postal_code(self):
        loc_w_postal_code = Location('Kreuzsteinweg 79a','Fuerth','Germany', '90765')
        self.assertEqual(loc_w_postal_code.street,'Kreuzsteinweg 79a')
        self.assertEqual(loc_w_postal_code.city,'Fuerth')
        self.assertEqual(loc_w_postal_code.country,'Germany')
        self.assertEqual(loc_w_postal_code.postal_code,'90765')

    def test_from_string(self):
        location = Location.from_string('Kreuzsteinweg 79a Fuerth Germany')
        self.assertEqual(location.street, 'Kreuzsteinweg 79a')
        self.assertEqual(location.city, 'Fuerth')
        self.assertEqual(location.country, 'Germany')
        self.assertEqual(location.postal_code, None)

    def test_from_json(self):
        loc_wo_pc_json_str = '''
        {
            "street_name": "Kreuzsteinweg",
            "house_no": "79a",
            "city": "Fuerth",
            "country": "Germany"
        }
        '''
        location_wo_pc = Location.from_json(loc_wo_pc_json_str)
        self.assertEqual(location_wo_pc.street, 'Kreuzsteinweg 79a')
        self.assertEqual(location_wo_pc.city, 'Fuerth')
        self.assertEqual(location_wo_pc.country, 'Germany')

        if location_wo_pc.has_postal_code():
            self.assertEqual(location_wo_pc.postal_code,'90765')
        else:
            self.assertEqual(location_wo_pc.postal_code, None)
        
        loc_w_pc_json_str = '''
        {
            "street_name": "Kreuzsteinweg",
            "house_no": "79a",
            "city": "Fuerth",
            "country": "Germany",
            "postal_code": "90765"
        }
        '''
        location_w_pc = Location.from_json(loc_w_pc_json_str)
        self.assertEqual(location_w_pc.street, 'Kreuzsteinweg 79a')
        self.assertEqual(location_w_pc.city, 'Fuerth')
        self.assertEqual(location_w_pc.country, 'Germany')

        if location_w_pc.has_postal_code():
            self.assertEqual(location_w_pc.postal_code,'90765')
        else:
            self.assertEqual(location_w_pc.postal_code, None)

        
       

if __name__ == '__main__':
    unittest.main()