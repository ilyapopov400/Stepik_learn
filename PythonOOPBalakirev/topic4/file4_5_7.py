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
    """
    - класс для представления маршрутов в навигаторе
    """

    def __init__(self, *args):
        self.__points = self.__date_of_points(*args)

    @property
    def points(self):
        return tuple(self.__points)

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
            return list(args)
        else:
            raise ValueError("Неверные входные данные")

    def add_back(self, pt: PointTrack):
        """
        - добавление новой точки в конец маршрута(pt - объект класса PointTrack)
        """
        self.__points.append(pt)

    def add_front(self, pt):
        """
        - добавление новой точки в начало маршрута(pt - объект класса PointTrack)
        """
        self.__points = [pt, ] + self.__points

    def pop_back(self):
        """
        - удаление последней точки из маршрута
        """
        self.__points.pop()

    def pop_front(self):
        """
        - удаление первой точки из маршрута
        """
        self.__points.pop(0)


if __name__ == "__main__":
    tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
    tr.add_back(PointTrack(1.4, 0))
    tr.pop_front()
    for pt in tr.points:
        print(pt)
