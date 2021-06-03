import json

class Location:
    def __init__(self, street, city, country, postal_code=None, ) -> None:
        self.street = street
        self.city = city
        self.country = country

        if postal_code is None:
            self.postal_code = None
        else:
            self.postal_code = postal_code
    
    def has_postal_code(self):
        return not (self.postal_code is None)

    @classmethod
    def from_string(cls, location_str):
        street_name, house_no, city, country = location_str.split(' ')
        street = street_name + ' ' + house_no
        return cls(street, city, country)

    @classmethod
    def from_json(cls, json_str):
        loc_data = json.loads(json_str)
        street_name = loc_data['street_name']
        house_no = loc_data['house_no']
        street = street_name + ' ' + house_no
        city = loc_data['city']
        country = loc_data['country']
        if 'postal_code' in loc_data:
            postal_code = loc_data['postal_code']
        else:
            postal_code = None

        return cls(street, city, country, postal_code)



    