import unittest
from .location import Location


class TestLocation(unittest.TestCase):
    
    location_w_postal_code = Location.Location(
        'Kreuzsteinweg 79a',
        'Fuerth',
        'Germany',
        '90765'
    )

    def test_init_wo_postal_code(self):
        loc_wo_postal_code = Location.Location('Kreuzsteinweg 79a','Fuerth','Germany')
        self.assertEqual(loc_wo_postal_code.street,'Kreuzsteinweg 79a')
        self.assertEqual(loc_wo_postal_code.city,'Fuerth')
        self.assertEqual(loc_wo_postal_code.country,'Germany')
        
if __name__ == '__main__':
    unittest.main()