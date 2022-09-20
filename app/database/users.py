from ..config import Pymongo
from bson import ObjectId


db = Pymongo.db


def user_findone(user):
    """
    db.users에서 username 혹은 user_id에 해당하는 사용자 정보 가져오기
    """
    if len(user) == 24:
        return db.users.find_one({"_id": ObjectId(user)})
    else:
        return db.users.find_one({"username": user})


def user_insertone(doc):
    """
    db.users에 사용자 등록
    """
    return ""


def user_updateone(doc):
    """
    db.users에 사용자 정보 수정
    """
    result = db.users.update_one({"_id": doc["user_id"]}, {"set": doc}, upsert=True)

    if result.upserted_id is not None:
        return "프로필을 수정했습니다."        


def user_update_likes(user_id, book_id):
    """
    user_id와 book_id를 받아서
    각각 해당 user와 book likes 리스트에 book_id와 user_id를 추가
    """
    db.books.update_one({"_id": book_id}, {"$push": {"likes": user_id}})
    db.users.update_one({"_id": user_id}, {"$push": {"likes": book_id}})