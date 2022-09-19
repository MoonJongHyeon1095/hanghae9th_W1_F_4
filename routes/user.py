from flask import Blueprint
from ..config import Pymongo

user_bp = Blueprint("user", __name__, url_prefix="/user")
db = Pymongo.db


# 회원가입 페이지 렌더링
@user_bp.route("/")
def user_signup_page():
    return ""


# 회원가입 요청
@user_bp.route("")
def user_signup():
    return ""


# 로그인 창         >> 모달 팝업 방식에 따라 안 쓸 수도 있어요.
@user_bp.route("")
def user_signin_modal():
    return ""


# 로그인 요청
@user_bp.route("")
def user_signin():
    return ""