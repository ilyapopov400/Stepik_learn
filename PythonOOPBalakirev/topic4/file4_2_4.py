class Tuple(tuple):
    def __add__(self, other):
        if hasattr(other, "__iter__"):
            return self.__class__(tuple(self) + tuple(other))
        return self.__class__(tuple(self) + other)


if __name__ == "__main__":
    t = Tuple([1, 2, 3])
    t = t + "Python"
    print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
    t = (t + "Python") + "ООП"
    print(t)
