"""
부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

[조회 조건]
1. daum.net에 접속
2. '송파 헬리오시티' 검색
3. 다음 부동산 부분에 나오는 결과 정보

매물 5개 정도로
"""
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

url = "https://new.land.naver.com/complexes/111515?ms=37.497624,127.107268,17&a=APT:ABYG:JGC:PRE&e=RETAIL"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

# with open("quiz.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

browser = webdriver.Chrome()
browser.get(url)

# 매매 아이템들 스크롤 내리기


div_scroll = browser.find_element(By.CLASS_NAME, "item_list.item_list--article")
prev_height = browser.execute_script("return arguments[0].scrollHeight", div_scroll)

# 스크롤을 가장 아래로 내림
for x in range(2):
    browser.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight)", div_scroll)

    time.sleep(1)

    curr_height = browser.execute_script("return arguments[0].scrollHeight", div_scroll)
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

soup = BeautifulSoup(browser.page_source, "lxml")

# with open("real_estate.html", "w", encoding='utf-8') as f:
#     f.write(soup.prettify())
real_estate = soup.find_all("div", attrs={"class": 'item_inner'})
print(real_estate)

# for item in real_estate:
#     name = item.find("span", attrs={"class": "text"}).get_text()
#     deal_type = item.find("span", attrs={"class", "type"}).get_text()
#     price = item.find("span", attrs={"class", "price"}).get_text()
#     spec = item.find("span", attrs={"class", "spec"}).get_text()
#
#     print("=" * 100)
#     print(name)
#     print(deal_type, price)
#     print(spec)
#     print("=" * 100)

with open("real_estate.txt", "w", encoding="utf-8") as f:
    for item in real_estate:
        name = item.find("span", attrs={"class": "text"}).get_text()
        deal_type = item.find("span", attrs={"class", "type"}).get_text()
        price = item.find("span", attrs={"class", "price"}).get_text()
        spec = item.find("span", attrs={"class", "spec"}).get_text()

        f.write("=" * 100)
        f.write('\n')
        f.write(name+"\n")
        f.write(f"{deal_type} {price}\n")
        f.write(spec+'\n')
        f.write('\n')

input("끝내시려면 Enter를 입력하세요")
