from .Rank import Rank

from .Position import Position

from .Location import Location

from .Restaurant import Restaurant;

from .get_data_sources import get_data_sources;

data_source = get_data_sources([
    "data/sources/restaurants_1.json",
    "data/sources/restaurants_2.json",
    "data/sources/restaurants_3.json",
    "data/sources/restaurants_4.json",
    "data/sources/restaurants_5.json",
])

def get_restaurant_position(restaurantData) -> Position:
    
    return Position(
        restaurantData.get("latitude"),
        restaurantData.get("longitude")
    )

def get_restaurant_location(restaurantData) -> Location:
    
    city = None
    
    region = None

    country = None

    position = get_restaurant_position(restaurantData)

    for ancestor in restaurantData.get("ancestors", {}):
        
        key = ancestor.get("subcategory")[0].get("key")

        value = ancestor.get("name")

        if key == "city":
            
            city = value

        if key == "region":
            
            region = value

        if key == "country":
            
            country = value

    return Location(
        city = city,
        region = region,
        country = country,
        position = position
    )

def get_restaurant_rank(restaurantData) -> Rank:

    rating = restaurantData.get("rating")
    
    num_reviews = restaurantData.get("num_reviews")
    
    local_ranking = restaurantData.get("ranking_position")
    
    global_ranking = restaurantData.get("raw_ranking")

    return Rank(
        rating = rating,
        num_reviews = num_reviews,
        local_ranking = local_ranking,
        global_ranking = global_ranking,
    )

def get_restaurants() -> list[Restaurant]:

    restaurants = []

    for restaurantData in data_source:

        location = get_restaurant_location(restaurantData)

        rank = get_restaurant_rank(restaurantData)

        name = restaurantData.get("name")

        image_url = restaurantData.get("photo", {}).get("images", {}).get("original", {}).get("url")
        
        id = restaurantData.get("location_id")

        price_level = restaurantData.get("price_level")

        if price_level != None and type(price_level) == str and not price_level:
            price_level = None

        price = restaurantData.get("price")

        if price != None:
    
            price = (
                price
                .replace(" ", "")
                .replace("\xa0", "")
                .replace("kr", "")
            )

            price = price.split("-")[0]

        restaurant = Restaurant(
            id = id,
            price = price,
            name = name,
            rank = rank,
            location = location,
            image_url = image_url,
            price_level = price_level
        )

        restaurants.append(restaurant)

    return restaurants