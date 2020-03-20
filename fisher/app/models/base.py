from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # hasattr\setattr python中的动态赋值
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
