from sqlalchemy import Column, Integer, String, Boolean, Float
from app.models.base import Base
from werkzeug.security import generate_password_hash


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column("password", String(128))
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
