import copy


class Box:
    def __init__(self, name: str, max_weight: (int, float)):
        self._name = name
        self._max_weight = max_weight
        self._things = list()

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst):
        self._things = lst

    def add_thing(self, obj: tuple) -> None:
        """
        для добавления новой вещи в ящик, где obj - кортеж из двух значений:
        (название_вещи, вес_вещи)
        Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight,
        то генерировать исключение: raise ValueError('превышен суммарный вес вещей')
        :param obj: tuple
        :return: None
        """
        weight = sum(map(lambda x: x[1], self._things))

        if (weight + obj[1]) > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)


class BoxDefender:
    def __init__(self, box: Box):
        self.__box = box
        self._things = copy.deepcopy(box.things)

    def __enter__(self):
        return self.__box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.__box.things = self._things
        return False


if __name__ == "__main__":
    b = Box('name', 2000)
    assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"
    b.add_thing(("1", 100))
    b.add_thing(("2", 200))
    try:
        with BoxDefender(b) as bb:
            bb.add_thing(("3", 1000))
            bb.add_thing(("4", 1900))
    except ValueError:
        assert len(b._things) == 2

    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        with BoxDefender(b) as bb:
            bb.add_thing(("3", 100))
    except ValueError:
        assert False, "возникло исключение ValueError, хотя, его не должно было быть"
    else:
        assert len(b._things) == 3, "неверное число элементов в списке _things"
