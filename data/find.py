from get_restaurants import get_restaurants

from Restaurant import Restaurant

from Position import Position



restaurants_data = get_restaurants()

def contains(a: str | float | int | None, b: str | float | int | None) -> bool:
    
    return a != None and b != None and str(a).lower().__contains__(str(b).lower())

def is_value_matching(a: str | float | int | None, b: str | float | int | None) -> bool:

    return contains(a, b) and a == b

def is_restaurant_in_range(max_distance: float | None, user_position: Position | None, restaurant_position: Position | None) -> bool:
    
    if user_position == None or restaurant_position == None or max_distance == None:
        
        return True

    return user_position.distance(restaurant_position) <= max_distance

def is_search_matching(search_text: str | None, fields: list[str | None]) -> bool:

    has_matched = False

    for field in fields:

        has_matched = has_matched or contains(search_text, field)

def find(
    name: str | None = None,
    city: str | None = None,
    country: str | None = None,
    region: str | None = None,
    search_text: str | None = None,
    user_position: str | None = None,
    max_distance_in_km: str | None = None,
) -> Restaurant:

    filtered_restaurants = []
    
    for restaurant in restaurants_data:

        is_name_matching = is_value_matching(restaurant.name, name)
        
        is_city_matching = is_value_matching(restaurant.location.city, city)
        
        is_country_matching = is_value_matching(restaurant.location.country, country)

        is_region_matching = is_value_matching(restaurant.location.region, region)

        is_in_range = is_restaurant_in_range(
            user_position = user_position,
            max_distance = max_distance_in_km,
            restaurant_position = restaurant.location.position
        )

        has_search_matches = is_search_matching(
            search_text = search_text,
            fields = [
                restaurant.name,
                restaurant.location.city,
                restaurant.location.region,
                restaurant.location.country,
            ]
        )

        is_matching = is_in_range and (
            has_search_matches
            or is_name_matching
            or is_city_matching
            or is_country_matching
            or is_region_matching
        )

        if is_matching:
            
            filtered_restaurants.append(restaurant)

    return filtered_restaurants