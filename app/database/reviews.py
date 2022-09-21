from bson import ObjectId
from ..config import Pymongo

db = Pymongo.db


def review_findone(_id):
    """
    db.reviews에서 review_id로 검색
    """
    return db.reviews.find_one({"_id": ObjectId(_id)})


def review_find():
    """
    db.reviews 전체 리스트 가져오기
    """
    return ""


def review_insertone(doc):
    """
    db.reviews에 전달받은 데이터 삽입
    """
    review_id = db.reviews.insert_one(doc).inserted_id
    print(doc["username"], doc["book_id"])

    db.users.update_one({"username": doc["username"]}, {"$push": {"reviews": str(review_id)}})
    db.books.update_one({"_id": ObjectId(doc["book_id"])}, {"$push": {"reviews": str(review_id)}})

    return review_id


def review_deleteone(ids):
    """
    ids = { review_id, user_id, book_id }
    user와 book에서 해당 리뷰 아이디 삭제
    """
    review_id = ids["review_id"]
    user_id = ids["user_id"]
    book_id = ids["book_id"]

    db.users.update_one({"_id": user_id}, {"$pop": {"reviews": review_id}})
    db.books.update_one({"_id": book_id}, {"$pop": {"reviews": review_id}})
