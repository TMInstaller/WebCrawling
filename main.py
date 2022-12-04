# main.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_page_count(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get(f"https://www.kurly.com/search?sword={keyword}")
    browser.implicitly_wait(time_to_wait=3)
    pages = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[3]').text
    pages = pages.splitlines()
    count = []
    for page in pages:
        count.append(int(page))
    count = max(count)
    if count >= 10:
        return 10
    else:
        return count


def extract_kurly_items(keyword):
    # 화면에 띄워져 있는 페이지의 최대 수를 검색하기 위한 코드
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    # 페이지 수 만큼 반복시키며 데이터를 가져오는 코드 실행
    results = []
    for page in range(1, pages+1):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options=options)
        url = 'https://www.kurly.com/search?sword='
        final_url = f"{url}{keyword}&page={page}"
        print("Requesting", final_url)
        browser.get(final_url)
        browser.implicitly_wait(time_to_wait=3)

        elements = browser.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]').text
        items = elements.split('\n샛별배송')
        items[0] = items[0][4:]
        elements_list = []
        for item in items:
            items = item.splitlines()
            elements_list.append(items)
        # 뭔가 문제가 생기면 아래 코드를 실행해보면 답이 나온다
        # print(elements_list)
        for element in elements_list:
            # 최대 고전 부분
            # 현재 element 의 길이가 4가 아닌 경우 불량인 배열이므로 폐기
            # 삭제 활용 시 리스트의 길이가 달라져서 실행 불가능
            if len(element) != 4:
                continue
            title = element[1]
            price = element[2].replace('%', '% 할인, ')
            memo = element[3]
            items_data = {
                '상품명': title,
                '가격': price,
                '상품 설명': memo,
            }
            results.append(items_data)
    return results


search = "상추"
ite = extract_kurly_items(search)
print(ite)
