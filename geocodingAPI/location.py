import json

class Location:
    def __init__(self, street, city, country, house_no=None, postal_code=None) -> None:
        if house_no is None:
            self.street_ = street
        else:
            self.street_ = house_no + ' ' + street

        self.city_ = city
        self.country_ = country
              
        if postal_code is None:
            self.postal_code_ = None
        else:
            self.postal_code_ = postal_code    

    @property
    def city(self):
        return self.city_
    
    @city.setter
    def city(self, city):
        self.city_ = city

    @property
    def country(self):
        return self.country_
               
    @country.setter
    def country(self, country):
        self.country_ = country

    @property
    def postal_code(self):
        return self.postal_code_

    @postal_code.setter
    def postal_code(self, postal_code):
        self.postal_code_ = postal_code
    
    @property
    def street(self):
        return self.street_

    @street.setter
    def street(self, street):
        self.street_ = street

    def has_postal_code(self):
        return not (self.postal_code_ is None)

    @classmethod
    def from_json(cls, json_str):
        loc_data = json.loads(json_str)
        
        street_name = loc_data['street_name']
        if 'house_no' in loc_data:
            house_no = loc_data['house_no']
        else:
            house_no = None
        
        if 'postal_code' in loc_data:
            postal_code = loc_data['postal_code']
        else:
            postal_code = None

        city = loc_data['city']
        country = loc_data['country']
        
        return cls(street_name, city, country, house_no, postal_code)

    
    
 

 

    