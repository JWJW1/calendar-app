import requests
from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday"
# res = requests.get(url)
# res.raise_for_status()

# #네이버 웹툰 전체목록 가져오기
# soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("a",attrs = {"class":"title"})
# # class 속성이 title인 모든 "a" element를 반환
# for cartoon in cartoons:
#     print(cartoon.get_text())
url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# cartoons = soup.find_all("td",attrs={"class":"title"})

# for i in range(5):
#     print(cartoons[i].a.get_text())
    
# title = cartoons[0].a.get_text()
# print(title)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "http://comic.naver.com"+cartoon.a["href"]
#     print(title,link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div",attrs= {"class":"rating_type"})
for cartoon in cartoons:
    rate= cartoon.find("strong").get_text()
    print(rate)
    total_rates +=float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ",total_rates / len(cartoons))
