import unittest
from PythonOOPBalakirev.topic5.topic5_6.file5_6_1 import Ship, GamePole


class TestGamePole(unittest.TestCase):
    def test_something(self):
        p = GamePole(10)
        p.init()
        for nn in range(5):
            for s in p._ships:
                assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
                for ship in p.get_ships():
                    if s != ship:
                        assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
            p.move_ships()


if __name__ == '__main__':
    unittest.main()
