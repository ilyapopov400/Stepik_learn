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

    def _get_cords(self) -> list:
        """
        - получаем список координат с головы корабля
        :return: tuple
        """
        result = list()
        if self._tp == 1:
            for x in range(self.length):
                coord = self._x + x, self._y
                result.append(coord)
        else:
            for y in range(self.length):
                cords = self._x, self._y + y
                result.append(cords)
        return result

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

    def is_collide(self, ship) -> bool:
        """
        - проверка на столкновение с другим кораблем ship
              (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
              в том числе и по диагонали);
              метод возвращает True, если столкновение есть и False - в противном случае
        :param ship:
        :return:
        """
        for self_cord in self._get_cords():
            for other_cord in ship._get_cords():
                a = (self_cord[0] - other_cord[0]) ** 2
                b = (self_cord[1] - other_cord[1]) ** 2
                hippo = (a + b) ** 0.5
                if hippo <= 2 ** 0.5:
                    return True

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
    b = Ship(length=3, x=9, y=3, tp=1)
