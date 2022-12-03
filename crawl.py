from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://time-map-installer.tistory.com/")

bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.find_all('span', class_='title'):
    print(link.text.strip(), link.get('span'))