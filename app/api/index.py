
from flask import Blueprint, render_template, jsonify, session

from ..config import Pymongo
from ..database import *
from ..util import *

index_bp = Blueprint("index", __name__)
db = Pymongo.db


# 메인페이지 렌더링
@index_bp.route("/")
def home_page():
    checked_token = token_check()
    token_info = bool(checked_token)

    if session.get("login") is None:
        return render_template("index.html", token_info=token_info)
    flag = session.get("login")
    session.clear()
    return render_template("index.html", flag=flag, token_info=token_info)


# book 전체 리스트 반환
@index_bp.route("/list")
def book_list():
    b_lists = list(db.books.find({},{"_id":False}))
    return jsonify({"b_list" : b_lists})





