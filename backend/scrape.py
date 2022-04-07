from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def scrape_bistro():
    url="https://bistroroyal.se/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    
    soup = BeautifulSoup(webpage, 'lxml')
    opening_hours = soup.find('div', class_ = 'open_hours').text.replace(' ', '')
    print(opening_hours)


def scrape_kfc():
    url = "https://www.kfc.nu/hitta-oss/kfc-stortorget/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    
    soup = BeautifulSoup(webpage, 'lxml')
    opening_hours = soup.find('dl', class_ = 'inline-dl open').text
    print(opening_hours)


def scrape_max():
    url = "https://www.max.se/hitta-max/restauranger/malmo-stortorget/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    
    soup = BeautifulSoup(webpage, 'lxml')
    opening_hours = soup.find('div', class_ = 'o-restaurant__opening-hours').text
    print(opening_hours)

scrape_max()