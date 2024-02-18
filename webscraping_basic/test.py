from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("https://comic.naver.com/webtoon")

time.sleep(60)

