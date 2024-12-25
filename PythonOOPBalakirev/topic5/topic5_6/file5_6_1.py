class Ship:
    """
    - для представления кораблей
    """

    def __init__(self, length: int, x: int = None, y: int = None, tp: int = 1):
        """

        :param x: - координаты начала расположения корабля (целые числа)
        :param y: - координаты начала расположения корабля (целые числа)
        :param length:  - длина корабля (число палуб: целое значение: 1, 2, 3 или 4)
        :param tp:  - ориентация корабля (1 - горизонтальная; 2 - вертикальная)
        :_is_move:  - возможно ли перемещение корабля (изначально равно True).
                        При попадании в корабль (хотя бы одну его палубу),
                        флаг _is_move устанавливается в False
                        и перемещение корабля по игровому полю прекращается
        :_cells:  -изначально список длиной length,
                   состоящий из единиц (например, при length=3, _cells = [1, 1, 1])
                      Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля.
                      Если стоит 1, то попадания не было,
                      а если стоит значение 2, то произошло попадание в соответствующую палубу.
        """
        if not isinstance(length, int) or length not in range(1, 5):
            raise ValueError("не верные параметры длинны корабля")
        self.length = length
        self._x = x
        self._y = y
        self._tp = tp
        self._is_move = True
        self._cells = list(map(lambda x: 1, range(length)))

    @property
    def tp(self):
        return self._tp

    def __repr__(self):
        if self._tp == 1:
            orient = "горизонтальная"
        else:
            orient = "вертикальная"
        return "{}: x={}, y={}, ориентация: {}, трубы: {}".format(self.__class__.__name__,
                                                                  self._x, self._y, orient, self._cells)

    def set_start_coords(self, x: int, y: int):
        """
        - установка начальных координат (запись значений в локальные атрибуты _x, _y)
        """
        self._x, self._y = x, y

    def get_start_coords(self) -> tuple:
        """
        - получение начальных координат корабля в виде кортежа x, y
        """
        return self._x, self._y

    def move(self, go: int):  # TODO
        """
        - перемещение корабля в направлении его ориентации на go клеток
            (go = 1 - движение в одну сторону на клетку;
            go = -1 - движение в другую сторону на одну клетку);
            движение возможно только если флаг _is_move = True

        :param go: int
        :return: None
        """

    def is_collide(self, ship) -> bool:  # TODO
        """
        - проверка на столкновение с другим кораблем ship
              (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
              в том числе и по диагонали);
              метод возвращает True, если столкновение есть и False - в противном случае
        :param ship:
        :return:
        """
        self_x_start, self_y_start = self.get_start_coords()
        other_x_start, other_y_start = ship.get_start_coords()

        if self._tp == 1:
            self_x_end, self_y_end = self_x_start + self.length - 1, self_y_start
            """
            - self горизонтальный
            """
            if ship.tp == 1:
                """
                - self горизонтальный
                - other горизонтальный
                """
                other_x_end, other_y_end = other_x_start + ship.length - 1, other_y_start
                if abs(self_y_start - other_y_start) <= 1:
                    if self_x_start - other_x_end >= 2:
                        return False
                    if other_x_start - self_x_end >= 2:
                        return False
                    return True

            else:  # TODO
                """
                - self горизонтальный
                - other вертикальный
                """
        else:
            """
            - self вертикальный
            """
            self_x_end, self_y_end = self_x_start, self_y_start + self.length
            if ship.tp == 1:  # TODO
                """
                - self вертикальный
                - other горизонтальный
                """
            else:  # TODO
                """
                - self вертикальный
                - other вертикальный
                """
        return False

    def is_out_pole(self, size: int = 10) -> bool:
        """
        - проверка на выход корабля за пределы игрового поля
            (size - размер игрового поля, обычно, size = 10);
            возвращается булево значение True, если корабль вышел из игрового поля
            и False - в противном случае

        :param size: int
        :return:
        """
        if self._x + 1 > size or self._y + 1 > size:
            return True
        if self._x < 0 or self._y < 0:
            return True
        if self._tp == 1:
            """
            - при горизонтальном расположении
            """
            if self._x + self.length > size:
                return True
        else:
            """
            - при вертикальном расположении
            """
            if self._y + self.length > size:
                return True
        return False

    def __getitem__(self, item: int) -> int:
        """
        - считывание значения из _cells по индексу index (индекс отсчитывается от 0)
        :param item: int
        :return: int
        """
        if not isinstance(item, int) or item not in range(len(self._cells)):
            raise ValueError("значение индекса неверно")
        return self._cells[item]

    def __setitem__(self, key: int, value: int):
        """
        - запись нового значения в коллекцию _cells
        :param key: int
        :param value: int
        :return:
        """
        if not isinstance(key, int) or key not in range(len(self._cells)):
            raise ValueError("значение индекса неверно")
        if not isinstance(value, int) or value not in (1, 2):
            raise ValueError("обозначение палубы неверно")
        self._cells[key] = value


class GamePole:
    """
    - для описания игрового поля
    """


if __name__ == "__main__":
    a = Ship(length=4, x=2, y=2, tp=1)
    b = Ship(length=3, x=7, y=3, tp=1)

    assert a.is_out_pole(size=10) is False, "ошибка выхода за поле игры"
    assert b.is_out_pole(size=10) is False, "ошибка выхода за поле игры"

    a = Ship(length=4, x=2, y=2, tp=1)
    b = Ship(length=3, x=2, y=4, tp=1)
    assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

    a = Ship(length=4, x=2, y=2, tp=1)
    b = Ship(length=1, x=0, y=2, tp=1)
    assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

    a = Ship(length=4, x=2, y=2, tp=1)
    b = Ship(length=2, x=0, y=2, tp=1)
    assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, нет столкновения"

    a = Ship(length=4, x=2, y=2, tp=1)
    b = Ship(length=2, x=7, y=2, tp=1)
    assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

    a = Ship(length=4, x=2, y=2, tp=1)
    b = Ship(length=2, x=6, y=2, tp=1)
    assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, нет столкновения"
