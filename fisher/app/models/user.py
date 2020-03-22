from sqlalchemy import Column, Integer, String, Boolean, Float

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column("password", String(128), nullable=True)
    email = Column(String(50), unique=True, nullable=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        """
        getter
        :return: password
        """
        return self._password

    @password.setter
    def password(self, raw):
        """
        password的加密算法
        :param raw: 原始密码
        :return:
        """
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        """
        校验密码
        :param raw: 原始密码
        :return:
        """
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        """
        检测用户上传的图书是否符合规范
        :param isbn:
        :return:
        """
        if is_isbn_or_key(isbn):
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        # 书籍既不在赠送清单也不在心愿清单
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
