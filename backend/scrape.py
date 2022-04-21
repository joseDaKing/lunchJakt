import string
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def scrape_bistro():
    url="https://bistroroyal.se/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    
    soup = BeautifulSoup(webpage, 'lxml')
    opening_hours = soup.find('div', class_ = 'open_hours').text
    formated_string = opening_hours.replace('\t', '').replace('\n', ' ')
    print(formated_string)


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


def crazy_foodora():
    url = "https://www.foodora.se/en/restaurant/sbua/malmo-city-pizzeria-sbua"
    req = Request(url, headers={'User-Agent': 'request'})

    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    soup = BeautifulSoup(webpage, 'lxml')
    information = soup.find('div', class_='vendor-section')
    info2 = information.find('div', class_='box-flex vendor-info-main section-container ai-start  fw-wrap')
    print(info2)

crazy_foodora()