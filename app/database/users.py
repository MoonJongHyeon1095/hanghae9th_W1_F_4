from bson import ObjectId
from ..config import Pymongo

db = Pymongo.db


def user_findone(user):
    """
    : db.users에서 username 혹은 user_id에 해당하는 사용자 정보 가져오기.
    : 반드시 문자열로 주세요
    """
    if len(user) == 24:
        return db.users.find_one({"_id": ObjectId(user)})
    else:
        return db.users.find_one({"username": user})


def user_findone_email(email):
    """
    db.users에서 email에 해당하는 사용자 정보 가져오기
    """
    return db.users.find_one({"email": email})


def user_upsertone(doc):
    id = db.users.update_one({"email": doc["email"]}, {"$set": doc}, upsert=True).upserted_id
    return user_findone_email(doc["email"])["_id"] if id is None else id


# def user_insertone(doc):
#     """
#     db.users에 사용자 등록 및 수정. 등록 혹은 수정한 사용자 _id 반환
#     """
#     # doc["_id"] = doc["_id"] if "_id" in doc else None
#     return db.users.insert_one(doc).inserted_id


# def user_updateone(doc):
#     """
#     db.users에 사용자 정보 수정
#     """
#     return db.users.update_one({"email": doc["email"]}, {"$set": doc})


def push_likes(user_id, book_id):
    """
    user_id와 book_id를 받아서
    각각 해당 user와 book likes 리스트에 book_id와 user_id를 추가
    """
    db.books.update_one({"_id": ObjectId(book_id)}, {"$push": {"likes": user_id}})
    db.users.update_one({"_id": ObjectId(user_id)}, {"$push": {"likes": book_id}})


def pull_likes(user_id, book_id):
    """
    user_id와 book_id를 받아서
    각각 해당 user와 book likes 리스트에 book_id와 user_id를 추가
    """
    db.books.update_one({"_id": ObjectId(book_id)}, {"$pull": {"likes": user_id}})
    db.users.update_one({"_id": ObjectId(user_id)}, {"$pull": {"likes": book_id}})

