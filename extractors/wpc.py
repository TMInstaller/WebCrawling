# wpc.py
# = web page crawling
from requests import get
from bs4 import BeautifulSoup


def extract_timemapexe_keys(keyword):
    url = "https://time-map-installer.tistory.com/search/"
    response = get(f"{url}{keyword}")
    if response.status_code != 200:
        print("페이지를 불러올 수 없습니다", response.status_code)
    else:
        results = []
        soup = BeautifulSoup(response.text, 'html.parser')
        keys = soup.find_all('div', class_='inner')
        for key_section in keys:
            key_posts = key_section.find_all('div', class_='post-item')
            for post in key_posts:
                span = post.find('a')
                title = span.find('span', class_='title')
                meta = span.find('span', class_='meta')
                date = meta.find('span', class_='date')
                excerpt = span.find('span', class_='excerpt')
                key_data = {
                    'title': title.string,
                    'date': date.string,
                    'prev': excerpt.string
                }
                results.append(key_data)
        return results
