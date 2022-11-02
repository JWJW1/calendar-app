# import requests
# import re
# from bs4 import BeautifulSoup
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=&backgroundColor="
# res = requests.get(url, headers=headers)

# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")
# items = soup.find_all("li", attrs= {"class": re.compile("^search-product")})
# print(items[0].find("div",attrs={"class":"name"}).get_text())
    


    # 광고 제품은 제외
    # ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
    # if ad_badge:
    #     print("광고 상품 제외")
    #     continue