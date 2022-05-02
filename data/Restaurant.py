'''
@author Yousif Abdulkarim
'''

from cmath import sqrt

from json import load



class Position:

    __ONE_DEGREE_LAT_IN_KM = 111

    __ONE_DEGREE_LOT_IN_KM = 111.321



    def __init__(self, lat, lon):
        
        self.__lat = lat
        
        self.__lon = lon
    


    @property
    def lat(self):
        
        return self.__lat

    @property
    def lon(self):

        return self.__lon

    

    def distance(self, position):

        x1 = self.lot * Position.__ONE_DEGREE_LOT_IN_KM
        
        y1 = self.lat * Position.__ONE_DEGREE_LAT_IN_KM

        x2 = position.lot * Position.__ONE_DEGREE_LOT_IN_KM
        
        y2 = position.lat * Position.__ONE_DEGREE_LAT_IN_KM

        distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

        return distance



class Restaurant:

    @staticmethod
    def __get_data_source():

        file = open("data/information.json", "r")

        data_source = load(file)
        
        file.close()
        
        return data_source["data"]

    __data_source = __get_data_source()



    @staticmethod
    def __data_source_to_restaurants():

        restaurants = []

        for restaurantData in Restaurant.__data_source:

            name = restaurantData.get("name")

            ancestors = restaurantData.get("ancestors")

            for ancestor in ancestors:
                
                key = ancestor.get("subcategory").get("0").get("key")

                value = ancestor.get("name")

                if key == "city":
                    
                    city = value

                if key == "region":
                    
                    region = value

                if key == "country":
                    
                    country = value

            lat = restaurantData.get("latitude")

            lon = restaurantData.get("longitude")

            if lat != None and lon != None:

                position = Position(
                    restaurantData.get("latitude"),
                    restaurantData.get("longitude")
                )

            imageUrl = restaurantData.get("photo", {}).get("images", {}).get("original", {}).get("url") 
            
            restaurantData.get()

            restaurant = Restaurant(
                name = name,
                city = city,
                region = region,
                country = country,
                position = position,
                imageUrl = imageUrl
            )

            restaurants.append(restaurant)

        return restaurants

    __restaurants_data = __data_source_to_restaurants()



    @staticmethod
    def find(
        name = "",
        city = "",
        region = "",
        country = "",
        user_position = None,
        max_distance_in_km = None,
    ):

        filtered_restaurants = []
        
        for restaurant in Restaurant.__restaurants_data:
            
            is_name_matching = name != None and name.lower().__contains__(restaurant.name)

            is_city_matching = name != None and city.lower().__contains__(restaurant.city)

            is_region_matching = name != None and region.lower().__contains__(restaurant.region)

            is_country_matching = name != None and country.lower().__contains__(restaurant.country)

            is_user_in_range = True

            if user_position != None and max_distance_in_km != None and 0 < max_distance_in_km:
                
                distance = user_position.distance(restaurant.position)

                is_user_in_range = distance < max_distance_in_km

            is_matching = (is_name_matching or is_city_matching or is_region_matching or is_country_matching) and is_user_in_range

            if is_matching:
                
                filtered_restaurants.append()

        return filtered_restaurants



    def __init__(
        self,
        name,
        city,
        region,
        country,
        position,
        imageUrl
    ):
        
        self.__name = name

        self.__position = position

        self.__imageUrl = imageUrl

        self.__city = city

        self.__region = region

        self.__country = country



    @property
    def name(self):

        return self.__name

    def hasName(self):

        return self.__name != None
    
    

    @property
    def position(self):

        return self.__position
    
    def hasPosition(self):

        return self.__position != None



    @property
    def imageUrl(self):

        return self.__imageUrl

    def hasImageUrl(self):

        return self.__imageUrl != None



    @property
    def city(self):

        return self.__city

    def hasCity(self):

        return self.__city != None


    
    @property
    def region(self):

        return self.__region

    def hasRegion(self):

        return self.__region != None
    


    @property
    def country(self):

        return self.__country

    def hasCountry(self):

        return self.__country != None