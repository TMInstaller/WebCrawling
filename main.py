# main.py
from extractors.wpc import extract_kurly_items
from extractors.wpc import extract_timemapexe_keys

keyword = input("어떤 것을 검색하시겠습니까??(블로그) : ")
timemapexe = extract_timemapexe_keys(keyword)

keyword = input("어떤 것을 검색하시겠습니까??(마켓컬리) : ")
kurly = extract_kurly_items(keyword)

search = timemapexe + kurly

for key in search:
    print(key)
    print("/////////////\n/////////////")
