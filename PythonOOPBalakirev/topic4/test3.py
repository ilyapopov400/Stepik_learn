"""
Реализуйте рекурсивную функцию factorial() для вычисления факториала строки
"""


def date_validate_to_int(number: str) -> int:
    if not isinstance(number, str):
        raise ValueError("not string")
    try:
        num = int(number)
    except ValueError:
        raise ValueError("not number")
    return num


def factorial(number: str) -> str:
    num = date_validate_to_int(number=number)
    if num in (0, 1):
        return "1"
    else:
        result = num * int(factorial(str(num - 1)))
        return str(result)


if __name__ == "__main__":
    result_of_factorial = factorial("4")
    print(result_of_factorial)
