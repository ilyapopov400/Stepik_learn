# Найти все простые числа меньше или равные заданному числу N
class NumberSearch:
    def __init__(self, number: int):
        """

        :param number: передаваемое число N
        """
        self._data_verification(number)
        self._n = number
        self._numbers = [1, ]

    @staticmethod
    def _data_verification(number: int):
        """
        проверка вводных данных
        :param number:
        :return:
        """
        if not isinstance(number, int) or number < 1:
            raise ValueError("только целые положительные числа")

    @staticmethod
    def _checking_prime_number(number: int):
        """
        проверка, является ли число простым
        :param number:
        :return:
        """
        for num in range(2, number // 2 + 1):
            if number % num == 0:
                return False
        return True

    def __call__(self) -> list:
        """
        - перебираем все числа до N
        - проверяем их, являются ли они простыми
        - заносим в список self._numbers
        - возвращаем список self._numbers
        :return:
        """
        if self._n != 1:
            for num in range(2, self._n + 1):
                if self._checking_prime_number(number=num):
                    self._numbers.append(num)
        return self._numbers


if __name__ == "__main__":
    n = int(input("input N "))
    number_search = NumberSearch(number=n)()
    print(*number_search, sep=", ")
    print("сложность O(n**2)")
