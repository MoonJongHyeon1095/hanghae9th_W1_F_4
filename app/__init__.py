from flask import Flask

def router(flask_app: Flask):
    from .api import book_bp, index_bp, mypage_bp, user_bp

    flask_app.register_blueprint(book_bp)
    flask_app.register_blueprint(index_bp)
    flask_app.register_blueprint(mypage_bp)
    flask_app.register_blueprint(user_bp)


def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="hanghaeF4"
    )
    router(app)

    return app