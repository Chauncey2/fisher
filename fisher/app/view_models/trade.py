class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__prase(goods)

    def __prase(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            return dict(
                user_name=single.user.nickname,
                time=single.create_datetime.strftime('%Y-%m-%d'),
                id=single.id
             )
        else:
            time='未知'

        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )

