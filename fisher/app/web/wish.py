from flask import flash, redirect, url_for
from flask_login import current_user, login_required

from app.models.base import db
from app.models.wish import Wish
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish(isbn):
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # auto_commit为自定义上下文管理器
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash("书籍已经存在心愿清单或者愿望清单中")
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
