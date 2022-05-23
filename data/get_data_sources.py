from json import load



def get_data_source(data_source_path: str) -> list:

    data_source_file = open(data_source_path, "r")

    data_source = load(data_source_file)
    
    data = data_source["data"]

    data_source_file.close()
    
    return data

def get_data_sources(data_source_paths: list[str]) -> list:

    data = []

    for data_source_path in data_source_paths:
        
        data = data + get_data_source(data_source_path)
    
    return data
