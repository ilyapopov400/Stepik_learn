class IteratorAttrs:
    def __init__(self, *args, **kwargs):
        if args:
            for key in args:
                setattr(self, str(key), key)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory


if __name__ == "__main__":
    a = IteratorAttrs(1, 2, 3, a=4)
    for i in a:
        print(i)
    print("*" * 30)
    phone = SmartPhone("iphone", (12, 34), 8)
    for attr, value in phone:
        print(attr, value)
