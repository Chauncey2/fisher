from collections import namedtuple

from flask import current_app
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

# EachGiftWishCount=namedtuple('EachGiftWishCount',['count','isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_wish_counts(cls, isbn_list:list):
        """
        根据传入的一组isbn，到Wish表中检索出相应的礼物
        并且计算出某个礼物的isbn心愿清单
        :param isbn_list:
        :return:
        """
        count_list = db.session.query(func.count(Wish.id)).filter(Wish.launched == False,
                   Wish.isbn.in_(isbn_list),
                   Wish.status == 1).group_by(
                   Wish.isbn).all()
        count_list=[{'count':w[0],'isbn':w[1]} for w in count_list]

        return count_list

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['PECENT_BOOK_COUNT']).distinct().all()
        return recent_gift

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # @classmethod
    # def get_wish_counts(cls,isbn_list):
    #     count_list=[EachGiftWishCount(w[0],w[1]) for w in isbn_list]
