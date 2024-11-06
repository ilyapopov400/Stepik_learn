class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    def __init__(self, name: str, weight: int, price: int):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__hash__()

    def get_id(self):
        return self.__id


if __name__ == "__main__":
    a = ShopItem("apple", 2, 3)
    print(a.get_id())
