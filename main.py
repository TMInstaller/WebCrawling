# main.py
from extractors.wpc import extract_kurly_items
from extractors.wpc import extract_timemapexe_keys


keyword_b, keyword_k = input("어떤 것을 검색하시겠습니까??(블로그, 마켓컬리) : ").split()

timemapexe = extract_timemapexe_keys(keyword_b)
kurly = extract_kurly_items(keyword_k)

file = open(f"{keyword_b}.csv", "w", encoding='UTF-8')
file.write("Title,Date,Prev\n")

for key in timemapexe:
    file.write(f"{key['title']},{key['date']},{key['prev']}\n\n")

file.close()

file = open(f"{keyword_k}.csv", "w", encoding='UTF-8')
file.write("상품명,가격,상품 설명\n")

for key in kurly:
    file.write(f"{key['상품명']},{key['가격']},{key['상품 설명']}\n\n")

file.close()
