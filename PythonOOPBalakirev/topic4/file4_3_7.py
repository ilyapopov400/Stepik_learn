class StringDigit(str):
    def __init__(self, value='', encoding=None, errors='strict'):
        self.__data_verification(data=value)
        super().__init__()

    @staticmethod
    def __data_verification(data):
        result = list(map(lambda x: x.isdigit(), data))

        if not all(result):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self.__data_verification(data=other)
        result = self.__class__(super().__add__(other))
        return result

    def __radd__(self, other):
        self.__data_verification(data=other)
        result = self.__class__(str(other) + str(self))
        return result


if __name__ == "__main__":
    sd = StringDigit("123")

    assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

    try:
        sd2 = StringDigit("123a")
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    sd = sd + "345"
    assert sd == "123345", "неверно отработал оператор +"
    sd = "0" + sd
    assert sd == "0123345", "неверно отработал оператор +"

    try:
        sd = sd + "12d"
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при выполнении оператора: +"

    try:
        sd = "12d" + sd
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
