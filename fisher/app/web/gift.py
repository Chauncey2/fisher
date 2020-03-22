from flask import current_app, flash
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from . import web

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.id = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash("书籍已经存在心愿清单或者愿望清单中")


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
