class Test():
    def __init__(self, descr: str):
        self.__validate_descr(descr=descr)
        self.descr = descr

    @staticmethod
    def __validate_descr(descr):
        if not isinstance(descr, str) or len(descr) not in range(10, 10_001):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr: str, ans_digit: float, max_error_digit: float = 0.01):
        super().__init__(descr=descr)
        self.__validate_digit(ans_digit=ans_digit, max_error_digit=max_error_digit)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    @staticmethod
    def __validate_digit(ans_digit: float, max_error_digit: float):
        if not all(
                map(lambda x: isinstance(x, (int, float)), (ans_digit, max_error_digit))
        ) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')

    def run(self) -> bool:
        ans = float(input())
        result = (self.ans_digit - self.max_error_digit) <= ans <= (self.ans_digit + self.max_error_digit)
        return result


try:
    descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
    ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

    result = TestAnsDigit(descr=descr, ans_digit=ans)
    print(result.run())
except Exception as ex:
    print(ex)

if __name__ == "__main__":
    try:
        test = Test('descr')
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

    try:
        test = Test('descr ghgfhgjg ghjghjg')
        test.run()
    except NotImplementedError:
        assert True
    else:
        assert False
    assert issubclass(TestAnsDigit, Test)

    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

    try:
        t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
    except ValueError:
        assert True
    else:
        assert False
