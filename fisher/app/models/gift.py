from flask import current_app
from sqlalchemy.orm import relationship
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['PECENT_BOOK_COUNT']).distinct().all()

        return recent_gift
