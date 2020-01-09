from flask import jsonify,request

from app.view_models.book import BookViewModel
from . import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

@web.route('/book/search')
def search():

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key=is_isbn_or_key(q)
        if isbn_or_key=='isbn':
            result=YuShuBook.search_by_isbn(q)
            result=BookViewModel.package_single(result,q)
        else:
            result=YuShuBook.search_by_keyword(q,page)
            result = BookViewModel.package_collection(result, q)

        # # 缓存书籍信息
        # book=query_from_mysql()
        # if book:
        #     return book
        # else:
        #     save(result)

        return jsonify(result)
    else:
        return jsonify(form.err)