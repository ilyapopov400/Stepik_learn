text = "1 -5.6 2 abc 0 False 22.5 hello world"

lst_in = text.split()


def f(ls: list):
    result = 0
    for num in ls:
        try:
            result += int(num)
        except ValueError:
            pass
    return result


if __name__ == "__main__":
    print(f(lst_in))
