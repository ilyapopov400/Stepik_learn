class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    def __repr__(self):
        return str(self.__value)

    def __validate_value(self, value) -> bool:
        result = bool(self._min_value <= value <= self._max_value)
        if not result:
            raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
        return result

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__validate_value(value=value)
        self.__value = value


class CellFloat:
    def __init__(self, min_value: float, max_value: float):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    def __repr__(self):
        return str(self.__value)

    def __validate_value(self, value) -> bool:
        result = bool(self._min_value <= value <= self._max_value)
        if not result:
            raise CellFloatException('значение выходит за допустимый диапазон')  # для объектов класса CellFloat
        return result

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__validate_value(value=value)
        self.__value = value


class CellString:
    def __init__(self, min_length: int, max_length: int):
        self._min_length = min_length
        self._max_length = max_length
        self.__value = None

    def __repr__(self):
        if self.__value:
            return self.__value
        return str(self.__value)

    def __validate_value(self, value) -> bool:
        if not isinstance(value, str):
            raise TypeError
        result = bool(self._min_length <= len(value) <= self._max_length)
        if not result:
            raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
        return result

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__validate_value(value=value)
        self.__value = value


class TupleData:
    def __init__(self, *args):
        self._data = list(args)

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index not in range(len(self._data) + 1):
            raise IndexError
        self._data[index] = value

    def __getitem__(self, index):
        if not isinstance(index, int) or index not in range(len(self._data) + 1):
            raise IndexError
        return self._data[index]

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
    d = (1, 0, 'sergey')
    t[0] = d[0]
    t[1] = d[1]
    t[2] = d[2]
    for i, x in enumerate(t):
        assert x == d[i], "объект класса TupleData хранит неверную информацию"
    assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

    cell = CellFloat(-5, 5)
    try:
        cell.value = -6.0
    except CellFloatException:
        assert True
    else:
        assert False, "не сгенерировалось исключение CellFloatException"

    cell = CellInteger(-1, 7)
    try:
        cell.value = 8
    except CellIntegerException:
        assert True
    else:
        assert False, "не сгенерировалось исключение CellIntegerException"

    cell = CellString(5, 7)
    try:
        cell.value = "hello world"
    except CellStringException:
        assert True
    else:
        assert False, "не сгенерировалось исключение CellStringException"
    assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException,
                                                                          CellException) and issubclass(
        CellStringException,
        CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
