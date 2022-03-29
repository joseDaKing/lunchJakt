from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
url="https://restaurangniagara.se/lunch/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')

soup = BeautifulSoup(webpage, 'lxml')
opening_hours = soup.find('div', class_ = 'rn-working-hours').text
print(opening_hours)