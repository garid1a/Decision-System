class Consumer:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        # Other attributes can be added as needed

class Farmer:
    def __init__(self, name, location, soil_type):
        self.name = name
        self.location = location
        self.soil_type = soil_type
        # Other attributes can be added as needed

class Preference:
    def __init__(self, consumer_id, product_id, month):
        self.consumer_id = consumer_id
        self.product_id = product_id
        self.month = month
        # Other attributes can be added as needed

class Product:
    def __init__(self, product_name, season, soil_type):
        self.product_name = product_name
        self.season = season
        self.soil_type = soil_type
        # Other attributes can be added as needed
