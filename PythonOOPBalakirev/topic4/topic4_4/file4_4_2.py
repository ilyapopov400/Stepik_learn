class Furniture:
    def __init__(self, name: str, weight: (int, float)):
        self.__verify_name(name=name)
        self.__verify_weight(weight=weight)
        self._name = name
        self._weight = weight

    def __repr__(self):
        return "{}-{}".format(self._name, self._weight)

    @staticmethod
    def __verify_name(name: str):
        """
        - для проверки корректности имени
        """
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight):
        """
        - для проверки корректности веса
        """
        if not isinstance(weight, (int, float)) and weight < 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == "_name":
            self.__verify_name(name=value)
        if key == "_weight":
            self.__verify_weight(weight=value)
        super().__setattr__(key, value)


class Closet(Furniture):
    """
    - для представления шкафов
    """

    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        result = self.__dict__.items()
        result = filter(lambda x: x[0][0] == "_", result)
        result = map(lambda x: x[1], result)
        return tuple(result)


class Chair(Furniture):
    """
    - для представления стульев
    """

    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        result = self.__dict__.items()
        result = filter(lambda x: x[0][0] == "_", result)
        result = map(lambda x: x[1], result)
        return tuple(result)


class Table(Furniture):
    """
    - для представления столов
    """

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        result = self.__dict__.items()
        result = filter(lambda x: x[0][0] == "_", result)
        result = map(lambda x: x[1], result)
        return tuple(result)


if __name__ == "__main__":
    cl = Closet('шкаф-купе', 342.56, True, 3)
    chair = Chair('стул', 14, 55.6)
    tb = Table('стол', 34.5, 75, 10)
    print(tb.get_attrs())
