from Rank import Rank

from Position import Position

from Location import Location

from Restaurant import Restaurant;

from get_data_source import get_data_source;



data_source = get_data_source()

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
        
        restaurant = Restaurant(
            name = name,
            rank = rank,
            location = location,
            image_url = image_url
        )

        restaurants.append(restaurant)

    return restaurants