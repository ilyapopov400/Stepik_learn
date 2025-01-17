"""
Палиндром - такое сочетание цифр, которые
читаются одинаково слева направо и справа налево,
например, 323, 6996. Найти все палиндромы в
заданном диапазоне [a...b], в составе которых
встречаются только нечетные числа
"""


class Palindoms:
    @staticmethod
    def __chesk_palindom(number: int) -> bool:
        return str(number) == str(number)[::-1]

    @staticmethod
    def __odd_number(number: int) -> bool:
        for num in str(number):
            if int(num) % 2 == 0:
                return False
        return True

    def __call__(self, start, stop) -> list:
        result = list(
            filter(lambda x: self.__chesk_palindom(number=x) & self.__odd_number(number=x), range(start, stop+1))
        )
        return result


if __name__ == "__main__":
    start, stop = 100, 200

    result = Palindoms()(start, stop)
    print(result)
