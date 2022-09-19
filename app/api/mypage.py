from flask import Blueprint, render_template
from ..config import Pymongo

mypage_bp = Blueprint("mypage", __name__, url_prefix="/mypage")
db = Pymongo.db


# 마이페이지 렌더링
@mypage_bp.route("/")
def mypage_page():
    return render_template("mypage.html")


# 내 리뷰 리스트 반환
@mypage_bp.route("/likes")
def mypage_likes_list():
    return ""


# 내 좋아요 책 리스트 반환
@mypage_bp.route("/reviews")
def mypage_reviews_list():
    return ""


# 프로필 수정창
@mypage_bp.route("/profile")
def mypage_profile_modal():
    return render_template("profile.html")


# 프로필 수정
@mypage_bp.route("/profile", methods=["POST"])
def mypage_profile_update():
    return ""