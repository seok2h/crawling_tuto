import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(res.text)
#
# cartoons = soup.find_all("span", attrs={"class": "EpisodeListList__title--lfIzU"})
#
# print(cartoons)
#
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a["href"]
#
