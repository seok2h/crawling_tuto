from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x080")
# headless로 페이지 요청을 날리면 header에는 headless의 정보를 header에 저장하기 때문에 차단될 수도 있음
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
# 따라서 내가 인위적으로 user-agent를 지정해서 header로 날려줄 수가 있다.


browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
detected_value = browser.find_element(By.ID, "detected_value")
print(detected_value.text)  # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
# HeadlessChrome/121.0.6167.185 Safari/537.36


