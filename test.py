# # ENV = "production"

# SECRET_KEY = "MOVIEMOVIE"
# MongoDB_URL = "mongodb+srv://test:sparta@cluster0.g2d328l.mongodb.net/?retryWrites=true&w=majority"
# HASH_KEY = "SPARTA"

# NMovie_Search = "https://openapi.naver.com/v1/search/movie.json?query="
# Client_ID = "AUuy26sTI3omaaDoltpX"
# Client_Secret = "2Yr8Cz0jWo"


import urllib.request
import json

CID = "AUuy26sTI3omaaDoltpX"
CSC = "2Yr8Cz0jWo"

def search_naver(keyword):
    """
    keyword로 영화제목 네이버영화 검색
    """
    query = "query=" + urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/book.json?" + query
    print(url)

    request_search = urllib.request.Request(url)
    request_search.add_header("X-Naver-Client-Id", CID)
    request_search.add_header("X-Naver-Client-Secret", CSC)
    response = urllib.request.urlopen(request_search)

    rescode = response.getcode()
    if rescode==200:
        result = []
        items = json.loads(response.read().decode("utf-8"))["items"]
        
        return print(items)
    else:
        return print(f"Error Code: {rescode}")


search_naver("톨킨")