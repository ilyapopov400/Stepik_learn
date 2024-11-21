import random


class Digit:
    """
    - любое число
    """

    def __init__(self, value):
        self.__check_value(value=value)
        self.value = value

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')

    def __repr__(self):
        return str(self.value)


class Integer(Digit):
    """
    - целое число
    """

    def __init__(self, value):
        self.__check_value(value=value)
        super().__init__(value=value)

    @staticmethod
    def __check_value(value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    """
    - вещественное число
    """

    def __init__(self, value):
        self.__check_value(value=value)
        super().__init__(value=value)

    @staticmethod
    def __check_value(value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    """
    - положительное число
    """

    def __init__(self, value):
        self.__check_value(value=value)
        super().__init__(value=value)

    @staticmethod
    def __check_value(value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        self.__check_value(value=value)
        super().__init__(value=value)

    @staticmethod
    def __check_value(value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


if __name__ == "__main__":
    prime_number = list(map(lambda x: PrimeNumber(random.randint(1, 10)), range(3)))
    float_positive = list(map(lambda x: FloatPositive(random.random() * 100), range(6)))

    digits = list(prime_number + float_positive)

    lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
    lst_float = list(filter(lambda x: isinstance(x, Float), digits))

    print(lst_positive)
    print(lst_float)
