from flask import Blueprint, render_template, jsonify, request, session

from ..config import *
from ..database import *
from ..util import *


user_bp = Blueprint("user", __name__, url_prefix="/user")


# 회원가입 페이지 렌더링
@user_bp.route("/sign_up")
def user_signup_page():
    checked_token = token_check()
    token_info = bool(checked_token)
    return render_template('signup.html', token_info=token_info)


# 회원가입 이메일 중복체크
@user_bp.route('/check_dup', methods=['POST'])
def check_dup():
    email_receive = request.form['email_give']
    exists = bool(user_findone_email(email_receive))
    return jsonify({'result': 'success', 'exists': exists})


# 회원가입 요청
@user_bp.route("/sign_up/save", methods=['POST'])
def user_signup():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    username_receive = request.form['username_give']

    doc = {
        "email": email_receive,  # 로그인 아이디
        "password": password_hash(password_receive),  # 비밀번호
        "username": username_receive,  # 서비스 내 표시되는 사용자의 이름
        "likes": [],
        "reviews": [],
        "image": "",
        "image_data": "/static/profiles/profile_default.png",
    }

    user_id = user_upsertone(doc)
    print(user_id)

    return jsonify({'result': 'success'})


@user_bp.route("/sign_in")
def user_signin_modal():
    print("!!!")
    return render_template("modals/signin.html")


# 로그인 요청
@user_bp.route('/sign_in', methods=['POST'])
def user_signin():
    # 로그인
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    user = db.users.find_one({'email': email_receive, 'password': password_hash(password_receive)})

    if user is not None:
        token = create_token(user)
        session.clear()
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '이메일/비밀번호가 일치하지 않습니다.'})
