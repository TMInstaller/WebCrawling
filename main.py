# main.py
from requests import get
from bs4 import BeautifulSoup

# 검색 시 작동 하는 url link 가져오기
url = "https://time-map-installer.tistory.com/search/"
# 검색 시 입력 될 키워드 입력하기
keyword = "Python"
# 두 값을 합쳐 검색 시 나오는 url link 설정하기
response = get(f"{url}{keyword}")
if response.status_code != 200:
    # status_code가 200이 아니면 정상적인 실행이 아니라는 뜻이다
    print("페이지를 불러올 수 없습니다", response.status_code)
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    # 찾을 정보를 keys 변수에 새로 저장
    keys = soup.find_all('div', class_='inner')
    for key_section in keys:
        # key posts에 div 태그의 post-item들만 불러오기 위한 준비
        key_posts = key_section.find_all('div', class_='post-item')
        for post in key_posts:
            # 그 안에서 a 태그 안의 모든 것을 가져올 준비
            # a 태그가 하나라 find_all 대신 find 사용
            span = post.find('a')
            # a 태그 안에 각각의 태그들이 하나씩이면 find, 여러개면 find_all로 불러오기
            thum = span.find('span', class_='thum')
            title = span.find('span', class_='title')
            excerpt = span.find('span', class_='excerpt')
            meta = span.find('span', class_='meta')
            # 출력하고 구분자로 나눠보기
            print(thum, title, excerpt, meta)
            print('//////////////////')
