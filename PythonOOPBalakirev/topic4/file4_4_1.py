class Animal:
    def __init__(self, name: str, kind: str, old: int):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        self.__kind = kind

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


if __name__ == "__main__":
    animals = [
        Animal(name="Васька", kind="дворовый кот", old=5),
        Animal(name="Рекс", kind="немецкая овчарка", old=8),
        Animal(name="Кеша", kind="попугай", old=3),

    ]
