# import pytest


class PointTrack:
    def __init__(self, x: (int, float), y: (int, float)):
        for date in (x, y):
            self.__date_validator(date=date)

        self.x = x
        self.y = y

    @staticmethod
    def __date_validator(date: (int, float)):
        if not isinstance(date, (int, float)):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return "PointTrack: {}, {}".format(self.x, self.y)

    def __repr__(self):
        return "PointTrack: {}, {}".format(self.x, self.y)


class Track:
    def __init__(self, *args):
        self.__points = self.__date_of_points(*args)

    def __repr__(self):
        result = list()
        for point in self.__points:
            result.append("PointTrack: {}, {}".format(point.x, point.y))
        return ", ".join(result)

    @staticmethod
    def __date_of_points(*args) -> list:
        if len(args) == 2 and all(
                map(lambda x: isinstance(x, (int, float)), args)
        ):
            return [PointTrack(x=args[0], y=args[1]), ]
        elif all(
                map(lambda x: isinstance(x, PointTrack), args)
        ):
            return args
        else:
            raise ValueError("Неверные входные данные")

    def add_back(self, pt):
        """
        - добавление новой точки в конец маршрута(pt - объект класса PointTrack)
        """

    def add_front(self, pt):
        """
        - добавление новой точки в начало маршрута(pt - объект класса PointTrack)
        """

    def pop_back(self):
        """
        - удаление последней точки из маршрута
        """

    def pop_front(self):
        """
        - удаление первой точки из маршрута
        """


if __name__ == "__main__":
    # start_x, start_y = 1, 2
    start_x, start_y = PointTrack(1, 2), PointTrack(3, 4)
    tr = Track(start_x, start_y)
    print(tr)

    # @pytest.mark.parametrize('arguments', [
    #     (15, -12.3),
    #     (PointTrack(0.23, -54), PointTrack(-1, 101),),
    #     (PointTrack(0.23, -54),),
    # ])
    # def test_track_class_structure(arguments):
    #     assert hasattr(Track, "points")
    #     assert type(getattr(Track, "points")) is property
    #     assert hasattr(Track, 'add_back')
    #     assert callable(getattr(Track, 'add_back'))
    #     assert hasattr(Track, 'add_front')
    #     assert callable(getattr(Track, 'add_front'))
    #     assert hasattr(Track, 'pop_back')
    #     assert callable(getattr(Track, 'pop_back'))
    #     assert hasattr(Track, 'pop_front')
    #     assert callable(getattr(Track, 'pop_front'))
    #
    #     tr = Track(*arguments)
    #     assert hasattr(tr, "points")
    #     assert type(getattr(tr, "points")) is tuple
    #
    #
    # def test_point_track_class_structure():
    #     pt = PointTrack(-12, 22.43)
    #     assert hasattr(pt, 'x')
    #     assert hasattr(pt, 'y')
    #     with pytest.raises(TypeError) as ex:
    #         pt_error = PointTrack(-11, [22, 4, 7])
    #     assert 'координаты должны быть числами' in str(ex.value)
    #     assert str(pt) == f"PointTrack: -12, 22.43"
