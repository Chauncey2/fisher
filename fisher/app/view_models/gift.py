from collections import namedtuple

MyGift = namedtuple('MyGift', ['id', 'book', 'count'])


class MyGifts:
    def __init__(self, gift_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gift_of_mine
        self.__wish_count_list = wish_count_list

    def __parse(self):
        for gift in self.__gifts_of_mine:
            self.__match(gift)

    def __match(self, gift):
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        my_gift = MyGift(gift.id, gift.book, count)
        return my_gift
