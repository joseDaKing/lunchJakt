from json import load



def get_data_source():

    file = open("data/sources/restaurants.json", "r")

    data_source = load(file)
    
    file.close()
    
    return data_source["data"]
