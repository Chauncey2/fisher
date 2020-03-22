from sqlalchemy.orm import relationship
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
