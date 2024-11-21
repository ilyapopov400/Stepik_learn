class SoftList(list):
    def __getitem__(self, y):
        if y not in range(-len(self), len(self)):
            return False
        return super().__getitem__(y)


if __name__ == "__main__":
    sl = SoftList("python")
    print(sl[0])  # 'p'
    print(sl[-1])  # 'n'
    print(sl[6])  # False
    print(sl[-7])  # False

    assert sl[0] == 'p', "IndexError: list index out of range"
    assert sl[-1] == 'n', "IndexError: list index out of range"
    assert sl[6] is False, "IndexError: list index out of range"
    assert sl[-7] is False, "IndexError: list index out of range"
