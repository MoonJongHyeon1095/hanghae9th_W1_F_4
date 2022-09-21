from flask import Blueprint, render_template, jsonify
from ..config import Pymongo
from ..util import *

index_bp = Blueprint("index", __name__)
db = Pymongo.db


# 메인페이지 렌더링
@index_bp.route("/")
def home_page():
    checked_token = token_check()
    token_info = bool(checked_token)

    return render_template("index.html", token_info = token_info)


# book 전체 리스트 반환
@index_bp.route("/book/list")
def book_list():
    book_list = db.books.find({},{"_id":False})
    return jsonify({'book_list':book_list})