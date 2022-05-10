from inspect import _void
from .Location import Location

from .Rank import Rank

from .add_tabs import add_tabs



class Restaurant:
    
    def __init__(
        self,
        id: str,
        price: str | None = None,
        name: str | None = None,
        image_url: str | None = None,
        rank: Rank | None = None,
        location: Location | None = None,
    ):
        if id != None and type(id) != str:
                
            raise Exception("id must be a string")

        if price != None and type(price) != str:

            raise Exception("price must be a string")

        if name != None and type(name) != str:
            
            raise Exception("name must be string")

        if image_url != None and type(image_url) != str:
            
            raise Exception("image_url must be string")

        if rank != None and type(rank) != Rank:
            
            raise Exception("rank must be a Rank object")

        if location != None and type(location) != Location:

            raise Exception("location must be a Location Object")

        self.__id = id
        
        self.__price = price

        self.__name = name

        self.__image_url = image_url

        self.__rank = rank

        self.__location = location

        self.__comparator_property = "rank"



    @property
    def id(self) -> str:

        return self.__id


    @property
    def price(self) -> int | None:

        if (self.__price == None):
            
            return None

        return int(self.__price)

    def has_price(self) -> bool:

        return self.__price != None

    

    @property
    def name(self) -> str | None:
        
        return self.__name
    
    def has_name(self) -> bool:

        return self.__name != None



    @property
    def image_url(self) -> str | None:
        
        return self.__image_url
    
    def has_image_url(self) -> bool:

        return self.__image_url != None



    @property
    def rank(self) -> Rank | None:
        
        return self.__rank
    
    def has_rank(self) -> bool:

        return self.__rank != None

    @property
    def location(self) -> Location | None:
        
        return self.__location
    
    def has_location(self) -> bool:

        return self.__location != None

    

    def __str__(self) -> str:

        text = "Restaurant\n"

        text += add_tabs("id: " + self.__id)

        if self.has_price():

            text += add_tabs("price: " + self.__price)

        if self.has_name():

            text += add_tabs("name: " + self.__name + "\n")

        if self.has_image_url():
            
            text += add_tabs("image_url: " + self.__image_url + "\n")
            
        
        if self.has_rank():

            text += add_tabs("rank:\n" + add_tabs(str(self.__rank)))
            
        
        if self.has_location():

            text += add_tabs("location:\n" + add_tabs(str(self.__location)))

        return text