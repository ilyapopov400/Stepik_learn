"""
Напишите код для создания бесконечного массива с конечным количеством элементов
"""


class StackObj:
    """
    - для представления отдельных объектов стека
    """

    def __init__(self, data, next_obj=None):
        """

        :param data: - данные, хранящиеся в объекте стека
        :param next_obj: - ссылка на следующий объект стека (если его нет, то next_obj = None)
        """
        self.data = data
        self.next_obj = next_obj

    def __repr__(self):
        return self.data


class InfiniteArray:
    """
    - бесконечный массив, реализованный через односвязный список
    """

    def __init__(self):
        """
        - self.top ссылка на первый объект стека (при пустом стеке top = None)
        """
        self.top = None

    def __repr__(self):
        result = list()
        ob = self.top
        for _ in range(len(self)):
            result.append(ob.data)
            ob = ob.next_obj
        if not bool(result):
            return "{} is None".format(self.__class__.__name__)
        return ", ".join(result)

    def __len__(self):
        count = 0
        if self.top:
            obj = self.top
            while obj.next_obj:
                count += 1
                obj = obj.next_obj
            count += 1
        return count

    def push_back(self, data):
        """
        - для добавления новых данных в конец стека
        """
        obj = StackObj(data=data)
        if self.top:
            ob = self.top
            for i in range(len(self) - 1):
                ob = ob.next_obj
            ob.next_obj = obj
            obj.next_obj = None
        else:
            obj.next_obj = None
            self.top = obj

    def push_front(self, data):
        """
        - для добавления новых данных в начало стека
        """
        obj = StackObj(data=data)
        if self.top:
            obj.next_obj = self.top
            self.top = obj
        else:
            obj.next_obj = None
            self.top = obj

    def __index_validate(self, index: int):
        """
        - проверка передаваемого индекса в сравнении с длинной масива
        :param index:
        :return:
        """
        if not isinstance(index, int) or index not in range(len(self)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int):
        """
        - получение значения элемента массива с номером item
        :param item:
        :return:
        """
        self.__index_validate(index=item)
        obj = self.top
        for _ in range(item):
            obj = obj.next_obj
        return obj.data

    def _get_item_object(self, item: int) -> StackObj:
        """
        - получение самого элемента массива с номером item
        :param item:
        :return:
        """
        self.__index_validate(index=item)
        obj = self.top
        for _ in range(item):
            obj = obj.next_obj
        return obj

    def __setitem__(self, key, value):
        """
        - установление на номер key значение value в массиве
        :param key:
        :param value:
        :return:
        """
        self.__index_validate(index=key)

        if key == 0:
            nxt = self.top.next_obj
            now = StackObj(data=value, next_obj=nxt)
            self.top = now
            return

        if key == len(self) - 1:
            later = self._get_item_object((key - 1))
            now = StackObj(data=value, next_obj=None)
            later.next_obj = now
            return

        later, nxt = self._get_item_object((key - 1)), self._get_item_object((key + 1))
        now = StackObj(data=value, next_obj=nxt)
        later.next_obj = now

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        if self.count >= len(self) - 1:
            raise StopIteration
        else:
            self.count += 1
            return self._get_item_object(item=self.count)


if __name__ == "__main__":
    infinite_array = InfiniteArray()

    infinite_array.push_back("a")
    infinite_array.push_back("b")
    infinite_array.push_back("c")
    infinite_array.push_front("one")
    print(infinite_array)

    infinite_array.__setitem__(0, "first")
    infinite_array.__setitem__(3, "out")

    print(infinite_array)
    print()

    for data in infinite_array:
        print(data)
