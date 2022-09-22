from flask import Blueprint, request, render_template, jsonify, abort
import time
from datetime import datetime

from ..database import *
from ..util import *


book_bp = Blueprint("book", __name__, url_prefix="/book")


# 책 상세 페이지 렌더링
@book_bp.route("/view/")
def book_detail():
    payload = token_check()
    token_info = bool(payload)
    print(token_info, payload)

    isbn = request.args.get("book_id")
    bookView = book_findone_isbn(isbn)
    bookView["_id"] = str(bookView["_id"])
    if payload == None:
        bookView["flag"] = False
    else:
        bookView["flag"] = True if payload["user_id"] in bookView["likes"] else False
    bookView["likes"] = len(bookView["likes"])
    
    return render_template("book.html", bookView=bookView, token_info=token_info)


# 해당 책의 리뷰 리스트 반환
@book_bp.route("/review")
def bookReview_list():
    # request.arg s[" "]를 사용하면 쿼리스트링으로 받은 데이터를 가져올 수 있어요.
    isbn_receive = request.args.get("isbn_give")

    book = book_findone_isbn(isbn_receive)
    # books 리뷰목록이고
    book_reviews = book["reviews"]
    # objectid 안이 인트값
    print(type(book_reviews)) # list 형식임

    result=[]
    for r_id in book_reviews:
        review = review_findone(r_id)
        review["_id"] = str(review["_id"])
        review["time"] = str(datetime.fromtimestamp(review["time"]))
        result.append(review)

    result.reverse()
    return jsonify({ "reviews": result })



# DEPRECATED
# 리뷰 작성 모달 팝업
@book_bp.route("/postreview")
def book_review_modal():
    payload = token_check()
    if payload is None:
        abort(401)
    return render_template("/modals/review.html")


# 리뷰 작성
@book_bp.route("/postreview", methods=["POST"])
def book_review_post():
    payload = token_check()
    if payload is None:
        abort(401)
    
    isbn = request.form["book_id"]
    book = book_findone_isbn(isbn)

    doc = {
        "book_id": str(book["_id"]),
        "username": payload["username"],
        "content": request.form["content"],
        "rating": int(request.form["star"]),
        "time": int(time.time()),
    }
    review_id = review_insertone(doc)
    
    return "success"


# 리뷰 삭제
@book_bp.route("/reviewdelete")
def book_review_delete():
    review_id = request.args.get("review_id")
    r_username = review_findone(review_id)["username"]
    payload = token_check()

    if payload is None or payload["username"] != r_username:
        abort(401)
        
    user_id = payload["user_id"]
    book_id = str(review_findone(review_id)["book_id"])
    ids = {
        "review_id": review_id,
        "user_id": user_id,
        "book_id": book_id,
    }
    review_deleteone(ids)

    return "success"


@book_bp.route("/likes")
def book_likes():
    """
    : 책 좋아요 토글링.
    : 쿼리스트링 book_id(:str), flag(:str, true|True 나머지는 false 취급)
    """
    payload = token_check()
    if payload is None:
        abort(401)
    user_id = payload["user_id"]
    book_id = request.args.get("book_id")
    flag = bool(request.args.get("flag")=="True" or request.args.get("flag")=="true")
    print(flag, type(flag))

    pull_likes(user_id, book_id) if flag else push_likes(user_id, book_id) 
    return "success"
