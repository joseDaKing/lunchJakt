from cmath import sqrt



class Position:

    __ONE_DEGREE_LAT_IN_KM: float = 111

    __ONE_DEGREE_LOT_IN_KM: float = 111.321



    def __init__(
        self, 
        lat: str | None = None,
        lon: str | None = None,
    ):
        
        self.__lat = lat
        
        self.__lon = lon
    


    @property
    def lat(self) -> float | None:
        
        if self.__lat == None:
            
            return None

        return float(self.__lat)

    @property
    def lon(self) -> float | None:

        if self.__lon == None:
            
            return None

        return float(self.__lon)

    

    def distance(self, position) -> float | None:

        if self.lot == None or self.lat == None:

            return None

        x1 = self.lot * Position.__ONE_DEGREE_LOT_IN_KM
        
        y1 = self.lat * Position.__ONE_DEGREE_LAT_IN_KM

        x2 = position.lot * Position.__ONE_DEGREE_LOT_IN_KM
        
        y2 = position.lat * Position.__ONE_DEGREE_LAT_IN_KM

        distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

        return distance
    
    

    def __str__(self) -> str:

        str = "";

        if self.__lot:

            str += "lot: " + self.__lot + "\n"


        if self.__lat:

            str += "lat: " + self.__lat + "\n"

        return str