import hashlib
import datetime
import jwt
from datetime import datetime, timedelta

from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from ..config import Pymongo

user_bp = Blueprint("user", __name__, url_prefix="/user")
db = Pymongo.db

SECRET_KEY = 'SPARTA'


# 회원가입 페이지 렌더링
@user_bp.route("/sign_up")
def user_signup_page():
    return render_template('signup.html')

# 회원가입 이메일 중복체크
@user_bp.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    email_receive = request.form['email_give']
    exists = bool(db.users.find_one({"email": email_receive}))
    return jsonify({'result': 'success', 'exists': exists})

# 회원가입 요청
@user_bp.route("/sign_up/save", methods=['POST'])
def user_signup():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    username_receive = request.form['username_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    doc = {
        "email": email_receive,  # 로그인 아이디
        "password": password_hash,  # 비밀번호
        "username": username_receive,  # 서비스 내 표시되는 사용자의 이름

    }

    db.users.insert_one(doc)

    return jsonify({'result': 'success'})


# 로그인 창         >> 모달 팝업 방식에 따라 안 쓸 수도 있어요.
@user_bp.route("/")
def user_signin_modal():
    return ""


# 로그인 요청
@user_bp.route('/sign_in', methods=['POST'])
def user_signin():

    # 로그인
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'email': email_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'email': email_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60)  # 로그인 1시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')#.decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '이메일/비밀번호가 일치하지 않습니다.'})
