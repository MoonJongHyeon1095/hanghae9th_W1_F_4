from flask import Blueprint, render_template
from ..config import Pymongo
from ..database import *
from ..util import *

mypage_bp = Blueprint("mypage", __name__, url_prefix="/mypage")
db = Pymongo.db


# 마이페이지 렌더링
@mypage_bp.route("/")
def mypage_page():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)
    # return render_template("mypage.html", user=user)
    return render_template("mypage.html")


# 내 리뷰 리스트 반환
@mypage_bp.route("/likes")
def mypage_likes_list():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)
    # review_ids = user["reviews"]

    # result = []
    # for r_id in review_ids:
    #     review = review_findone(r_id)
    #     result.append(review)
    # return jsonify({ "reviews": result })

    return ""


# 내 좋아요 책 리스트 반환
@mypage_bp.route("/reviews")
def mypage_reviews_list():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)
    # book_ids = user["likes"]

    # result = []
    # for b_id in book_ids:
    #     book = book_findone(r_id)
    #     result.append(book)
    # return jsonify({ "books": result })

    return ""


# 프로필 수정창
@mypage_bp.route("/profile")
def mypage_profile_modal():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)

    # return render_template("profile.html", user=user)

    return render_template("profile.html")


# 프로필 수정
@mypage_bp.route("/profile", methods=["POST"])
def mypage_profile_update():
    # payload = token_check()
    # user_id = payload["user_id"]
    # user = user_findone(user_id)

    # doc = {
    #    "user_id": user_id,
    #    "password": password_hash(request.form.get("password")),
    #    "username": request.form.get("username"),
    #    "image": ""
    # }
    # 
    return ""