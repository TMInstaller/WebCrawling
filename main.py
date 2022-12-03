# main.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from extractors.wpc import extract_timemapexe_keys

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
keyword = "감자"
browser.get(f"https://www.kurly.com/search?sword={keyword}")
browser.implicitly_wait(time_to_wait=5)

elements = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]').text

elm_list = elements.splitlines(True)
print(elm_list)
