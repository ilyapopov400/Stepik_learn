class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView

class ShopGenericView:
    """
    - для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book)
    """

    def __str__(self):
        result = list()
        for key, value in self.__dict__.items():
            result.append("{}: {}".format(key, value))
        return "\n".join(result)


class ShopUserView:
    """
    - для отображения всех локальных атрибутов,
     кроме атрибута _id,
     объектов любых дочерних классов (не только Book)
    """

    def __str__(self):
        result = list()
        for key, value in self.__dict__.items():
            if not key == "_id":
                result.append("{}: {}".format(key, value))
        return "\n".join(result)


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


if __name__ == "__main__":
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
