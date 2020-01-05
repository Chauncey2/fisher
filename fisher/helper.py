
def is_isbn_or_key(word):
    """
    判断传入的字符串是key或者是isbn
    :param word:
    :return: str
    """
    isbn_or_key='key'
    if len(word)==13 and word.isdigit():
        isbn_or_key='isbn'
    short_word=word.replace('-','')
    if '-' in word and len(word)==10 and word.isdigit():
        isbn_or_key='isbn'
    return isbn_or_key