from selenium import webdriver
import time



browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
# 구글 무비 사이트가 변해서 구글에 대한민국을 검색한 결과 페이지로 대체
url = 'https://www.google.com/search?q=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&sca_esv=41af24155a5007c9&sxsrf=ACQVn090q5Lf2eP9IkzEiHX808NNjKX6_Q%3A1708326148089&ei=BP3SZc36BJrm2roPtbOTuAw&udm=&ved=0ahUKEwjNjN7p6raEAxUas1YBHbXZBMcQ4dUDCBA&uact=5&oq=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&gs_lp=Egxnd3Mtd2l6LXNlcnAiDOuMgO2VnOuvvOq1rTIKEC4YgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIIEC4YgAQYsQMyBRAAGIAEMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMggQABiABBixAzIZEC4YgAQYigUYQxiXBRjcBBjeBBjgBNgBAki1FVCjAlicFHADeAGQAQOYAYwCoAGfE6oBBjAuMTYuMbgBA8gBAPgBAagCEcICBBAAGEfCAgoQIxiABBiKBRgnwgIEEAAYHsICBhAAGAgYHsICCBAAGAUYHhgPwgIGEAAYHhgPwgIHECMY6gIYJ8ICFBAAGIAEGOMEGOkEGOoCGLQC2AEBwgIEECMYJ8ICERAuGIAEGLEDGIMBGMcBGNEDwgIEEAAYA8ICDhAuGIAEGLEDGMcBGNEDwgILEC4YgAQYsQMYgwHCAhEQLhiABBixAxiDARjHARivAcICCBAuGLEDGIAEwgIgEC4YgAQYsQMYgwEYxwEY0QMYlwUY3AQY3gQY4ATYAQLCAgoQLhhDGIAEGIoFwgIXEC4YgAQYsQMYlwUY3AQY3gQY4ATYAQKIBgGQBgq6BgYIARABGAG6BgYIAhABGBQ&sclient=gws-wiz-serp#ip=1'
browser.get(url)


# 화면 아래로 내리기 (1080만큼)
browser.execute_script("window.scrollTo(0, 1080)")
browser.execute_script("window.scrollTo(0, 2080)")
# 현재 문서 높이만큼 내림 (가장 아래로)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 스크롤을 가장 아래로 내림
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(2)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


