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

def review_upsertone(doc):
    """
    db.reviews에 전달받은 데이터 삽입
    """
    id = doc["_id"] if "_id" in doc else None
    return db.reviews.update_one({"_id": ObjectId(id)}, {"$set": doc}, upsert=True).upserted_id


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
