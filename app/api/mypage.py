from flask import Blueprint, render_template, jsonify, request, session, redirect
from datetime import datetime
from ..database import *
from ..util import *

from ..config import Pymongo
db = Pymongo.db

mypage_bp = Blueprint("mypage", __name__, url_prefix="/mypage")


# 마이페이지 렌더링
@mypage_bp.route("/")
def mypage_page():
    payload = token_check()
    if payload is not None:
        user_id = payload["user_id"]
        user = user_findone(user_id)
        session["login"] = "true"

        return render_template("mypage.html", user=user)
    else:
        session["login"] = "false"
        return redirect("/")


@mypage_bp.route("/401")
def mypage_nav():
    print("this is nav")
    return render_template("401.html")



# 내 리뷰 리스트 반환
@mypage_bp.route("/reviews")
def mypage_reviews_list():
    payload = token_check()
    user_id= payload["user_id"]
    user = user_findone(user_id)
    review_ids = user["reviews"]

    result = []
    for r_id in review_ids:
        review = review_findone(r_id)
        review["_id"] = r_id
        review["time"] = str(datetime.fromtimestamp(int(review["time"])))
        result.append(review)

    result.reverse()
    return jsonify({ "reviews": result })


# 내 좋아요 책 리스트 반환
@mypage_bp.route("/likes")
def mypage_likes_list():
    payload = token_check()
    user_id = payload["user_id"]
    user = user_findone(user_id)
    book_ids = user["likes"]

    result = []
    for b_id in book_ids:
        book = book_findone_id(b_id)
        book["_id"] = b_id
        book["flag"] = True if user_id in book["likes"] else False
        result.append(book)

    return jsonify({ "books": result })


# 프로필 수정창
@mypage_bp.route("/profile")
def mypage_profile_modal():
    payload = token_check()
    user_id = payload["user_id"]
    user = user_findone(user_id)

    return render_template("modals/profile.html", user=user)


# 프로필 수정
@mypage_bp.route("/profile", methods=["POST"])
def mypage_profile_update():
    payload = token_check()
    user_id = payload["user_id"]

    doc = {
       "_id": user_id,
       "email": payload["email"],
       "username": request.form.get("username"),
       "password": password_hash(request.form.get("password")),
       "image": request.files.get("image"),
    }
    user_upsertone(doc)
    print(doc)

    return ""




# 임시 로그인
@mypage_bp.route("/signin", methods=["GET"])
def testsignin():
    user_id = "632948bf97d615c443052562"
    user = user_findone(user_id)
    token = create_token(user)

    return jsonify({ "token": token })



@mypage_bp.route("/test")
def test():
    payload = token_check()

    doc = {
        # "_id": payload["user_id"],
        "email": "sparta@hanghae.com",
        "username": "whoami",
        "password": password_hash("qwe123123"),
    }
    user_id = user_upsertone(doc)
    print(user_id)

    return "success"