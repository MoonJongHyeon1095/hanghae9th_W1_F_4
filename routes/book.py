from flask import Blueprint
from ..config import Pymongo

book_bp = Blueprint("book", __name__, url_prefix="/book")
db = Pymongo.db


# 책 상세 페이지 렌더링
@book_bp.route("/")
def book_page():
    return ""


# 해당 책의 리뷰 리스트 반환
@book_bp.route("")
def book_review_list():
    return ""


# 리뷰 작성창         >> 모달 팝업 방식에 따라 안 쓸 수도 있어요.
@book_bp.route("")
def book_review_modal():
    return ""


# 리뷰 작성
@book_bp.route("")
def book_review_post():
    return ""