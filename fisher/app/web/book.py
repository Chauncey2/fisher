from flask import jsonify,request
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

@web.route('/book/search')
def search():

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data.strip()

        isbn_or_key=is_isbn_or_key(q)
        if isbn_or_key=='isbn':
            result=YuShuBook.search_by_isbn(q)
        else:
            result=YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
    else:
        return jsonify(form.err)