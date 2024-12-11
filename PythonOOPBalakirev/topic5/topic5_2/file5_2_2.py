class Point:
    def __init__(self, x: (int, float) = 0, y: (int, float) = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


if __name__ == "__main__":
    in_put = input().split()[:2]
    try:
        x, y = map(int, in_put)
        pt = Point(x, y)
    except ValueError:
        try:
            x, y = map(float, in_put)
            pt = Point(x, y)
        except:
            pt = Point()
    finally:
        print("Point: x = {}, y = {}".format(pt.x, pt.y))
