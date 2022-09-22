from flask import Blueprint, render_template, jsonify, request, session, redirect
from werkzeug.utils import secure_filename
from datetime import datetime
import sys

from ..database import *
from ..util import *


mypage_bp = Blueprint("mypage", __name__, url_prefix="/mypage")


# 마이페이지 렌더링
@mypage_bp.route("/")
def mypage_page():
    payload = token_check()
    if payload is not None:
        user_id = payload["user_id"]
        user = user_findone(user_id)
        session["login"] = "true"

        user["profile"] = user["image_data"].split("static")[1]

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

    return render_template("/modals/profile.html", user=user)


# 프로필 수정
@mypage_bp.route("/profile", methods=["POST"])
def mypage_profile_update():
    payload = token_check()

    if "image" in request.files:
        image = request.files["image"]
        filename = secure_filename(image.filename)
        extension = filename.split(".")[-1]

        file_path = sys.path[0]+"/app/static/profiles/"+ payload['user_id'] + "." + extension
        image.save(file_path)
        
        doc = {
            "email": payload["email"],
            "username": request.form.get("username"),
            "password": password_hash(request.form.get("password")),
            "image": filename,
            "image_data": file_path,
        }    
    user_id = user_upsertone(doc)

    user = user_findone(str(user_id))
    token = create_token(user)
    session.clear()

    return jsonify({ "msg": "회원 정보를 수정했습니다.", "mytoken": token })



# 임시 로그인
@mypage_bp.route("/signin", methods=["GET"])
def testsignin():
    user_id = "632948bf97d615c443052562"
    user = user_findone(user_id)
    token = create_token(user)

    return jsonify({ "token": token })
