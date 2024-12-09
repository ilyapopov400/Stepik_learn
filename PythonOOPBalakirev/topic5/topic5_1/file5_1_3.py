text = "1 -5.6 True abc 0 23.56 hello"

lst_in = text.split()


def f(ls: list):
    result = list()
    for num in ls:
        try:
            result.append(int(num))
        except ValueError:
            try:
                result.append(float(num))
            except ValueError:
                result.append(num)
    return result


if __name__ == "__main__":
    lst_out = f(ls=lst_in)
    print(lst_out)
