from flask import Blueprint, request
from ..config import Pymongo


book_bp = Blueprint("book", __name__, url_prefix="/book")
db = Pymongo.db


# 책 상세 페이지 렌더링
@book_bp.route("/")
def book_page():
    return ""


# 해당 책의 리뷰 리스트 반환
@book_bp.route("/")
def book_review_list():
    return ""


# 리뷰 작성창         >> 모달 팝업 방식에 따라 안 쓸 수도 있어요.
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
