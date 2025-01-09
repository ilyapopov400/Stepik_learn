s = input()


# s = "hello"


class CreaterSubstring:
    def __init__(self, string: str):
        self.string = string
        self.result = dict(zip(tuple(self.string), map(lambda x: 0, range(len(self.string)))))

    def creater_lst(self) -> list:
        res = list()
        for j in range(len(self.string)):
            for i in range(len(self.string)):
                st = self.string[j:i + 1]
                if bool(st):
                    res.append(st)

        return res

    def count(self) -> dict:
        lst = self.creater_lst()

        for i in self.result:
            for j in lst:
                if i in j:
                    old = j
                    new = old.replace(i, '')
                    summa = len(old) - len(new)
                    self.result[i] += summa
        return self.result

    def show(self):
        result = self.count()
        sorted_dict = dict(sorted(result.items()))
        for key, value in sorted_dict.items():
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    s = CreaterSubstring(string=s)

    s.show()
