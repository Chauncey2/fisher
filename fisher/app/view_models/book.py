
class BookViewModel:

    @classmethod
    def package_single(cls,data,keyword):
        """
        返回单本书籍信息
        :param data:
        :param keyword:
        :return: dict
        """
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books']=[cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls,data,keyword):
        """
        返回多本书籍信息
        :param data:
        :param keyword:
        :return: dict
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls,data):
        """
        裁剪数据数据
        :param data:
        :return:dict
        """
        book={
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'],
        }
        return book