from flask import Blueprint, render_template, jsonify
from datetime import datetime
from ..database import *
from ..util import *

from ..config import Pymongo
db = Pymongo.db

mypage_bp = Blueprint("mypage", __name__, url_prefix="/mypage")


# 마이페이지 렌더링
@mypage_bp.route("/")
def mypage_page():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)
    # return render_template("mypage.html", user=user)

    username = "testtest"
    user = db.users.find_one({"username": username}, {"_id": False})
    return render_template("mypage.html", user=user)



# 내 리뷰 리스트 반환
@mypage_bp.route("/reviews")
def mypage_reviews_list():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)
    # review_ids = user["reviews"]

    # result = []
    # for r_id in review_ids:
    #     review = review_findone(r_id)
    #     review["time"] = str(datetime.fromtimestamp(int(review["time"])))
    #     result.append(review)
    # result.reverse()

    # return jsonify({ "reviews": result })

    username = "testtest"
    user = db.users.find_one({"username": username})
    review_ids = user["reviews"]

    result = []
    for r_id in review_ids:
        from bson import ObjectId
        review = db.reviews.find_one({"_id": ObjectId(r_id)})
        review["_id"] = r_id
        review["time"] = str(datetime.fromtimestamp(int(review["time"])))
        result.append(review)
    result.reverse()
    

    return jsonify({ "reviews": result })

    return ""


# 내 좋아요 책 리스트 반환
@mypage_bp.route("/likes")
def mypage_likes_list():
    # payload = token_check()
    # user_id = payload["user_id"]
    # user = user_findone(user_id)
    # book_ids = user["likes"]

    # result = []
    # for b_id in book_ids:
    #     book = book_findone(r_id)
    #     result.append(book)
    # return jsonify({ "books": result, "user_id": user_id })

    user_id = "632948bf97d615c443052562"
    from bson import ObjectId
    user = db.users.find_one({"_id": ObjectId(user_id)}, {"_id": False})
    book_ids = user["likes"]

    result = []
    for b_id in book_ids:
        from bson import ObjectId
        book = db.books.find_one({"_id": ObjectId(b_id)})
        book["_id"] = b_id
        book["flag"] = True if user_id in book["likes"] else False
        result.append(book)
    return jsonify({ "books": result })

    return ""


# 프로필 수정창
@mypage_bp.route("/profile")
def mypage_profile_modal():
    # payload = token_check()
    # username = payload["username"]
    # user = user_findone(username)

    # return render_template("profile.html", user=user)

    return render_template("/modals/profile.html")


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