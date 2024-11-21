class SellItem:
    def __init__(self, name: str, price: (int, float)):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str):
        self.name = name
        self.__obj = list()

    def add_object(self, obj):
        """
        - добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land)
        """
        self.__obj.append(obj)

    def remove_object(self, obj):
        """
        - удаление объекта obj из списка объектов для продажи
        """
        if obj in self.__obj:
            self.__obj.remove(obj)
        else:
            print("not {} in {}".format(obj, self))

    def get_objects(self):
        """
        - возвращает список из всех объектов для продажи
        """
        return self.__obj


if __name__ == "__main__":
    ag = Agency("Рога и копыта")
    ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
    ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
    ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
    ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
    ag.add_object(Land("участок под застройку", 3000000, 6.74))
    for obj in ag.get_objects():
        print(obj.name)
        ag.remove_object(obj)
        ag.remove_object(obj)

    lst_houses = [x for x in ag.get_objects() if isinstance(x, House)]  # выделение списка домов
