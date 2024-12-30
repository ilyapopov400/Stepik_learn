import random


class Ship:
    """
    - для представления кораблей
    """

    def __init__(self, length: int, tp: int = 1, x: int = None, y: int = None):
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
        self._length = length
        self._x = x
        self._y = y
        self._tp = tp
        self._is_move = True
        self._cells = list(map(lambda x: 1, range(length)))

    @property
    def tp(self):
        return self._tp

    @property
    def length(self):
        return self._length

    def __repr__(self):
        if self._tp == 1:
            orient = "горизонтальная"
        else:
            orient = "вертикальная"
        return "{}: x={}, y={}, ориентация: {}, трубы: {}".format(self.__class__.__name__,
                                                                  self._x, self._y, orient, self._cells)

    def get_cords(self) -> list:
        """
        - получаем список координат с головы корабля
        :return: tuple
        """
        result = list()
        if self._tp == 1:
            for x in range(self._length):
                coord = self._x + x, self._y
                result.append(coord)
        else:
            for y in range(self._length):
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

    def move(self, go: int):
        """
        - перемещение корабля в направлении его ориентации на go клеток
            (go = 1 - движение в одну сторону на клетку;
            go = -1 - движение в другую сторону на одну клетку);
            движение возможно только если флаг _is_move = True

        :param go: int
        :return: None
        """
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship) -> bool:
        """
        - проверка на столкновение с другим кораблем ship
              (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
              в том числе и по диагонали);
              метод возвращает True, если столкновение есть и False - в противном случае
        :param ship:
        :return:
        """
        for self_cord in self.get_cords():
            for other_cord in ship.get_cords():
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
            if self._x + self._length > size:
                return True
        else:
            """
            - при вертикальном расположении
            """
            if self._y + self._length > size:
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

    def __init__(self, size: int = 10):
        """
        _ships - список из кораблей (объектов класса Ship); изначально пустой список
        :param size: - размер игрового поля (целое положительное число)
        """
        self._size = size
        self._ships = list()

    @property
    def ships(self):
        return self._ships

    @ships.setter
    def ships(self, ships):
        self._ships = ships

    def get_ships(self):
        return self._ships

    @staticmethod
    def _temp_ship(ship: Ship):
        """

        :param ship:
        :return: - возвращаем копию корабля
        """
        result = Ship(
            length=ship.length,
            tp=ship.tp,
            x=ship.get_cords()[0],
            y=ship.get_cords()[0],
        )
        return result

    @staticmethod
    def get_list_ship_without_cords() -> list:
        """

        :return: список кораблей без координат для инициализации
        """
        result = [
            Ship(length=4, tp=random.randint(1, 2)),
            Ship(length=3, tp=random.randint(1, 2)),
            Ship(length=3, tp=random.randint(1, 2)),
            Ship(length=2, tp=random.randint(1, 2)),
            Ship(length=2, tp=random.randint(1, 2)),
            Ship(length=2, tp=random.randint(1, 2)),
            Ship(length=1, tp=random.randint(1, 2)),
            Ship(length=1, tp=random.randint(1, 2)),
            Ship(length=1, tp=random.randint(1, 2)),
            Ship(length=1, tp=random.randint(1, 2)),
        ]
        return result

    def __set_cords_ships(self, list_ship: list) -> list:
        """

        :param list_ship: список с кораблями
        :return: список с кораблями с произвольно расставленными координатами
        """
        for ship in list_ship:
            x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)
            ship.set_start_coords(x=x, y=y)
        return list_ship

    @staticmethod
    def _validate_exit_cross(list_ship: list, size: int) -> bool:  # TODO
        """
        - True если корабли из списка не пересекаются друг с другом и не выходят зва границы поля
        :param list_ship:
        :return:
        """
        for ship in list_ship:
            if ship.is_out_pole(size=size):
                return False
        for ship in list_ship:
            for other in list_ship:
                if ship.__hash__() != other.__hash__() and ship.is_collide(ship=other):
                    return False
        return True

    def init(self):
        """
        - начальная инициализация игрового поля;
                       здесь создается список из кораблей (объектов класса Ship):
                       однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1
                       (ориентация этих кораблей должна быть случайной)
          Начальные координаты x, y не расставленных кораблей равны None
          После этого, выполняется их расстановка на игровом поле со случайными координатами так,
                      чтобы корабли не пересекались между собой
        """
        flag, step, list_ship = True, 0, list()
        while flag:
            step += 1
            start_list_ship = self.get_list_ship_without_cords()
            list_ship = self.__set_cords_ships(list_ship=start_list_ship)

            if self._validate_exit_cross(list_ship=list_ship, size=self._size):
                flag = False
                break
        self._ships = list_ship

    def move_ships(self):  # TODO
        """
        - перемещает каждый корабль из коллекции _ships на одну клетку
         (случайным образом вперед или назад) в направлении ориентации корабля;
         если перемещение в выбранную сторону невозможно
         (другой корабль или пределы игрового поля),
         то попытаться переместиться в противоположную сторону,
         иначе (если перемещения невозможны), оставаться на месте;
        :return:
        """

        for ship in self._ships:
            ship.move(go=1)
            if not self._validate_exit_cross(self._ships, self._size):
                ship.move(go=-2)
                if not self._validate_exit_cross(self._ships, self._size):
                    ship.move(go=1)

    def get_pole(self) -> tuple:
        """
        - получение текущего игрового поля в виде двумерного(вложенного) кортежа размерами size x size элементов
        """
        show_list = [
            [0 for y in range(self._size)] for x in range(self._size)
        ]
        for ship in self._ships:
            for x, y in ship.get_cords():
                show_list[y][x] = 1

        result = tuple(
            map(lambda x: tuple(x), show_list)
        )

        return result

    def show(self):
        """
        - отображение игрового поля в консоли
         (корабли должны отображаться значениями из коллекции _cells каждого корабля,
         вода - значением 0)
        :return:
        """
        show_list = self.get_pole()
        for line in show_list:
            for column in line:
                print(column, end=" ")
            print("")


if __name__ == "__main__":
    ship = Ship(2)
    ship = Ship(2, 1)
    ship = Ship(3, 2, 0, 0)
    assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
    assert ship._cells == [1, 1, 1], "неверный список _cells"
    assert ship._is_move, "неверное значение атрибута _is_move"
    ship.set_start_coords(1, 2)
    assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
    assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
    ship.move(1)
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 0, 0)
    s3 = Ship(3, 2, 0, 2)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
    assert s1.is_collide(
        s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
    s2 = Ship(3, 2, 1, 1)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
    s2 = Ship(3, 1, 8, 1)
    assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
    s2 = Ship(3, 2, 1, 5)
    assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
    s2[0] = 2
    assert s2[0] == 2, "неверно работает обращение ship[indx]"
    p = GamePole(10)
    p.init()
    for nn in range(5):
        for s in p._ships:
            assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
            for ship in p.get_ships():
                if s != ship:
                    assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
        p.move_ships()

    gp = p.get_pole()
    assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
    assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
    pole_size_8 = GamePole(8)
    pole_size_8.init()
