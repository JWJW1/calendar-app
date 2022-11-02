# import requests
# res = requests.get("http://naver.com")
# print(res.status_code)
# print(len(res.text))

import re
p = re.compile("ca.e")
def print_match(m):
    if m:
        print("group = ",m.group()) # 일치하는 문자열 반환
        print("string = ",m.string) #입력받은 문자열
        print("start = ", m.start()) #일치하는 문자열의 시작 index
        print("end = ", m.end()) #일치하는 문자열의 끝 index
        print("span = ",m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("cselsee") # 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m= p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

m = p.findall("care cafe") # 일치하는 모든 것을 리스트 형태로 반환
print(m)