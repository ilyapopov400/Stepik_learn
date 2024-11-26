class Money:
    def __init__(self, value: (int, float)):
        self.__data_validate(value=value)
        self._money = value

    @staticmethod
    def __data_validate(value):
        if not isinstance(value, (int, float)):
            raise TypeError('сумма должна быть числом')

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self.__data_validate(value=money)
        self._money = money


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


if __name__ == "__main__":
    class MoneyR(Money, MoneyOperators):
        def __str__(self):
            return f"MoneyR: {self.money}"


    class MoneyD(Money, MoneyOperators):
        def __str__(self):
            return f"MoneyD: {self.money}"


    m1 = MoneyR(1)
    m2 = MoneyD(2)
    m = m1 + 10
    print(m)  # MoneyR: 11
    assert m.money == 11, "Error"

    m = m1 - 5.4
    print(m)  # MoneyR: -4.4
    assert m.money == -4.4, "Error"

    try:
        m = m1 + m2  # TypeError
    except TypeError:
        assert True
    else:
        assert False, "Error"
