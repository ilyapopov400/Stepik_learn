class Rect:
    def __init__(self, x: (int, float), y: (int, float), width: (int, float), height: (int, float)):
        self.__validate_input_date(x, y, width, height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __repr__(self):
        return "(x={}, y={}, width={}, height={})".format(self._x, self._y, self._width,
                                                          self._height)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @staticmethod
    def __validate_input_date(x, y, width, height):
        if not all(map(
                lambda number: isinstance(number, (int, float)), (x, y, width, height)
        )) or not all(map(lambda number: number > 0, (width, height))):
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def is_collision(self, rect):  # TODO
        if not isinstance(rect, self.__class__):
            raise TypeError("некорректный класс {}".format(rect.__class__.__name__))

        ax1, ay1 = self._x, self._y
        ax2, ay2 = self._x + self._width, self._y + self._height

        bx1, by1 = rect.x, rect.y
        bx2, by2 = rect.x + rect.width, rect.y + rect.height

        if (
                (ax1 < bx2) and (ax2 > bx1) and (ay1 < by2) and (ay2 > by1)
        ):
            raise TypeError('прямоугольники пересекаются')


lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1),

]


def result_f(ls: list):
    result = set()
    for rect1 in ls:
        try:
            for rect2 in ls:
                if rect1.__hash__() != rect2.__hash__():
                    rect1.is_collision(rect2)
        except TypeError:
            pass
        else:
            result.add(rect1)
    result = list(result)
    return result


lst_not_collision = result_f(ls=lst_rect)

if __name__ == "__main__":
    r = Rect(1, 2, 10, 20)
    assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"
    r2 = Rect(1.0, 2, 10.5, 20)
    try:
        r2 = Rect(0, 2, 0, 20)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"

    assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
    assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"


    def not_collision(rect):
        for x in lst_rect:
            try:
                if x != rect:
                    rect.is_collision(x)
            except TypeError:
                return False
        return True


    f = list(filter(not_collision, lst_rect))
    assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"
    r = Rect(3, 2, 2, 5)
    rr = Rect(1, 4, 6, 2)
    try:
        r.is_collision(rr)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
