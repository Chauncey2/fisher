from flask import jsonify,request

from app.view_models.book import  BookCollection
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
import json

@web.route('/book/search')
def search():
    """
    视图函数，根据关键字搜索书籍信息
    :return: json序列化数据
    """
    # 信息验证
    form = SearchForm(request.args)
    # 实例化book
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key=is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key=='isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)

        books.fill(yushu_book,q)
        return json.dumps(books, default=lambda obj: obj.__dict__)
    else:
        return jsonify(form.err)