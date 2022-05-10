from Location import Location

from Rank import Rank

from add_tabs import add_tabs



class Restaurant:
    
    def __init__(
        self,
        name: str | None = None,
        image_url: str | None = None,
        rank: Rank | None = None,
        location: Location | None = None,
    ):
        if name != None and type(name) != str:
            
            raise Exception("name must be string")

        if image_url != None and type(image_url) != str:
            
            raise Exception("image_url must be string")

        if rank != None and type(rank) != Rank:
            
            raise Exception("rank must be a Rank object")

        if location != None and type(location) != Location:
            raise Exception("location must be a Location Object")

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


    def __can_compare(self, restaurant) -> bool:
        
        return (
            self.has_rank()
            and restaurant.has_rank()
            and self.__rank.has_global_ranking()
            and restaurant.rank.has_global_ranking()
        )

    def __eq__(self, restaurant) -> bool:
        
        return self.__can_compare(restaurant) and self.rank.global_ranking == restaurant.__rank.global_ranking

    def __gt__(self, restaurant) -> bool:
        
        return self.__can_compare(restaurant) and restaurant.__rank.global_ranking < self.__rank.global_ranking

    def __lt__(self, restaurant) -> bool:
        
        return self.__can_compare(restaurant) and restaurant.__rank.global_ranking > self.__rank.global_ranking

    def __ne__(self, restaurant) -> bool:
        
        return not self.__eq__(restaurant)

    def __ge__(self, restaurant) -> bool:
        
        return self.__gt__(restaurant) or self.__eq__(restaurant)

    def __le__(self, restaurant) -> bool:

        return self.__lt__(restaurant) or self.__eq__(restaurant)



    def __str__(self) -> str:

        text = "Restaurant\n"

        if self.has_name():

            text += add_tabs("name: " + self.__name + "\n")

        if self.has_image_url():
            
            text += add_tabs("image_url: " + self.__image_url + "\n")
            
        
        if self.has_rank():

            text += add_tabs("rank:\n" + add_tabs(str(self.__rank)))
            
        
        if self.has_location():

            text += add_tabs("location:\n" + add_tabs(str(self.__location)))

        return text