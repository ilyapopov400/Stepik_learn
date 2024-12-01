class Function:
    def __init__(self):
        self._amplitude = 1.0  # амплитуда функции
        self._bias = 0.0  # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    # здесь добавляйте еще один магический метод для умножения


# здесь объявляйте класс Linear
class Linear(Function):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], self.__class__):
            self._k = args[0]._k
            self._b = args[0]._b
        elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self._k = args[0]
            self._b = args[1]
        else:
            raise ValueError("Error")
        super().__init__()

    def _get_function(self, x):
        result = self._k * x + self._b
        # result = self._amplitude * (self._k * x + self._b) + self._bias
        return result

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj


if __name__ == "__main__":
    f = Linear(1, 0.5)
    f2 = f + 10  # изменение смещения (атрибут _bias)
    y1 = f(0)  # 0.5
    assert y1 == 0.5, "Error"
    y2 = f2(0)  # 10.5
    assert y2 == 10.5, "Error"

    f = Linear(1, 0.5)
    f2 = f * 5  # изменение амплитуды (атрибут _amplitude)
    y1 = f(0)  # 0.5
    y2 = f2(0)  # 2.5
    assert y1 == 0.5, "Error"
    assert y2 == 2.5, "Error"
