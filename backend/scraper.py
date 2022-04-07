import re, json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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
    
    tider = "11-14"

    niagara = read_Content_From_File()
    niagara[0]['name'] = "MC"
    niagara[0]['opening_hours'] = "00-24"
    niagara[0]['helger'] = "00-24"
    
    my_file = open("content.json", "w")
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
    
    print(formatedHours)

    woso = read_Content_From_File()
    woso[0]['name'] = "Woso"
    woso[0]['opening_hours'] = formatedHours
    woso[0]['helger'] = "Closed"
    
    my_file = open("backend/content.json", "w")
    my_file.write(json.dumps(woso))
    my_file.close


def scrape(name):
    if name == 'niagara':
        scrape_niagara()
    elif name == 'woso':
        scrape_woso()    