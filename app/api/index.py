from flask import Blueprint, render_template
from ..config import Pymongo

index_bp = Blueprint("index", __name__)
db = Pymongo.db


# 메인페이지 렌더링
@index_bp.route("/")
def home_page():
    return render_template("index.html")


# book 전체 리스트 반환
@index_bp.route("/")
def book_list():
    return ""