class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight


class DictShop(dict):
    def __init__(self, dc=None):
        if not dc:
            dc = dict()
        self.__data_checking(dc=dc)
        super().__init__(dc)

    @staticmethod
    def __data_checking(dc):
        if isinstance(dc, dict):
            res = map(lambda x: isinstance(x, Thing), dc.keys())
            if not all(res):
                raise TypeError('ключами могут быть только объекты класса Thing')
        else:
            if not isinstance(dc, Thing):
                raise TypeError('ключами могут быть только объекты класса Thing')

    def __setitem__(self, key, value):
        self.__data_checking(key)
        super().__setitem__(key, value)


if __name__ == "__main__":
    th_1 = Thing('Лыжи', 11000, 1978.55)
    th_2 = Thing('Книга', 1500, 256)

    dict_things = DictShop()
    dict_things[th_1] = th_1
    dict_things[th_2] = th_2
    for x in dict_things:
        print(x.name)

    try:
        dict_things[1] = th_1
    except TypeError:
        assert True, "исключение TypeError"

    dc = {
        "th_1": th_1,
        th_2: th_2,
    }

    try:
        dt = DictShop([th_1, th_2])
    except TypeError:
        assert True, "исключение TypeError"
