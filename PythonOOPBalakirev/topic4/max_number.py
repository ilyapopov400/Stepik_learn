"""
Даны два строковых представления чисел A и B.
Нужно максимизировать A, заменив в нём любую цифру на цифру из B.
Каждую цифру B можно использовать только один раз
"""


class MaxNumber:
    def __init__(self, a, b):
        self._a = list(map(int, a))
        self._b = list(map(int, b))

    def _engine(self):
        result = list()
        for index, number in enumerate(self._a):
            max_b = max(self._b)
            if max_b < number:
                result.append(number)
            else:
                result.append(max_b)
                self._b.remove(max_b)
        result_str = "".join(map(str, result))
        return result_str

    def __call__(self):
        result = self._engine()
        return result


if __name__ == "__main__":
    max_number = MaxNumber("123", "2223")
    print(max_number())
