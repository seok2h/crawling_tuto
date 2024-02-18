import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element를 반환
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a['href']) # a element의 href 속성 '값' 정보를 출력

print(soup.a)

print(soup.find("a", attrs={"class": "GlobalNavigationBar__link--WMOzG"})) # class="" 인 a element를  찾아줘
print(soup.find(attrs={"class": "GlobalNavigationBar__link--WMOzG"})) # class=""인 어떤 element를 찾아줘

# 실행되지 않음
# print(soup.find("li", attrs={"class": "rank01"}) # li 태그의 클래스가 rank01인 것을 출력
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # li 태그의 클래스가 rank01의 a태그를 가져옴
# print(rank1.a.get_text())
# print(rank1.next_sibling) # 객체의 형제를 가져옴
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank2 = rank3.previous_sibling.previous_sibling # 이전 형제를 가져옴
# print(rank1.parent) # 부모 객체를 가져옴
# rank2 = rank1.find_next_sibling("li") # 다음 형제를 찾는데 안에 조건을 토대로 찾아줌
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank1.find_next_siblings("li") # 형제"모두"르 가져옴

# webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마")