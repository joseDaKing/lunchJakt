from cmath import sqrt



class Position:

    __ONE_DEGREE_LAT_IN_KM: float = 111

    __ONE_DEGREE_LON_IN_KM: float = 111.321



    def __init__(
        self, 
        lat: str | None = None,
        lon: str | None = None,
    ):
        if lat != None and type(lat) != str:
            raise Exception("lat must be a string")

        if lon != None and type(lon) != str:
            raise Exception("lon must be a string")
        
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

        if self.lon == None or self.lat == None:

            return None

        x1 = float(self.__lon) * Position.__ONE_DEGREE_LON_IN_KM
        
        y1 = float(self.__lat) * Position.__ONE_DEGREE_LAT_IN_KM

        x2 = float(position.lon) * Position.__ONE_DEGREE_LON_IN_KM
        
        y2 = float(position.lat) * Position.__ONE_DEGREE_LAT_IN_KM

        distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

        return distance
    
    

    def __str__(self) -> str:

        text = "";

        if self.__lon != None:

            text += "lon: " + self.__lon + "\n"


        if self.__lat != None:

            text += "lat: " + self.__lat + "\n"

        return text