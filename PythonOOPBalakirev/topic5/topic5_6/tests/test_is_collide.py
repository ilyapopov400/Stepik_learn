import unittest
from PythonOOPBalakirev.topic5.topic5_6.file5_6_1 import Ship


class Test_is_collide(unittest.TestCase):
    def test_1(self):
        a = Ship(length=4, x=2, y=2, tp=1)
        b = Ship(length=3, x=9, y=3, tp=1)

        assert a.is_out_pole(size=10) is False, "ошибка выхода за поле игры"
        assert b.is_out_pole(size=10) is True, "ошибка выхода за поле игры, корабль за полем игры"

    def test_2(self):
        """
        - столкновение двух горизонтальный кораблей
        """

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

    def test_3(self):
        """
        - столкновение двух вертикальных кораблей
        """

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=3, x=2, y=1, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=3, x=4, y=6, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=3, x=3, y=2, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=3, x=3, y=3, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=3, x=3, y=5, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=2, x=3, y=9, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=5, tp=2)
        b = Ship(length=1, x=3, y=10, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

    def test_4(self):
        """
        - self горизонтальный
        - other вертикальный
        """

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=4, x=2, y=5, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=4, x=1, y=4, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=4, x=1, y=3, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=3, x=2, y=0, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=3, x=7, y=4, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=3, x=7, y=3, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=3, x=4, y=2, tp=2)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=3, x=9, y=7, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=3, tp=1)
        b = Ship(length=2, x=4, y=0, tp=2)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

    def test_5(self):
        """
        - self вертикальный
        - other горизонтальный
        """

        a = Ship(length=4, x=2, y=3, tp=2)
        b = Ship(length=2, x=4, y=2, tp=1)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=3, tp=2)
        b = Ship(length=1, x=0, y=2, tp=1)
        assert a.is_collide(b) is False, "ошибка проверки на столкновение кораблей, нет столкновения"

        a = Ship(length=4, x=2, y=3, tp=2)
        b = Ship(length=2, x=0, y=2, tp=1)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"

        a = Ship(length=4, x=2, y=3, tp=2)
        b = Ship(length=2, x=2, y=2, tp=1)
        assert a.is_collide(b) is True, "ошибка проверки на столкновение кораблей, есть столкновение"


if __name__ == '__main__':
    unittest.main()
