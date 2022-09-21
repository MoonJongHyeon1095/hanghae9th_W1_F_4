from flask import Blueprint, request, render_template, jsonify
from ..config import Pymongo
from ..util import *


book_bp = Blueprint("book", __name__, url_prefix="/book")
db = Pymongo.db

# 책 상세 페이지 렌더링
@book_bp.route("/")
def book_page():
    checked_token = token_check()
    token_info = bool(checked_token)

    # DB에서 저장된 책 찾아서 HTML에 불러오기
    return render_template("book.html", token_info=token_info)

# 해당 상세정보
@book_bp.route("/view/")
def book_detail():
    # db에서 결과 보내기
    bookid_receive = request.args.get("book_id")
    bookView = list(db.books.find({"isbn":bookid_receive}))[0]
    book_id = bookView["_id"]
    return render_template("book.html", bookView=bookView, book_id=book_id)


# 해당 책의 리뷰 리스트 반환
@book_bp.route("/list", methods=["GET"])
def book_list():
    books = list(db.books.find({},{"_id": False}))
    return jsonify({"books":books})


@book_bp.route("/review", methods=["GET"])
def bookReview_list():
    reviews = list(db.reviews.find({},{"_id": False}))
    return jsonify({"reviews":reviews})


# 리뷰 작성창     >> 모달 팝업 방식에 따라 안 쓸 수도 있어요.
@book_bp.route("/")
def book_review_modal():
    return ""


# 리뷰 작성
@book_bp.route("/")
def book_review_post():
    return ""


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
