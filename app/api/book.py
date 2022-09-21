from flask import Blueprint, request, render_template, jsonify, abort
import time

from ..config import Pymongo
from ..database import *
from ..util import *


book_bp = Blueprint("book", __name__, url_prefix="/book")
db = Pymongo.db

# 책 상세 페이지 렌더링
@book_bp.route("/view/")
def book_detail():
    # db에서 결과 보내기
    checked_token = token_check()
    token_info = bool(checked_token)
    
    bookid_receive = request.args.get("book_id")
    bookView = list(db.books.find({"isbn":bookid_receive},{"_id": False}))[0]
    
    return render_template("book.html", bookView=bookView, token_info=token_info)


# 해당 책의 리뷰 리스트 반환
@book_bp.route("/review")
def bookReview_list():
    # request.args[" "]를 사용하면 쿼리스트링으로 받은 데이터를 가져올 수 있어요.

    # isbn으로 book 검색 
    # book["reviews"]로 리뷰 id 리스트 받기
    # 각각 리뷰id로 리뷰 데이터 받아오기
    books = list(db.books.find({},{"_id": False}))
    return jsonify({"books":books})


# 리뷰 작성창
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
        "username": payload["username"],
        "book_id": str(book["_id"]),
        "content": request.form["content"],
        "rating": int(request.form["star"]),
        "time": int(time.time()),
    }
    review_id = str(review_upsertone(doc))

    db.users.update_one({"username": doc["username"]}, {"$push": {"reviews": review_id}})
    db.books.update_one({"isbn": isbn}, {"$push": {"reviews": review_id}})
    
    return "success"


# 리뷰 삭제
@book_bp.route("/delete")
def book_review_delete():
    # payload = token_check()
    # user_id = payload["user_id"]
    # review_id = request.args.get("review_id")
    # book_id = review_findone(review_id)["book_id"]

    # ids = {
    #     "review_id": review_id,
    #     "user_id": user_id,
    #     "book_id": book_id,
    # }
    # review_deleteone(ids)

    return ""


# 책 좋아요
@book_bp.route("/likes")
def book_likes():
    # payload = token_check()
    # user_id = payload["user_id"]
    # book_id = request.args.get("book_id")

    # user_update_likes(user_id, book_id)

    return ""
