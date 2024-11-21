class ItemAttrs:
    def __getitem__(self, key):
        """
        - для получения значения атрибута по индексу
        """
        return list(self.__dict__.values())[key]

    def __setitem__(self, key, value):
        """
        - для изменения значения атрибута по индексу
        """
        for e, res in enumerate(self.__dict__.items()):
            if e == key:
                setattr(self, res[0], value)


class Point(ItemAttrs):
    def __init__(self, x: (int, float), y: (int, float)):
        self.x = x
        self.y = y


if __name__ == "__main__":
    pt = Point(1, 2.5)
    assert pt[0] == 1, "pt[0] == 1"
    assert pt[1] == 2.5, "pt[1] == 2.5"
    x = pt[0]  # 1
    assert x == 1, "x = pt[0] -> 1"
    y = pt[1]  # 2.5
    assert y == 2.5, "y = pt[1] -> 2.5"
    pt[0] = 10
    assert pt[0] == 10, "pt[0] = 10"
