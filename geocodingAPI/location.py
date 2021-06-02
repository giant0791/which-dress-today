# loc = Location('Kreuzsteinweg 79a Fuerth Germany')


class Location:
    def __init__(self, street, city, country, postal_code=None, ) -> None:
        self.street = street
        self.city = city
        self.country = country

        if postal_code is None:
            self.postal_code = None
        else:
            self.postal_code = postal_code

    @classmethod
    def from_string(cls, location_str):
        street_name, house_no, city, country = location_str.split(' ')
        street = street_name + ' ' + house_no
        return cls(street, city, country)


    