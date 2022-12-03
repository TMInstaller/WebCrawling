# main.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# selenium을 이용하여 웹사이트의 정보를 얻어올 준비
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# selenium을 이용하여 검색 했을 때의 결과 페이지 정보를 가져오기
browser = webdriver.Chrome(options=options)
keyword = "고구마"
browser.get(f"https://www.kurly.com/search?sword={keyword}")
# 5초의 대기 시간(페이지가 로딩 될 때까지 기다리는 역할)
browser.implicitly_wait(time_to_wait=5)

# XPATH를 이용하여 검색결과 아이템들의 텍스트 정보만 가져오기
elements = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]').text

# 모든 상품들이 샛별배송으로 시작하기에 그에 맞는 작업 진행
items = elements.split('\n샛별배송')
items[0] = items[0][4:]
elements_list = []
# 2차원 배열 안에 넣어두기
for item in items:
    items = item.splitlines()
    elements_list.append(items)

# 결과를 담을 results 배열 초기화
results = []
for element in elements_list:
    # 상품명, 가격[변수 처리 작업], 상품 설명 설정
    title = element[1]
    price = element[2].replace('%', '% 할인, ')
    memo = element[3]
    # 설정한 변수들 dict type 으로 저장
    items_data = {
        '상품명': title,
        '가격': price,
        '상품 설명': memo,
    }
    results.append(items_data)

# 결과 출력
for result in results:
    print(result, '\n')
