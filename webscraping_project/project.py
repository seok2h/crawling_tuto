import requests
from bs4 import BeautifulSoup


def create_soup(url: str) -> BeautifulSoup:
    """this function is create soup"""
    res = requests.get(url, timeout=30)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


# def print_news(index, title, link):
#     return None


def scrape_weather():
    """Function crawling weather information in naver.com"""
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?" \
        "where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" \
            "%EA%B4%91%EB%AA%85%EC%8B%9C+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    curr_temp = soup.find("div", attrs={"class": "temperature_text"}).get_text().strip().replace("도", "도 ")
    diff_temp = soup.find("p", attrs={"class": "summary"}).get_text().strip()
    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text().strip().replace("온", "온 ")
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text().strip().replace("온", "온 ")
    # 최고기온 OO / 최저기온 OO
    print(f"{curr_temp} ({min_temp}/{max_temp})")
    print(diff_temp)
    # 오전 강수확률 oo% / 오후 강수확률 oo%
    morning_rain_rate = soup.find_all("span", attrs={"class": "rainfall"})
    print(f"오전 강수확률 {morning_rain_rate[0].get_text()} / 오후 강수확률 {morning_rain_rate[1].get_text()}")

    # text에 "미세먼지"가 있는 걸 찾고 싶을 때 -> soup.find(" " , attrs={}, text="미세먼지")


def scrape_headline_news() -> None:
    """Function crawling headline news in naver.com"""
    # print("[헤드라인 뉴스]")
    # url = "https://news.naver.com"
    # soup = create_soup(url)
    # news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    # for index, news in enumerate(news_list):
    #     title = news.find("a").get_text().strip()
    #     link = url + news.find("a")["href"]
    #     print_news(index, title, link)
    # print()
    # soup.find_all("", attrs={}, limit=3) # 최대 3개까지만 찾아줌
    return None


if __name__ == "__main__":
    scrape_weather()
