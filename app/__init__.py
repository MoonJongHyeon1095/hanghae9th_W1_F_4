from flask import Flask
from .config import *


# 라우터
def router(flask_app: Flask):
    from .api import book_bp, index_bp, mypage_bp, user_bp

    flask_app.register_blueprint(book_bp)
    flask_app.register_blueprint(index_bp)
    flask_app.register_blueprint(mypage_bp)
    flask_app.register_blueprint(user_bp)


# 애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SSN
    router(app)

    return app