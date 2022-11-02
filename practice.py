from urllib import request
import requests
from bs4 import BeautifulSoup

types = ['episode', 'omnibus', 'story']
def url_select(types):
    url = f"https://comic.naver.com/webtoon/genre?order=StarScore&view=image&genre={types}"
    res = requests.get(url)
    res.raise_for_status()
    return res.text


for type in types:
    soup = BeautifulSoup(url_select(type),"lxml")
    cartoons = soup.find_all("dt")
    print(type, "\n")
    for i in range(20):
        print(cartoons[i].a.get_text())
    print("\n")