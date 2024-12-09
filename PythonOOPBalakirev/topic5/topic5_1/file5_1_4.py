class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.__validate_date(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    def __repr__(self):
        return "({}_{}_{})".format(self._a, self._b, self._c)

    @staticmethod
    def __validate_date(a, b, c):
        if not all(map(lambda x: isinstance(x, (int, float)), (a, b, c))) or not all(map(lambda x: x > 0, (a, b, c))):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a >= (b + c) or b >= (a + c) or c >= (a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


if __name__ == "__main__":
    input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

    lst_tr = list()
    for triangle in input_data:
        try:
            lst_tr.append(Triangle(*triangle))
        except:
            pass
    print(lst_tr)
