from abc import ABC, abstractmethod


class StackObj:
    def __init__(self, data: str):
        self._data = data
        self._next = None

    def __repr__(self):
        return self._data


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """
        - добавление объекта в конец стека
        """

    @abstractmethod
    def pop_back(self):
        """
        - удаление последнего объекта из стека
        """


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def __repr__(self):
        result = list()
        object_now = self._top

        while object_now:
            last = object_now
            object_now = object_now._next
            result.append(last._data)

        return ", ".join(result)

    def push_back(self, obj: StackObj):
        if self._top:
            object_now = self._top
            object_next = object_now._next
            while object_next:
                object_now = object_next
                object_next = object_now._next
            object_now._next = obj
        else:
            self._top = obj

    def pop_back(self):
        if not self._top:
            return None
        elif not self._top._next:
            result = self._top
            self._top = None
            return result
        object_now = self._top
        last = object_now
        while object_now:
            if object_now._next:
                last = object_now
                object_now = object_now._next
            else:
                last._next = None
                return object_now


if __name__ == "__main__":
    st = Stack()
    st.push_back(StackObj("obj 1"))
    obj = StackObj("obj 2")
    st.push_back(obj)

    del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
    assert del_obj == obj, "Error"

    del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
    print(del_obj)

    print(st)
