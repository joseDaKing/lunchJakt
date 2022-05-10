class Rank:
    
    def __init__(
        self,
        rating: str | None = None,
        num_reviews: str | None = None,
        local_ranking: str | None = None,
        global_ranking: str | None = None,
    ):

        if rating != None and type(rating) != str:
            raise Exception("rating must be a string")
        
        if num_reviews != None and type(num_reviews) != str:
            raise Exception("num_reviews must be a string")
        
        if local_ranking != None and type(local_ranking) != str:
            raise Exception("local_ranking must be a string")
        
        if global_ranking != None and type(global_ranking) != str:
            raise Exception("global_ranking must be a string")

        self.__rating = rating

        self.__num_reviews = num_reviews

        self.__global_ranking = global_ranking

        self.__local_ranking = local_ranking



    @property
    def rating(self) -> str | None:

        return self.__rating

    def has_rating(self) -> bool:

        return self.__rating != None



    @property
    def num_reviews(self) -> int | None:

        if self.__num_reviews == None:
            
            return None

        return int(self.__num_reviews)

    def has_num_reviews(self) -> bool:

        return self.__num_reviews != None


    
    @property
    def global_ranking(self) -> float | None:

        if self.__global_ranking == None:

            return None

        return float(self.__global_ranking)

    def has_global_ranking(self) -> bool:

        return self.__global_ranking != None


    
    @property
    def local_ranking(self) -> int | None:

        if self.__local_ranking == None:
            
            return None

        return int(self.__local_ranking)

    def has_local_ranking(self) -> bool:

        return self.__local_ranking != None
    

    
    def __str__(self) -> str:

        text = ""

        if (self.has_rating()):

            text += "rating: " + self.__rating + "\n"


        if (self.has_num_reviews()):

            text += "num_review: " + self.__num_reviews + "\n"


        if (self.has_local_ranking()):

            text += "local_ranking: " + self.__local_ranking + "\n"


        if (self.has_global_ranking()):

            text += "global_ranking: " + self.__global_ranking + "\n"
            

        return text