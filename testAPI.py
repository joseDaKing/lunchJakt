import requests
import json

#kör inte denna filen då vi har begränsat antal anrop!

url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

querystring = {"latitude":"55.60825248560394","longitude":"13.0047951939668","limit":"30","currency":"SEK","distance":"10","open_now":"false","lunit":"km","lang":"sv_SE"}

headers = {
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
	"X-RapidAPI-Key": "8be6115624mshff10e281dcd567ep113658jsnf5e95f2cae94"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

with open('resturantsKockeriet.json', 'w') as json_file:
    json.dump(response, json_file)

print(response.text)