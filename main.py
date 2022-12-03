# main.py
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from extractors.wpc import extract_timemapexe_keys

# selenium을 이용하여 웹사이트의 정보를 얻어올 준비
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# selenium을 이용하여 검색 했을 때의 결과 페이지 정보를 가져오기
browser = webdriver.Chrome(options=options)
keyword = "감자"
browser.get(f"https://www.kurly.com/search?sword={keyword}")
browser.implicitly_wait(time_to_wait=5)

# XPATH를 이용하여 검색결과 아이템들의 텍스트 정보만 가져오기
elements = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]').text

# 줄바꿈을 기준으로 리스트화
elm_list = elements.splitlines(True)
elms_list = []

for i in range(len(elm_list)):
    elms_list.append(elm_list[i].strip('\n'))

print(elms_list)
