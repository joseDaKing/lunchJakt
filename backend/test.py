import requests
import json


'''
def scrapeNiagara():
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

    querystring = {"latitude":"55.60908686020099","longitude":"12.994734396731932","limit":"30","currency":"SEK","distance":"5","lunit":"km","lang":"sv_SE"}

    headers = {
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
        "X-RapidAPI-Key": "8be6115624mshff10e281dcd567ep113658jsnf5e95f2cae94"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Converts input dictionary into
    # string and stores it in json_string
    data = response.json()
    
    with open('information.json', 'w') as j:
        json.dump(data, j)
'''

# Opening JSON file
with open('information.json', 'r') as j:
    information = json.load(j)
    j.close

    for i in information['data']:
        if i.get('name') == 'Restaurang Niagara':
            print (i.get('name'))
            print (i.get('price_level'))
            print (i.get('rating'))
            print (i.get('website'))
            print (i.get('location_string'))

         