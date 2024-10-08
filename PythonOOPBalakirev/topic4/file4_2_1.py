class ListInteger(list):
    def __init__(self, ls: list):
        super().__init__(ls)
        self.__data_checking(ls=ls)

    def __setitem__(self, key, value):
        self.__data_checking(value)
        super().__setitem__(key, value)

    def append(self, __object) -> None:
        self.__data_checking(__object)
        super().append(__object)

    @staticmethod
    def __data_checking(ls):
        if hasattr(ls, "__iter__"):
            if not all(map(lambda x: isinstance(x, int), ls)):
                raise TypeError('можно передавать только целочисленные значения')
        else:
            if not isinstance(ls, int):
                raise TypeError('можно передавать только целочисленные значения')


if __name__ == "__main__":
    a = ListInteger((1, 2))
    a.append(22)
    print(a)
    print(a[2])
    a[2] = 33
    print(a)
