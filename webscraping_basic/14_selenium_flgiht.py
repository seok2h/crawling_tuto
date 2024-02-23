from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화 =


url = 'https://flight.naver.com/'
browser.get(url)    # url로 이동

# 클래스 이름(CLASS_NAME)으로 가져올 때, 이름에 공백이 존재한다면 '.'으로 대체해야 한다 예) abc def -> abc.def

browser.find_element(By.XPATH, '//button[text() = "가는 날"]').click()
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "3"]')))
browser.find_elements(By.XPATH, '//b[text() = "3"]')[1].click()     # 3월 3일 선택
browser.find_elements(By.XPATH, '//b[text() = "11"]')[1].click()    # 3월 11일 선택

# 제주도 선택
browser.find_element(By.CLASS_NAME, "tabContent_route__1GI8F.select_City__2NOOZ.end").click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//button[text() = "국내"]')))
# time.sleep(1)
browser.find_element(By.XPATH, '//button[text() = "국내"]').click()
# browser.find_element(By.XPATH, '//button[contains() = "제주"]')
jeju_button = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')  # '제주국제공항'이라는 문자열이 포함된 태그를 찾아준다
jeju_button.click()
# 항공권 검색 버튼 누르기
browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]').click()


elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA"]')))
print(elem.text)

input("종료하려면 Enter키를 입력하세요")
browser.quit()

