from .Position import Position


class Location:

    def __init__(
        self,
        city: str | None = None,
        region: str | None = None,
        country: str | None = None,
        position: Position | None = None
    ):
        if city != None and type(city) != str:
            raise Exception("city must be a string")

        if region != None and type(region) != str:
            raise Exception("region must be a string")

        if country != None and type(country) != str:
            raise Exception("country must be a string")

        if position != None and type(position) != Position:
            raise Exception("position must be a Position object")
    
        self.__city = city

        self.__region = region

        self.__country = country

        self.__position = position
    


    @property
    def city(self) -> str | None:

        return self.__city

    def has_city(self) -> bool:

        return self.__city != None


    
    @property
    def region(self) -> str | None:

        return self.__region

    def has_region(self) -> bool:

        return self.__region != None
    


    @property
    def country(self) -> str | None:

        return self.__country

    def has_country(self) -> bool:

        return self.__country != None


    @property
    def position(self) -> Position | None:

        return self.__position

    def has_position(self) -> bool:

        return self.__position != None


    
    def __str__(self) -> str | None:

        text = ""

        if self.has_city():
            
            text += "city: " + self.city + "\n"

        
        if self.has_region():
            
            text += "region: " + self.region + "\n"


        if self.has_country():
            
            text += "country: " + self.country + "\n"

        if self.has_position():

            text += "position:\n" + add_tabs(str(self.__position))

        return text