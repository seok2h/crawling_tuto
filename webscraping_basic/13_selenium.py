from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

browser = webdriver.Chrome()
browser.get("http://www.naver.com")
# browser.find_element()
# .find_element_by_class_name 삭제 .find_element

# driver.find_element(By.CLASS_NAME, "") # 클래스 네임에 공백이 존재하는 경우 '.'으로 대체해야 한다!!!!! 예) abc efg -> abc.efg
# driver.find_element(By.ID, "")
# driver.find_element(By.CSS_SELECTOR, "")
# driver.find_element(By.NAME, "")
# driver.find_element(By.TAG_NAME, "")
# driver.find_element(By.XPATH, "")
# driver.find_element(By.LINK_TEXT, "")
# driver.find_element(By.PARTIAL_LINK_TEXT, "")
# (복수형 driver.find_elements(By.~~, "")

# browser.back()
# browser.forward()
# browser.refresh()
# elem.click()
# elem.send_keys("입력할 무언가")
# elem.clear() 텍스트 창 지워줌
# elem.send_keys(Keys.ENTER) 엔터 입력
# browser.close() 현재 탭 닫기
# browser.quit() 전체 다 닫기


# 네이버 로그인 하기
# 자동입력 방지 때문에 실제로 로그인할 수는 없음
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

browser.find_element(By.ID, "id").send_keys(os.getenv('ID'))
browser.find_element(By.ID, "pw").send_keys(os.getenv('PW'))

browser.find_element(By.ID, "log.login").click()

time.sleep(2)

# html 정보 출력
print(browser.page_source)

browser.quit()


