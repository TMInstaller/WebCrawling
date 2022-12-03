# main.py
from requests import get
from bs4 import BeautifulSoup

url = "https://time-map-installer.tistory.com/search/"
keyword = "Python"
response = get(f"{url}{keyword}")
if response.status_code != 200:
    print("페이지를 불러올 수 없습니다", response.status_code)
else:
    # dict type의 결과를 출력하기 위한 빈 배열 생성
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    keys = soup.find_all('div', class_='inner')
    for key_section in keys:
        key_posts = key_section.find_all('div', class_='post-item')
        for post in key_posts:
            span = post.find('a')
            # 이미지 출력값을 데이터에서 제외
            title = span.find('span', class_='title')
            # meta class 안에 date 클래스가 있으므로 한 번 더 찾아 준다
            meta = span.find('span', class_='meta')
            date = meta.find('span', class_='date')

            excerpt = span.find('span', class_='excerpt')
            # dict 형태로 key, value 값 담을 key_data 생성
            key_data = {
                'title': title.string,
                'date': date.string,
                'prev': excerpt.string
            }
            results.append(key_data)
    # for loop 밖에서 결과 실행
    for result in results:
        print(result)
        print('////////////////')
