import unittest
from PythonOOPBalakirev.topic5.topic5_6.file5_6_1 import Ship


class TestShip(unittest.TestCase):
    def test_1(self):
        ship = Ship(2)
        ship = Ship(2, 1)
        ship = Ship(3, 2, 0, 0)
        assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"

        assert ship._cells == [1, 1, 1], "неверный список _cells"
        assert ship._is_move, "неверное значение атрибута _is_move"
        ship.set_start_coords(1, 2)
        assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
        assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

    def test_2(self):
        ship = Ship(3, 2, 0, 0)

        ship.move(1)
        s1 = Ship(4, 1, 0, 0)
        s2 = Ship(3, 2, 0, 0)
        s3 = Ship(3, 2, 0, 2)
        assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
        assert s1.is_collide(
            s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

    def test_3(self):
        s1 = Ship(4, 1, 0, 0)
        s2 = Ship(3, 2, 1, 1)
        assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
        s2 = Ship(3, 1, 8, 1)
        assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
        s2 = Ship(3, 2, 1, 5)
        assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
        s2[0] = 2
        assert s2[0] == 2, "неверно работает обращение ship[indx]"


if __name__ == '__main__':
    unittest.main()
