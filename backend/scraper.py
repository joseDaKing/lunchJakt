from flask import jsonify
import requests, json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



def resturantsAroundNiagara():
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

    querystring = {"latitude":"55.60908686020099","longitude":"12.994734396731932","limit":"30","currency":"SEK","distance":"5","lunit":"km","lang":"sv_SE"}

    headers = {
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
        "X-RapidAPI-Key": "8be6115624mshff10e281dcd567ep113658jsnf5e95f2cae94"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Converts input dictionary into
    # string and stores it in json_string
    # then dumps data to json file
    data = response.json()
    with open('backend/information.json', 'w') as j:
        json.dump(data, j)


# Opening JSON file
with open('backend/information.json', 'r') as j:
    information = json.load(j)
    j.close

    for i in information['data']:
        if i.get('name') == 'Soprano':
            print (i.get('name'))
            print (i.get('price_level'))
            print (i.get('rating'))
            print (i.get('website'))
            print (i.get('location_string'))



#Returnerar resturanginformation
def getResturantByName(name):
     for i in information['data']:
        if i.get('name') == name:
            name = (i.get('name'))
            price_level = (i.get('price_level'))
            rating = (i.get('rating'))
            website = (i.get('website'))
            location_string = (i.get('location_string'))
            return jsonify(name, price_level, rating, website, location_string) #?




'''
def read_Content_From_File():
    with open('backend/content.json', 'r') as j:
        content = json.loads(j.read())
        return content
   

def scrape_niagara():
    url="https://restaurangniagara.se/lunch/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')

    soup = BeautifulSoup(webpage, 'lxml')
    opening_hours = soup.find('div', class_ = 'rn-working-hours').text
    
    print('Scraped niagara')

    niagara = read_Content_From_File()
    niagara[0]['name'] = "Niagara"
    niagara[0]['opening_hours'] = opening_hours
    niagara[0]['helger'] = "Closed"
    
    my_file = open("backend/content.json", "w")
    my_file.write(json.dumps(niagara))
    my_file.close



def scrape_woso():
    url="https://woso.se/?page_id=1309"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    html = webpage.replace("&nbsp;",' ').encode('utf-8')

    soup = BeautifulSoup(html, 'lxml')
    
    div = soup.find('div', class_ = 'elementor-element elementor-element-3e05085 elementor-widget elementor-widget-text-editor')
    opening_hours = div.find(class_ = 'elementor-text-editor elementor-clearfix').text

    formatedHours = re.findall('[A-Z][^A-Z]*', opening_hours)
    
    print('scraped woso')

    woso = read_Content_From_File()
    woso[0]['name'] = "Woso"
    woso[0]['opening_hours'] = formatedHours
    woso[0]['helger'] = "Closed"
    
    my_file = open("backend/content.json", "w")
    my_file.write(json.dumps(woso))
    my_file.close


def scrape(name):
    if name == "niagara":
        scrape_niagara()
        
    elif name == "woso":
        scrape_woso()    
'''