class Protists:
    def __init__(self, name: str, weight: float, old: int):
        self.name = name
        self.weight = weight
        self.old = old

    def __repr__(self):
        return self.__class__.__name__


class Plants(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Animals(Protists):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


lst_objs = [
    Monkey("мартышка", 30.4, 7),
    Monkey("шимпанзе", 24.6, 8),
    Person("Балакирев", 88, 34),
    Person("Верховный жрец", 67.5, 45),
    Flower("Тюльпан", 0.2, 1),
    Flower("Роза", 0.1, 2),
    Worm("червь", 0.01, 1),
    Worm("червь 2", 0.02, 1)
]

# все объекты, относящиеся к животным (Animals)
lst_animals = [i for i in lst_objs if isinstance(i, Animals)]

# все объекты, относящиеся к растениям (Plants)
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]

# все объекты, относящиеся к млекопитающим (Mammals)
lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]

if __name__ == "__main__":
    print(lst_animals)
    print(lst_plants)
    print(lst_mammals)
