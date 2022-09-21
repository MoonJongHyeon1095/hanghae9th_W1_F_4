from flask import Blueprint, render_template, jsonify, request, url_for, session
import requests
from ..config import Pymongo

index_bp = Blueprint("index", __name__)
db = Pymongo.db

from ..database import *

# 메인페이지 렌더링
@index_bp.route("/")
def home_page():
    if session.get("login") is None:
        return render_template("index.html")
    flag = session.get("login")
    session.clear()
    return render_template("index.html", flag=flag)


# book 전체 리스트 반환
@index_bp.route("/book/list")
def book_list():
    book_list = db.books.find({},{"_id":False})
    return jsonify({'book_list':book_list})