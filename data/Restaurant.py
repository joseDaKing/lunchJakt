from .Location import Location

from .Rank import Rank


class Restaurant:
    
    def __init__(
        self,
        name: str | None = None,
        image_url: str | None = None,
        rank: Rank | None = None,
        location: Location | None = None,
    ):
        
        self.__name = name

        self.__image_url = image_url

        self.__rank = rank

        self.__location = location



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

        str = ""

        if self.name:

            str += self.name + "\n"
            
        
        if self.image_url:

            str += self.image_url + "\n"
            
        
        if self.rank:

            str += self.rank + "\n"
            
        
        if self.location:

            str += self.location + "\n"
            
        
        if self.position:

            str += self.position + "\n"
            

        return str