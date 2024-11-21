class Vector:
    _all_types = (int, float,)

    def __init__(self, *cords):
        self.__check_coords(cords)
        self.__cords = cords

    def __check_coords(self, cords):
        """
        - проверка типа переданных координат
        :param cords:
        :return:
        """
        res = map(lambda x: (type(x) in self._all_types), cords)
        if not all(res):
            raise ValueError("неверный тип")

    def __repr__(self):
        res = ', '.join(map(str, self.__cords))
        return "{}({})".format(self.__class__.__name__, res)

    def get_coords(self):
        return tuple(self.__cords)

    def __len__(self):
        return len(self.__cords)

    def __check_len(self, other):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

    def __make_vector(self, cords):
        try:
            return self.__class__(*cords)
        except:
            return Vector(*cords)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Правый операнд должен быть типом {}".format(self.__class__.__name__))

        self.__check_len(other)

        new_cords = tuple(map(lambda x: x[0] + x[1], zip(self.get_coords(), other.get_coords())))
        return self.__make_vector(new_cords)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError("Правый операнд должен быть типом {}".format(self.__class__.__name__))

        self.__check_len(other)

        new = map(lambda x: x[0] - x[1], zip(self.get_coords(), other.get_coords()))
        return self.__class__(*new)


class VectorInt(Vector):
    _all_types = (int,)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(3, 4, 5)
    assert (v1 + v2).get_coords() == (
        4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
    assert (v1 - v2).get_coords() == (
        -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
    v = VectorInt(1, 2, 3, 4)
    assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
    try:
        v = VectorInt(1, 2, 3.4, 4)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

    v1 = VectorInt(1, 2, 3, 4)
    v2 = VectorInt(4, 2, 3, 4)
    v3 = Vector(1.0, 2, 3, 4)
    v = v1 + v2
    assert type(
        v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
    v = v1 + v3
    assert type(
        v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
