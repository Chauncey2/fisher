from flask import Flask

from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = "请先登录或注册"

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        user = db.session.query(User).get(user_id)
        return user

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
