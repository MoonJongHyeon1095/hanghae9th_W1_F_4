from flask import request
from datetime import datetime, timedelta
import hashlib
import jwt

from ..config import *


def password_hash(password):
    """
    password를 해쉬 암호화하여 반환
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def create_token(user):
    """
    사용자 정보를 받아서 로그인 토큰 생성
    """
    payload = {
        "user_id": str(user["_id"]),
        "email": user["email"],
        "username": user["username"],
        "exp": datetime.utcnow() + timedelta(seconds=60 * 60),
    }
    return jwt.encode(payload, KEY, algorithm="HS256")#.decode('utf-8')


def token_check():
    """
    현재 세션의 로그인 토큰 유효성 확인 이후 payload 혹은 None 반환
    """
    print("token check")
    token = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token, KEY, algorithms="HS256")
        return payload
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return None
