from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화 =


url = 'https://flight.naver.com/'
browser.get(url)    # url로 이동

# 클래스 이름(CLASS_NAME)으로 가져올 때, 이름에 공백이 존재한다면 '.'으로 대체해야 한다 예) abc def -> abc.def


browser.find_element(By.XPATH, '//button[text() = "가는 날"]').click()
browser.find_elements(By.XPATH, '//b[text() = "3"]')[1].click()
browser.find_elements(By.XPATH, '//b[text() = "11"]')[1].click()

time.sleep(10)
