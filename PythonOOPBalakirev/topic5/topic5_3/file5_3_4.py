digits = list(map(float, input().split()))


class TupleLimit(tuple):
    def __new__(cls, lst: (list, tuple), max_length: int):
        result = super().__new__(cls, lst)
        result.max_length = max_length
        return result

    def __init__(self, lst: (list, tuple), max_length: int):
        super().__init__()
        self.__validate_max_length(lst=lst, max_length=max_length)

        self.lst = lst
        self.max_lenght = max_length

    @staticmethod
    def __validate_max_length(lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')

    def __str__(self):
        result = list(map(str, self.lst))
        result = ' '.join(result)
        return result

    def __repr__(self):
        result = list(map(str, self.lst))
        result = ' '.join(result)
        return result


if __name__ == "__main__":
    try:
        a = TupleLimit(digits, 5)
        print(a)
    except ValueError as ex:
        print(ex)
