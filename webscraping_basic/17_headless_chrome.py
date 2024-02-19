from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.headless = True     # 작동 안함
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.get("https://www.google.com/search?q=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&sca_esv=5d48de1e8e0fb59b&sxsrf=ACQVn0-rS4rh2QrkYMBuT5LNLI1Cvmj5mQ%3A1708328077574&ei=jQTTZdHPIoml2roP8tCBuA0&udm=&ved=0ahUKEwiRyuSB8raEAxWJklYBHXJoANcQ4dUDCBA&uact=5&oq=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&gs_lp=Egxnd3Mtd2l6LXNlcnAiDOuMgO2VnOuvvOq1rTIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwA0jvBFAAWABwAXgBkAEAmAEAoAEAqgEAuAEDyAEAiAYBkAYK&sclient=gws-wiz-serpwww.naver.com")


prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(2)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file('test.png')

browser.quit()
