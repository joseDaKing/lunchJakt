'''
@author Yousif Abdulkarim
'''

from json import load



class Position:
    def __init__(self, lat, lon):
        
        self.__lat = lat
        
        self.__lon = lon
    
    @property
    def lat(self):
        
        return self.__lat

    @property
    def lon(self):

        return self.__lon



class Restaurant:

    @staticmethod
    def __get_data_source():

        file = open("data/information.json", "r")

        data_source = load(file)
        
        file.close()
        
        return data_source["data"]

    __restaurants_data = __get_data_source()

    @staticmethod
    def find_all():

        restaurants = []

        for restaurantData in Restaurant.__restaurants_data:

            name = restaurantData.get("name")

            location = restaurantData.get("location_string")

            position = Position(
                restaurantData.get("latitude"),
                restaurantData.get("longitude")
            )

            imageUrl = restaurantData.get("photo", {}).get("images", {}).get("original", {}).get("url") 
            
            restaurant = Restaurant(
                name,
                location,
                position,
                imageUrl
            )

            restaurants.append(restaurant)

        return restaurants

    def __init__(self, name, location, position, imageUrl):
        
        self.__name = name

        self.__position = position

        self.__location = location

        self.__imageUrl = imageUrl



    @property
    def name(self):

        return self.__name

    @property
    def position(self):

        return self.__position

    @property
    def location(self):

        return self.__location
    
    @property
    def imageUrl(self):

        return self.__imageUrl

