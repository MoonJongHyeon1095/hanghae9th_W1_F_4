from bson import ObjectId
from ..config import Pymongo


db = Pymongo.db



def book_findone(_id):
    """
    db.books에서 _id에 해당하는 책 정보 가져오기
    """
    return db.books.find_one({"_id": ObjectId(_id)})


def book_find():
    """
    db.books에서 전체 책 리스트 가져오기
    """
    return ""


def book_insertone(doc):
    """
    db.books에 책 등록하기"""
    return ""






### 유지보수용 책 DB 등록###

# import urllib.request
# import json
# import bs4
# import requests
# from selenium import webdriver
# from time import sleep

# CID = "AUuy26sTI3omaaDoltpX"
# CSC = "2Yr8Cz0jWo"

# def main(url):
#     titles = search_kyobo(url)

#     # print(titles)
#     for title in titles:
#         books = search_naver(title)
        
#         link = books[0]["link"]
#         image = get_naver_image(link)

#         doc = {
#             "title": books[0]["title"],
#             "image": image,
#             "author": books[0]["author"],
#             "pubdate": books[0]["pubdate"],
#             "publisher": books[0]["publisher"],
#             "discount": books[0]["discount"],
#             "description": books[0]["description"],
#             "isbn": books[0]["isbn"],
#             "likes": [],
#         }

#         from pymongo import MongoClient
#         client = MongoClient("mongodb+srv://test:sparta@cluster0.g2d328l.mongodb.net/?retryWrites=true&w=majority", 
#             tls=True, tlsAllowInvalidCertificates=True)
#         db = client.minibook

#         if db.books.find_one({"title": doc["title"]}) is None:
#             db.books.insert_one(doc)


# def search_naver(keyword):
#     """
#     keyword로 영화제목 네이버영화 검색
#     """
#     query = "query=" + urllib.parse.quote(keyword) + "&display=1"
#     url = "https://openapi.naver.com/v1/search/book.json?" + query
#     # print(url)

#     request_search = urllib.request.Request(url)
#     request_search.add_header("X-Naver-Client-Id", CID)
#     request_search.add_header("X-Naver-Client-Secret", CSC)
#     response = urllib.request.urlopen(request_search)

#     rescode = response.getcode()
#     if rescode==200:
#         result = []
#         items = json.loads(response.read().decode("utf-8"))["items"]
        
#         for item in items:
#             result.append(item)

#         return result
#     else:
#         return print(f"Error Code: {rescode}")


# def search_kyobo(url):    
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(url, headers=headers)
#     soup = bs4.BeautifulSoup(data.text, 'html.parser')
#     titles = soup.select("#main_contents > ul > li > div.detail > div.title > a")

#     #main_contents > ul > li:nth-child(6) > div.detail > div.title > a
#     title_list = []
#     for title in titles:
#         # print(title.text.split("(")[0])
#         title_list.append(title.text.split("(")[0])

#     return title_list


# def get_naver_image(link):
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(link, headers=headers)
#     soup = bs4.BeautifulSoup(data.text, 'html.parser')

#     #__next > div > div.bookCatalog_book_container__b3htO > div.bookCatalog_inner_container__JUfKQ > div.bookCatalog_book_catalog__yiiIc > div.bookCatalog_book_info_top__SUILS > div.bookImage_book_image__myUU5 > div.bookImage_img_area__kiGb6 > div > img
#     image = soup.select_one("#__next > div > div.bookCatalog_book_container__b3htO > div.bookCatalog_inner_container__JUfKQ > div.bookCatalog_book_catalog__yiiIc > div.bookCatalog_book_info_top__SUILS > div.bookImage_book_image__myUU5 > div.bookImage_img_area__kiGb6 > div > img")
    
#     return image["src"].split("?")[0]



# def mains():
#     list = [
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=C&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=D&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=E&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=F&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=G&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=I&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=J&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=K&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=M&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=b&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=c&range=0&kind=&orderClick=DDb",
#             "https://www.kyobobook.co.kr/bestSellerNew/steadyseller.laf?mallGb=KOR&linkClass=d&range=0&kind=&orderClick=DDb",    
#             ]

#     for url in list:
#         main(url)

# mains()
    



