from .Position import Position


class Location:

    def __init__(
        self: str | None = None,
        city: str | None = None,
        region: str | None = None,
        country: str | None = None,
        position: Position | None = None
    ):
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

        if self.has_city():
            
            str = "city: " + self.city + "\n"

        
        if self.has_region():
            
            str = "region: " + self.region + "\n"


        if self.has_country():
            
            str = "country: " + self.country + "\n"

        if self.has_position():

            str += self.__position

        return str