"""
Напиши алгоритм сортировки массива,
где каждый следующий элемент должен быть равен предыдущему,
но строго больше его
"""
import random


def func(date: list):
    result = list()
    copy_date = date.copy()
    for num in date:
        a = min(copy_date)
        result.append(a)
        copy_date.remove(a)
    return result


if __name__ == "__main__":
    date = list(map(
        lambda x: int(random.random() * 100), range(10)
    ))
    print(date)
    result = func(date)
    print(result)
